# Smart Waste Management System ♻️

A **Smart Waste Management Dashboard** built using **Python, Flask, HTML, and CSS** to monitor waste bin sensor data and improve waste collection efficiency.

---

# 📌 Project Overview

The **Smart Waste Management System** is designed to monitor garbage bins and display their status through a **web dashboard**.

The project works using a **hybrid data approach**:

* **Simulated sensor data** is used to represent multiple bins across a city.
* **One physical smart bin prototype** is implemented using **Arduino Uno and an ultrasonic sensor** to demonstrate how real-world IoT hardware can send data to the system.

This allows the project to demonstrate both:

* **Large-scale simulation of smart bins**
* **Real-world hardware integration**

---

# 🚀 Features

* 📊 Interactive dashboard to monitor bin fill levels
* 📡 Simulated sensor data for multiple bins
* 🔌 Real hardware integration for one smart bin
* 🌐 Web interface built using HTML and CSS
* ⚡ Backend powered by Flask
* 🔄 Automatic bin status updates

---

# 🛠️ Technologies Used

* Python
* Flask
* HTML
* CSS
* JavaScript
* Arduino Uno
* Ultrasonic Sensor

---

# ⚙️ Installation

### 1. Clone the repository

```
git clone https://github.com/your-username/smart-waste-management.git
```

### 2. Navigate to the project folder

```
cd smart-waste-management
```

### 3. Create a virtual environment

```
python -m venv venv
```

### 4. Activate the environment

**Windows**

```
venv\Scripts\activate
```

**Mac/Linux**

```
source venv/bin/activate
```

### 5. Install dependencies

```
pip install flask
```

---

# ▶️ Running the Application

Start the Flask server:

```
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

You will see the **Smart Waste Dashboard** displaying bin status.

---

# 🔄 Sensor Data

## Simulated Data

To simulate multiple bins and update their levels automatically:

```
python update_sensor.py
```

This script generates **sample bin-level data** to demonstrate how the system would function at a larger scale.

---

# 🔌 Hardware Setup (Real Bin Prototype)

To demonstrate real-world functionality, **one waste bin is equipped with sensors connected to an Arduino Uno**. The sensor measures the bin fill level and sends the data to the system.

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

```
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

```
Tools → Board → Arduino Uno
```

3. Select the correct port:

```
Tools → Port → COM (Arduino)
```

4. Upload the ultrasonic sensor code to the Arduino.

---

### 4. Sensor Data Collection

Once the code is uploaded:

* The ultrasonic sensor measures the **distance to the garbage level**.
* Arduino calculates the **bin fill level**.
* Data is sent to the computer through the **serial port**.

---

### 5. Run the Flask Server

Start the backend server:

```
python app.py
```

The Flask application reads the sensor values and processes them.

---

### 6. Open the Dashboard

Open your browser and visit:

```
http://127.0.0.1:5000
```

The dashboard will display:

* Simulated bin data
* Real-time data from the hardware-enabled bin

---

# 🧠 Working Principle

1. The ultrasonic sensor measures the **distance between the sensor and the garbage level**.
2. Arduino processes the sensor readings.
3. Data is transmitted to the computer via **serial communication**.
4. Python processes the data.
5. Flask displays the information on the **web dashboard**.

This setup demonstrates how a **single smart bin prototype can scale into a city-wide smart waste monitoring system**.

---

# 📸 Future Improvements

* Integration with multiple real IoT bins
* Cloud-based data storage
* Mobile application for waste collection teams
* Garbage truck route optimization
* Data analytics for waste management

---

# 👨‍💻 Author

**Neel Nemade**

---

⭐ If you found this project interesting, consider giving it a star!
