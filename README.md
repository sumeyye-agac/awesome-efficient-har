<!--lint disable awesome-github-->
# Awesome Efficient HAR [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> This repository is under active development.

A curated list of resources for **efficient, edge, and wearable Human Activity Recognition (HAR)**.

Focus areas: wearable and smartphone sensor data (IMU, multimodal), compact models for time-series HAR, and on-device deployment with reliable benchmarking.

Legend: `[📄 paper]` `[💻 code]` `[📦 dataset]` `[⚡ efficient]` `[📱 on-device]` `[🧪 benchmark]` `[🧠 distillation]` `[🧩 attention]` `[🔧 quantization]` `[🪓 pruning]` `[🧰 tooling]`

This README is generated from `data/entries.yaml` via `scripts/generate_readme.py`.

## Contents

1. [Datasets (wearable/IMU/multimodal)](#datasets-wearableimumultimodal)
2. [Lightweight architectures for time-series](#lightweight-architectures-for-time-series)
3. [Attention modules for sensor/time-series](#attention-modules-for-sensortime-series)
4. [Knowledge distillation for HAR/time-series](#knowledge-distillation-for-hartime-series)
5. [Quantization/pruning/compression](#quantizationpruningcompression)
6. [On-device benchmarking and tooling](#on-device-benchmarking-and-tooling)
7. [Reproducible benchmarks/leaderboards](#reproducible-benchmarksleaderboards)
8. [Deployment patterns (windowing/streaming/personalization)](#deployment-patterns-windowingstreamingpersonalization)
9. [Efficiency reporting checklist for HAR papers](#efficiency-reporting-checklist-for-har-papers)
10. [Edge HAR starter packs](#edge-har-starter-packs)

## Datasets (wearable/IMU/multimodal)

- [KU-HAR](https://www.sciencedirect.com/science/article/pii/S0167865521000933) (2020) - Open HAR dataset for heterogeneous smartphone sensing with 18 daily activities and standardized splits. `[📦 dataset] [🧪 benchmark]`
- [MotionSense](https://github.com/mmalekzadeh/motion-sense) (2019) - Motion data from iPhone sensors for activity and user context tasks. `[📦 dataset] [💻 code]`
- [SHL Dataset (Sussex-Huawei Locomotion)](http://www.shl-dataset.org/) (2018) - Large-scale multimodal wearable and phone locomotion challenge data. `[📦 dataset] [🧪 benchmark]`
- [ExtraSensory](http://extrasensory.ucsd.edu/) (2017) - Smartphone, smartwatch, and context labels in the wild. `[📦 dataset]`
- [SisFall](https://www.mdpi.com/1424-8220/17/1/198) (2017) - Fall and movement dataset with elderly participants, released with the SisFall benchmark paper. `[📦 dataset]`
- [UniMiB SHAR](https://www.mdpi.com/2076-3417/7/10/1101) (2017) - Smartphone accelerometer ADL and fall dataset introduced with the UniMiB SHAR benchmark paper. `[📦 dataset]`
- [MobiAct](https://bmi.hmu.gr/the-mobifall-and-mobiact-datasets-2/) (2016) - Smartphone inertial dataset for daily activities and falls from the MobiAct benchmark collection. `[📦 dataset]`
- [RealWorld HAR](https://www.uni-mannheim.de/dws/research/projects/activity-recognition/) (2016) - Smartphone and smartwatch placement diversity in real-world conditions. `[📦 dataset]`
- [Heterogeneity HAR (HHAR)](https://archive.ics.uci.edu/dataset/344/heterogeneity+activity+recognition) (2015) - Device and user heterogeneity benchmark across phones and watches. `[📦 dataset] [🧪 benchmark]`
- [mHealth](https://archive.ics.uci.edu/dataset/319/mhealth+dataset) (2014) - Body-worn sensor dataset for activity monitoring. `[📦 dataset]`
- [DSADS (Daily and Sports Activities)](https://archive.ics.uci.edu/dataset/256/daily+and+sports+activities) (2013) - Body-worn motion sensors across daily and sport actions. `[📦 dataset]`
- [OPPORTUNITY Activity Recognition](https://archive.ics.uci.edu/dataset/226/opportunity+activity+recognition) (2012) - Multimodal ambient and wearable sensor dataset. `[📦 dataset] [🧪 benchmark]`
- [PAMAP2 Physical Activity Monitoring](https://archive.ics.uci.edu/dataset/231/pamap2+physical+activity+monitoring) (2012) - Multi-sensor IMU and heart-rate recordings. `[📦 dataset] [🧪 benchmark]`
- [UCI HAR Dataset](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones) (2012) - Smartphone inertial HAR benchmark with subject-wise protocol. `[📦 dataset] [🧪 benchmark]`
- [USC-HAD](https://sipi.usc.edu/had/) (2012) - Wearable sensor activities with multiple subjects and repetitions. `[📦 dataset]`
- [WISDM](https://www.cis.fordham.edu/wisdm/dataset.php) (2011) - Phone/watch accelerometer HAR data with classic activity labels. `[📦 dataset]`

## Lightweight architectures for time-series

- [Hydra](https://arxiv.org/abs/2203.13652) (2022) - Competing convolutional kernels for fast and accurate time-series classification in low-latency settings. `[📄 paper] [⚡ efficient] [🧪 benchmark]`
- [MultiROCKET](https://arxiv.org/abs/2102.00457) (2021) - Extends ROCKET with multiple pooling operators and transformations for faster, accurate time-series classification. `[📄 paper] [⚡ efficient] [🧪 benchmark] [💻 code]`
- [Benchmarking TinyML Systems: Challenges and Direction](https://arxiv.org/abs/2003.04821) (2020) - Surveys TinyML benchmarking challenges, including hardware variability, metrics, and reproducibility constraints for edge deployments. `[📄 paper] [⚡ efficient] [📱 on-device] [🧪 benchmark]`
- [MiniROCKET](https://arxiv.org/abs/2012.08791) (2020) - Faster deterministic ROCKET variant with strong speed-accuracy tradeoff. `[📄 paper] [⚡ efficient] [🧪 benchmark]`
- [EfficientNet](https://arxiv.org/abs/1905.11946) (2019) - Compound scaling principles adaptable to time-series CNNs. `[📄 paper] [⚡ efficient]`
- [InceptionTime](https://arxiv.org/abs/1909.04939) (2019) - Competitive time-series architecture often used as HAR baseline. `[📄 paper] [🧪 benchmark]`
- [MobileNetV3](https://arxiv.org/abs/1905.02244) (2019) - Hardware-aware search and lightweight attention for edge latency. `[📄 paper] [⚡ efficient] [📱 on-device]`
- [ROCKET](https://arxiv.org/abs/1910.13051) (2019) - Fast random convolution features for time-series classification. `[📄 paper] [⚡ efficient] [🧪 benchmark]`
- [MobileNetV2](https://arxiv.org/abs/1801.04381) (2018) - Inverted residuals and linear bottlenecks for compact sensor models. `[📄 paper] [⚡ efficient] [📱 on-device]`
- [ShuffleNet V2](https://arxiv.org/abs/1807.11164) (2018) - Practical efficiency guidelines for real hardware throughput. `[📄 paper] [⚡ efficient] [📱 on-device]`
- [TCN Sequence Modeling](https://arxiv.org/abs/1803.01271) (2018) - Strong and efficient sequence baseline for sensor windows. `[📄 paper] [⚡ efficient]`
- [DeepSense](https://dl.acm.org/doi/10.1145/3090076.3090087) (2017) - Unified deep architecture for mobile sensing signals and tasks. `[📄 paper] [📱 on-device]`
- [MobileNets](https://arxiv.org/abs/1704.04861) (2017) - Depthwise separable convolutions widely reused for mobile HAR backbones. `[📄 paper] [⚡ efficient] [📱 on-device]`
- [ShuffleNet](https://arxiv.org/abs/1707.01083) (2017) - Pointwise group convolution and channel shuffle for low FLOPs. `[📄 paper] [⚡ efficient]`
- [DeepConvLSTM for HAR](https://www.mdpi.com/1424-8220/16/1/115) (2016) - Early strong wearable HAR model combining temporal conv and recurrence. `[📄 paper] [🧪 benchmark]`
- [SqueezeNet](https://arxiv.org/abs/1602.07360) (2016) - Fire modules for very small parameter footprint. `[📄 paper] [⚡ efficient]`

## Attention modules for sensor/time-series

- [PatchTST](https://arxiv.org/abs/2211.14730) (2022) - Patching strategy for efficient transformer-style time-series representation. `[📄 paper] [🧩 attention]`
- [Informer](https://arxiv.org/abs/2012.07436) (2020) - ProbSparse attention for long time-series encoding. `[📄 paper] [🧩 attention] [⚡ efficient]`
- [Linformer](https://arxiv.org/abs/2006.04768) (2020) - Linear-complexity attention approximation for longer windows. `[📄 paper] [🧩 attention] [⚡ efficient]`
- [Performer](https://arxiv.org/abs/2009.14794) (2020) - FAVOR+ linear attention with kernel feature maps. `[📄 paper] [🧩 attention] [⚡ efficient]`
- [ECA-Net](https://arxiv.org/abs/1910.03151) (2019) - Efficient channel attention without heavy dimensionality reduction. `[📄 paper] [🧩 attention] [⚡ efficient]`
- [CBAM](https://arxiv.org/abs/1807.06521) (2018) - Lightweight channel and spatial attention plug-in module. `[📄 paper] [🧩 attention]`
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) (2017) - Transformer self-attention foundation for sequence modeling. `[📄 paper] [🧩 attention]`
- [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507) (2017) - Channel reweighting block often adapted to 1D sensor CNNs. `[📄 paper] [🧩 attention] [⚡ efficient]`

## Knowledge distillation for HAR/time-series

- [DeiT Distillation through Attention](https://arxiv.org/abs/2012.12877) (2020) - Distillation-token strategy transferable to sensor transformers. `[📄 paper] [🧠 distillation] [🧩 attention]`
- [KD-Lib](https://github.com/SforAiDl/KD_Lib) (2020) - Open-source PyTorch distillation framework for rapid experiments. `[💻 code] [🧠 distillation] [🧰 tooling]`
- [MobileBERT](https://arxiv.org/abs/2004.02984) (2020) - Distilled and compressed transformer optimized for mobile. `[📄 paper] [🧠 distillation] [📱 on-device]`
- [DistilBERT](https://arxiv.org/abs/1910.01108) (2019) - Practical distillation recipe for lighter transformer deployment. `[📄 paper] [🧠 distillation] [⚡ efficient]`
- [TinyBERT](https://arxiv.org/abs/1909.10351) (2019) - Multi-stage transformer distillation with layer-wise constraints. `[📄 paper] [🧠 distillation] [⚡ efficient]`
- [Born-Again Neural Networks](https://arxiv.org/abs/1805.04770) (2018) - Self-distillation via sequential teacher-student training. `[📄 paper] [🧠 distillation]`
- [Paying More Attention to Attention](https://arxiv.org/abs/1612.03928) (2016) - Attention transfer losses for compact students. `[📄 paper] [🧠 distillation] [🧩 attention]`
- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) (2015) - Foundational teacher-student distillation objective. `[📄 paper] [🧠 distillation]`
- [FitNets](https://arxiv.org/abs/1412.6550) (2014) - Hint-based intermediate feature matching. `[📄 paper] [🧠 distillation]`

## Quantization/pruning/compression

- [AIMET (AI Model Efficiency Toolkit)](https://github.com/quic/aimet) (2021) - Compression toolkit with quantization and pruning recipes. `[💻 code] [🧰 tooling] [🔧 quantization] [🪓 pruning]`
- [Movement Pruning](https://arxiv.org/abs/2005.07683) (2020) - Structured sparsification for transfer and compression. `[📄 paper] [🪓 pruning]`
- [ONNX Runtime Quantization](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) (2020) - Dynamic and static quantization for portable runtime stacks. `[🧰 tooling] [🔧 quantization]`
- [PyTorch Quantization](https://pytorch.org/docs/stable/quantization.html) (2019) - Eager, FX, and PT2 quantization flows for production models. `[🧰 tooling] [🔧 quantization]`
- [TensorFlow Lite Post-Training Integer Quantization](https://www.tensorflow.org/lite/performance/post_training_integer_quant) (2019) - Full-int8 export path for edge inference. `[🧰 tooling] [🔧 quantization] [📱 on-device]`
- [TensorFlow Model Optimization Toolkit](https://www.tensorflow.org/model_optimization) (2019) - Pruning and quantization-aware training utilities. `[🧰 tooling] [🔧 quantization] [🪓 pruning]`
- [The Lottery Ticket Hypothesis](https://arxiv.org/abs/1803.03635) (2018) - Sparse subnetworks for compact retraining. `[📄 paper] [🪓 pruning]`
- [Deep Compression](https://arxiv.org/abs/1510.00149) (2015) - Classical prune-quantize-Huffman compression pipeline. `[📄 paper] [🪓 pruning] [🔧 quantization]`
- [TensorRT](https://docs.nvidia.com/deeplearning/tensorrt/) (2014) - Deployment-oriented precision and kernel optimization. `[🧰 tooling] [🔧 quantization] [📱 on-device]`

## On-device benchmarking and tooling

- [LiteRT for Microcontrollers](https://ai.google.dev/edge/litert/microcontrollers/overview) (2024) - Official LiteRT microcontroller runtime guide for deploying tiny models on embedded targets. `[🧰 tooling] [📱 on-device]`
- [PyTorch ExecuTorch](https://pytorch.org/executorch/stable/) (2023) - On-device inference runtime and tooling for edge deployment. `[🧰 tooling] [📱 on-device]`
- [Edge Impulse Deployment](https://docs.edgeimpulse.com/studio/projects/deployment) (2021) - Deployment guides for exporting and running edge ML models across embedded and mobile runtimes. `[🧰 tooling] [📱 on-device]`
- [MLPerf Tiny](https://github.com/mlcommons/tiny) (2021) - Standardized tiny and edge benchmarking suite including HAR-relevant tasks. `[🧪 benchmark] [📱 on-device]`
- [TensorFlow Lite Model Analyzer](https://ai.google.dev/edge/api/tflite/python/tf/lite/experimental/Analyzer) (2021) - Inspect model memory and op-level deployment constraints. `[🧰 tooling] [📱 on-device]`
- [TensorFlow Lite Benchmark Tool](https://www.tensorflow.org/lite/performance/measurement) (2019) - CLI profiling for latency and memory on target hardware. `[🧰 tooling] [📱 on-device] [🧪 benchmark]`
- [TensorFlow Lite for Microcontrollers (tflite-micro)](https://github.com/tensorflow/tflite-micro) (2019) - Reference embedded inference runtime and kernels for tiny on-device ML deployments. `[🧰 tooling] [📱 on-device] [💻 code]`
- [Apache TVM](https://tvm.apache.org/docs/) (2018) - End-to-end model compilation stack with microTVM support for constrained edge targets. `[🧰 tooling] [📱 on-device]`
- [CMSIS-NN](https://github.com/ARM-software/CMSIS-NN) (2018) - Optimized neural network kernels for Arm Cortex-M CPUs to accelerate edge inference. `[🧰 tooling] [📱 on-device] [💻 code] [⚡ efficient]`
- [Perfetto](https://perfetto.dev/) (2018) - System-level tracing for CPU scheduling and thermal effects. `[🧰 tooling] [📱 on-device] [🧪 benchmark]`
- [Android Battery Historian](https://developer.android.com/topic/performance/power/setup-battery-historian) (2015) - Power usage inspection to support energy proxy reporting. `[🧰 tooling] [📱 on-device]`
- [Android ADB](https://developer.android.com/tools/adb) (2008) - Essential deployment and repeatable benchmark automation entrypoint. `[🧰 tooling] [📱 on-device]`

## Reproducible benchmarks/leaderboards

- [sktime Benchmarking](https://www.sktime.net/en/stable/api_reference/benchmarking.html) (2022) - Reproducible experiment tooling for time-series models. `[💻 code] [🧰 tooling] [🧪 benchmark]`
- [Monash Time Series Forecasting Repository](https://forecastingdata.org/) (2021) - Protocol and split hygiene references transferable to sensor tasks. `[📦 dataset] [🧪 benchmark]`
- [Papers with Code - Human Activity Recognition](https://paperswithcode.com/task/human-activity-recognition) (2019) - Community benchmark tracking and reproducibility references. `[🧪 benchmark]`
- [UCR Time Series Classification Archive](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/) (2018) - Standardized time-series benchmark collection for sanity checks. `[📦 dataset] [🧪 benchmark]`

## Deployment patterns (windowing/streaming/personalization)

Windowing policy: report window length, stride, overlap, and label-assignment rule; avoid hidden overlap leakage between train and test.
Streaming inference: prefer causal feature extraction and stateful models for low-latency online HAR.
Subject split discipline: always separate users across train/val/test when claiming generalization.
Personalization track: report both cold-start (no user fine-tune) and adaptation (few-shot or calibration) metrics.
Fallback behavior: define unknown and transition states plus confidence thresholds for real-world deployment.
Battery-accuracy tradeoff: jointly report duty cycle, sampling rate, and latency.

## Efficiency reporting checklist for HAR papers

Report these metrics together: parameter count, MACs/FLOPs for the stated input window, end-to-end latency on target hardware, peak memory (RAM and model size), and an energy proxy (power draw, battery drain rate, or joules per inference).

Common pitfalls to document and avoid: window leakage from overlap across data splits, subject split mistakes from random splitting instead of subject-wise splitting, and personalization evaluation without a clear adaptation budget or protocol.

## Edge HAR starter packs

- [Starter pack: Distillation-ready sensor training loop](https://github.com/sumeyye-agac/awesome-efficient-har/blob/main/recipes/knowledge_distillation.md) (2026) - Recipe-backed starter path for teacher-student training experiments. `[🧰 tooling] [🧠 distillation]`
- [Starter pack: Reproducible benchmark harness](https://github.com/sumeyye-agac/awesome-efficient-har/blob/main/recipes/android_latency_benchmark.md) (2026) - Recipe-backed starter path for repeatable Android edge benchmark runs. `[🧰 tooling] [🧪 benchmark]`
- [Starter pack: TFLite Android HAR baseline](https://github.com/sumeyye-agac/awesome-efficient-har/blob/main/recipes/tflite_int8_export.md) (2026) - Recipe-backed starter path for TFLite int8 export and mobile deployment setup. `[🧰 tooling] [📱 on-device]`

MIT license. See https://github.com/sumeyye-agac/awesome-efficient-har/blob/main/LICENSE.
