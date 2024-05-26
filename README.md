# frida-start

Wrapper tool to identify the remote device and push device specific frida-server binary.

## Installing

```bash
pip install frida-start
```

## Running

```bash
$ frida-start -h

usage: frida-start [-h] [-d DEVICE_NAME] [--version]

optional arguments:
  -h, --help            show this help message and exit
  -d DEVICE_NAME, --device-name DEVICE_NAME
  -f, --force           force download
  --version             show program's version number and exit
```

```bash
$ adb devices -l

List of devices attached
emulator-5554          device product:sdk_google_phone_x86 model:Android_SDK_built_for_x86 device:generic_x86 transport_id:5
emulator-5553          device product:sdk_google_phone_x86 model:Android_SDK_built_for_x86 device:generic_x86 transport_id:4
emulator-5552          device product:sdk_google_phone_x86 model:Android_SDK_built_for_x86 device:generic_x86 transport_id:3

$ frida-start -d emulator-5554

[2018-01-16 13:15:21,230] [frida-start: INFO]: Devices: emulator-5554, 0617627d0069ace6
[2018-01-16 13:15:21,230] [frida-start: INFO]: Current installed Frida version: 10.6.32
[2018-01-16 13:15:21,242] [frida-start: INFO]: Found arch: x86
[2018-01-16 13:15:21,243] [frida-start: WARNING]: Downloading: https://github.com/frida/frida/releases/download/10.6.32/frida-server-10.6.32-android-x86.xz
[2018-01-16 13:15:27,577] [frida-start: INFO]: Writing file as: /home/raul/.frida-start/frida-server-10.6.32-android-x86
[2018-01-16 13:15:27,676] [frida-start: INFO]: File pushed to device successfully.
[2018-01-16 13:15:27,686] [frida-start: INFO]: Killing all frida-server on device.
[2018-01-16 13:15:27,704] [frida-start: INFO]: Executing frida-server on device.

```
