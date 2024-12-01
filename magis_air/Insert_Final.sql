

---------------------------------------------- CREW ASSIGNMENTS ----------------------------------------------
-- Insert data into CrewMember table
INSERT INTO "crew_assignments_crewmember" ("crew_id", "role", "first_name", "last_name", "middle_name")
VALUES
    ('C00001', 'Pilot', 'John', 'Doe', 'A'),
    ('C00002', 'Co-Pilot', 'Jane', 'Smith', 'B'),
    ('C00003', 'Flight Attendant', 'Emily', 'Johnson', 'C'),
    ('C00004', 'Flight Attendant', 'Michael', 'Brown', 'D');

------------------------------------ FLIGHT ROUTES APP ----------------------------------------
-- Insert data into Flight table
INSERT INTO "flight_routes_flight" ("flight_id", "origin", "destination", "departure_time", "travel_duration_hours", "travel_duration_minutes")
VALUES
    ('F00001', 'New York', 'London', '10:00:00', 7, 30),
    ('F00002', 'Los Angeles', 'Tokyo', '15:00:00', 11, 45),
    ('F00003', 'Paris', 'Berlin', '08:30:00', 1, 45);

------------------------------------ FLIGHT SCHEDULES -------------------------------------------
-- Insert data into CrewSchedule table
INSERT INTO "crew_assignments_flightschedule" ("schedule_id", "date")
VALUES
    ('S00001', '2024-12-01'),
    ('S00002', '2024-12-02'),
    ('S00003', '2024-12-03');

-- Insert data into FlightSchedule table
INSERT INTO "flight_schedules_flightschedule" ("schedule_id", "date", "flight_id")
VALUES
    ('FS0001', '2024-12-01', 'F00001'),
    ('FS0002', '2024-12-02', 'F00002'),
    ('FS0003', '2024-12-03', 'F00003');

-- Insert data into CrewMember and FlightSchedule relationship table
INSERT INTO "crew_assignments_flightschedule_crew_members" ("flightschedule_id", "crewmember_id")
VALUES
    ('S00001', 'C00001'),
    ('S00001', 'C00002'),
    ('S00002', 'C00003'),
    ('S00003', 'C00004');

-- Insert data into CrewMember's flight schedules table
INSERT INTO "crew_assignments_crewmember_flight_schedules" ("crewmember_id", "flightschedule_id")
VALUES
    ('C00001', 'FS0001'),
    ('C00002', 'FS0001'),
    ('C00003', 'FS0002'),
    ('C00004', 'FS0003');

------------------------------------ FLIGHT BOOKING ----------------------------------------------



-- Insert data into BookingAdditionalItems table
INSERT INTO "flight_booking_additionalitem" ("item_id", "description")
VALUES
    ('I00001', 'Banana'),
    ('I00002', 'Baggage'),
    ('I00003', 'Shoes');


-- Insert data into Passenger table
INSERT INTO "flight_booking_passenger" ("passenger_id", "name", "birth_date", "gender")
VALUES
    ('P00001', 'Alice Williams', '1990-05-14', 'F'),
    ('P00002', 'Bob Brown', '1985-11-22', 'M'),
    ('P00003', 'Charlie Davis', '1992-08-19', 'M');

-- Insert data into Booking table with a placeholder for additional_items
INSERT INTO "flight_booking_booking" ("booking_id", "total_cost", "booking_date", "flight_id", "passenger_id", "additional_items")
VALUES
    ('B00001', 500.00, '2024-11-30', 'F00001', 'P00001', 'Banana'),
    ('B00002', 300.00, '2024-11-29', 'F00002', 'P00002', 'Baggage'),
    ('B00003', 450.00, '2024-11-28', 'F00003', 'P00003', 'Shoes');





------------------------------------ Flight Schedules -------------------------------------------
-- Insert data into FlightScheduleCrewMembers table
INSERT INTO "flight_schedules_flightschedule_crew_members" ("flightschedule_id", "crewmember_id")
VALUES
    ('FS0001', 'C00001'),
    ('FS0001', 'C00002'),
    ('FS0002', 'C00003'),
    ('FS0003', 'C00004');

