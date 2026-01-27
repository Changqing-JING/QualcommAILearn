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
