from flask import Flask, render_template, request, redirect, url_for # type: ignore
import mysql.connector # type: ignore

app = Flask(__name__)

# ✅ Database connection
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

# ✅ Valuation form route
@app.route("/", methods=["GET", "POST"])
def booking():
    if request.method == "POST":
        try:
            # Collect form data
            sno = request.form["sno"]
            regno = request.form["regno"]
            engineno = request.form["engineno"]
            model = request.form["model"]
            fuel = request.form["fuel"]
            year = request.form["year"]
            color = request.form["color"]
            insurance = request.form["insurance"]
            km = request.form["km"]
            rfcost = request.form["rfcost"]
            hp = request.form["hp"]
            trafic = request.form["trafic"]
            pprice = request.form["pprice"]
            margine = request.form["margine"]
            pending = request.form["pending"]
            poname = request.form["poname"]
            pdate = request.form["pdate"]
            customername = request.form["customername"]
            mobilenumber = request.form["mobilenumber"]
            soname = request.form["soname"]
            ncar = request.form["ncar"]

            # Insert into database
            cursor = db.cursor()
            cursor.execute("""
                INSERT INTO valuations (
                    sno, regno, engineno, model, fuel, year, color, insurance, km,
                    rfcost, hp, trafic, pprice, margine, pending, poname, pdate,
                    customername, mobilenumber, soname, ncar
                ) VALUES (
                    %s, %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s, %s, %s, %s, %s,
                    %s, %s, %s, %s
                )
            """, (
                sno, regno, engineno, model, fuel, year, color, insurance, km,
                rfcost, hp, trafic, pprice, margine, pending, poname, pdate,
                customername, mobilenumber, soname, ncar
            ))
            db.commit()

            return redirect(url_for("success"))

        except Exception as e:
            print("Form error:", e)
            return "Bad form submission"
    return render_template("booking_form.html")

# ✅ Success page
@app.route("/success")
def success():
    return render_template("success.html")

# ✅ Public view page
@app.route("/view")
def view():
    try:
        cursor = db.cursor(dictionary=True)
        cursor.execute("SELECT * FROM valuations ORDER BY pdate DESC")
        records = cursor.fetchall()
        return render_template("view.html", records=records)
    except Exception as e:
        print("View error:", e)
        return "Unable to load valuation records"

# ✅ Run the app
if __name__ == "__main__":
    app.run()