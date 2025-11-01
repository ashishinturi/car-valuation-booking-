from flask import Flask, render_template, request, redirect, url_for # pyright: ignore[reportMissingImports]
import mysql.connector # pyright: ignore[reportMissingImports]
import os

app = Flask(__name__)

# ✅ Connect to Railway MySQL
db = mysql.connector.connect(
    host="maglev.proxy.rlwy.net",
    user="root",
    password="mEoNxqOPsxHUwuVBiVpJcfeBeEDcoPIJ",
    database="railway"
)

# ✅ Route: Valuation Form
@app.route("/", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        try:
            data = {key: request.form[key] for key in [
                "sno", "valuation_date", "poname", "ncrso", "customername", "contact",
                "make", "model", "suffix", "color", "insurance", "fuel", "year", "regno",
                "date_of_reg", "milage", "satish_price", "venu_price", "expected_price",
                "gap", "accident", "rfcost", "newcar_model", "newcar_booking",
                "followup1", "followup2", "asm_remark"
            ]}

            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO valuations (
                    sno, valuation_date, poname, ncrso, customername, contact,
                    make, model, suffix, color, insurance, fuel, year, regno,
                    date_of_reg, milage, satish_price, venu_price, expected_price,
                    gap, accident, rfcost, newcar_model, newcar_booking,
                    followup1, followup2, asm_remark
                ) VALUES (
                    %(sno)s, %(valuation_date)s, %(poname)s, %(ncrso)s, %(customername)s, %(contact)s,
                    %(make)s, %(model)s, %(suffix)s, %(color)s, %(insurance)s, %(fuel)s, %(year)s, %(regno)s,
                    %(date_of_reg)s, %(milage)s, %(satish_price)s, %(venu_price)s, %(expected_price)s,
                    %(gap)s, %(accident)s, %(rfcost)s, %(newcar_model)s, %(newcar_booking)s,
                    %(followup1)s, %(followup2)s, %(asm_remark)s
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
    return "<h3 style='text-align:center; margin-top:50px;'>✅ Valuation submitted successfully!</h3>"

# ✅ Route: View Entries
@app.route("/view")
def view():
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM valuations ORDER BY valuation_date DESC")
        rows = cursor.fetchall()
        return render_template("view.html", rows=rows)
    except Exception as e:
        print("❌ View error:", e)
        return "Error loading data"

# ✅ Run Locally or on Render
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)