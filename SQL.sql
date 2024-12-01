CREATE TABLE flight (
    flight_id SERIAL PRIMARY KEY,
    origin VARCHAR(255),
    destination VARCHAR(255),
    travel_duration INTERVAL,
    departure_time TIME,
    arrival_time TIME
);

CREATE TABLE flight_schedule (
    flight_schedule_id SERIAL PRIMARY KEY,
    date DATE,
    flight_id INT REFERENCES flight(flight_id) ON DELETE CASCADE -- Mandatory participation for flight
);

CREATE TABLE crew_member (
    crew_id SERIAL PRIMARY KEY,
    role VARCHAR(255) CHECK (role IN ('Captain', 'Crew Member')),
    flight_id INT REFERENCES flight(flight_id) ON DELETE CASCADE
);

CREATE TABLE passenger (
    passenger_id SERIAL PRIMARY KEY,
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    birth_date DATE,
    gender VARCHAR(10) CHECK (gender IN ('Male', 'Female', 'Other')) -- ENUM for gender
);

CREATE TABLE booking (
    booking_id SERIAL PRIMARY KEY,
    passenger_id INT REFERENCES passenger(passenger_id) ON DELETE CASCADE, -- Mandatory participation for passenger
    flight_id INT REFERENCES flight(flight_id) ON DELETE CASCADE, -- If flight id is deleted, flight is cancelled.
    booking_date DATE,
    total_cost NUMERIC(10, 2)
);

CREATE TABLE additional_item (
    item_id SERIAL PRIMARY KEY,
    booking_id INT REFERENCES booking(booking_id) ON DELETE CASCADE, -- Mandatory participation for booking
    description TEXT,
    cost NUMERIC(10, 2)
);


