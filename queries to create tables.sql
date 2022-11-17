CREATE TABLE owner(
	government_number VARCHAR(64) PRIMARY KEY,
	engine_number VARCHAR(64),
	color VARCHAR(64), 
	brand VARCHAR(64), 
	technical_passport_number VARCHAR(64),
	driver_license_number VARCHAR(64),
	owner_name VARCHAR(64),
	place_of_residence VARCHAR(64),
	year_of_birth VARCHAR(64),
	sex VARCHAR(64)
);


CREATE TABLE police(
	name VARCHAR(64) PRIMARY KEY,
    job_title VARCHAR(64),
    rank VARCHAR(64),
);


CREATE TABLE inspection(
    government_number VARCHAR(64) REFERENCES owner(government_number),
    name VARCHAR(64) REFERENCES police(name), 
    CONSTRAINT government_number_name PRIMARY KEY (government_number, name),
    result VARCHAR(64), 
    result_inspection TEXT,
    date VARCHAR(64),
)

