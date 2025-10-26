from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

db = mysql.connector.connect(
    host="localhost:3306",
    user="root",
    password="ashish@123",
    database="car_valuation"
)

@app.route('/')
def form():
    return render_template('booking_form.html')

@app.route('/book', methods=['POST'])
def book():
    data = request.form
    cursor = db.cursor()
    cursor.execute("""
        INSERT INTO Bookings (customer_name, email, phone, car_make, car_model, car_year, mileage, car_condition, preferred_date, preferred_time)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """, (
        data['name'], data['email'], data['phone'],
        data['make'], data['model'], data['year'],
        data['mileage'], data['condition'],
        data['date'], data['time']
    ))
    db.commit()
    return "Booking successful!"

if __name__ == '__main__':
    app.run(debug=True)
if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)