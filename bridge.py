import serial
import os
import time

SERIAL_PORT = 'YOURCOMHERE'
BAUD_RATE = 9600

def start_bridge():
    print("Bridge active. Waiting for signal...")
    try:
        ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=1)
        time.sleep(2)
        
        while True:
            if ser.in_waiting > 0:
                msg = ser.readline().decode('utf-8').strip()
                
               
                if msg == "START_SELECT":
                    print("Please Select Media")
                
                
                elif msg.startswith("PLAY:"):
                    path = msg.replace("PLAY:", "")
                    print(f"Opening: {path}")
                    if os.path.exists(path):
                        os.startfile(path)
                    else:
                        print(f"Error: File not found at {path}")
                    
    except KeyboardInterrupt:
        print("Bridge stopped.")
    finally:
        if 'ser' in locals(): ser.close()

if __name__ == "__main__":
    start_bridge()
