Graph execute start ~120.3ms
Graph execute done ~129.9ms
Inference time ~9.6ms

```shell
adb shell "export ADSP_LIBRARY_PATH=/data/local/tmp/hexagon-v79/unsigned && cd /data/local/tmp && ./qnn-sample-app --backend /data/local/tmp/aarch64-android/libQnnHtp.so --retrieve_context efficientnet_b0-qnn_context_binary-float-qualcomm-snapdragon-8-elite-for-galaxy/efficientnet_b0.bin --input_list input_list.txt --output_dir output --system_library /data/local/tmp/aarch64-android/libQnnSystem.so"
     0.0ms [  INFO ] Backend: /data/local/tmp/aarch64-android/libQnnHtp.so
     0.9ms [  INFO ] Model wasn't loaded from a shared library.
     4.5ms [  INFO ] qnn-sample-app build version: v2.42.0.251225135753_193295
     4.6ms [  INFO ] Backend        build version: v2.42.0.251225135753_193295
     4.8ms [  INFO ] Initializing logging in the backend. Callback: [0x5900944458], Log Level: [3]
     0.0ms [  INFO ] QnnDsp <I> QnnLog_create started.

     0.0ms [WARNING] QnnDsp <W> Initializing HtpProvider

     0.0ms [  INFO ] QnnDsp <I> exit with 0

     0.0ms [  INFO ] QnnDsp <I> exit with 0

     0.0ms [  INFO ] QnnDsp <I> QnnLog_create exit.

     0.0ms [  INFO ] QnnDsp <I> QnnBackend_create started. backend = 0x646eefd0

     0.0ms [  INFO ] QnnDsp <I> QnnBackend_create done successfully. backend = 0x646eefd0

     6.5ms [  INFO ] Initialize Backend Returned Status = 0
     0.0ms [  INFO ] QnnDsp <I> QnnDevice_create started

     0.0ms [  INFO ] QnnDsp <I> First connection to QNN stub established!

     0.0ms [  INFO ] QnnDsp <I> QnnDevice_create done. device = 0x1. status 0x0

     0.0ms [  INFO ] QnnDsp <I> QnnContext_createFromBinary started. backend = 0x1, device = 0x1

     0.0ms [WARNING] QnnDsp <W> m_CFBCallbackInfoObj is not initialized, return emptyList

     0.0ms [  INFO ] QnnDsp <I> Number of existing contexts: 1, graphs: 1

     0.0ms [  INFO ] QnnDsp <I> QnnContext_createFromBinary done successfully. context = 0x1

     0.0ms [  INFO ] QnnDsp <I> QnnGraph_retrieve started. context = 0x1

     0.0ms [  INFO ] QnnDsp <I> Number of existing contexts: 1, graphs: 1

     0.0ms [  INFO ] QnnDsp <I> QnnGraph_retrieve done. status 0x0

   120.3ms [ ERROR ] Device property is not supported
     0.0ms [  INFO ] QnnDsp <I> QnnGraph_execute started. graph = 0x1

     0.0ms [  INFO ] QnnDsp <I> Graph graph__ixy753d execution finished with result 0

     0.0ms [  INFO ] QnnDsp <I> QnnGraph_execute done. status 0x0

   129.9ms [  INFO ] cleaning up resources for input tensors
   129.9ms [  INFO ] cleaning up resources for output tensors
     0.0ms [  INFO ] QnnDsp <I> QnnContext_free started. context = 0x1

     0.0ms [WARNING] QnnDsp <W> m_CFBCallbackInfoObj is not initialized, return emptyList

     0.0ms [  INFO ] QnnDsp <I> Graph Rpc memory was not initialized for graph 1

     0.0ms [  INFO ] QnnDsp <I> Number of existing contexts: 0, graphs: 0

     0.0ms [  INFO ] QnnDsp <I> QnnContext_free done successfully.

     0.0ms [  INFO ] QnnDsp <I> QnnDevice_free started. device = 0x1

     0.0ms [  INFO ] QnnDsp <I> Exiting thread

     0.0ms [  INFO ] QnnDsp <I> exits with 0

     0.0ms [  INFO ] QnnDsp <I> QnnDevice_free done. status 0x0

     0.0ms [  INFO ] QnnDsp <I> QnnBackend_free started. backend = 0x1
```
