"""
Smart Building Energy Management System - IoT Sensor Integration
Schneider Electric EcoStruxure Building Automation

This module reads temperature and occupancy sensors,
sends data to cloud, and triggers HVAC control based on room occupancy.

Author: Shri Harsan, Divya, Sravya
Date: 2024-02-23
Building: Corporate Office - Chennai
System: EcoStruxure Building Operation
"""

import time
import os
from typing import Dict, Optional, Tuple
import requests
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration constants
SERVER_URL: str = "http://ecostruxure.schneider.com/api"
TEMPERATURE_THRESHOLD: float = 24.0  # Celsius
POLLING_INTERVAL: int = 60  # seconds
API_KEY: str = os.getenv("ECOSTRUXURE_API_KEY", "")  # Secure API key from environment


def read_temperature_sensor(sensor_id: str) -> float:
    """
    Read temperature from IoT sensor.
    
    Args:
        sensor_id: Unique identifier for the temperature sensor
        
    Returns:
        Temperature reading in Celsius
        
    Raises:
        ValueError: If sensor_id is invalid
    """
    if not sensor_id:
        raise ValueError("Sensor ID cannot be empty")
    
    # Simulate sensor reading (replace with actual sensor API)
    temperature: float = 26.5
    return temperature


def check_occupancy(room_id: str) -> bool:
    """
    Check if room is occupied using PIR motion sensor.
    
    Args:
        room_id: Unique identifier for the room
        
    Returns:
        True if room is occupied, False otherwise
    """
    if not room_id:
        raise ValueError("Room ID cannot be empty")
    
    # Simulate PIR sensor reading (replace with actual sensor API)
    is_occupied: bool = True
    return is_occupied


def calculate_power_consumption(voltage: float, current: float) -> float:
    """
    Calculate electrical power consumption.
    
    Args:
        voltage: Voltage in Volts (V)
        current: Current in Amperes (A)
        
    Returns:
        Power consumption in Watts (W)
        
    Example:
        >>> calculate_power_consumption(230.0, 5.0)
        1150.0
    """
    if voltage < 0 or current < 0:
        raise ValueError("Voltage and current must be non-negative")
    
    power: float = voltage * current
    return power


def send_to_cloud(data: Dict) -> bool:
    """
    Send sensor data to EcoStruxure cloud platform.
    
    Args:
        data: Dictionary containing sensor readings and metadata
        
    Returns:
        True if data was sent successfully, False otherwise
    """
    if not API_KEY:
        raise ValueError("API_KEY not configured in environment variables")
    
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        
        response = requests.post(
            f"{SERVER_URL}/sensors",
            json=data,
            headers=headers,
            timeout=10
        )
        
        return response.status_code == 200
        
    except requests.exceptions.RequestException as e:
        print(f"Error sending data to cloud: {e}")
        return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False


def control_hvac(
    room_temperature: float,
    is_occupied: bool
) -> Tuple[str, int]:
    """
    Determine HVAC control command based on temperature and occupancy.
    
    Implements energy-efficient control:
    - Full cooling/heating when room is occupied
    - Reduced operation when room is empty
    
    Args:
        room_temperature: Current room temperature in Celsius
        is_occupied: Whether the room is currently occupied
        
    Returns:
        Tuple of (hvac_mode, fan_speed)
        hvac_mode: One of ["cooling_on", "heating_on", "off"]
        fan_speed: Fan speed level (0-3)
    """
    if room_temperature > TEMPERATURE_THRESHOLD:
        # Room too hot - activate cooling
        if is_occupied:
            return "cooling_on", 3  # Full cooling for comfort
        else:
            return "cooling_on", 1  # Minimal cooling to save energy
            
    elif room_temperature < TEMPERATURE_THRESHOLD - 2.0:
        # Room too cold - activate heating
        if is_occupied:
            return "heating_on", 3  # Full heating for comfort
        else:
            return "heating_on", 1  # Minimal heating to save energy
    else:
        # Temperature within acceptable range
        return "off", 0


def main() -> None:
    """
    Main control loop for Smart Building Energy Management.
    
    Continuously monitors sensors and controls HVAC system
    for optimal energy efficiency and occupant comfort.
    """
    room_id: str = "CR-101"
    
    print(f"Starting Smart Building Energy Management for {room_id}")
    print(f"Temperature threshold: {TEMPERATURE_THRESHOLD}°C")
    print(f"Polling interval: {POLLING_INTERVAL}s")
    
    while True:
        try:
            # Read sensors
            room_temperature: float = read_temperature_sensor(room_id)
            is_occupied: bool = check_occupancy(room_id)
            
            # Determine HVAC control
            hvac_mode, fan_speed = control_hvac(room_temperature, is_occupied)
            
            # Prepare data payload
            sensor_data: Dict = {
                "room_id": room_id,
                "temperature": room_temperature,
                "is_occupied": is_occupied,
                "hvac_mode": hvac_mode,
                "fan_speed": fan_speed,
                "timestamp": time.time()
            }
            
            # Send to cloud
            success: bool = send_to_cloud(sensor_data)
            
            if success:
                print(f"✅ Data sent: Temp={room_temperature}°C, "
                      f"Occupied={is_occupied}, HVAC={hvac_mode}")
            else:
                print("⚠️ Failed to send data to cloud")
            
            # Wait before next reading
            time.sleep(POLLING_INTERVAL)
            
        except KeyboardInterrupt:
            print("\n🛑 Stopping Smart Building Energy Management")
            break
        except Exception as e:
            print(f"❌ Error in main loop: {e}")
            time.sleep(POLLING_INTERVAL)


if __name__ == '__main__':
    main()
