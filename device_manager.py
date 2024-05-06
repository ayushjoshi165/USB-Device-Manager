# device_manager.py

import pywinusb.hid as hid
from tabulate import tabulate

class DeviceManager:
    def __init__(self, category):
        self.category = category
        self.devices = []

    def categorize_device(self, device):
        # Check if the product name contains keywords for this category
        if self.category.lower() in device.product_name.lower():
            return True
        else:
            return False

    def add_device(self, device):
        self.devices.append({
            "Manufacturer": device.vendor_name,
            "Product": device.product_name,
            "Serial Number": device.serial_number,
            "Vendor ID": device.vendor_id,
            "Product ID": device.product_id
        })

    def print_devices_table(self):
        table_data = []
        for device in self.devices:
            table_data.append([
                device["Manufacturer"],
                device["Product"],
                device["Serial Number"],
                device["Vendor ID"],
                device["Product ID"]
            ])
        print(tabulate(table_data, headers=["Manufacturer", "Product", "Serial Number", "Vendor ID", "Product ID"], tablefmt="grid"))
