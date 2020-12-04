DROP SCHEMA IF EXISTS collision_insight CASCADE;
CREATE SCHEMA AUTHORIZATION collision_insight;

CREATE TABLE collision_insight.location_data (
	zipcode NUMERIC(5), 
	county VARCHAR(50),
	city VARCHAR(85),
	state VARCHAR(2),
	PRIMARY KEY(zipcode)
);

create type hospital_types as enum('GENERAL ACUTE CARE', 'PSYCHIATRIC', 'CHILDREN', 'LONG TERM CARE',
	'CRITICAL ACCESS', 'REHABILITATION', 'MILITARY', 'WOMEN', 'SPECIAL', 'CHRONIC DISEASE');

create type hospital_naics_code as enum('622110', '622210', '622310');

create type hospital_val_method as enum('IMAGERY/OTHER', 'IMAGERY');

create type hospital_owners as enum('PROPRIETARY', 'GOVERNMENT - LOCAL','GOVERNMENT - DISTRICT/AUTHORITY', 
	'NON-PROFIT', 'GOVERNMENT - STATE', 'NOT AVAILABLE', 'GOVERNMENT - FEDERAL', 'LIMITED LIABILITY COMPANY');

create type sitting_interest as enum('sidewalk', 'both', 'roadway', 'openstreets');

create type business as enum('RS', 'RSB');

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
	trauma VARCHAR(127),
	helipad BOOLEAN, 
	PRIMARY KEY (id)
);

CREATE TABLE collision_insight.hospital_type (
	id NUMERIC(10) PRIMARY KEY, 
	type hospital_types,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE collision_insight.hospital_naics (
	id NUMERIC(10) PRIMARY KEY, 
	naics_code hospital_naics_code,
	naics_desc TEXT,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE collision_insight.hospital_val (
	id NUMERIC(10) PRIMARY KEY, 
	val_date TIMESTAMP, 
	val_method hospital_val_method,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE collision_insight.hospital_owner (
	id NUMERIC(10) PRIMARY KEY, 
	owner hospital_owners,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id) ON UPDATE CASCADE ON DELETE CASCADE
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
	others TEXT
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
	zipcode NUMERIC(5)
);

CREATE TABLE collision_insight.vehicle_repair_business_type (
	facility_id NUMERIC(7) PRIMARY KEY,
	business_type business, 
	FOREIGN KEY(facility_id) REFERENCES collision_insight.vehicle_repair_info (facility_id) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE collision_insight.vehicle_collision (
	collision_id NUMERIC(7) PRIMARY KEY,
	crash_date DATE,
	crash_time TIME,
	BORO VARCHAR,
	street_address TEXT,
	person_injured INTEGER,
	person_killed INTEGER,
	pedistrian_injured INTEGER,
	pedistrian_killed INTEGER,
	cyclist_injured INTEGER,
	cyclist_killed INTEGER,
	motorist_injured INTEGER,
	motorist_killed INTEGER,	
	zipcode NUMERIC(5),
	contributing_factors TEXT, --All the contributing factors in a single table as advised.
	vehicle_type_code TEXT -- All colliding Vehicle types in a single column
);


GRANT ALL PRIVILEGES ON collision_insight.location_data, collision_insight.hospital_details, collision_insight.hospital_type, collision_insight.hospital_naics, collision_insight.hospital_val,
collision_insight.hospital_owner, collision_insight.liquor_shop_info, collision_insight.vehicle_repair_info, collision_insight.vehicle_repair_business_type, collision_insight.vehicle_collision
to collision_insight;

