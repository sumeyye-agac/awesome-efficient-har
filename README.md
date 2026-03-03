# awesome-efficient-har

A curated list of resources for **efficient, edge, and wearable Human Activity Recognition (HAR)**.

Focus areas:
- wearable and smartphone sensor data (IMU, multimodal)
- compact models for time-series HAR
- on-device deployment and reliable benchmarking

## Legend

`[📄 paper]` `[💻 code]` `[📦 dataset]` `[⚡ efficient]` `[📱 on-device]` `[🧪 benchmark]` `[🧠 distillation]` `[🧩 attention]` `[🔧 quantization]` `[🪓 pruning]` `[🧰 tooling]`

## Contents

1. [Datasets (wearable/IMU/multimodal)](#1-datasets-wearableimumultimodal)
2. [Lightweight architectures for time-series](#2-lightweight-architectures-for-time-series)
3. [Attention modules for sensor/time-series](#3-attention-modules-for-sensortime-series)
4. [Knowledge distillation for HAR/time-series](#4-knowledge-distillation-for-hartime-series)
5. [Quantization/pruning/compression](#5-quantizationpruningcompression)
6. [On-device benchmarking and tooling](#6-on-device-benchmarking-and-tooling)
7. [Reproducible benchmarks/leaderboards](#7-reproducible-benchmarksleaderboards)
8. [Deployment patterns (windowing/streaming/personalization)](#8-deployment-patterns-windowingstreamingpersonalization)
9. [Efficiency reporting checklist for HAR papers](#efficiency-reporting-checklist-for-har-papers)
10. [Edge HAR starter packs](#edge-har-starter-packs)

## 1) Datasets (wearable/IMU/multimodal)

- [UCI HAR Dataset](https://archive.ics.uci.edu/dataset/240/human+activity+recognition+using+smartphones) - Smartphone inertial HAR benchmark with subject-wise protocol. `[📦 dataset] [🧪 benchmark]`
- [WISDM](https://www.cis.fordham.edu/wisdm/dataset.php) - Phone/watch accelerometer HAR data with classic activity labels. `[📦 dataset]`
- [PAMAP2 Physical Activity Monitoring](https://archive.ics.uci.edu/dataset/231/pamap2+physical+activity+monitoring) - Multi-sensor IMU + heart-rate recordings. `[📦 dataset] [🧪 benchmark]`
- [OPPORTUNITY Activity Recognition](https://archive.ics.uci.edu/dataset/226/opportunity+activity+recognition) - Rich multimodal ambient and wearable sensor dataset. `[📦 dataset] [🧪 benchmark]`
- [mHealth](https://archive.ics.uci.edu/dataset/319/mhealth+dataset) - Body-worn sensor dataset for activity monitoring. `[📦 dataset]`
- [RealWorld HAR](https://www.uni-mannheim.de/dws/research/projects/activity-recognition/) - Smartphone + smartwatch placement diversity in real-world conditions. `[📦 dataset]`
- [USC-HAD](https://sipi.usc.edu/had/) - Wearable sensor activities with multiple subjects and repetitions. `[📦 dataset]`
- [UniMiB SHAR](http://www.sal.disco.unimib.it/technologies/unimib-shar/) - Smartphone accelerometer ADL + fall events. `[📦 dataset]`
- [SisFall](https://ieee-dataport.org/open-access/sisfall-and-fall-detection-datasets) - Fall detection focused wearable dataset with older-adult scenarios. `[📦 dataset]`
- [Heterogeneity HAR (HHAR)](https://archive.ics.uci.edu/dataset/344/heterogeneity+activity+recognition) - Device and user heterogeneity benchmark across phones/watches. `[📦 dataset] [🧪 benchmark]`
- [MotionSense](https://github.com/mmalekzadeh/motionsense) - iPhone motion data for activity and user context tasks. `[📦 dataset] [💻 code]`
- [SHL Dataset (Sussex-Huawei Locomotion)](http://www.shl-dataset.org/) - Large-scale multimodal wearable/phone locomotion challenge data. `[📦 dataset] [🧪 benchmark]`
- [ExtraSensory](http://extrasensory.ucsd.edu/) - Smartphone + smartwatch + context labels in the wild. `[📦 dataset]`
- [DSADS (Daily and Sports Activities)](https://archive.ics.uci.edu/dataset/256/daily+and+sports+activities) - Body-worn motion sensors across daily and sport actions. `[📦 dataset]`

## 2) Lightweight architectures for time-series

- [MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications](https://arxiv.org/abs/1704.04861) - Depthwise separable convolutions widely reused for mobile HAR backbones. `[📄 paper] [⚡ efficient] [📱 on-device]`
- [MobileNetV2](https://arxiv.org/abs/1801.04381) - Inverted residuals and linear bottlenecks; common baseline for compact sensor models. `[📄 paper] [⚡ efficient] [📱 on-device]`
- [MobileNetV3](https://arxiv.org/abs/1905.02244) - Hardware-aware search + lightweight attention (SE) for edge latency. `[📄 paper] [⚡ efficient] [📱 on-device]`
- [ShuffleNet](https://arxiv.org/abs/1707.01083) - Pointwise group convolution and channel shuffle for low FLOPs. `[📄 paper] [⚡ efficient]`
- [ShuffleNet V2](https://arxiv.org/abs/1807.11164) - Practical efficiency guidelines for real hardware throughput. `[📄 paper] [⚡ efficient] [📱 on-device]`
- [SqueezeNet](https://arxiv.org/abs/1602.07360) - Fire modules for very small parameter footprint. `[📄 paper] [⚡ efficient]`
- [EfficientNet](https://arxiv.org/abs/1905.11946) - Compound scaling principles adaptable to time-series CNNs. `[📄 paper] [⚡ efficient]`
- [TCN: An Empirical Evaluation of Generic Convolutional and Recurrent Networks for Sequence Modeling](https://arxiv.org/abs/1803.01271) - Strong and efficient sequence baseline for sensor windows. `[📄 paper] [⚡ efficient]`
- [ROCKET](https://arxiv.org/abs/1910.13051) - Extremely fast random convolution features for time-series classification. `[📄 paper] [⚡ efficient] [🧪 benchmark]`
- [MiniROCKET](https://arxiv.org/abs/2012.08791) - Faster deterministic ROCKET variant with strong accuracy/speed tradeoff. `[📄 paper] [⚡ efficient] [🧪 benchmark]`
- [InceptionTime](https://arxiv.org/abs/1909.04939) - Competitive time-series architecture often used as HAR baseline. `[📄 paper] [🧪 benchmark]`
- [DeepConvLSTM for HAR](https://www.mdpi.com/1424-8220/16/1/115) - Early strong wearable HAR model combining temporal conv and recurrence. `[📄 paper] [🧪 benchmark]`
- [DeepSense](https://dl.acm.org/doi/10.1145/3090076.3090087) - Unified deep architecture for mobile sensing signals and tasks. `[📄 paper] [📱 on-device]`
- [TinyML Model Optimization Techniques for Embedded AI](https://arxiv.org/abs/2003.04821) - Practical compact-model perspective for MCU/edge deployments. `[📄 paper] [⚡ efficient] [📱 on-device]`

## 3) Attention modules for sensor/time-series

- [Squeeze-and-Excitation Networks](https://arxiv.org/abs/1709.01507) - Channel reweighting block frequently adapted to 1D sensor CNNs. `[📄 paper] [🧩 attention] [⚡ efficient]`
- [CBAM: Convolutional Block Attention Module](https://arxiv.org/abs/1807.06521) - Lightweight channel+spatial attention plug-in. `[📄 paper] [🧩 attention]`
- [ECA-Net](https://arxiv.org/abs/1910.03151) - Efficient channel attention without heavy dimensionality reduction. `[📄 paper] [🧩 attention] [⚡ efficient]`
- [Attention Is All You Need](https://arxiv.org/abs/1706.03762) - Transformer self-attention foundation for sequence modeling. `[📄 paper] [🧩 attention]`
- [Linformer](https://arxiv.org/abs/2006.04768) - Linear-complexity attention approximation for longer windows. `[📄 paper] [🧩 attention] [⚡ efficient]`
- [Performer](https://arxiv.org/abs/2009.14794) - FAVOR+ linear attention with kernel feature maps. `[📄 paper] [🧩 attention] [⚡ efficient]`
- [Informer](https://arxiv.org/abs/2012.07436) - ProbSparse attention for long time-series forecasting and representation. `[📄 paper] [🧩 attention] [⚡ efficient]`
- [PatchTST](https://arxiv.org/abs/2211.14730) - Patching strategy for efficient transformer-style time-series encoding. `[📄 paper] [🧩 attention]`

## 4) Knowledge distillation for HAR/time-series

- [Distilling the Knowledge in a Neural Network](https://arxiv.org/abs/1503.02531) - Foundational teacher-student distillation objective. `[📄 paper] [🧠 distillation]`
- [FitNets](https://arxiv.org/abs/1412.6550) - Hint-based intermediate feature matching. `[📄 paper] [🧠 distillation]`
- [Paying More Attention to Attention](https://arxiv.org/abs/1612.03928) - Attention transfer losses for compact students. `[📄 paper] [🧠 distillation] [🧩 attention]`
- [Born-Again Neural Networks](https://arxiv.org/abs/1805.04770) - Self-distillation via sequential teacher-student training. `[📄 paper] [🧠 distillation]`
- [DistilBERT](https://arxiv.org/abs/1910.01108) - Practical distillation recipe for lighter transformer deployment. `[📄 paper] [🧠 distillation] [⚡ efficient]`
- [MobileBERT](https://arxiv.org/abs/2004.02984) - Distilled and compressed transformer optimized for mobile. `[📄 paper] [🧠 distillation] [📱 on-device]`
- [DeiT: Training data-efficient image transformers & distillation through attention](https://arxiv.org/abs/2012.12877) - Distillation-token strategy transferable to sensor transformers. `[📄 paper] [🧠 distillation] [🧩 attention]`
- [TinyBERT](https://arxiv.org/abs/1909.10351) - Multi-stage transformer distillation with layer-wise constraints. `[📄 paper] [🧠 distillation] [⚡ efficient]`
- [KD-Lib](https://github.com/SforAiDl/KD_Lib) - Open-source PyTorch distillation framework for rapid experiments. `[💻 code] [🧠 distillation] [🧰 tooling]`

## 5) Quantization/pruning/compression

- [Deep Compression](https://arxiv.org/abs/1510.00149) - Classical prune-quantize-Huffman pipeline. `[📄 paper] [🪓 pruning] [🔧 quantization]`
- [The Lottery Ticket Hypothesis](https://arxiv.org/abs/1803.03635) - Sparse subnetworks for compact retraining. `[📄 paper] [🪓 pruning]`
- [Movement Pruning](https://arxiv.org/abs/2005.07683) - Structured sparsification for transfer and compression. `[📄 paper] [🪓 pruning]`
- [TensorFlow Model Optimization Toolkit](https://www.tensorflow.org/model_optimization) - Pruning and quantization-aware training utilities. `[🧰 tooling] [🔧 quantization] [🪓 pruning]`
- [TensorFlow Lite Post-Training Integer Quantization](https://www.tensorflow.org/lite/performance/post_training_integer_quant) - Full-int8 export path for edge inference. `[🧰 tooling] [🔧 quantization] [📱 on-device]`
- [PyTorch Quantization](https://pytorch.org/docs/stable/quantization.html) - Eager/FX/PT2 quantization flows for production models. `[🧰 tooling] [🔧 quantization]`
- [ONNX Runtime Quantization](https://onnxruntime.ai/docs/performance/model-optimizations/quantization.html) - Dynamic/static quantization for portable runtime stacks. `[🧰 tooling] [🔧 quantization]`
- [AIMET (AI Model Efficiency Toolkit)](https://github.com/quic/aimet) - Compression toolkit with quantization and pruning recipes. `[💻 code] [🧰 tooling] [🔧 quantization] [🪓 pruning]`
- [TensorRT Model Optimizer](https://docs.nvidia.com/deeplearning/tensorrt/) - Deployment-oriented precision and kernel optimization. `[🧰 tooling] [🔧 quantization] [📱 on-device]`

## 6) On-device benchmarking and tooling

- [TensorFlow Lite Benchmark Tool](https://www.tensorflow.org/lite/performance/measurement) - CLI profiling for latency and memory on target hardware. `[🧰 tooling] [📱 on-device] [🧪 benchmark]`
- [MLPerf Tiny](https://mlcommons.org/benchmarks/tiny/) - Standardized tiny/edge benchmarking suite including HAR-relevant tasks. `[🧪 benchmark] [📱 on-device]`
- [Android ADB](https://developer.android.com/tools/adb) - Essential deployment and repeatable benchmark automation entrypoint. `[🧰 tooling] [📱 on-device]`
- [Perfetto](https://perfetto.dev/) - System-level tracing for CPU scheduling and thermal effects. `[🧰 tooling] [📱 on-device] [🧪 benchmark]`
- [Android Battery Historian](https://developer.android.com/topic/performance/power/setup-battery-historian) - Power usage inspection to support energy proxy reporting. `[🧰 tooling] [📱 on-device]`
- [PyTorch ExecuTorch](https://pytorch.org/executorch/stable/) - On-device inference runtime and tooling for edge deployment. `[🧰 tooling] [📱 on-device]`
- [TensorFlow Lite Model Analyzer](https://www.tensorflow.org/lite/performance/model_analyzer) - Inspect model memory and op-level deployment constraints. `[🧰 tooling] [📱 on-device]`

## 7) Reproducible benchmarks/leaderboards

- [Papers with Code: Human Activity Recognition](https://paperswithcode.com/task/human-activity-recognition) - Community benchmark tracking and reproducibility references. `[🧪 benchmark]`
- [UCR Time Series Classification Archive](https://www.cs.ucr.edu/~eamonn/time_series_data_2018/) - Standardized time-series benchmark collection for quick sanity checks. `[📦 dataset] [🧪 benchmark]`
- [Monash Time Series Forecasting Repository](https://forecastingdata.org/) - Protocol ideas and split hygiene transferable to sensor tasks. `[📦 dataset] [🧪 benchmark]`
- [sktime Benchmarking](https://www.sktime.net/en/stable/examples/benchmarking.html) - Reproducible experiment tooling for time-series models. `[💻 code] [🧰 tooling] [🧪 benchmark]`

## 8) Deployment patterns (windowing/streaming/personalization)

- **Windowing policy**: Report window length, stride, overlap, and label-assignment rule; avoid hidden overlap leakage between train and test.
- **Streaming inference**: Prefer causal feature extraction and stateful models for low-latency online HAR.
- **Subject split discipline**: Always separate users across train/val/test when claiming generalization.
- **Personalization track**: Report both cold-start (no user fine-tune) and adaptation (few-shot or calibration) metrics.
- **Fallback behavior**: Define unknown/transition states and confidence thresholds for real-world deployment.
- **Battery-accuracy tradeoff**: Jointly report duty cycle, sampling rate, and latency.

## Efficiency reporting checklist for HAR papers

Report these metrics together:
- Parameter count
- MACs/FLOPs (for stated input window)
- End-to-end latency on target hardware
- Peak memory (RAM and model size)
- Energy proxy (power draw, battery drain rate, or joules/inference)

Common pitfalls to document and avoid:
- Window leakage from overlap across data splits
- Subject split mistakes (random split instead of subject-wise split)
- Personalization evaluation without clear adaptation budget or protocol

## Edge HAR starter packs

- **Starter pack: TFLite Android HAR baseline** - placeholder template path: `templates/tflite-android-har/` `(check link)`
- **Starter pack: Distillation-ready sensor training loop** - placeholder template path: `templates/har-kd-pytorch/` `(check link)`
- **Starter pack: Reproducible benchmark harness** - placeholder template path: `templates/har-benchmark-harness/` `(check link)`

## Related recipes

- [Knowledge distillation recipe](recipes/knowledge_distillation.md)
- [TFLite int8 export recipe](recipes/tflite_int8_export.md)
- [Android latency benchmark recipe](recipes/android_latency_benchmark.md)

## License

List content is released under [CC0-1.0](LICENSE).
