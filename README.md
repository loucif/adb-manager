# ADB Device Monitor and APK Installer

This script monitors for newly connected Android devices and automatically installs a specified APK on them.

## Features

- Continuously monitors for new Android devices connected via ADB.
- Automatically installs a specified APK on any new device detected.
- Simple and easy to use.

## Prerequisites

- Python 3.x
- Android Debug Bridge (ADB)

## Installation

1. **Install ADB**: Ensure ADB is installed and added to your system's PATH.

    - **Windows**: [Download ADB](https://developer.android.com/studio/releases/platform-tools)
    - **macOS**: Use Homebrew:
      ```sh
      brew install android-platform-tools
      ```
    - **Linux**: Use your package manager, e.g., for Ubuntu:
      ```sh
      sudo apt-get install android-tools-adb
      ```

2. **Enable USB Debugging**: Ensure USB debugging is enabled on the Android devices you wish to monitor.

3. **Clone this repository**:
    ```sh
    git clone https://github.com/yourusername/adb-device-monitor.git
    cd adb-device-monitor
    ```

## Usage

1. **Replace the APK Path**: Open the script and replace `apk_path` with the path to your APK file.

2. **Run the script**:
    ```sh
    python monitor_devices.py
    ```

The script will start monitoring for connected devices and automatically install the specified APK on any new device it detects.

## Code Overview

### get_connected_devices()

Runs `adb devices` command to get a list of currently connected devices and returns their IDs.

### install_apk(device_id, apk_path)

Installs the specified APK on the device with the given ID.

### monitor_devices(apk_path, poll_interval=5)

Continuously monitors for new devices and installs the APK on any newly detected devices.

## Contributing

Feel free to submit issues or pull requests if you have any improvements or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
