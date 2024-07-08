# Automatic APK Installer for Android Devices via USB

This Python script monitors USB connections for new Android devices and automatically installs a specified APK file using the Android Debug Bridge (adb).

## Features

- **Automatic APK Installation**: Detects newly connected Android devices and installs a specified APK file automatically.
- **Error Handling**: Includes robust error handling with detailed logging for debugging purposes.
- **Customizable Polling**: Allows customization of polling interval for monitoring connected devices.

## Prerequisites

Before running the script, ensure you have the following installed:

- **adb (Android Debug Bridge)**: Make sure `adb` is installed and accessible from the command line.
- **Python**: The script is written in Python. Install Python 3.x from [python.org](https://www.python.org/) if not already installed.

## Installation

1. Clone this repository to your local machine:
  ```bash
  git clone https://github.com/your-username/automatic-apk-installer.git
  ```

2. Navigate into the project directory:
  ```bash
  cd automatic-apk-installer
  ```

3. Install dependencies (if any):
  ```bash
  # No dependencies required beyond Python standard library
  ```

## Usage

Run the script with Python, providing the required arguments:
```bash
python auto_install_apk.py /path/to/adb /path/to/app.apk --interval 5
```

- `/path/to/adb`: Full path to the adb executable.
- `/path/to/app.apk`: Path to the APK file you want to install.
- `--interval 5`: (Optional) Polling interval in seconds. Default is 5 seconds.

To view the help message and command-line options:
```bash
python auto_install_apk.py --help
```
2. The script will start monitoring USB connections. It will detect new devices and automatically install the specified APK file on them.

## Code Review

- **PEP 8 Compliance**: Ensure the code adheres to PEP 8 guidelines for Python code style. Review variable names, spacing, and indentation for consistency.
  
- **Error Handling**: Validate error handling across subprocess calls (`subprocess.run`). Verify that exceptions are properly caught and logged using the `logging` module.
  
- **Logging**: Check the logging setup (`logging.basicConfig`) for appropriate levels (`INFO` in this case) and formatting (`%(asctime)s - %(levelname)s - %(message)s`).
  
- **Documentation**: Review docstrings for classes (`ADBHandler`, `DeviceMonitor`, `Config`), methods (`__init__`, `get_connected_devices`, `install_apk`, `monitor_devices`), and functions (`parse_args`, `main`). Ensure they provide clear descriptions of functionality and parameters.
  
- **Command-line Argument Handling**: Evaluate the `parse_args` function and usage of `argparse` for correctly parsing and handling command-line arguments (`adb_path`, `apk_path`, `--interval`).
  
- **Dependency Management**: Verify if any external dependencies beyond standard library (`subprocess`, `time`, `argparse`, `logging`) are required and handled appropriately.
  
- **Scalability and Performance**: Consider performance implications of polling interval (`poll_interval`) and device detection logic (`monitor_devices` method). Ensure efficient handling, especially in scenarios with frequent device connections or large device lists.
  
- **Testing**: Implement or plan for unit tests to cover core functionalities (`ADBHandler`, `DeviceMonitor`). Include edge cases like unexpected output from `adb` commands or handling of different device states.

- **Modularity and Reusability**: Assess opportunities for modularizing code segments (`ADBHandler`, `DeviceMonitor`, `Config`, `parse_args`) to enhance reusability and maintainability.

- **Security Considerations**: Evaluate potential security risks related to handling paths (`adb_path`, `apk_path`). Consider sanitization or validation mechanisms where applicable.

- **Overall Design**: Evaluate the overall design for clarity, separation of concerns, and adherence to object-oriented principles.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
