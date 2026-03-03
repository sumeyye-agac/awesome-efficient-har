# TFLite Full-INT8 Export Recipe

This recipe converts a TensorFlow model to full INT8 for edge deployment.

## Minimal TensorFlow snippet

```python
import tensorflow as tf
import numpy as np

saved_model_dir = "saved_model"
converter = tf.lite.TFLiteConverter.from_saved_model(saved_model_dir)

# Full integer quantization
converter.optimizations = [tf.lite.Optimize.DEFAULT]

# Representative dataset generator
# Yield input tensors with the exact inference shape and realistic sensor ranges.
def rep_data_gen():
    for _ in range(300):
        sample = np.random.randn(1, 128, 6).astype(np.float32)  # [B, T, C] example
        yield [sample]

converter.representative_dataset = rep_data_gen
converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS_INT8]
converter.inference_input_type = tf.int8
converter.inference_output_type = tf.int8

tflite_model = converter.convert()
with open("model_int8.tflite", "wb") as f:
    f.write(tflite_model)
```

## Verification checklist

- Confirm all ops are INT8 in Netron or TFLite analyzer.
- Run golden-set parity check: FP32 vs INT8 top-1 and confusion matrix.
- Measure latency on target device, not desktop.
- Validate dynamic range handling for each sensor channel.

## Representative dataset guidance

- Use real windows from training distribution (not random noise in production).
- Cover idle, transitions, and high-motion segments.
- Include all placements/devices you support.

## Common failure modes

- **Converter fallback to float ops**: unsupported layers/activations; replace ops or adjust architecture.
- **Large accuracy drop**: poor representative dataset coverage; recalibrate and retrain with QAT.
- **Input scale mismatch**: preprocessing at inference differs from training.
- **Saturation/clipping artifacts**: abnormal channel ranges; normalize per channel before export.
