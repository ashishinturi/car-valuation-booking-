@app.route("/", methods=["GET", "POST"]) # type: ignore
def booking():
    if request.method == "POST": # type: ignore
        try:
            # Collect form data
            data = {key: request.form[key] for key in [ # type: ignore # type: ignore
                "sno", "valuation_date", "poname", "ncrso", "customername", "contact",
                "make", "model", "suffix", "color", "insurance", "fuel", "year", "regno",
                "date_of_reg", "milage", "satish_price", "venu_price", "expected_price",
                "gap", "accident", "rfcost", "newcar_model", "newcar_booking",
                "followup1", "followup2", "asm_remark"
            ]}

            # Insert into database
            cursor = db.cursor() # type: ignore
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
            db.commit() # type: ignore
            return redirect(url_for("success")) # type: ignore
        except Exception as e:
            print("❌ Form submission error:", e)
            return "Error submitting form"
    return render_template("booking_form.html") # type: ignore