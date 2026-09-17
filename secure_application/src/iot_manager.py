import os
import sqlite3


devices = {}


def register_device():
    device_id = input("Enter device ID: ")
    device_name = input("Enter device name: ")
    device_type = input("Enter device type: ")

    devices[device_id] = {
        "name": device_name,
        "type": device_type,
        "status": "OFFLINE"
    }

    print("Device registered successfully.")


def show_devices():
    if not devices:
        print("No devices registered.")
        return

    print("\n--- Device Status ---")

    for device_id, device in devices.items():
        print("ID:", device_id)
        print("Name:", device["name"])
        print("Type:", device["type"])
        print("Status:", device["status"])
        print()


def upload_firmware():
    device_id = input("Enter device ID: ")
    filename = input("Enter firmware filename: ")

    path = "firmware/" + filename

    try:
        with open(path, "rb") as file:
            data = file.read()

        print("Firmware uploaded for", device_id)
        print("Size:", len(data), "bytes")

    except FileNotFoundError:
        print("Firmware file not found.")


def configure_device():
    device_id = input("Enter device ID: ")
    command = input("Enter configuration command: ")

    print("Executing configuration...")
    os.system(command)

    if device_id in devices:
        devices[device_id]["status"] = "ONLINE"

    print("Configuration completed.")


def main():
    while True:
        print("\n==============================")
        print("     IoT Device Manager")
        print("==============================")
        print("1. Register Device")
        print("2. View Device Status")
        print("3. Upload Firmware")
        print("4. Configure Device")
        print("5. Exit")
        print("==============================")

        choice = input("Enter your choice: ")

        if choice == "1":
            register_device()

        elif choice == "2":
            show_devices()

        elif choice == "3":
            upload_firmware()

        elif choice == "4":
            configure_device()

        elif choice == "5":
            print("Exiting...")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()
