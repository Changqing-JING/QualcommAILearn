41.9ms [ INFO ] [QNN_CPU] QnnGraph execute start
81.0ms [ INFO ] [QNN_CPU] QnnGraph execute end
Execution time 39.1ms

```
adb shell "export LD_LIBRARY_PATH=/data/local/tmp/aarch64-android && cd /data/local/tmp && ./qnn-sample-app --backend /data/local/tmp/aarch64-android/libQnnCpu.so --dlc_path efficientnet_b0-qnn_dlc-float/efficientnet_b0.dlc --input_list input_list.txt --output_dir output --system_library /data/local/tmp/aarch64-android/libQnnSystem.so"
     0.0ms [  INFO ] Backend: /data/local/tmp/aarch64-android/libQnnCpu.so
     3.9ms [  INFO ] Model wasn't loaded from a shared library.
     7.2ms [  INFO ] qnn-sample-app build version: v2.42.0.251225135753_193295
     7.2ms [  INFO ] Backend        build version: v2.42.0.251225135753_193295
     7.2ms [  INFO ] Initializing logging in the backend. Callback: [0x649fd84458], Log Level: [3]
     0.6ms [  INFO ] [QNN_CPU] CpuBackend creation start
     0.6ms [  INFO ] [QNN_CPU] CpuBackend creation end
     7.9ms [  INFO ] Initialize Backend Returned Status = 0
     7.9ms [WARNING] Device property is not supported
     0.6ms [  INFO ] [QNN_CPU]  Code: QNN_DEVICE_ERROR_UNSUPPORTED_FEATURE
     0.6ms [  INFO ] [QNN_CPU] QnnContext create start
     0.6ms [  INFO ] [QNN_CPU] QnnContext create end
     7.9ms [  INFO ] DLC path provided, using DLC-based graph composition
     7.9ms [  INFO ] Composing graphs from DLC
     7.9ms [  INFO ] Creating DLC handle from file: efficientnet_b0-qnn_dlc-float/efficientnet_b0.dlc
     7.9ms [  INFO ] Initializing logging in the System Library for DLC. Callback: [0x649fd84458], Log Level: [3]
     8.8ms [  INFO ] Successfully created DLC handle
     8.8ms [  INFO ] Composing graphs from DLC
     8.8ms [  INFO ] Calling systemDlcComposeGraphs
     5.5ms [  INFO ] [QNN_CPU] CpuGraph creation start
     5.5ms [  INFO ] [QNN_CPU] CpuGraph creation end
     5.5ms [  INFO ] [QNN_CPU] QnnGraph create end
    48.1ms [  INFO ] Successfully composed 1 graphs from DLC
    48.1ms [  INFO ] Successfully composed 1 graphs from DLC
    40.9ms [  INFO ] [QNN_CPU] QnnGraph finalize start
    41.4ms [  INFO ] [QNN_CPU] QnnGraph finalize end
    41.9ms [  INFO ] [QNN_CPU] QnnGraph execute start
    81.0ms [  INFO ] [QNN_CPU] QnnGraph execute end
    88.4ms [  INFO ] cleaning up resources for input tensors
    88.4ms [  INFO ] cleaning up resources for output tensors
    81.1ms [  INFO ] [QNN_CPU] QnnContext Free start
    85.9ms [  INFO ] [QNN_CPU] QnnContext Free end
    85.9ms [  INFO ] [QNN_CPU] QnnBackend Free start
    86.0ms [  INFO ] [QNN_CPU] QnnBackend Free end
```
