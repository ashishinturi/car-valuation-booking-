from flask import Flask, render_template, request, redirect, url_for # pyright: ignore[reportMissingImports]
import mysql.connector # pyright: ignore[reportMissingImports]

app = Flask(__name__)

# ✅ Connect to MySQL database
try:
    db = mysql.connector.connect(
        host="maglev.proxy.rlwy.net",
        port=55869,
        user="root",
        password="mEoNxqOPsxHUwuVBiVpJcfeBeEDcoPIJ",
        database="railway"
    )
    print("✅ Connected to database successfully.")
except Exception as e:
    print("❌ Database connection failed:", e)
    exit()

# ✅ Route: Valuation Form
@app.route("/", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        try:
            # Collect form data
            data = {key: request.form[key] for key in [
                "sno", "regno", "engineno", "model", "fuel", "year", "color", "insurance", "km",
                "rfcost", "hp", "trafic", "pprice", "margine", "pending", "poname", "pdate",
                "customername", "mobilenumber", "soname", "ncar"
            ]}
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO valuations (
                    sno, regno, engineno, model, fuel, year, color, insurance, km,
                    rfcost, hp, trafic, pprice, margine, pending, poname, pdate,
                    customername, mobilenumber, soname, ncar
                ) VALUES (
                    %(sno)s, %(regno)s, %(engineno)s, %(model)s, %(fuel)s, %(year)s, %(color)s, %(insurance)s, %(km)s,
                    %(rfcost)s, %(hp)s, %(trafic)s, %(pprice)s, %(margine)s, %(pending)s, %(poname)s, %(pdate)s,
                    %(customername)s, %(mobilenumber)s, %(soname)s, %(ncar)s
                )
            """, data)
            db.commit()
            return redirect(url_for("success"))
        except Exception as e:
            print("❌ Form submission error:", e)
            return "Error submitting form"
    return render_template("booking_form.html")

# ✅ Route: Success Page
@app.route("/success")
def success():
    return render_template("success.html")

# ✅ Route: View All Entries
@app.route("/view")
def view():
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM valuations ORDER BY pdate DESC")
        records = cursor.fetchall()
        return render_template("view.html", records=records)
    except Exception as e:
        print("❌ View error:", e)
        return "Unable to load valuation records"

# ✅ Run the app
if __name__ == "__main__":
    app.run(debug=True)