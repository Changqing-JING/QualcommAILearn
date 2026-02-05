```
     0.0ms [  INFO ] Backend: /data/local/tmp/aarch64-android/libQnnGpu.so
     4.1ms [  INFO ] Model wasn't loaded from a shared library.
     7.3ms [  INFO ] qnn-sample-app build version: v2.42.0.251225135753_193295
     7.3ms [  INFO ] Backend        build version: v2.42.0.251225135753_193295
     7.4ms [  INFO ] Initializing logging in the backend. Callback: [0x648bbb7458], Log Level: [3]
     0.0ms [  INFO ] QNN API Version: 2.32.0
     0.0ms [  INFO ] QNN GPU API Version: 3.12.0
     0.8ms [  INFO ] Found /vendor/lib64/libOpenCL.so
    19.8ms [  INFO ] Successfully resolved extension function clGetDeviceImageInfoQCOM using clGetExtensionFunctionAddressForPlatform
    19.8ms [  INFO ] Successfully resolved extension function clSetPerfHintQCOM using clGetExtensionFunctionAddressForPlatform
    19.8ms [  INFO ] Successfully resolved extension function clNewRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    19.8ms [  INFO ] Successfully resolved extension function clEndRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    19.8ms [  INFO ] Successfully resolved extension function clReleaseRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    19.8ms [  INFO ] Successfully resolved extension function clRetainRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    19.8ms [  INFO ] Successfully resolved extension function clEnqueueRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    19.9ms [  INFO ] Device version: 3.0    Device tier: 830
    19.9ms [  INFO ] OpenCL Driver version: OpenCL 3.0 QUALCOMM build: 0800.35 Compiler E031.47.18.28
    46.1ms [  INFO ] QnnOpPackage: v2.0.0
     0.0ms [  INFO ] Creating operation package: qti.aisw
     0.1ms [  INFO ] Found /vendor/lib64/libOpenCL.so
    46.3ms [  INFO ] QnnOpPackage: qti.aisw
    53.8ms [  INFO ] Initialize Backend Returned Status = 0
    46.5ms [  INFO ] Found /vendor/lib64/libOpenCL.so
    46.6ms [  INFO ] Successfully resolved extension function clGetDeviceImageInfoQCOM using clGetExtensionFunctionAddressForPlatform
    46.6ms [  INFO ] Successfully resolved extension function clSetPerfHintQCOM using clGetExtensionFunctionAddressForPlatform
    46.6ms [  INFO ] Successfully resolved extension function clNewRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    46.6ms [  INFO ] Successfully resolved extension function clEndRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    46.6ms [  INFO ] Successfully resolved extension function clReleaseRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    46.6ms [  INFO ] Successfully resolved extension function clRetainRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    46.6ms [  INFO ] Successfully resolved extension function clEnqueueRecordingQCOM using clGetExtensionFunctionAddressForPlatform
    54.1ms [  INFO ] DLC path provided, using DLC-based graph composition
    54.1ms [  INFO ] Composing graphs from DLC
    54.1ms [  INFO ] Creating DLC handle from file: efficientnet_b0-qnn_dlc-float/efficientnet_b0.dlc
    54.1ms [  INFO ] Initializing logging in the System Library for DLC. Callback: [0x648bbb7458], Log Level: [3]
    54.6ms [  INFO ] Successfully created DLC handle
    54.6ms [  INFO ] Composing graphs from DLC
    54.6ms [  INFO ] Calling systemDlcComposeGraphs
    48.9ms [  INFO ] Graph precision mode is user provided
    48.9ms [  INFO ] Memory Optimizations enabled
    48.9ms [  INFO ] Node Optimizations enabled
    48.9ms [  INFO ] Queue Recording enabled
    76.1ms [  INFO ] Successfully composed 1 graphs from DLC
    76.2ms [  INFO ] Successfully composed 1 graphs from DLC
    68.8ms [  INFO ] QnnGraph_finalize: start
    23.4ms [  INFO ] Creating operations:
    23.4ms [  INFO ]   ElementWiseBinary
    23.4ms [  INFO ]   ElementWiseBinary
    23.6ms [  INFO ] Create operation: Conv2d
    23.7ms [  INFO ] Create operation: ElementWiseNeuron
    23.7ms [  INFO ] Create operation: ElementWiseBinary
    23.7ms [  INFO ] Create operation: DepthWiseConv2d
    23.8ms [  INFO ] Create operation: ElementWiseNeuron
    23.8ms [  INFO ] Create operation: ElementWiseBinary
    23.8ms [  INFO ] Create operation: PoolAvg2d
    23.8ms [  INFO ] Create operation: Conv2d
    23.9ms [  INFO ] Create operation: ElementWiseNeuron
    23.9ms [  INFO ] Create operation: ElementWiseBinary
    23.9ms [  INFO ] Creating operations:
    23.9ms [  INFO ]   Conv2d
    23.9ms [  INFO ]   ElementWiseNeuron
    24.0ms [  INFO ] Create operation: ElementWiseBinary
    24.0ms [  INFO ] Create operation: Conv2d
    24.1ms [  INFO ] Create operation: Conv2d
    24.1ms [  INFO ] Create operation: ElementWiseNeuron
    24.1ms [  INFO ] Create operation: ElementWiseBinary
    24.1ms [  INFO ] Create operation: DepthWiseConv2d
    24.2ms [  INFO ] Create operation: ElementWiseNeuron
    24.2ms [  INFO ] Create operation: ElementWiseBinary
    24.2ms [  INFO ] Create operation: PoolAvg2d
    24.2ms [  INFO ] Create operation: Conv2d
    24.3ms [  INFO ] Create operation: ElementWiseNeuron
    24.3ms [  INFO ] Create operation: ElementWiseBinary
    24.3ms [  INFO ] Creating operations:
    24.3ms [  INFO ]   Conv2d
    24.3ms [  INFO ]   ElementWiseNeuron
    24.3ms [  INFO ] Create operation: ElementWiseBinary
    24.3ms [  INFO ] Create operation: Conv2d
    24.4ms [  INFO ] Create operation: Conv2d
    24.4ms [  INFO ] Create operation: ElementWiseNeuron
    24.4ms [  INFO ] Create operation: ElementWiseBinary
    24.5ms [  INFO ] Create operation: DepthWiseConv2d
    24.5ms [  INFO ] Create operation: ElementWiseNeuron
    24.5ms [  INFO ] Create operation: ElementWiseBinary
    24.5ms [  INFO ] Create operation: PoolAvg2d
    24.5ms [  INFO ] Create operation: Conv2d
    24.6ms [  INFO ] Create operation: ElementWiseNeuron
    24.6ms [  INFO ] Create operation: ElementWiseBinary
    24.6ms [  INFO ] Creating operations:
    24.6ms [  INFO ]   Conv2d
    24.6ms [  INFO ]   ElementWiseNeuron
    24.6ms [  INFO ] Create operation: ElementWiseBinary
    24.7ms [  INFO ] Create operation: Conv2d
    24.7ms [  INFO ] Create operation: ElementWiseBinary
    24.7ms [  INFO ] Create operation: Conv2d
    24.7ms [  INFO ] Create operation: ElementWiseNeuron
    24.7ms [  INFO ] Create operation: ElementWiseBinary
    24.8ms [  INFO ] Create operation: DepthWiseConv2d
    24.8ms [  INFO ] Create operation: ElementWiseNeuron
    24.8ms [  INFO ] Create operation: ElementWiseBinary
    24.8ms [  INFO ] Create operation: PoolAvg2d
    24.8ms [  INFO ] Create operation: Conv2d
    24.9ms [  INFO ] Create operation: ElementWiseNeuron
    24.9ms [  INFO ] Create operation: ElementWiseBinary
    24.9ms [  INFO ] Creating operations:
    24.9ms [  INFO ]   Conv2d
    24.9ms [  INFO ]   ElementWiseNeuron
    24.9ms [  INFO ] Create operation: ElementWiseBinary
    25.0ms [  INFO ] Create operation: Conv2d
    25.0ms [  INFO ] Create operation: Conv2d
    25.0ms [  INFO ] Create operation: ElementWiseNeuron
    25.0ms [  INFO ] Create operation: ElementWiseBinary
    25.1ms [  INFO ] Create operation: DepthWiseConv2d
    25.1ms [  INFO ] Create operation: ElementWiseNeuron
    25.1ms [  INFO ] Create operation: ElementWiseBinary
    25.1ms [  INFO ] Create operation: PoolAvg2d
    25.1ms [  INFO ] Create operation: Conv2d
    25.2ms [  INFO ] Create operation: ElementWiseNeuron
    25.2ms [  INFO ] Create operation: ElementWiseBinary
    25.2ms [  INFO ] Creating operations:
    25.2ms [  INFO ]   Conv2d
    25.2ms [  INFO ]   ElementWiseNeuron
    25.2ms [  INFO ] Create operation: ElementWiseBinary
    25.3ms [  INFO ] Create operation: Conv2d
    25.3ms [  INFO ] Create operation: ElementWiseBinary
    25.3ms [  INFO ] Create operation: Conv2d
    25.3ms [  INFO ] Create operation: ElementWiseNeuron
    25.4ms [  INFO ] Create operation: ElementWiseBinary
    25.4ms [  INFO ] Create operation: DepthWiseConv2d
    25.4ms [  INFO ] Create operation: ElementWiseNeuron
    25.4ms [  INFO ] Create operation: ElementWiseBinary
    25.4ms [  INFO ] Create operation: PoolAvg2d
    25.5ms [  INFO ] Create operation: Conv2d
    25.5ms [  INFO ] Create operation: ElementWiseNeuron
    25.5ms [  INFO ] Create operation: ElementWiseBinary
    25.5ms [  INFO ] Creating operations:
    25.5ms [  INFO ]   Conv2d
    25.5ms [  INFO ]   ElementWiseNeuron
    25.6ms [  INFO ] Create operation: ElementWiseBinary
    25.6ms [  INFO ] Create operation: Conv2d
    25.6ms [  INFO ] Create operation: Conv2d
    25.6ms [  INFO ] Create operation: ElementWiseNeuron
    25.7ms [  INFO ] Create operation: ElementWiseBinary
    25.7ms [  INFO ] Create operation: DepthWiseConv2d
    25.7ms [  INFO ] Create operation: ElementWiseNeuron
    25.7ms [  INFO ] Create operation: ElementWiseBinary
    25.7ms [  INFO ] Create operation: PoolAvg2d
    25.8ms [  INFO ] Create operation: Conv2d
    25.8ms [  INFO ] Create operation: ElementWiseNeuron
    25.8ms [  INFO ] Create operation: ElementWiseBinary
    25.8ms [  INFO ] Creating operations:
    25.8ms [  INFO ]   Conv2d
    25.8ms [  INFO ]   ElementWiseNeuron
    25.9ms [  INFO ] Create operation: ElementWiseBinary
    25.9ms [  INFO ] Create operation: Conv2d
    25.9ms [  INFO ] Create operation: ElementWiseBinary
    25.9ms [  INFO ] Create operation: Conv2d
    25.9ms [  INFO ] Create operation: ElementWiseNeuron
    26.0ms [  INFO ] Create operation: ElementWiseBinary
    26.0ms [  INFO ] Create operation: DepthWiseConv2d
    26.0ms [  INFO ] Create operation: ElementWiseNeuron
    26.0ms [  INFO ] Create operation: ElementWiseBinary
    26.1ms [  INFO ] Create operation: PoolAvg2d
    26.1ms [  INFO ] Create operation: Conv2d
    26.1ms [  INFO ] Create operation: ElementWiseNeuron
    26.1ms [  INFO ] Create operation: ElementWiseBinary
    26.1ms [  INFO ] Creating operations:
    26.2ms [  INFO ]   Conv2d
    26.2ms [  INFO ]   ElementWiseNeuron
    26.2ms [  INFO ] Create operation: ElementWiseBinary
    26.2ms [  INFO ] Create operation: Conv2d
    26.2ms [  INFO ] Create operation: ElementWiseBinary
    26.2ms [  INFO ] Create operation: Conv2d
    26.3ms [  INFO ] Create operation: ElementWiseNeuron
    26.3ms [  INFO ] Create operation: ElementWiseBinary
    26.3ms [  INFO ] Create operation: DepthWiseConv2d
    26.3ms [  INFO ] Create operation: ElementWiseNeuron
    26.3ms [  INFO ] Create operation: ElementWiseBinary
    26.4ms [  INFO ] Create operation: PoolAvg2d
    26.4ms [  INFO ] Create operation: Conv2d
    26.4ms [  INFO ] Create operation: ElementWiseNeuron
    26.4ms [  INFO ] Create operation: ElementWiseBinary
    26.4ms [  INFO ] Creating operations:
    26.5ms [  INFO ]   Conv2d
    26.5ms [  INFO ]   ElementWiseNeuron
    26.5ms [  INFO ] Create operation: ElementWiseBinary
    26.5ms [  INFO ] Create operation: Conv2d
    26.5ms [  INFO ] Create operation: Conv2d
    26.6ms [  INFO ] Create operation: ElementWiseNeuron
    26.6ms [  INFO ] Create operation: ElementWiseBinary
    26.6ms [  INFO ] Create operation: DepthWiseConv2d
    26.6ms [  INFO ] Create operation: ElementWiseNeuron
    26.6ms [  INFO ] Create operation: ElementWiseBinary
    26.6ms [  INFO ] Create operation: PoolAvg2d
    26.7ms [  INFO ] Create operation: Conv2d
    26.7ms [  INFO ] Create operation: ElementWiseNeuron
    26.7ms [  INFO ] Create operation: ElementWiseBinary
    26.7ms [  INFO ] Creating operations:
    26.7ms [  INFO ]   Conv2d
    26.7ms [  INFO ]   ElementWiseNeuron
    26.8ms [  INFO ] Create operation: ElementWiseBinary
    26.8ms [  INFO ] Create operation: Conv2d
    26.8ms [  INFO ] Create operation: ElementWiseBinary
    26.8ms [  INFO ] Create operation: Conv2d
    26.8ms [  INFO ] Create operation: ElementWiseNeuron
    26.9ms [  INFO ] Create operation: ElementWiseBinary
    26.9ms [  INFO ] Create operation: DepthWiseConv2d
    26.9ms [  INFO ] Create operation: ElementWiseNeuron
    26.9ms [  INFO ] Create operation: ElementWiseBinary
    26.9ms [  INFO ] Create operation: PoolAvg2d
    27.0ms [  INFO ] Create operation: Conv2d
    27.0ms [  INFO ] Create operation: ElementWiseNeuron
    27.0ms [  INFO ] Create operation: ElementWiseBinary
    27.0ms [  INFO ] Creating operations:
    27.0ms [  INFO ]   Conv2d
    27.0ms [  INFO ]   ElementWiseNeuron
    27.1ms [  INFO ] Create operation: ElementWiseBinary
    27.1ms [  INFO ] Create operation: Conv2d
    27.1ms [  INFO ] Create operation: ElementWiseBinary
    27.1ms [  INFO ] Create operation: Conv2d
    27.1ms [  INFO ] Create operation: ElementWiseNeuron
    27.2ms [  INFO ] Create operation: ElementWiseBinary
    27.2ms [  INFO ] Create operation: DepthWiseConv2d
    27.2ms [  INFO ] Create operation: ElementWiseNeuron
    27.2ms [  INFO ] Create operation: ElementWiseBinary
    27.2ms [  INFO ] Create operation: PoolAvg2d
    27.3ms [  INFO ] Create operation: Conv2d
    27.3ms [  INFO ] Create operation: ElementWiseNeuron
    27.3ms [  INFO ] Create operation: ElementWiseBinary
    27.3ms [  INFO ] Creating operations:
    27.3ms [  INFO ]   Conv2d
    27.3ms [  INFO ]   ElementWiseNeuron
    27.3ms [  INFO ] Create operation: ElementWiseBinary
    27.4ms [  INFO ] Create operation: Conv2d
    27.4ms [  INFO ] Create operation: Conv2d
    27.4ms [  INFO ] Create operation: ElementWiseNeuron
    27.4ms [  INFO ] Create operation: ElementWiseBinary
    27.5ms [  INFO ] Create operation: DepthWiseConv2d
    27.5ms [  INFO ] Create operation: ElementWiseNeuron
    27.5ms [  INFO ] Create operation: ElementWiseBinary
    27.5ms [  INFO ] Create operation: PoolAvg2d
    27.5ms [  INFO ] Create operation: Conv2d
    27.6ms [  INFO ] Create operation: ElementWiseNeuron
    27.6ms [  INFO ] Create operation: ElementWiseBinary
    27.6ms [  INFO ] Creating operations:
    27.6ms [  INFO ]   Conv2d
    27.6ms [  INFO ]   ElementWiseNeuron
    27.6ms [  INFO ] Create operation: ElementWiseBinary
    27.7ms [  INFO ] Create operation: Conv2d
    27.7ms [  INFO ] Create operation: ElementWiseBinary
    27.7ms [  INFO ] Create operation: Conv2d
    27.7ms [  INFO ] Create operation: ElementWiseNeuron
    27.8ms [  INFO ] Create operation: ElementWiseBinary
    27.8ms [  INFO ] Create operation: DepthWiseConv2d
    27.8ms [  INFO ] Create operation: ElementWiseNeuron
    27.8ms [  INFO ] Create operation: ElementWiseBinary
    27.8ms [  INFO ] Create operation: PoolAvg2d
    27.8ms [  INFO ] Create operation: Conv2d
    27.9ms [  INFO ] Create operation: ElementWiseNeuron
    27.9ms [  INFO ] Create operation: ElementWiseBinary
    27.9ms [  INFO ] Creating operations:
    27.9ms [  INFO ]   Conv2d
    27.9ms [  INFO ]   ElementWiseNeuron
    27.9ms [  INFO ] Create operation: ElementWiseBinary
    28.0ms [  INFO ] Create operation: Conv2d
    28.0ms [  INFO ] Create operation: ElementWiseBinary
    28.0ms [  INFO ] Create operation: Conv2d
    28.0ms [  INFO ] Create operation: ElementWiseNeuron
    28.1ms [  INFO ] Create operation: ElementWiseBinary
    28.1ms [  INFO ] Create operation: DepthWiseConv2d
    28.1ms [  INFO ] Create operation: ElementWiseNeuron
    28.1ms [  INFO ] Create operation: ElementWiseBinary
    28.1ms [  INFO ] Create operation: PoolAvg2d
    28.1ms [  INFO ] Create operation: Conv2d
    28.2ms [  INFO ] Create operation: ElementWiseNeuron
    28.2ms [  INFO ] Create operation: ElementWiseBinary
    28.2ms [  INFO ] Creating operations:
    28.2ms [  INFO ]   Conv2d
    28.2ms [  INFO ]   ElementWiseNeuron
    28.2ms [  INFO ] Create operation: ElementWiseBinary
    28.3ms [  INFO ] Create operation: Conv2d
    28.3ms [  INFO ] Create operation: ElementWiseBinary
    28.3ms [  INFO ] Create operation: Conv2d
    28.3ms [  INFO ] Create operation: ElementWiseNeuron
    28.4ms [  INFO ] Create operation: ElementWiseBinary
    28.4ms [  INFO ] Create operation: DepthWiseConv2d
    28.4ms [  INFO ] Create operation: ElementWiseNeuron
    28.4ms [  INFO ] Create operation: ElementWiseBinary
    28.4ms [  INFO ] Create operation: PoolAvg2d
    28.4ms [  INFO ] Create operation: Conv2d
    28.5ms [  INFO ] Create operation: ElementWiseNeuron
    28.5ms [  INFO ] Create operation: ElementWiseBinary
    28.5ms [  INFO ] Creating operations:
    28.5ms [  INFO ]   Conv2d
    28.5ms [  INFO ]   ElementWiseNeuron
    28.5ms [  INFO ] Create operation: ElementWiseBinary
    28.6ms [  INFO ] Create operation: Conv2d
    28.6ms [  INFO ] Create operation: Conv2d
    28.6ms [  INFO ] Create operation: ElementWiseNeuron
    28.6ms [  INFO ] Create operation: ElementWiseBinary
    28.6ms [  INFO ] Create operation: PoolAvg2d
    28.7ms [  INFO ] Create operation: Transpose
    28.7ms [  INFO ] Create operation: FullyConnected
    28.7ms [  INFO ] Create operation: Reshape
   708.9ms [  INFO ] finalize: total host time: 640.2 [ms]
   709.0ms [  INFO ] QnnGraph_finalize: finish
   709.3ms [  INFO ] QnnGraph_execute: start
   717.0ms [  INFO ] execute: total host time: 7.7 [ms]
   717.0ms [  INFO ] QnnGraph_execute: finish
   724.5ms [  INFO ] cleaning up resources for input tensors
   724.6ms [  INFO ] cleaning up resources for output tensors
```
