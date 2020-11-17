CREATE TABLE collision_insight.location_data (
	zipcode NUMERIC(5),
	city TEXT,
	county TEXT,
	country TEXT,
	countyfips NUMERIC(5),
	state VARCHAR(2),
	state_id TEXT,
	state_fips NUMERIC(2),
	latitude NUMERIC,
	longitude NUMERIC,
	PRIMARY KEY(zipcode, latitude, longitude)
);

-- CREATE TABLE collision_insight.geometric_data (
-- 	latitude NUMERIC,
-- 	longitude NUMERIC,
-- 	PRIMARY KEY(latitude, longitude) 
-- );

CREATE TABLE collision_insight.hospital_extra (
	alt_name TEXT, 
	beds INT CHECK (beds >= 0), 
	helipad TEXT, 
	id NUMERIC(10), 
	name TEXT, 
	owner TEXT, 
	population INT, 
	ttl_staff INT, 
	type TEXT,
	PRIMARY KEY (id),
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode,latitude, longitude) REFERENCES location_data (zipcode,latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);

CREATE TABLE collision_insight.hospital_details (
	address TEXT, 
	id NUMERIC(10), 
	name TEXT, 
	owner TEXT, 
	status TEXT NOT NULL, 
	telephone TEXT, 
	type TEXT,
	val_date TIMESTAMP, 
	val_method TEXT, 
	website TEXT, 
	PRIMARY KEY (id),
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode,latitude, longitude) REFERENCES location_data (zipcode,latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);

CREATE TABLE collision_insight.hospital_source (
	naics_code TEXT, 
	naics_desc TEXT, 
	source TEXT, 
	sourcedate TIMESTAMP, 
	status TEXT, 
	website TEXT, 
	id NUMERIC(10), 
	PRIMARY KEY (id),
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode,latitude, longitude) REFERENCES location_data (zipcode,latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);

CREATE TABLE collision_insight.liquor_shop_license (
	serial_number BIGSERIAL PRIMARY KEY, 
	license_type_code INT, 
	license_class_code INT,
	certificate_number INTEGER, 
	license_issued_date DATE, 
	license_expiration_date DATE, 
	method_of_operation TEXT, 
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode, latitude, longitude) REFERENCES location_data (zipcode, latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);

CREATE TABLE collision_insight.liquor_shop_info (
	serial_number BIGSERIAL PRIMARY KEY,  
	premise_name TEXT, 
	premise_address TEXT, 
	premise_address2 TEXT, 
	dba TEXT,
	days_hours_of_operation TEXT, 
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode, latitude, longitude) REFERENCES location_data (zipcode, latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);

CREATE TABLE collision_insight.vehicle_repair_license (
	facility_id INTEGER PRIMARY KEY,
	business_type TEXT,	
	original_issuance DATE, 	
	last_renewal DATE, 	
	expiration DATE, 	
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode, latitude, longitude) REFERENCES location_data (zipcode, latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);

CREATE TABLE collision_insight.vehicle_repair_info (
	facility_id INTEGER PRIMARY KEY,
	facility_name TEXT, 	
	facility_name_overflow TEXT, 	
	facility_street TEXT,  	
	owner_name TEXT,	
	owner_name_overflow TEXT,	 	
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode, latitude, longitude) REFERENCES location_data (zipcode, latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);

CREATE TABLE collision_insight.vehicle_repair_owner (
	facility_id INTEGER PRIMARY KEY, 	
	owner_name TEXT,	
	owner_name_overflow TEXT,	 	
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode, latitude, longitude) REFERENCES location_data (zipcode, latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);

CREATE TABLE collision_insight.vehicle_crashes_event (
	serial_no BIGSERIAL PRIMARY KEY,
	year YEAR, 	
	time TIME, 	
	date DATE,	
	event_descriptor TEXT, 
	police_report BOOLEAN,
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode, latitude, longitude) REFERENCES location_data (zipcode, latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);

CREATE TABLE collision_insight.vehicle_crashes_desciption (
	serial_no BIGSERIAL PRIMARY KEY,
	day_of_week TEXT, 	
	lighting_conditions TEXT,	
	municipality TEXT,
	collision_type_descriptor TEXT, 		
	road_descriptor TEXT,	
	weather_conditions TEXT, 	
	traffic_control_device TEXT,	
	road_surface_conditions TEXT,	
	dot_reference_marker_location VARCHAR(20), 	
	pedestrian_bicyclist_action TEXT,		
	number_of_vehicles_involved INTEGER,
	zipcode NUMERIC(5),
	latitude NUMERIC,
	longitude NUMERIC,
	FOREIGN KEY(zipcode, latitude, longitude) REFERENCES location_data (zipcode, latitude, longitude),
	-- FOREIGN KEY(latitude, longitude) REFERENCES geometric_data (latitude, longitude)
);