## Fetch AI module

Doc:
https://aihub.qualcomm.com/get-started

##### Account Setup

```shell
python -m venv venv
.\venv\Scripts\Activate.ps1 #windows
source ./venv/bin/active #Unix
pip install qai-hub
qai-hub configure --api_token API_TOKEN
qai-hub list-devices
pip install qai-hub-models
```

##### Fetch LLM module

**Important:when apply for access of llama modules on huggingface, country need to be US or Europe**

```shell
pip install transformers torch torchvision accelerate sentencepiece
export HF_TOKEN=your_token_here
python -m qai_hub_models.models.llama_v3_2_1b_instruct.export --chipset qualcomm-snapdragon-8-elite --skip-profiling --output-dir genie_bundle_llama3_1b
```

#### Download qairt sdk

https://docs.qualcomm.com/doc/80-70018-15B/topic/qairt-install.html#qairt-install

```shell
export QAIRT_SDK=sdk_location
```

Verify the `QAIRT_SDK`

```shell
$ ls $QAIRT_SDK
benchmarks  GENIE_README.txt  NOTICE.txt              QNN_README.txt                        sdk.yaml
bin         include           NOTICE_WINDOWS.txt      QNN_TFLITE_DELEGATE_NOTICE.txt        share
docs        lib               QAIRT_ReleaseNotes.txt  QNN_TFLITE_DELEGATE_README.txt
examples    LICENSE.pdf       QNN_NOTICE.txt          QNN_TFLITE_DELEGATE_ReleaseNotes.txt
```

#### Test on Phone

Use samsung remote test lab can get a phone runner
https://developer.samsung.com/remotetestlab

Install SDK libs on Android device

```shell
adb push $QAIRT_SDK/lib/aarch64-android /data/local/tmp/
adb push $QAIRT_SDK/lib/hexagon-v73/unsigned /data/local/tmp/hexagon-v73/
```

Alternative if adb push is very slow

```shell
adb shell "cd /data/local/tmp && curl -LO https://github.com/Changqing-JING/QualcommAILearn/releases/download/init/qairt_aarch64_android_libs.tar.gz && tar -xzf qairt_aarch64_android_libs.tar.gz"
adb shell "cd /data/local/tmp && curl -LO https://github.com/Changqing-JING/QualcommAILearn/releases/download/init/qairt_hexagon_v79.tar.gz && tar -xzf qairt_hexagon_v79.tar.gz"
```

```shell
tar -czf genie_bundle.tar.gz -C genie_bundle_llama3_1b llama_v3_2_1b_instruct-genie-w4-qualcomm-snapdragon-8-elite
adb push genie_bundle.tar.gz /data/local/tmp/
```

Note: if the adb push is very slow, there is a pre built binary

```shell
adb shell "cd /data/local/tmp && curl -LO https://github.com/Changqing-JING/QualcommAILearn/releases/download/init/genie_bundle.tar.gz"
```

```shell
adb shell "cd /data/local/tmp && tar -xzvf genie_bundle.tar.gz --strip-components=1"
adb push $QAIRT_SDK/bin/aarch64-android/genie-t2t-run /data/local/tmp/
adb shell "chmod +x /data/local/tmp/genie-t2t-run"
adb push prompt.txt /data/local/tmp/
```

```shell
export LD_LIBRARY_PATH=/data/local/tmp/aarch64-android:$LD_LIBRARY_PATH
export ADSP_LIBRARY_PATH=/data/local/tmp/hexagon-v79/unsigned
./genie-t2t-run -c genie_config.json --prompt_file prompt.txt --profile perf.json
```

##### FAQ

1. `Failed to create device: 14001`. It's due to ADSP_LIBRARY version missing or mismatch.

2. adb disconnected

```
Disconnected device: SM-S937N
ADB disconnected from RDB
```

Close the RTL web client and reopen it, it will auto reboot the phone

#### build Example from source

setup NDK and qairt sdk

```shell
NDK=/opt/android-ndk
QAIRT_SDK=$(pwd)/qairt
```

```shell
cd genie-t2t-run
cmake -B build-android \
    -DCMAKE_TOOLCHAIN_FILE=$NDK/build/cmake/android.toolchain.cmake \
    -DANDROID_ABI=arm64-v8a \
    -DANDROID_PLATFORM=android-35 \
    -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_FIND_ROOT_PATH=$QAIRT_SDK \
    -DCMAKE_CXX_FLAGS="-I$QAIRT_SDK/include/Genie" \
    -DCMAKE_EXE_LINKER_FLAGS="-L$QAIRT_SDK/lib/aarch64-android -lGenie"
cmake --build build-android --parallel
```

##### CNN model

export module for npu

```shell
python -m qai_hub_models.models.efficientnet_b0.export --device "Samsung Galaxy S25" --device-os 15 --target-runtime qnn_context_binary --compile-options "--qairt_version 2.42" --skip-profiling --skip-inferencing --output-dir efficientnet_b0_npu
```

export for gpu

```shell
python -m qai_hub_models.models.efficientnet_b0.export --device "Samsung Galaxy S25" --device-os 15 --target-runtime qnn_dlc --compile-options "--qairt_version 2.42" --skip-profiling --skip-inferencing --output-dir efficientnet_b0_dlc
```

Build Sample aqpp

```shell
sudo apt install rename
cd $QAIRT_SDK/examples/QNN/SampleApp/SampleApp
export ANDROID_NDK_ROOT=$NDK
make aarch64-android -j 16
```

Get test image

```shell
wget https://qaihub-public-assets.s3.us-west-2.amazonaws.com/qai-hub-models/models/imagenet_classifier/v1/dog.jpg
python3 preprocess_image.py dog.jpg dog.raw
```

###### Test on device

###### Deploy module

```shell
adb push efficientnet_b0_npu/efficientnet_b0-qnn_context_binary-float-qualcomm-snapdragon-8-elite-for-galaxy /data/local/tmp
```

Or when ADB is slow

```shell
adb shell "cd /data/local/tmp && curl -LO https://github.com/Changqing-JING/QualcommAILearn/releases/download/init/efficientnet_b0_npu.tar.gz && tar -xzvf efficientnet_b0.tar.gz --strip-components=1"
```

```shell
adb push $QAIRT_SDK/examples/QNN/SampleApp/SampleApp/bin/aarch64-android/qnn-sample-app /data/local/tmp
adb shell "chmod +x /data/local/tmp/qnn-sample-app"
adb push dog.raw /data/local/tmp
adb push input_list.txt /data/local/tmp
```

###### Run with GPU

```shell
adb shell "export LD_LIBRARY_PATH=/data/local/tmp/aarch64-android && cd /data/local/tmp && ./qnn-sample-app --backend /data/local/tmp/aarch64-android/libQnnGpu.so --dlc_path efficientnet_b0-qnn_dlc-float/efficientnet_b0.dlc --input_list input_list.txt --output_dir output --system_library /data/local/tmp/aarch64-android/libQnnSystem.so"
```

###### Run with NPU

```shell
adb shell "export ADSP_LIBRARY_PATH=/data/local/tmp/hexagon-v79/unsigned && cd /data/local/tmp && ./qnn-sample-app --backend /data/local/tmp/aarch64-android/libQnnHtp.so --retrieve_context efficientnet_b0-qnn_context_binary-float-qualcomm-snapdragon-8-elite-for-galaxy/efficientnet_b0.bin --input_list input_list.txt --output_dir output --system_library /data/local/tmp/aarch64-android/libQnnSystem.so"
```

###### Post actions

```shell
adb pull /data/local/tmp/output/ .
wget https://raw.githubusercontent.com/pytorch/hub/master/imagenet_classes.txt
python3 postprocess_output.py output/Result_0/class_logits.raw
```
