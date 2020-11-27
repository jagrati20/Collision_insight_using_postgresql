-- This table combines the column which are in 3 of the 4 tabels 
-- The last table i.e. vehicle collision has only zip code, but we 
-- will get the county city and state from out additional dataset.

CREATE TABLE collision_insight.location_data (
	zipcode NUMERIC(5), 
	county VARCHAR(50),
	city VARCHAR(85),
	state VARCHAR(2),
	PRIMARY KEY(zipcode)
);


-- Although our dataset has latitude and longitude, we are not considering it now.

-- CREATE TABLE collision_insight.geometric_data (
-- 	latitude INTEGER,
-- 	longitude INTEGER,
-- 	zipcode NUMERIC(5),
-- 	PRIMARY KEY(latitude, longitude), 
-- 	FOREIGN KEY(zipcode) REFERENCES location_data (zipcode)
-- );


-- https://hifld-geoplatform.opendata.arcgis.com/datasets/hospitals/data
-- This is for USA and has 7596 rows

CREATE TABLE collision_insight.hospital_details (
	-- To remove these 4 column or keep them here in the schema 
	-- instead of placing them in the combined location dataset
	country TEXT,
	countyfips NUMERIC(5),
	state_id VARCHAR(10),
	state_fips NUMERIC(2),


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

	FOREIGN KEY(zipcode) REFERENCES collision_insight.location_data (zipcode)
);

CREATE TABLE collision_insight.hospital_type (
	id NUMERIC(10) PRIMARY KEY, 
	type VARCHAR(20),
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id),
);

CREATE TABLE collision_insight.hospital_status (
	id NUMERIC(10) PRIMARY KEY, 
	status BOOLEAN,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id)
);

CREATE TABLE collision_insight.hospital_naics (
	id NUMERIC(10) PRIMARY KEY, 
	naics_code NUMERIC(6),
	naics_desc TEXT,
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id)
);

CREATE TABLE collision_insight.hospital_val (
	id NUMERIC(10) PRIMARY KEY, 
	val_date TIMESTAMP, 
	val_method TEXT, 
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id)
);

CREATE TABLE collision_insight.hospital_owner (
	id NUMERIC(10) PRIMARY KEY, 
	owner 
	FOREIGN KEY(id) REFERENCES collision_insight.hospital_details (id)
);


-- https://data.ny.gov/Economic-Development/Liquor-Authority-Current-List-of-Active-Licenses/hrvs-fxs2
-- This is for NY State and has 50.5K rows 
-- Full county name

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
	FOREIGN KEY(zipcode) REFERENCES collision_insight.location_data (zipcode)
);

CREATE TABLE collision_insight.liquor_shop_extras (
	days_hours_of_operation TEXT, 
	serial_number BIGSERIAL PRIMARY KEY, 
	FOREIGN KEY(serial_number) REFERENCES collision_insight.liquor_shop_info (serial_number)
);


-- https://data.ny.gov/Transportation/Vehicle-Repair-Shops-Across-New-York-State/icjc-x44x
-- This is for NY State with 23.7K rows
-- This dataset has county in 4 letters 

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
	-- RS and RSB types
	facility_id NUMERIC(7) PRIMARY KEY, 
	FOREIGN KEY(facility_id) REFERENCES collision_insight.vehicle_repair_info (facility_id)
);


-- https://data.cityofnewyork.us/Public-Safety/Motor-Vehicle-Collisions-Crashes/h9gi-nx95
-- This is for NYC only with 1.73M rows.

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


