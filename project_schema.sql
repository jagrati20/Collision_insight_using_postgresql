CREATE TABLE collision_insight.location_data (
	zipcode NUMERIC(5), 
	county VARCHAR(50),
	city VARCHAR(85),
	state VARCHAR(2),
	PRIMARY KEY(zipcode)
);

create type hospital_type as enum('GENERAL ACUTE CARE', 'PSYCHIATRIC', 'CHILDREN', 'LONG TERM CARE',
	'CRITICAL ACCESS', 'REHABILITATION', 'MILITARY', 'WOMEN', 'SPECIAL', 'CHRONIC DISEASE');

create type hospital_naics_code as enum('622110', '622210', '622310');

create type hospital_val_method as enum('IMAGERY/OTHER', 'IMAGERY');

create type hospital_owner as enum('PROPRIETARY', 'GOVERNMENT - LOCAL','GOVERNMENT - DISTRICT/AUTHORITY', 
	'NON-PROFIT', 'GOVERNMENT - STATE', 'NOT AVAILABLE', 'GOVERNMENT - FEDERAL', 'LIMITED LIABILITY COMPANY');

CREATE TABLE collision_insight.hospital_details (
	id NUMERIC(10),   
	name VARCHAR(255),
	alt_name TEXT,
	address VARCHAR(255),
	zipcode NUMERIC(5), 
	telephone NUMERIC(10), 
	status BOOLEAN,
	population INT, 
	source TEXT, 
	sourcedate TIMESTAMP, 
	website TEXT,  
	beds INT CHECK (beds >= 0), 
	trauma VARCHAR(25),
	helipad BOOLEAN, 
	PRIMARY KEY (id),
	FOREIGN KEY(zipcode) REFERENCES collision_insight.location_data (zipcode)
);

CREATE TABLE collision_insight.hospital_type (
	id NUMERIC(10) PRIMARY KEY, 
	type hospital_type,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id)
);

CREATE TABLE collision_insight.hospital_naics (
	id NUMERIC(10) PRIMARY KEY, 
	naics_code hospital_naics_code,
	naics_desc TEXT,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id)
);

CREATE TABLE collision_insight.hospital_val (
	id NUMERIC(10) PRIMARY KEY, 
	val_date TIMESTAMP, 
	val_method hospital_val_method,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id)
);

CREATE TABLE collision_insight.hospital_owner (
	id NUMERIC(10) PRIMARY KEY, 
	owner hospital_owner,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id)
);

CREATE TABLE collision_insight.liquor_shop_info (
	serial_number BIGSERIAL PRIMARY KEY,
	license_type_code VARCHAR(2), 
	license_class_code NUMERIC(3),
	certificate_number INTEGER, 
	premise_name VARCHAR(255), 
	dba VARCHAR(255),
	premise_address TEXT, 
	premise_address2 TEXT, 
	zipcode NUMERIC(5),
	license_issued_date DATE, 
	license_expiration_date DATE, 
	method_of_operation VARCHAR(255), 
	days_hours_of_operation TEXT, 
	others TEXT,
	FOREIGN KEY(zipcode) REFERENCES collision_insight.location_data (zipcode)
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
	FOREIGN KEY(zipcode) REFERENCES collision_insight.location_data (zipcode)
);

CREATE TABLE collision_insight.vehicle_repair_business_type (
	business_type BOOLEAN,
	facility_id NUMERIC(7) PRIMARY KEY, 
	FOREIGN KEY(facility_id) REFERENCES collision_insight.vehicle_repair_info (facility_id)
);

CREATE TABLE collision_insight.vehicle_collision (
	crash_date DATE,
	crash_time TIME,
	BORO VARCHAR,
	on_street_name VARCHAR,
	cross_street_name VARCHAR,
	off_street_name VARCHAR,
	person_injured INTEGER,
	person_killed INTEGER,
	pedistrian_injured INTEGER,
	pedistrian_killed INTEGER,
	cyclist_injured INTEGER,
	cyclist_killed INTEGER,
	motorist_injured INTEGER,
	motorist_killed INTEGER,
	collision_id NUMERIC(7) PRIMARY KEY,	
	zipcode NUMERIC(5),
	FOREIGN KEY(zipcode) REFERENCES collision_insight.location_data (zipcode)
);

CREATE TABLE collision_insight.contributing_factor_vehicle (
	contributing_factor_vehicle_1 VARCHAR(20),
	contributing_factor_vehicle_2 VARCHAR(20),
	contributing_factor_vehicle_3 VARCHAR(20),
	contributing_factor_vehicle_4 VARCHAR(20),
	contributing_factor_vehicle_5 VARCHAR(20),
	collision_id NUMERIC(7) PRIMARY KEY,
	FOREIGN KEY(collision_id) REFERENCES collision_insight.vehicle_collision (collision_id)
);

CREATE TABLE collision_insight.vehicle_type (
	vehicle_1 TEXT,
	vehicle_2 TEXT,
	vehicle_3 TEXT,
	vehicle_4 TEXT,
	vehicle_5 TEXT,
	collision_id NUMERIC(7) PRIMARY KEY,
	FOREIGN KEY(collision_id) REFERENCES collision_insight.vehicle_collision (collision_id)
);

GRANT ALL PRIVILEGES ON location_data, hospital_details, hospital_type, hospital_naics, hospital_val,
hospital_owner, liquor_shop_info, vehicle_repair_info, vehicle_repair_business_type, vehicle_collision,
contributing_factor_vehicle, vehicle_type TO collision_insight;

