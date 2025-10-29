
import mysql.connector # type: ignore

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

# ✅ Insert sample valuation entry
try:
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
        "001", "TS09AB1234", "ENG123456", "Swift Dzire", "Petrol", 2020, "White", "Comprehensive", 35000,
        15000, "HP123", "Hyderabad", 450000, 50000, "None", "Ravi Kumar", "2025-10-29",
        "Anil Reddy", "9876543210", "Suresh", "Used"
    ))
    db.commit()
    print("✅ Sample valuation entry inserted.")
except Exception as e:
    print("❌ Failed to insert record:", e)

# ✅ Fetch and display all entries
try:
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM valuations ORDER BY pdate DESC")
    records = cursor.fetchall()

    print("\n📋 Valuation Records:\n")
    for row in records:
        print(f"{row['sno']} | {row['regno']} | {row['engineno']} | {row['model']} | {row['fuel']} | {row['year']} | {row['color']} | {row['insurance']} | {row['km']} | {row['rfcost']} | {row['hp']} | {row['trafic']} | {row['pprice']} | {row['margine']} | {row['pending']} | {row['poname']} | {row['pdate']} | {row['customername']} | {row['mobilenumber']} | {row['soname']} | {row['ncar']}")
except Exception as e:
    print("❌ Failed to fetch records:", e)
finally:
    cursor.close()
    db.close()