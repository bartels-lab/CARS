# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 12:01:43 2025

@author: admin2
"""

from pyThorlabsPM100x.driver import ThorlabsPM100x

from pymeasure.instruments.newport import ESP300
from pymeasure.adapters import SerialAdapter

# Connect via RS-232 using COM port (adjust 'COM3' as needed)
adapter = SerialAdapter("COM3", baudrate=19200, timeout=1)
adapter.write_terminator = "\r"
esp = ESP300(adapter)

# Move axis 1 to 5.0 mm
esp.y.position = 5.0
esp.y.wait_for_stop()

# Query position
print("Position:", esp.y.position)

# Shutdown (recommended)
esp.shutdown()




powermeter = ThorlabsPM100x()
available_devices = powermeter.list_devices()

powermeter.connect_device(device_addr = available_devices[0][0])



# Safely close ESP300
esp.close()

# Safely disconnect Thorlabs power meter
powermeter.disconnect_device()
