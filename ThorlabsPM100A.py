# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 11:46:12 2025

@author: admin2
"""

#import the library to talk to the power meter
from pyThorlabsPM100x.driver import ThorlabsPM100x


powermeter = ThorlabsPM100x()

available_devices = powermeter.list_devices()
print(available_devices)

#from the list of available devices, take the item that's in the first row, first column

powermeter.connect_device(device_addr = available_devices[0][0])
print(powermeter.power)




powermeter.disconnect_device()