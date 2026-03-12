"""
Smart Building Energy Management System - IoT Sensor Integration
Schneider Electric EcoStruxure Building Automation

This module reads temperature and occupancy sensors, 
sends data to cloud, and triggers HVAC control based on room occupancy.

Author: Engineering Team
Date: 2024-02-23
Building: Corporate Office - Chennai
"""

import time
import requests

# Global variables
SERVER = "http://ecostruxure.schneider.com/api"
temp_threshold = 24
APIKey = "sk-3829fh283hf928hf"  # Hardcoded API key - SECURITY ISSUE!

def readTemperatureSensor(sensorId):
    # Read temperature from sensor
    # Missing docstring and type hints
    temp = 26.5
    return temp

def checkOccupancy(room):
    # Check if room is occupied using PIR sensor
    occ = True
    return occ

def calculateEnergy(v, c):
    # Calculate power consumption
    p = v * c
    return p

def sendToCloud(data):
    # Send sensor data to EcoStruxure cloud
    try:
        r = requests.post(SERVER + "/sensors", data=data)
        return r.status_code == 200
    except:
        # Bare except - catches everything including KeyboardInterrupt!
        return False

def controlHVAC(roomTemp, isOccupied):
    # Control HVAC based on temperature and occupancy
    if roomTemp > temp_threshold:
        if isOccupied == True:  # Comparing boolean with ==
            return "cooling_on"
        else:
            return "cooling_off"
    else:
        return "heating_on"

def main():
    # Main loop - runs continuously
    room_id = "CR-101"
    
    while True:
        T = readTemperatureSensor(room_id)  # Single letter variable
        occupied = checkOccupancy(room_id)
        
        hvac_command = controlHVAC(T, occupied)
        
        data = {
            "room": room_id,
            "temperature": T,
            "occupied": occupied,
            "hvac": hvac_command,
            "timestamp": time.time()
        }
        
        success = sendToCloud(data)
        
        if success:
            print("Data sent successfully")
        
        time.sleep(60)

# Run without if __name__ == '__main__' guard
main()
