from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# 🔽 Paste your DB connection here
try:
    db = mysql.connector.connect(
        host="maglev.proxy.rlwy.net",
        port=55869,
        user="root",
        password="mEoNxqOPsxHUwuVBiVpJcfeBeEDcoPIJ",
        database="railway"
    )
except Exception as e:
    print("Database connection failed:", e)
app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        car_model = request.form["car_model"]
        car_year = request.form["car_year"]

        cursor = db.cursor()
        cursor.execute("""
            INSERT INTO bookings (name, email, car_model, car_year)
            VALUES (%s, %s, %s, %s)
        """, (name, email, car_model, car_year))
        db.commit()
        return "Booking submitted successfully!"

    return render_template("booking_form.html")

if __name__ == "__main__":
    app.run()