BEGIN;

---------------------------------------------- CREW ASSIGNMENTS ----------------------------------------------
-- Create CrewMember table
CREATE TABLE "crew_assignments_crewmember" (
    "crew_id" varchar(6) NOT NULL PRIMARY KEY,
    "role" varchar(100) NOT NULL,
    "first_name" varchar(20) NULL,
    "last_name" varchar(20) NULL,
    "middle_name" varchar(20) NULL
);

-- EDIT IT TO
-- CREATE TABLE "crew_assignments_crewmember" (
--     "crew_id" varchar(6) NOT NULL PRIMARY KEY,
--     "role" varchar(100) NOT NULL,
--     "first_name" varchar(20) NOT NULL,
--     "last_name" varchar(20) NOT NULL,
--     "middle_name" varchar(20)
-- );

-- Create FlightSchedule table
CREATE TABLE "crew_assignments_flightschedule" (
    "schedule_id" varchar(20) NOT NULL PRIMARY KEY,
    "date" date NOT NULL
);

-- Create table for CrewMember and FlightSchedule relationship 
CREATE TABLE "crew_assignments_flightschedule_crew_members" (
    "id" bigint PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "flightschedule_id" varchar(20) NOT NULL,
    "crewmember_id" varchar(6) NOT NULL,
    UNIQUE ("flightschedule_id", "crewmember_id"),
    FOREIGN KEY ("flightschedule_id") REFERENCES "crew_assignments_flightschedule" ("schedule_id")
        DEFERRABLE INITIALLY DEFERRED,
    FOREIGN KEY ("crewmember_id") REFERENCES "crew_assignments_crewmember" ("crew_id")
        DEFERRABLE INITIALLY DEFERRED
);

-- Create table for CrewMember's flight schedules with constraints
CREATE TABLE "crew_assignments_crewmember_flight_schedules" (
    "id" bigint PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "crewmember_id" varchar(6) NOT NULL,
    "flightschedule_id" varchar(20) NOT NULL,
    UNIQUE ("crewmember_id", "flightschedule_id"),
    FOREIGN KEY ("crewmember_id") REFERENCES "crew_assignments_crewmember" ("crew_id")
        DEFERRABLE INITIALLY DEFERRED,
    FOREIGN KEY ("flightschedule_id") REFERENCES "crew_assignments_flightschedule" ("schedule_id")
        DEFERRABLE INITIALLY DEFERRED
);

-- Add necessary indexes directly within the create statements if needed for performance
CREATE INDEX "idx_crewmember_role" ON "crew_assignments_crewmember" ("role" varchar_pattern_ops);
CREATE INDEX "idx_flightschedule_id" ON "crew_assignments_flightschedule" ("schedule_id" varchar_pattern_ops);
CREATE INDEX "idx_flightschedule_crewmember" ON "crew_assignments_flightschedule_crew_members" ("flightschedule_id");
CREATE INDEX "idx_crewmember_id" ON "crew_assignments_flightschedule_crew_members" ("crewmember_id");

------------------------------------ FLIGHT ROUTES APP ----------------------------------------
CREATE TABLE "flight_routes_flight" (
    "flight_id" varchar(6) NOT NULL PRIMARY KEY,
    "origin" varchar(255) NOT NULL,
    "destination" varchar(255) NOT NULL,
    "departure_time" time NOT NULL,
    "travel_duration_hours" integer DEFAULT 0 NOT NULL,
    "travel_duration_minutes" integer DEFAULT 0 NOT NULL,
    -- Ensuring no two rows have the same origin and destination
    CONSTRAINT unique_origin_destination UNIQUE ("origin", "destination")
);


-- Create an index for the flight_id to support pattern matching
CREATE INDEX "flight_routes_flight_flight_id_18e4f03d_like" ON "flight_routes_flight" ("flight_id" varchar_pattern_ops);

------------------------------------ FLIGHT BOOKING ----------------------------------------------
-- Create AdditionalItem table with constraints
CREATE TABLE "flight_booking_additionalitem" (
    "item_id" varchar(15) NOT NULL PRIMARY KEY,
    "description" text NOT NULL
);

-- Create Passenger table with constraints
CREATE TABLE "flight_booking_passenger" (
    "passenger_id" varchar(15) NOT NULL PRIMARY KEY,
    "first_name" varchar(20) NOT NULL,
    "last_name" varchar(20) NOT NULL,
    "middle_name" varchar(20) NULL
    "birth_date" date NOT NULL,
    "gender" varchar(1) NOT NULL
);

-- ALTER TABLE flight_booking_passenger
-- ADD COLUMN first_name VARCHAR(20),
-- ADD COLUMN last_name VARCHAR(20);
-- ADD COLUMN middle_name VARCHAR(20),

-- Create Booking table with constraints
CREATE TABLE "flight_booking_booking" (
    "booking_id" varchar(15) NOT NULL PRIMARY KEY,
    "total_cost" numeric(10, 2) NOT NULL,
    "booking_date" date NOT NULL,
    "flight_id" varchar(6) NOT NULL,
    "passenger_id" varchar(15) NOT NULL,
    FOREIGN KEY ("flight_id") REFERENCES "flight_routes_flight" ("flight_id")
        DEFERRABLE INITIALLY DEFERRED,
    FOREIGN KEY ("passenger_id") REFERENCES "flight_booking_passenger" ("passenger_id")
        DEFERRABLE INITIALLY DEFERRED
);

-- Create BookingAdditionalItems table with constraints
CREATE TABLE "flight_booking_booking_additional_items" (
    "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "booking_id" varchar(15) NOT NULL,
    "additionalitem_id" varchar(15) NOT NULL,
    UNIQUE ("booking_id", "additionalitem_id"),
    FOREIGN KEY ("booking_id") REFERENCES "flight_booking_booking" ("booking_id")
        DEFERRABLE INITIALLY DEFERRED,
    FOREIGN KEY ("additionalitem_id") REFERENCES "flight_booking_additionalitem" ("item_id")
        DEFERRABLE INITIALLY DEFERRED
);

-- Create indexes directly within the table creation for performance optimization
CREATE INDEX "flight_booking_additionalitem_item_id_acacec33_like" ON "flight_booking_additionalitem" ("item_id" varchar_pattern_ops);
CREATE INDEX "flight_booking_passenger_passenger_id_31f5800f_like" ON "flight_booking_passenger" ("passenger_id" varchar_pattern_ops);
CREATE INDEX "flight_booking_booking_booking_id_c2983c9d_like" ON "flight_booking_booking" ("booking_id" varchar_pattern_ops);
CREATE INDEX "flight_booking_booking_flight_id_6eb7a670" ON "flight_booking_booking" ("flight_id");
CREATE INDEX "flight_booking_booking_flight_id_6eb7a670_like" ON "flight_booking_booking" ("flight_id" varchar_pattern_ops);
CREATE INDEX "flight_booking_booking_passenger_id_c4f9fcdc" ON "flight_booking_booking" ("passenger_id");
CREATE INDEX "flight_booking_booking_passenger_id_c4f9fcdc_like" ON "flight_booking_booking" ("passenger_id" varchar_pattern_ops);
CREATE INDEX "flight_booking_booking_additional_items_booking_id_4c3b7b5b" ON "flight_booking_booking_additional_items" ("booking_id");
CREATE INDEX "flight_booking_booking_a_booking_id_4c3b7b5b_like" ON "flight_booking_booking_additional_items" ("booking_id" varchar_pattern_ops);
CREATE INDEX "flight_booking_booking_add_additionalitem_id_1bee6be6" ON "flight_booking_booking_additional_items" ("additionalitem_id");
CREATE INDEX "flight_booking_booking_a_additionalitem_id_1bee6be6_like" ON "flight_booking_booking_additional_items" ("additionalitem_id" varchar_pattern_ops);

------------------------------------ Flight Schedules -------------------------------------------
CREATE TABLE "flight_schedules_flightschedule" (
    "schedule_id" varchar(17) NOT NULL PRIMARY KEY,
    "date" date NOT NULL,
    "flight_id" varchar(6) NOT NULL,
    CONSTRAINT "flight_schedules_fli_flight_id_de09f13f_fk_flight_ro" 
        FOREIGN KEY ("flight_id") REFERENCES "flight_routes_flight" ("flight_id") 
        DEFERRABLE INITIALLY DEFERRED
);

CREATE TABLE "flight_schedules_flightschedule_crew_members" (
    "id" bigint NOT NULL PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
    "flightschedule_id" varchar(17) NOT NULL,
    "crewmember_id" varchar(6) NOT NULL,
    CONSTRAINT "flight_schedules_fli_flightschedule_id_69e4c612_fk_flight_sc" 
        FOREIGN KEY ("flightschedule_id") REFERENCES "flight_schedules_flightschedule" ("schedule_id") 
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT "flight_schedules_fli_crewmember_id_cbb57302_fk_crew_assi" 
        FOREIGN KEY ("crewmember_id") REFERENCES "crew_assignments_crewmember" ("crew_id") 
        DEFERRABLE INITIALLY DEFERRED,
    CONSTRAINT "flight_schedules_flights_flightschedule_id_crewme_8cf7ff44_uniq" 
        UNIQUE ("flightschedule_id", "crewmember_id")
);

CREATE INDEX "flight_schedules_flightschedule_schedule_id_b060a275_like" 
    ON "flight_schedules_flightschedule" ("schedule_id" varchar_pattern_ops);

CREATE INDEX "flight_schedules_flightschedule_flight_id_de09f13f" 
    ON "flight_schedules_flightschedule" ("flight_id");

CREATE INDEX "flight_schedules_flightschedule_flight_id_de09f13f_like" 
    ON "flight_schedules_flightschedule" ("flight_id" varchar_pattern_ops);

CREATE INDEX "flight_schedules_flightsch_flightschedule_id_69e4c612" 
    ON "flight_schedules_flightschedule_crew_members" ("flightschedule_id");

CREATE INDEX "flight_schedules_flights_flightschedule_id_69e4c612_like" 
    ON "flight_schedules_flightschedule_crew_members" ("flightschedule_id" varchar_pattern_ops);

