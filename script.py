import serial
import time

ser = serial.Serial('COM6', 115200)  # użyj portu Pico
time.sleep(2)

while True:
    text = input("Wpisz tekst do wysłania: ")
    ser.write((text + "\n").encode('utf-8'))
    print("Wysłano:", text)
