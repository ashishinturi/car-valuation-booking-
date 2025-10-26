CREATE DATABASE car_valuation;
USE car_valuation;
CREATE TABLE Bookings (
    id INT AUTO_INCREMENT PRIMARY KEY,
    customer_name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    car_make VARCHAR(50),
    car_model VARCHAR(50),
    car_year INT,
    mileage INT,
    car_condition VARCHAR(20),
    preferred_date DATE,
    preferred_time TIME,
    status VARCHAR(20) DEFAULT 'Pending'
);
