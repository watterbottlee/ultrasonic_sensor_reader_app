import serial
import time
import requests
import json  # Import json to handle JSON data

# Set up the serial connection
ser = serial.Serial('COM7', 9600)  # Adjust the port name as necessary
time.sleep(1)  # Wait for the connection to establish

def read_sensor_data():
    while True:
        if ser.in_waiting > 0:  # Check if data is available
            line = ser.readline().decode('utf-8').strip()  # Read a line from the serial
            if line.startswith("Distance:"):
                distance = int(line.split(": ")[1].replace(" cm", ""))
                print(f"Distance: {distance} cm")

                # Send the distance data to your Django application as JSON
                response = requests.post('http://127.0.0.1:8000/api/sensor/', json={
                    'distance': distance
                }, timeout=30,)
                print(response.status_code)  # Print the response status

try:
    read_sensor_data()
except KeyboardInterrupt:
    ser.close()  # Close the serial connection on exit
#https://main-bvxea6i-vwgbuyftj5uri.us-3.platformsh.site
#http://127.0.0.1:8000