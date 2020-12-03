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

create type sitting_interest as enum('sidewalk', 'both', 'roadway', 'openstreets');

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

CREATE TABLE collision_insight.restaurant_info (
	id BIGSERIAL PRIMARY KEY,
	seating_interest sitting_interest,
	restaurant_name VARCHAR(127),
	legal_business_name VARCHAR(127),
	DBA VARCHAR(127),
	zipcode NUMERIC(5),
	business_address VARCHAR(255),
	food_service_establishment_permit NUMERIC(10),
	approved_for_sidewalk_seating BOOLEAN,
	approved_for_roadway_eating BOOLEAN,
	qualify_alcohol BOOLEAN,
	SLA_license_type VARCHAR(2),
	landmark_district_or_building BOOLEAN,
	landmark_district_terms BOOLEAN,
	health_compliance_terms BOOLEAN,
	time_of_submission TIMESTAMP,
	bin NUMERIC(10),
	bbl NUMERIC(10),
	nta VARCHAR(67),
	FOREIGN KEY(zipcode) REFERENCES collision_insight.location_data (zipcode)
);


GRANT ALL PRIVILEGES ON location_data, hospital_details, hospital_type, hospital_naics, hospital_val,
hospital_owner, liquor_shop_info, vehicle_repair_info, vehicle_repair_business_type, restaurant_info;

