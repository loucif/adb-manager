import subprocess
import time

def get_connected_devices():
    try:
        # Run adb devices command
        result = subprocess.run(["adb", "devices"], check=True, capture_output=True, text=True)
        
        # Parse the output to get device IDs
        output = result.stdout.splitlines()
        device_ids = []
        for line in output:
            if "\tdevice" in line:
                device_ids.append(line.split("\t")[0])
        
        return device_ids
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while getting the device ID: {e}")
        return None

def install_apk(device_id, apk_path):
    try:
        # Install the APK on the specified device
        result = subprocess.run(["adb", "-s", device_id, "install", apk_path], check=True, capture_output=True, text=True)
        print(result.stdout)
        print(f"Successfully installed APK on device {device_id}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while installing the APK on device {device_id}: {e}")

def monitor_devices(apk_path, poll_interval=5):
    previous_devices = set()
    print("Monitoring for connected devices...")

    while True:
        current_devices = set(get_connected_devices() or [])
        new_devices = current_devices - previous_devices
        
        if new_devices:
            for device_id in new_devices:
                print(f"New device detected: {device_id}")
                install_apk(device_id, apk_path)
        
        previous_devices = current_devices
        time.sleep(poll_interval)

if __name__ == "__main__":
    # Replace with the path to your APK file
    apk_path = "testX.apk"
    
    monitor_devices(apk_path)
