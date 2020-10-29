CREATE TABLE collision_insight.location_data (
	zipcode NUMERIC(5) PRIMARY KEY,
	city TEXT,
	county TEXT,
	country TEXT,
	countyfips NUMERIC(5),
	state VARCHAR(2),
	state_id TEXT,
	state_fips NUMERIC(2)
);

CREATE TABLE collision_insight.geometric_data (
	latitude NUMERIC PRIMARY KEY,
	longitude NUMERIC 
);

CREATE TABLE collision_insight.hospital (
	address TEXT, 
	alt_name TEXT, 
	beds INT CHECK (beds >= 0), 
	helipad TEXT, 
	id NUMERIC(10), 
	naics_code TEXT, 
	naics_desc TEXT, 
	name TEXT, 
	owner TEXT, 
	population INT, 
	source TEXT, 
	sourcedate TIMESTAMP, 
	status TEXT, 
	telephone TEXT, 
	trauma TEXT, 
	ttl_staff INT, 
	type TEXT,
	val_date TIMESTAMP, 
	val_method TEXT, 
	website TEXT, 
	PRIMARY KEY (id),
	zipcode NUMERIC(5),
	latitude NUMERIC,
	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode),
	FOREIGN KEY(latitude) REFERENCES geometric_data (latitude)

);

CREATE TABLE collision_insight.liquor_licence (
	serial_number BIGSERIAL PRIMARY KEY, 
	license_type_code INT, 
	license_class_code INT,
	certificate_number INTEGER, 
	premise_name TEXT, 
	dba TEXT, 
	premise_address TEXT, 
	premise_address2 TEXT, 
	license_issued_date DATE, 
	license_expiration_date DATE, 
	method_of_operation TEXT, 
	days_hours_of_operation TEXT, 
	other TEXT, 
	zipcode NUMERIC(5),
	latitude NUMERIC,
	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode),
	FOREIGN KEY(latitude) REFERENCES geometric_data (latitude)
);

CREATE TABLE collision_insight.vehicle_repair (
	facility_id INTEGER PRIMARY KEY,
	facility TEXT, 	
	facility_name TEXT, 	
	facility_street TEXT,  	
	owner_name TEXT,	
	owner_name_overflow TEXT,	
	business_type TEXT,	
	original_issuance DATE, 	
	last_renewal DATE, 	
	expiration DATE, 	
	zipcode NUMERIC(5),
	latitude NUMERIC,
	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode),
	FOREIGN KEY(latitude) REFERENCES geometric_data (latitude)
);

CREATE TABLE collision_insight.vehicle_crashes (
	serial_no BIGSERIAL PRIMARY KEY,
	year YEAR,
	crash_descriptor TEXT, 	
	time TIME, 	
	date DATE,
	day_of_week TEXT, 	
	police_report TEXT,
	lighting_conditions TEXT,	
	municipality TEXT,
	collision_type_descriptor TEXT, 		
	road_descriptor TEXT,	
	weather_conditions TEXT, 	
	traffic_control_device TEXT,	
	road_surface_conditions TEXT,	
	dot_reference_marker_location TEXT, 	
	pedestrian_bicyclist_action TEXT,	
	event_descriptor TEXT, 	
	number_of_vehicles_involved INTEGER,
	zipcode NUMERIC(5),
	latitude NUMERIC,
	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode),
	FOREIGN KEY(latitude) REFERENCES geometric_data (latitude)
);
