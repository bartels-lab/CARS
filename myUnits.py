# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 11:21:06 2025

@author: smith
"""

class myUnits:
    def __init__(self):
        # Physical constants
        self.c = 299792458  # Speed of light [m/s]
        self.q = 1.60217662e-19  # Elementary charge [C, A-s]
        self.h = 6.62607004e-34  # Planck constant [m^2*kg/s]

        # Lengths
        self.km = 1E3
        self.m = 1
        self.cm = 1E-2
        self.mm = 1E-3
        self.um = 1E-6
        self.nm = 1E-9
        self.pm = 1E-12

        # Times
        self.s = 1
        self.ms = 1E-3
        self.us = 1E-6
        self.ns = 1E-9
        self.ps = 1E-12
        self.fs = 1E-15

        # Frequencies
        self.PHz = 1E15
        self.THz = 1E12
        self.GHz = 1E9
        self.MHz = 1E6
        self.kHz = 1E3
        self.Hz = 1

        # Power
        self.mW = 1E-3
        self.mV = 1E-3

        # Current
        self.mA = 1E-3

        # Molar concentrations
        self.mM = 1E-3
        self.uM = 1E-6

        # Volumes
        self.mL = 1E-3
        self.uL = 1E-6
