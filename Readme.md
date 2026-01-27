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

```shell

tar -czf genie_bundle.tar.gz -C genie_bundle_llama3_1b llama_v3_2_1b_instruct-genie-w4-qualcomm-snapdragon-8-elite
adb push genie_bundle.tar.gz /data/local/tmp/
adb push $QAIRT_SDK/lib/aarch64-android/libGenie.so /data/local/tmp
adb push $QAIRT_SDK/bin/aarch64-android/genie-t2t-run /data/local/tmp/
adb shell "chmod +x /data/local/tmp/genie-t2t-run"
```

```shell
adb push genie_bundle_llama3_1b/llama_v3_2_1b_instruct-genie-w4-qualcomm-snapdragon-8-elite /data/local/tmp/genie_bundle/
```

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
