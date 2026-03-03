# Knowledge Distillation Recipe (HAR / Time-Series)

This is a minimal PyTorch-style recipe for teacher-student distillation on windowed sensor signals.

## Minimal pseudocode

```python
import torch
import torch.nn.functional as F

# x: [batch, channels, time], y: class ids
# teacher is frozen, student is trainable

def kd_loss(student_logits, teacher_logits, y, alpha=0.7, temperature=4.0):
    ce = F.cross_entropy(student_logits, y)

    log_p_s = F.log_softmax(student_logits / temperature, dim=-1)
    p_t = F.softmax(teacher_logits / temperature, dim=-1)
    kl = F.kl_div(log_p_s, p_t, reduction="batchmean") * (temperature ** 2)

    return alpha * kl + (1.0 - alpha) * ce

for x, y in train_loader:
    with torch.no_grad():
        t_logits = teacher(x)

    s_logits = student(x)
    loss = kd_loss(s_logits, t_logits, y, alpha=0.7, temperature=4.0)

    optimizer.zero_grad()
    loss.backward()
    optimizer.step()
```

## Defaults that usually work

- Temperature: `T=3` to `T=6`
- Distillation weight: `alpha=0.5` to `0.9`
- Start with a strong teacher checkpoint and freeze it.
- Keep identical label space and preprocessing between teacher and student.

## HAR-specific tips

- Distill with the same windowing policy used at inference.
- If classes are imbalanced, combine KD with class-balanced CE weighting.
- Use subject-wise validation for early stopping.
- For streaming HAR, validate on sequential chunks, not only shuffled windows.

## Failure modes

- **Student underfits**: reduce `alpha` or lower `T`.
- **No gain over CE baseline**: teacher quality too low or teacher/student preprocessing mismatch.
- **Instability**: clip gradients and reduce LR; check for NaNs after softmax temperature scaling.
- **Generalization drop**: overfitting to teacher biases; add augmentation and stronger subject-wise validation.
