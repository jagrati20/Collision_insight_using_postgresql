CREATE TABLE collision_insight.location_data (
	zipcode NUMERIC(5),
	city TEXT,
	county TEXT,
	country TEXT,
	countyfips NUMERIC(5),
	state VARCHAR(2),
	state_fips NUMERIC(2),
	latitude INTEGER,
	longitude INTEGER,
	PRIMARY KEY(zipcode)
);

CREATE TABLE collision_insight.geometric_data (
	latitude NUMERIC,
	longitude NUMERIC,
	zipcode NUMERIC(5),
	PRIMARY KEY(latitude, longitude), 
	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode)
);

CREATE TABLE collision_insight.hospital_details (

	address VARCHAR(255),  
	name VARCHAR(255), 
	owner TEXT,
	telephone NUMERIC(10), 
	population INT, 
	source TEXT, 
	sourcedate TIMESTAMP, 
	website TEXT, 
	alt_name TEXT, 
	beds INT CHECK (beds >= 0), 
	helipad BOOLEAN, 
	website TEXT, 
	id NUMERIC(10), 
	PRIMARY KEY (id),
	zipcode NUMERIC(5),

	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode),
);

CREATE TABLE collision_insight.hospital_type (
	id NUMERIC(10) PRIMARY KEY, 
	type VARCHAR(20),
	FOREIGN KEY(id) REFERENCES hospital_details (id),
);

CREATE TABLE collision_insight.hospital_type (
	id NUMERIC(10) PRIMARY KEY, 
	status BOOLEAN,
	FOREIGN KEY(id) REFERENCES hospital_details (id),
);

CREATE TABLE collision_insight.hospital_naics (
	id NUMERIC(10) PRIMARY KEY, 
	naics_code NUMERIC(6),
	naics_desc TEXT,
	FOREIGN KEY(id) REFERENCES hospital_details (id),
);

CREATE TABLE collision_insight.hospital_val (
	id NUMERIC(10) PRIMARY KEY, 
	val_date TIMESTAMP, 
	val_method TEXT, 
	FOREIGN KEY(id) REFERENCES hospital_details (id),
);

CREATE TABLE collision_insight.hospital_owner (
	id NUMERIC(10) PRIMARY KEY, 
	owner 
	FOREIGN KEY(id) REFERENCES hospital_details (id),
);

CREATE TABLE collision_insight.liquor_shop_info (
	
	license_type_code VARCHAR(2), 
	license_class_code NUMERIC(3),
	certificate_number INTEGER, 
	license_issued_date DATE, 
	license_expiration_date DATE, 
	method_of_operation VARCHAR(255), 
	premise_name VARCHAR(255), 
	premise_address TEXT, 
	premise_address2 TEXT, 
	dba VARCHAR(255),
	others TEXT,
	serial_number BIGSERIAL PRIMARY KEY, 
	zipcode NUMERIC(5),
	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode)
);

CREATE TABLE collision_insight.liquor_shop_extras (
	days_hours_of_operation TEXT, 
	serial_number BIGSERIAL PRIMARY KEY, 
	FOREIGN KEY(serial_number) REFERENCES liquor_shop_info (serial_number)
);

CREATE TABLE collision_insight.vehicle_repair_info (
	facility_id NUMERIC(7) PRIMARY KEY, 
	facility_name VARCHAR(255), 
	facility_name_overflow TEXT, 
	facility_street TEXT, 
	owner_name VARCHAR(255),	
	owner_name_overflow TEXT,	
	original_issuance DATE, 	
	last_renewal DATE, 	
	expiration DATE, 		
	zipcode NUMERIC(5),
	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode)
);

CREATE TABLE collision_insight.vehicle_repair_business_type (
	business_type BOOLEAN,
	facility_id NUMERIC(7) PRIMARY KEY, 
	FOREIGN KEY(facility_id) REFERENCES vehicle_repair_info (facility_id)
);

CREATE TABLE collision_insight.vehicle_crashes (
	serial_no BIGSERIAL PRIMARY KEY,
	year YEAR, 	
	time TIME, 	
	date DATE,	
	police_report BOOLEAN,
	municipality TEXT,
	traffic_control_device TEXT, 
	dot_reference_marker_location VARCHAR(20), 			
	number_of_vehicles_involved INTEGER,
	zipcode NUMERIC(5),
	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode)
);

CREATE TABLE collision_insight.vehicle_crashes_descriptor (
	serial_no BIGSERIAL PRIMARY KEY,
	crash_descriptor VARCHAR(63), 
	FOREIGN KEY(serial_no) REFERENCES vehicle_crashes(serial_no)
);

CREATE TABLE collision_insight.vehicle_crashes_day (
	serial_no BIGSERIAL PRIMARY KEY,
	day_of_week VARCHAR(9),
	FOREIGN KEY(serial_no) REFERENCES vehicle_crashes(serial_no)
);
		
CREATE TABLE collision_insight.vehicle_crashes_lighting (
	serial_no BIGSERIAL PRIMARY KEY,
	lighting_conditions VARCHAR(20),
	FOREIGN KEY(serial_no) REFERENCES vehicle_crashes(serial_no)
);

CREATE TABLE collision_insight.vehicle_crashes_collision_desc (
	serial_no BIGSERIAL PRIMARY KEY,
	collision_type_descriptor VARCHAR(15), 		
	FOREIGN KEY(serial_no) REFERENCES vehicle_crashes(serial_no)
);

CREATE TABLE collision_insight.vehicle_crashes_collision_weather (
	serial_no BIGSERIAL PRIMARY KEY,
	weather_conditions VARCHAR(30), 
	FOREIGN KEY(serial_no) REFERENCES vehicle_crashes(serial_no)
);
	
CREATE TABLE collision_insight.vehicle_crashes_collision_road_info (
	serial_no BIGSERIAL PRIMARY KEY,
	road_descriptor VARCHAR(30),
	road_surface_conditions VARCHAR(15),		
	FOREIGN KEY(serial_no) REFERENCES vehicle_crashes(serial_no)
);

CREATE TABLE collision_insight.vehicle_crashes_bicyclist (
	serial_no BIGSERIAL PRIMARY KEY,
	pedestrian_bicyclist_action VARCHAR(50),	
	FOREIGN KEY(serial_no) REFERENCES vehicle_crashes(serial_no)
);


