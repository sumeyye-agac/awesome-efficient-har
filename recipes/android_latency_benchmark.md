# Android Latency Benchmark Recipe (ADB + TFLite)

Use repeatable ADB commands and collect enough runs to reduce variance.

## Prerequisites

- Android device with developer mode + USB debugging.
- `adb` installed and device visible with `adb devices`.
- `benchmark_model` binary and your `.tflite` model on device.

## Minimal workflow

```bash
# 1) Push model and benchmark binary
adb push model_int8.tflite /data/local/tmp/model_int8.tflite
adb push benchmark_model /data/local/tmp/benchmark_model
adb shell chmod +x /data/local/tmp/benchmark_model

# 2) Optional: set fixed governor/profile if your lab policy allows it
# adb shell su -c 'echo performance > /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor'

# 3) Warm-up + timed runs
adb shell /data/local/tmp/benchmark_model \
  --graph=/data/local/tmp/model_int8.tflite \
  --num_threads=4 \
  --warmup_runs=20 \
  --num_runs=100
```

## Recommended reporting

- Device model, Android version, SoC, and thermal state.
- Thread count and delegate used (CPU, NNAPI, GPU).
- P50/P90/P99 latency and standard deviation.
- Peak RSS/memory (if available).

## Thermal and variance gotchas

- Run after cooldown; avoid charging during measurement.
- Discard first run block if app/process cold-start dominates.
- Repeat across multiple sessions; single-run numbers are noisy.
- Keep background services minimal (airplane mode helps consistency).

## Optional tracing

- Use Perfetto for scheduling/thermal traces around benchmark windows.
- Correlate latency spikes with frequency throttling events.
