import pywinusb.hid as hid
from tabulate import tabulate

class USBDeviceManager:
    def __init__(self):
        self.devices = []

    def find_usb_devices(self):
        all_hids = hid.find_all_hid_devices()

        for device in all_hids:
            self.devices.append({
                "Manufacturer": device.vendor_name,
                "Product": device.product_name,
                "Serial Number": device.serial_number,
                "Vendor ID": device.vendor_id,
                "Product ID": device.product_id
            })

    def print_usb_devices_table(self):
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

if __name__ == "__main__":
    usb_manager = USBDeviceManager()
    usb_manager.find_usb_devices()
    usb_manager.print_usb_devices_table()
