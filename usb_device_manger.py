# Importing the pywinusb.hid module for interacting with HID devices
import pywinusb.hid as hid
# Importing the tabulate module for formatting data into tables  
from tabulate import tabulate  

class USBDeviceManager:
    #Initializes a USBDeviceManager object.
    def __init__(self):
        # List to store USB devices information
        self.devices = []
        self.get_usb_devices()  
     
    #Retrieves USB devices information and populates the devices list.
    def get_usb_devices(self):
        # Get all HID devices connected to the system
        all_hids = hid.find_all_hid_devices()  

        for device in all_hids:
            # Extract relevant information from the device and add it to the devices list
            self.devices.append({
                "Manufacturer": device.vendor_name,
                "Product": device.product_name,
                "Serial Number": device.serial_number,
                "Vendor ID": device.vendor_id,
                "Product ID": device.product_id
            })
    #Prints the USB devices information in a tabular format.
    def print_in_tabular_format(self):
        table_data = []  # List to store data for tabulate

        # Prepare data for tabulate
        for device in self.devices:
            table_data.append([
                device["Manufacturer"],
                device["Product"],
                device["Serial Number"],
                device["Vendor ID"],
                device["Product ID"]
            ])

        # Print tabulated data
        print(tabulate(table_data, headers=["Manufacturer", "Product", "Serial Number", "Vendor ID", "Product ID"], tablefmt="grid"))

if __name__ == "__main__":
    # Retrieve USB devices information
    usb_manager = USBDeviceManager()
    # Print USB devices information in tabular format
    usb_manager.print_in_tabular_format()
