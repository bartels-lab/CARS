# -*- coding: utf-8 -*-
"""
Created on Tue Jun 10 15:16:47 2025

@author: admin2
"""

import serial

# Replace 'COM3' with your actual port
ser = serial.Serial(
    port='COM3',
    baudrate=19200,
    bytesize=serial.EIGHTBITS,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    timeout=2,
    xonxoff=False,
    rtscts=False
)

# Send *IDN? and read response
ser.write(b'*IDN?\r')  # Must end with \r for ESP300
response = ser.read(100)  # Read up to 100 bytes
print("Raw response:", response.decode(errors='ignore'))

ser.close()


#%%

import serial
import time

class ESP300Axis:
    def __init__(self, port='COM3', axis=1, baudrate=19200):
        self.axis = axis
        self.ser = serial.Serial(port, baudrate=baudrate, timeout=1)
        time.sleep(0.5)
        # Clear any pending junk
        self.ser.reset_input_buffer()
        self.ser.reset_output_buffer()

        
    
    def _write(self, cmd, axis_specific=True):
        self.ser.reset_input_buffer()  # Flush junk input
        
        if axis_specific:
            full_cmd = f"{self.axis}{cmd}\r"
        else:
            full_cmd = f"{cmd}\r"
        print(f"Sending: {repr(full_cmd)}")  # Always print command
        self.ser.write(full_cmd.encode())
        self.ser.flush()
        time.sleep(0.05)

       # Read and discard echo/response
        echo = self.ser.read(100).decode(errors='ignore').strip()
        if echo:
            print(f"Echo/response: {repr(echo)}")
    
    

    def _query(self, cmd):
        self._write(cmd)
        return self.ser.read(100).decode(errors='ignore').strip()

    def move_to(self, pos):
        self._write("SH", axis_specific=True)       # Servo ON (global command)
        time.sleep(0.2)
        
        self._write(f"PA{pos:.3f}", axis_specific=True)  # Move to absolute position
        time.sleep(0.2)

        self._write("WS", axis_specific=True)       # Wait for stop — global command
        time.sleep(0.2)
        # Flush any residual characters (error or status messages)
        leftover = self.ser.read_all().decode(errors='ignore').strip()
        if leftover:
            print(f"ESP300 residual: {repr(leftover)}")

    def get_position(self):
        return float(self._query("TP"))
    
    def home(self):
        self._write("OR")
        self._write("WS")

    def close(self):
        self.ser.close()
        
        
stage2 = ESP300Axis(port='COM3', axis=2)
stage2.move_to(3)
print("Axis 2 position:", stage2.get_position())
stage2.close()       
        
        
