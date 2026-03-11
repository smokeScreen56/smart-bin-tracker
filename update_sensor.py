import serial
import time
import mysql.connector

SERIAL_PORT = "COM10"  
BAUD_RATE = 9600

print("📡 Connecting to Arduino...")

try:
    ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
    time.sleep(2)
    print("✅ Connected to Arduino on", SERIAL_PORT)
except Exception as e:
    print("❌ ERROR: Cannot open serial port:", e)
    exit()

while True:
    try:
        if ser.in_waiting > 0:
            line = ser.readline().decode().strip()
            print("🔍 Raw Data:", line)

            if "Fill Level" in line:
                fill = int(line.split(":")[1].replace("%", "").strip())
                print("📊 Fill Level Detected:", fill)

                # Save to MySQL
                try:
                    conn = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="Qqhw5076@",
                        database="smart_waste"
                    )
                    cursor = conn.cursor()
                    cursor.execute("UPDATE bins SET current_fill_percent = %s WHERE bin_id = 1", (fill,))
                    conn.commit()
                    conn.close()

                    print("💾 Saved to DB!")

                except Exception as dbError:
                    print("❌ Database Error:", dbError)

    except Exception as e:
        print("⚠ Runtime Error:", e)

    time.sleep(1)
