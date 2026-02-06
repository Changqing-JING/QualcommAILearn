execute: total host time: 9.0 [ms]

```
adb shell "export LD_LIBRARY_PATH=/data/local/tmp/aarch64-android && cd /data/local/tmp && ./qnn-sample-app --backend /data/local/tmp/aarch64-android/libQnnGpu.so --dlc_path efficientnet_b0-qnn_dlc-float/efficientnet_b0.dlc --input_list input_list.txt --output_dir output --system_library /data/local/tmp/aarch64-android/libQnnSystem.so"
     0.0ms [  INFO ] Backend: /data/local/tmp/aarch64-android/libQnnGpu.so
     3.8ms [  INFO ] Model wasn't loaded from a shared library.
     6.7ms [  INFO ] qnn-sample-app build version: v2.42.0.251225135753_193295
     6.7ms [  INFO ] Backend        build version: v2.42.0.251225135753_193295
     6.8ms [  INFO ] Initializing logging in the backend. Callback: [0x56e23dc458], Log Level: [3]
     0.0ms [  INFO ] QNN API Version: 2.32.0
     0.0ms [  INFO ] QNN GPU API Version: 3.12.0
     1.3ms [  INFO ] Found /vendor/lib64/libOpenCL.so
    28.1ms [  INFO ] Successfully resolved extension function clGetDeviceImageInfoQCOM using clGetExtensionFunctionAddressForPlatform
    28.1ms [  INFO ] Successfully resolved extension function clSetPerfHintQCOM using clGetExtensionFunctionAddressForPlatform
    28.1ms [  INFO ] Successfully resolved extension function clNewRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    28.1ms [  INFO ] Successfully resolved extension function clEndRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    28.1ms [  INFO ] Successfully resolved extension function clReleaseRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    28.1ms [  INFO ] Successfully resolved extension function clRetainRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    28.1ms [  INFO ] Successfully resolved extension function clEnqueueRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    28.2ms [  INFO ] Device version: 3.0    Device tier: 830
    28.2ms [  INFO ] OpenCL Driver version: OpenCL 3.0 QUALCOMM build: 0800.35 Compiler E031.47.18.28
    72.9ms [  INFO ] QnnOpPackage: v2.0.0
     0.0ms [  INFO ] Creating operation package: qti.aisw
     0.1ms [  INFO ] Found /vendor/lib64/libOpenCL.so
    73.2ms [  INFO ] QnnOpPackage: qti.aisw
    80.1ms [  INFO ] Initialize Backend Returned Status = 0
    73.4ms [  INFO ] Found /vendor/lib64/libOpenCL.so
    73.5ms [  INFO ] Successfully resolved extension function clGetDeviceImageInfoQCOM using clGetExtensionFunctionAddressForPlatform
    73.5ms [  INFO ] Successfully resolved extension function clSetPerfHintQCOM using clGetExtensionFunctionAddressForPlatform
    73.5ms [  INFO ] Successfully resolved extension function clNewRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    73.5ms [  INFO ] Successfully resolved extension function clEndRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    73.5ms [  INFO ] Successfully resolved extension function clReleaseRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    73.5ms [  INFO ] Successfully resolved extension function clRetainRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    73.5ms [  INFO ] Successfully resolved extension function clEnqueueRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    80.4ms [  INFO ] DLC path provided, using DLC-based graph composition
    80.4ms [  INFO ] Composing graphs from DLC
    80.4ms [  INFO ] Creating DLC handle from file: efficientnet_b0-qnn_dlc-float/efficientnet_b0.dlc
    80.4ms [  INFO ] Initializing logging in the System Library for DLC. Callback: [0x56e23dc458], Log Level: [3]
    81.1ms [  INFO ] Successfully created DLC handle
    81.1ms [  INFO ] Composing graphs from DLC
    81.1ms [  INFO ] Calling systemDlcComposeGraphs
    77.3ms [  INFO ] Graph precision mode is user provided
    77.3ms [  INFO ] Memory Optimizations enabled
    77.3ms [  INFO ] Node Optimizations enabled
    77.3ms [  INFO ] Queue Recording enabled
   111.3ms [  INFO ] Successfully composed 1 graphs from DLC
   111.3ms [  INFO ] Successfully composed 1 graphs from DLC
   104.5ms [  INFO ] QnnGraph_finalize: start
    32.4ms [  INFO ] Creating operations:
    32.4ms [  INFO ]   ElementWiseBinary
    32.4ms [  INFO ]   ElementWiseBinary
    32.6ms [  INFO ] Create operation: Conv2d
    32.6ms [  INFO ] Create operation: ElementWiseNeuron
    32.6ms [  INFO ] Create operation: ElementWiseBinary
    32.7ms [  INFO ] Create operation: DepthWiseConv2d
    32.7ms [  INFO ] Create operation: ElementWiseNeuron
    32.7ms [  INFO ] Create operation: ElementWiseBinary
    32.8ms [  INFO ] Create operation: PoolAvg2d
    32.8ms [  INFO ] Create operation: Conv2d
    32.8ms [  INFO ] Create operation: ElementWiseNeuron
    32.8ms [  INFO ] Create operation: ElementWiseBinary
    32.9ms [  INFO ] Creating operations:
    32.9ms [  INFO ]   Conv2d
    32.9ms [  INFO ]   ElementWiseNeuron
    32.9ms [  INFO ] Create operation: ElementWiseBinary
    32.9ms [  INFO ] Create operation: Conv2d
    33.0ms [  INFO ] Create operation: Conv2d
    33.0ms [  INFO ] Create operation: ElementWiseNeuron
    33.0ms [  INFO ] Create operation: ElementWiseBinary
    33.0ms [  INFO ] Create operation: DepthWiseConv2d
    33.0ms [  INFO ] Create operation: ElementWiseNeuron
    33.0ms [  INFO ] Create operation: ElementWiseBinary
    33.1ms [  INFO ] Create operation: PoolAvg2d
    33.1ms [  INFO ] Create operation: Conv2d
    33.1ms [  INFO ] Create operation: ElementWiseNeuron
    33.1ms [  INFO ] Create operation: ElementWiseBinary
    33.1ms [  INFO ] Creating operations:
    33.1ms [  INFO ]   Conv2d
    33.1ms [  INFO ]   ElementWiseNeuron
    33.2ms [  INFO ] Create operation: ElementWiseBinary
    33.2ms [  INFO ] Create operation: Conv2d
    33.2ms [  INFO ] Create operation: Conv2d
    33.2ms [  INFO ] Create operation: ElementWiseNeuron
    33.2ms [  INFO ] Create operation: ElementWiseBinary
    33.2ms [  INFO ] Create operation: DepthWiseConv2d
    33.3ms [  INFO ] Create operation: ElementWiseNeuron
    33.3ms [  INFO ] Create operation: ElementWiseBinary
    33.3ms [  INFO ] Create operation: PoolAvg2d
    33.3ms [  INFO ] Create operation: Conv2d
    33.3ms [  INFO ] Create operation: ElementWiseNeuron
    33.3ms [  INFO ] Create operation: ElementWiseBinary
    33.4ms [  INFO ] Creating operations:
    33.4ms [  INFO ]   Conv2d
    33.4ms [  INFO ]   ElementWiseNeuron
    33.4ms [  INFO ] Create operation: ElementWiseBinary
    33.4ms [  INFO ] Create operation: Conv2d
    33.4ms [  INFO ] Create operation: ElementWiseBinary
    33.4ms [  INFO ] Create operation: Conv2d
    33.4ms [  INFO ] Create operation: ElementWiseNeuron
    33.4ms [  INFO ] Create operation: ElementWiseBinary
    33.5ms [  INFO ] Create operation: DepthWiseConv2d
    33.5ms [  INFO ] Create operation: ElementWiseNeuron
    33.5ms [  INFO ] Create operation: ElementWiseBinary
    33.5ms [  INFO ] Create operation: PoolAvg2d
    33.5ms [  INFO ] Create operation: Conv2d
    33.6ms [  INFO ] Create operation: ElementWiseNeuron
    33.6ms [  INFO ] Create operation: ElementWiseBinary
    33.6ms [  INFO ] Creating operations:
    33.6ms [  INFO ]   Conv2d
    33.6ms [  INFO ]   ElementWiseNeuron
    33.6ms [  INFO ] Create operation: ElementWiseBinary
    33.6ms [  INFO ] Create operation: Conv2d
    33.6ms [  INFO ] Create operation: Conv2d
    33.7ms [  INFO ] Create operation: ElementWiseNeuron
    33.7ms [  INFO ] Create operation: ElementWiseBinary
    33.7ms [  INFO ] Create operation: DepthWiseConv2d
    33.7ms [  INFO ] Create operation: ElementWiseNeuron
    33.7ms [  INFO ] Create operation: ElementWiseBinary
    33.7ms [  INFO ] Create operation: PoolAvg2d
    33.7ms [  INFO ] Create operation: Conv2d
    33.8ms [  INFO ] Create operation: ElementWiseNeuron
    33.8ms [  INFO ] Create operation: ElementWiseBinary
    33.8ms [  INFO ] Creating operations:
    33.8ms [  INFO ]   Conv2d
    33.8ms [  INFO ]   ElementWiseNeuron
    33.8ms [  INFO ] Create operation: ElementWiseBinary
    33.8ms [  INFO ] Create operation: Conv2d
    33.8ms [  INFO ] Create operation: ElementWiseBinary
    33.9ms [  INFO ] Create operation: Conv2d
    33.9ms [  INFO ] Create operation: ElementWiseNeuron
    33.9ms [  INFO ] Create operation: ElementWiseBinary
    33.9ms [  INFO ] Create operation: DepthWiseConv2d
    33.9ms [  INFO ] Create operation: ElementWiseNeuron
    33.9ms [  INFO ] Create operation: ElementWiseBinary
    33.9ms [  INFO ] Create operation: PoolAvg2d
    34.0ms [  INFO ] Create operation: Conv2d
    34.0ms [  INFO ] Create operation: ElementWiseNeuron
    34.0ms [  INFO ] Create operation: ElementWiseBinary
    34.0ms [  INFO ] Creating operations:
    34.0ms [  INFO ]   Conv2d
    34.0ms [  INFO ]   ElementWiseNeuron
    34.0ms [  INFO ] Create operation: ElementWiseBinary
    34.0ms [  INFO ] Create operation: Conv2d
    34.1ms [  INFO ] Create operation: Conv2d
    34.1ms [  INFO ] Create operation: ElementWiseNeuron
    34.1ms [  INFO ] Create operation: ElementWiseBinary
    34.1ms [  INFO ] Create operation: DepthWiseConv2d
    34.1ms [  INFO ] Create operation: ElementWiseNeuron
    34.1ms [  INFO ] Create operation: ElementWiseBinary
    34.2ms [  INFO ] Create operation: PoolAvg2d
    34.2ms [  INFO ] Create operation: Conv2d
    34.2ms [  INFO ] Create operation: ElementWiseNeuron
    34.2ms [  INFO ] Create operation: ElementWiseBinary
    34.2ms [  INFO ] Creating operations:
    34.2ms [  INFO ]   Conv2d
    34.2ms [  INFO ]   ElementWiseNeuron
    34.2ms [  INFO ] Create operation: ElementWiseBinary
    34.2ms [  INFO ] Create operation: Conv2d
    34.3ms [  INFO ] Create operation: ElementWiseBinary
    34.3ms [  INFO ] Create operation: Conv2d
    34.3ms [  INFO ] Create operation: ElementWiseNeuron
    34.3ms [  INFO ] Create operation: ElementWiseBinary
    34.3ms [  INFO ] Create operation: DepthWiseConv2d
    34.3ms [  INFO ] Create operation: ElementWiseNeuron
    34.4ms [  INFO ] Create operation: ElementWiseBinary
    34.4ms [  INFO ] Create operation: PoolAvg2d
    34.4ms [  INFO ] Create operation: Conv2d
    34.4ms [  INFO ] Create operation: ElementWiseNeuron
    34.4ms [  INFO ] Create operation: ElementWiseBinary
    34.4ms [  INFO ] Creating operations:
    34.4ms [  INFO ]   Conv2d
    34.4ms [  INFO ]   ElementWiseNeuron
    34.4ms [  INFO ] Create operation: ElementWiseBinary
    34.5ms [  INFO ] Create operation: Conv2d
    34.5ms [  INFO ] Create operation: ElementWiseBinary
    34.5ms [  INFO ] Create operation: Conv2d
    34.5ms [  INFO ] Create operation: ElementWiseNeuron
    34.6ms [  INFO ] Create operation: ElementWiseBinary
    34.6ms [  INFO ] Create operation: DepthWiseConv2d
    34.6ms [  INFO ] Create operation: ElementWiseNeuron
    34.6ms [  INFO ] Create operation: ElementWiseBinary
    34.7ms [  INFO ] Create operation: PoolAvg2d
    34.7ms [  INFO ] Create operation: Conv2d
    34.7ms [  INFO ] Create operation: ElementWiseNeuron
    34.7ms [  INFO ] Create operation: ElementWiseBinary
    34.7ms [  INFO ] Creating operations:
    34.7ms [  INFO ]   Conv2d
    34.7ms [  INFO ]   ElementWiseNeuron
    34.7ms [  INFO ] Create operation: ElementWiseBinary
    34.7ms [  INFO ] Create operation: Conv2d
    34.8ms [  INFO ] Create operation: Conv2d
    34.8ms [  INFO ] Create operation: ElementWiseNeuron
    34.8ms [  INFO ] Create operation: ElementWiseBinary
    34.8ms [  INFO ] Create operation: DepthWiseConv2d
    34.8ms [  INFO ] Create operation: ElementWiseNeuron
    34.8ms [  INFO ] Create operation: ElementWiseBinary
    34.9ms [  INFO ] Create operation: PoolAvg2d
    34.9ms [  INFO ] Create operation: Conv2d
    34.9ms [  INFO ] Create operation: ElementWiseNeuron
    34.9ms [  INFO ] Create operation: ElementWiseBinary
    34.9ms [  INFO ] Creating operations:
    34.9ms [  INFO ]   Conv2d
    34.9ms [  INFO ]   ElementWiseNeuron
    34.9ms [  INFO ] Create operation: ElementWiseBinary
    34.9ms [  INFO ] Create operation: Conv2d
    35.0ms [  INFO ] Create operation: ElementWiseBinary
    35.0ms [  INFO ] Create operation: Conv2d
    35.0ms [  INFO ] Create operation: ElementWiseNeuron
    35.0ms [  INFO ] Create operation: ElementWiseBinary
    35.0ms [  INFO ] Create operation: DepthWiseConv2d
    35.0ms [  INFO ] Create operation: ElementWiseNeuron
    35.0ms [  INFO ] Create operation: ElementWiseBinary
    35.0ms [  INFO ] Create operation: PoolAvg2d
    35.1ms [  INFO ] Create operation: Conv2d
    35.1ms [  INFO ] Create operation: ElementWiseNeuron
    35.1ms [  INFO ] Create operation: ElementWiseBinary
    35.1ms [  INFO ] Creating operations:
    35.1ms [  INFO ]   Conv2d
    35.1ms [  INFO ]   ElementWiseNeuron
    35.1ms [  INFO ] Create operation: ElementWiseBinary
    35.1ms [  INFO ] Create operation: Conv2d
    35.2ms [  INFO ] Create operation: ElementWiseBinary
    35.2ms [  INFO ] Create operation: Conv2d
    35.2ms [  INFO ] Create operation: ElementWiseNeuron
    35.2ms [  INFO ] Create operation: ElementWiseBinary
    35.2ms [  INFO ] Create operation: DepthWiseConv2d
    35.2ms [  INFO ] Create operation: ElementWiseNeuron
    35.2ms [  INFO ] Create operation: ElementWiseBinary
    35.3ms [  INFO ] Create operation: PoolAvg2d
    35.3ms [  INFO ] Create operation: Conv2d
    35.3ms [  INFO ] Create operation: ElementWiseNeuron
    35.3ms [  INFO ] Create operation: ElementWiseBinary
    35.3ms [  INFO ] Creating operations:
    35.3ms [  INFO ]   Conv2d
    35.3ms [  INFO ]   ElementWiseNeuron
    35.3ms [  INFO ] Create operation: ElementWiseBinary
    35.3ms [  INFO ] Create operation: Conv2d
    35.4ms [  INFO ] Create operation: Conv2d
    35.4ms [  INFO ] Create operation: ElementWiseNeuron
    35.4ms [  INFO ] Create operation: ElementWiseBinary
    35.4ms [  INFO ] Create operation: DepthWiseConv2d
    35.4ms [  INFO ] Create operation: ElementWiseNeuron
    35.4ms [  INFO ] Create operation: ElementWiseBinary
    35.4ms [  INFO ] Create operation: PoolAvg2d
    35.5ms [  INFO ] Create operation: Conv2d
    35.5ms [  INFO ] Create operation: ElementWiseNeuron
    35.5ms [  INFO ] Create operation: ElementWiseBinary
    35.5ms [  INFO ] Creating operations:
    35.5ms [  INFO ]   Conv2d
    35.5ms [  INFO ]   ElementWiseNeuron
    35.5ms [  INFO ] Create operation: ElementWiseBinary
    35.5ms [  INFO ] Create operation: Conv2d
    35.5ms [  INFO ] Create operation: ElementWiseBinary
    35.6ms [  INFO ] Create operation: Conv2d
    35.6ms [  INFO ] Create operation: ElementWiseNeuron
    35.6ms [  INFO ] Create operation: ElementWiseBinary
    35.6ms [  INFO ] Create operation: DepthWiseConv2d
    35.6ms [  INFO ] Create operation: ElementWiseNeuron
    35.6ms [  INFO ] Create operation: ElementWiseBinary
    35.6ms [  INFO ] Create operation: PoolAvg2d
    35.6ms [  INFO ] Create operation: Conv2d
    35.7ms [  INFO ] Create operation: ElementWiseNeuron
    35.7ms [  INFO ] Create operation: ElementWiseBinary
    35.7ms [  INFO ] Creating operations:
    35.7ms [  INFO ]   Conv2d
    35.7ms [  INFO ]   ElementWiseNeuron
    35.7ms [  INFO ] Create operation: ElementWiseBinary
    35.7ms [  INFO ] Create operation: Conv2d
    35.7ms [  INFO ] Create operation: ElementWiseBinary
    35.8ms [  INFO ] Create operation: Conv2d
    35.8ms [  INFO ] Create operation: ElementWiseNeuron
    35.8ms [  INFO ] Create operation: ElementWiseBinary
    35.8ms [  INFO ] Create operation: DepthWiseConv2d
    35.8ms [  INFO ] Create operation: ElementWiseNeuron
    35.8ms [  INFO ] Create operation: ElementWiseBinary
    35.8ms [  INFO ] Create operation: PoolAvg2d
    35.9ms [  INFO ] Create operation: Conv2d
    35.9ms [  INFO ] Create operation: ElementWiseNeuron
    35.9ms [  INFO ] Create operation: ElementWiseBinary
    35.9ms [  INFO ] Creating operations:
    35.9ms [  INFO ]   Conv2d
    35.9ms [  INFO ]   ElementWiseNeuron
    35.9ms [  INFO ] Create operation: ElementWiseBinary
    35.9ms [  INFO ] Create operation: Conv2d
    35.9ms [  INFO ] Create operation: ElementWiseBinary
    36.0ms [  INFO ] Create operation: Conv2d
    36.0ms [  INFO ] Create operation: ElementWiseNeuron
    36.0ms [  INFO ] Create operation: ElementWiseBinary
    36.0ms [  INFO ] Create operation: DepthWiseConv2d
    36.0ms [  INFO ] Create operation: ElementWiseNeuron
    36.0ms [  INFO ] Create operation: ElementWiseBinary
    36.0ms [  INFO ] Create operation: PoolAvg2d
    36.0ms [  INFO ] Create operation: Conv2d
    36.1ms [  INFO ] Create operation: ElementWiseNeuron
    36.1ms [  INFO ] Create operation: ElementWiseBinary
    36.1ms [  INFO ] Creating operations:
    36.1ms [  INFO ]   Conv2d
    36.1ms [  INFO ]   ElementWiseNeuron
    36.1ms [  INFO ] Create operation: ElementWiseBinary
    36.1ms [  INFO ] Create operation: Conv2d
    36.2ms [  INFO ] Create operation: Conv2d
    36.2ms [  INFO ] Create operation: ElementWiseNeuron
    36.2ms [  INFO ] Create operation: ElementWiseBinary
    36.2ms [  INFO ] Create operation: PoolAvg2d
    36.2ms [  INFO ] Create operation: Transpose
    36.2ms [  INFO ] Create operation: FullyConnected
    36.3ms [  INFO ] Create operation: Reshape
   711.4ms [  INFO ] finalize: total host time: 606.9 [ms]
   711.4ms [  INFO ] QnnGraph_finalize: finish
   711.7ms [  INFO ] QnnGraph_execute: start
   720.8ms [  INFO ] execute: total host time: 9.0 [ms]
   720.8ms [  INFO ] QnnGraph_execute: finish
   727.7ms [  INFO ] cleaning up resources for input tensors
   727.7ms [  INFO ] cleaning up resources for output tensors
```
