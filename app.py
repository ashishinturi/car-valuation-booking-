from flask import Flask, render_template, request, redirect, url_for  # type: ignore
import mysql.connector  # type: ignore

app = Flask(__name__)

# ✅ DB connection block
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

# ✅ Booking route
@app.route("/", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        try:
            name = request.form["name"]
            email = request.form["email"]
            phone = request.form["phone"]
            make = request.form["make"]
            model = request.form["model"]
            year = request.form["year"]
            mileage = request.form["mileage"]
            condition = request.form["condition"]
            date = request.form["date"]
            time = request.form["time"]

            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO bookings (name, email, phone, make, model, year, mileage, `condition`, `date`, `time`)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """, (name, email, phone, make, model, year, mileage, condition, date, time))
            db.commit()

            # ✅ Redirect to success page after successful booking
            return redirect(url_for("success"))

        except Exception as e:
            print("Form error:", e)
            return "Bad form submission"
    return render_template("booking_form.html")

# ✅ Success route
@app.route("/success")
def success():
    return render_template("success.html")

# ✅ Run the app
if __name__ == "__main__":
    app.run()