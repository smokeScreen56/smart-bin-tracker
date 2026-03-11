# app.py
from flask import Flask, render_template, request
import mysql.connector
from mysql.connector import Error
from datetime import date

app = Flask(__name__)

# Database credentials
DB_HOST = "localhost"
DB_USER = "root"
DB_PASS = "Qqhw5076@"          
DB_NAME = "smart_waste"

def get_db_connection():
    """Create and return a new MySQL connection."""
    return mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME
    )

@app.route("/")
def dashboard():
    conn = None
    try:
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)

        # Dashboard Stats
        cursor.execute("SELECT COUNT(*) AS total_bins FROM bins")
        total_bins = cursor.fetchone()["total_bins"]

        cursor.execute("SELECT COUNT(*) AS need_pickup FROM bins WHERE current_fill_percent >= 80")
        need_pickup = cursor.fetchone()["need_pickup"]

        cursor.execute("SELECT COUNT(*) AS active_trucks FROM trucks")
        active_trucks = cursor.fetchone()["active_trucks"]

        # Count today's collections
        cursor.execute("SELECT COUNT(*) AS today_collections FROM collections WHERE DATE(collected_at) = CURDATE()")
        today_collections = cursor.fetchone()["today_collections"]

        # Table Data
        # List of bins
        cursor.execute("""
            SELECT bin_id, name, location, capacity_liters, current_fill_percent, last_collected
            FROM bins
            ORDER BY bin_id ASC
        """)
        bins = cursor.fetchall()

        # Recent collections (last 5)
        cursor.execute("""
            SELECT collection_id, bin_id, truck_id, collected_liters, collected_at
            FROM collections
            ORDER BY collected_at DESC
            LIMIT 5
        """)
        collections = cursor.fetchall()

        # Trucks and drivers
        cursor.execute("""
            SELECT t.truck_id, t.plate_no, t.capacity_liters, d.name AS driver
            FROM trucks t
            LEFT JOIN drivers d ON t.driver_id = d.driver_id
        """)
        trucks = cursor.fetchall()

        # Render all data in dashboard
        return render_template("dashboard.html",
                               total_bins=total_bins,
                               need_pickup=need_pickup,
                               active_trucks=active_trucks,
                               today_collections=today_collections,
                               bins=bins,
                               collections=collections,
                               trucks=trucks)

    except Error as e:
        return f"<h3>Database error:</h3><p>{e}</p>"
    finally:
        if conn:
            conn.close()

@app.route("/add-bin", methods=["POST"])
def add_bin():
    name = request.form["name"]
    location = request.form["location"]
    capacity = request.form["capacity"]

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO bins (name, location, capacity_liters, current_fill_percent, last_collected)
        VALUES (%s, %s, %s, 0, NULL)
    """, (name, location, capacity))
    conn.commit()
    conn.close()
    return "OK"

@app.route("/log-collection", methods=["POST"])
def log_collection():
    bin_id = request.form["bin_id"]
    truck_id = request.form["truck_id"]
    liters = request.form["liters"]

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO collections (bin_id, truck_id, collected_liters, collected_at)
        VALUES (%s, %s, %s, CURDATE())
    """, (bin_id, truck_id, liters))

    cursor.execute("""
        UPDATE bins
        SET current_fill_percent = 0, last_collected = CURDATE()
        WHERE bin_id = %s
    """, (bin_id,))
    conn.commit()
    conn.close()
    return "OK"


if __name__ == "__main__":
    app.run(debug=True)
