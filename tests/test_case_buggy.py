"""
Simple Test Case - Violates 2 Schneider Rules
This code intentionally has issues to demonstrate the AI Code Reviewer.
"""

# VIOLATES R013: Hungarian notation required
# VIOLATES R017: Global variables must start with 'g_'

# Global variables (should be g_MaxVoltage, g_MinCurrent, etc.)
MAX_VOLTAGE = 240  
MIN_CURRENT = 5
server_url = "http://schneider.com/api"

def calculate_power(voltage, current):
    """Calculate electrical power consumption."""
    # VIOLATES R013: Variables should use Hungarian notation
    # Should be: fPower, iVoltage, iCurrent
    power = voltage * current
    return power

def check_limits(v, c):
    """Check if voltage and current are within safe limits."""
    # VIOLATES R013: Single letter variables
    # Should be: iVoltage, iCurrent
    if v > MAX_VOLTAGE:
        return False
    if c < MIN_CURRENT:
        return False
    return True

# Main execution
voltage_reading = 220  # Should be: iVoltageReading
current_reading = 10   # Should be: iCurrentReading

power = calculate_power(voltage_reading, current_reading)
safe = check_limits(voltage_reading, current_reading)

print(f"Power: {power}W, Safe: {safe}")
