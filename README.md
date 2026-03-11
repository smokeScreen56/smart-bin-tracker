# Smart Waste Management System ♻️

A **Smart Waste Management Dashboard** built using **Python, Flask, HTML, and CSS** to monitor waste bins, manage garbage collection operations, and track trucks and drivers involved in the waste management process.

---

# 📌 Project Overview

The **Smart Waste Management System** is designed to improve urban waste collection by combining **sensor monitoring with operational management**.

The system provides a **web-based dashboard** that allows administrators to:

* Monitor waste bin levels
* Track garbage collection activities
* Manage trucks and drivers
* Log collection events

The project works using a **hybrid approach**:

* **Simulated sensor data** represents multiple bins across a city.
* **One physical smart bin prototype** using **Arduino Uno and an ultrasonic sensor** demonstrates how real-world IoT hardware can send bin-level data to the system.

This allows the platform to demonstrate both **smart bin monitoring** and **waste collection management**.

---

# 🚀 Features

### Smart Bin Monitoring

* 📊 Dashboard to monitor bin fill levels
* 📡 Simulated sensor data for multiple bins
* 🔌 Hardware integration with one real smart bin
* ⚡ Automatic updates of bin status

### Waste Collection Management

* 🚛 Database of garbage trucks
* 👷 Database of drivers
* 🔗 Assign drivers to specific trucks
* 📝 Log garbage collection activities performed by drivers
* 📋 Track collection history

### Web Dashboard

* 🌐 User-friendly interface
* 📊 Centralized monitoring of waste management operations
* 🧾 Record and view operational data related to trucks, drivers, and collections

---

# 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Arduino Uno
* Ultrasonic Sensor
* Database (for storing trucks, drivers, and collection logs)

---


# ⚙️ Installation

### 1. Clone the repository

```id="d4e5f6"
git clone https://github.com/your-username/smart-waste-management.git
```

### 2. Navigate to the project folder

```id="g7h8i9"
cd smart-waste-management
```

### 3. Create a virtual environment

```id="j1k2l3"
python -m venv venv
```

### 4. Activate the environment

**Windows**

```id="m4n5o6"
venv\Scripts\activate
```

**Mac/Linux**

```id="p7q8r9"
source venv/bin/activate
```

### 5. Install dependencies

```id="s1t2u3"
pip install flask
```

---

# ▶️ Running the Application

Start the Flask server:

```id="v4w5x6"
python app.py
```

Open your browser and go to:

```id="y7z8a9"
http://127.0.0.1:5000
```

You will see the **Smart Waste Management Dashboard**.

---

# 🔄 Sensor Data

## Simulated Data

To simulate multiple bins and update their levels automatically:

```id="b1c2d3"
python update_sensor.py
```

This script generates **sample bin-level data** to represent multiple bins across different areas.

---

# 🔌 Hardware Setup (Real Bin Prototype)

To demonstrate real-world functionality, **one waste bin is equipped with sensors connected to an Arduino Uno**. The sensor measures the bin fill level and sends the data to the system.

---

## Components Used

* Arduino Uno
* Ultrasonic Sensor (HC-SR04)
* Jumper Wires
* USB Cable
* Laptop/Computer

---

# ⚙️ Steps to Run the Hardware Prototype

### 1. Connect the Hardware

Connect the **ultrasonic sensor** to the Arduino:

```id="e4f5g6"
VCC  → 5V
GND  → GND
TRIG → Pin 9
ECHO → Pin 10
```

Mount the ultrasonic sensor at the **top of the waste bin** so it can measure the distance to the garbage.

---

### 2. Connect Arduino to Computer

Use a **USB cable** to connect the Arduino Uno to your computer.

---

### 3. Upload the Arduino Code

1. Open the Arduino IDE
2. Select the board:

```id="h7i8j9"
Tools → Board → Arduino Uno
```

3. Select the correct port:

```id="k1l2m3"
Tools → Port → COM (Arduino)
```

4. Upload the ultrasonic sensor code to the Arduino.

---

### 4. Sensor Data Collection

After uploading the code:

* The ultrasonic sensor measures the **distance to the garbage level**
* Arduino calculates the **bin fill percentage**
* The data is transmitted to the computer through the **serial connection**

---

### 5. Run the Flask Server

Start the backend server:

```id="n4o5p6"
python app.py
```

The Flask application processes the sensor readings and updates the dashboard.

---

### 6. Open the Dashboard

Open your browser and visit:

```id="q7r8s9"
http://127.0.0.1:5000
```

The dashboard will display:

* Simulated bin data
* Real-time data from the hardware-enabled bin
* Truck and driver management information
* Garbage collection logs

---

# 🧠 Working Principle

1. The ultrasonic sensor measures the **distance between the sensor and the garbage level**.
2. Arduino processes the sensor readings and sends the data to the computer.
3. Python receives and processes the sensor data.
4. The **Flask backend updates the database and dashboard**.
5. The dashboard displays **bin status, truck assignments, driver information, and collection records**.

---

# 📸 Future Improvements

* Integration with multiple real IoT bins
* GPS tracking for garbage trucks
* Cloud-based data storage
* Mobile app for drivers and waste management staff
* Route optimization for garbage collection
* Data analytics for smart city planning

---

# 👨‍💻 Author

**Neel Nemade**

---

⭐ If you found this project interesting, consider giving it a star!
