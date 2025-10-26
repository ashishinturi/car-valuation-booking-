from flask import Flask, render_template, request
import mysql.connector

# 🔌 Paste your Railway connection block here
db = mysql.connector.connect(
    host="maglev.proxy.rlwy.net",
    port=55869,
    user="root",
    password="mEoNxqOPsxHUwuVBiVpJcfeBeEDcoPIJ",
    database="railway"
)

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

    return render_template("form.html")

if __name__ == "__main__":
    app.run()