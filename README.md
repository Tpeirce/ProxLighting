# Proximity-Lighting
Proximity-based (bluetooth) automatic lights

Currently running on a Raspberry Pi 2 Model B. Switches standard 433Mhz RF outlets on and off based on Bluetooth-detected proximity. 

Based on https://github.com/timleland/rfoutlet

IIRC this code requires WiringPi. Some test code for running a servo is included, originally intended as a door opener. I can't remember if doing the servo control signal in Python or https://github.com/richardghirst/PiBits/tree/master/ServoBlaster worked better.
