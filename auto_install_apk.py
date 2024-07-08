import subprocess
import time
import argparse
import logging
from typing import List, Optional, Set

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ADBHandler:
    def __init__(self, adb_path: str):
        self.adb_path = adb_path

    def get_connected_devices(self) -> Optional[List[str]]:
        """Get a list of connected device IDs."""
        try:
            result = subprocess.run([self.adb_path, "devices"], check=True, capture_output=True, text=True)
            output = result.stdout.splitlines()
            device_ids = [line.split("\t")[0] for line in output if "\tdevice" in line]
            return device_ids
        except subprocess.CalledProcessError as e:
            logging.error(f"An error occurred while getting the device ID: {e}")
            return None

    def install_apk(self, device_id: str, apk_path: str) -> None:
        """Install the APK on the specified device."""
        try:
            result = subprocess.run([self.adb_path, "-s", device_id, "install", apk_path], check=True, capture_output=True, text=True)
            logging.info(f"Successfully installed APK on device {device_id}: {result.stdout}")
        except subprocess.CalledProcessError as e:
            logging.error(f"An error occurred while installing the APK on device {device_id}: {e}")

class DeviceMonitor:
    def __init__(self, adb_handler: ADBHandler, apk_path: str, poll_interval: int = 5):
        self.adb_handler = adb_handler
        self.apk_path = apk_path
        self.poll_interval = poll_interval
        self.previous_devices: Set[str] = set()

    def monitor_devices(self) -> None:
        """Continuously monitor for new devices and install the APK on newly connected devices."""
        logging.info("Monitoring for connected devices...")
        while True:
            current_devices = set(self.adb_handler.get_connected_devices() or [])
            new_devices = current_devices - self.previous_devices

            if new_devices:
                for device_id in new_devices:
                    logging.info(f"New device detected: {device_id}")
                    self.adb_handler.install_apk(device_id, self.apk_path)
            
            self.previous_devices = current_devices
            time.sleep(self.poll_interval)

class Config:
    def __init__(self, adb_path: str, apk_path: str, poll_interval: int):
        self.adb_path = adb_path
        self.apk_path = apk_path
        self.poll_interval = poll_interval

def parse_args() -> Config:
    """Parse command-line arguments and return a Config object."""
    parser = argparse.ArgumentParser(description='Monitor USB connections and install an APK automatically.')
    parser.add_argument('adb_path', type=str, help='Full path to the adb executable.')
    parser.add_argument('apk_path', type=str, help='Path to the APK file to be installed.')
    parser.add_argument('--interval', type=int, default=5, help='Polling interval in seconds (default: 5 seconds).')

    args = parser.parse_args()
    return Config(args.adb_path, args.apk_path, args.interval)

def main() -> None:
    """Main function to start the device monitor."""
    config = parse_args()
    adb_handler = ADBHandler(config.adb_path)
    device_monitor = DeviceMonitor(adb_handler, config.apk_path, config.poll_interval)
    
    device_monitor.monitor_devices()

if __name__ == "__main__":
    main()

