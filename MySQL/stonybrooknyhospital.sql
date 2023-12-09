CREATE DATABASE stonybrooknyhospital;

USE stonybrooknyhospital;

CREATE TABLE physicians (
    physician_id INT PRIMARY KEY AUTO_INCREMENT,
    physician_name VARCHAR(50) NOT NULL,
    phys_specialty VARCHAR(50) NOT NULL,
);

CREATE TABLE patients (
    patient_id INT PRIMARY KEY AUTO_INCREMENT,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    date_of_birth DATE,
    onc_physician_id INT,
    FOREIGN KEY (onc_physician_id) REFERENCES physicians(physician_id)
);

CREATE TABLE patientlabs (
    lab_id INT PRIMARY KEY AUTO_INCREMENT,
    patient_id INT,
    physician_id INT,
    lab_name VARCHAR(50),
    lab_date DATE,
    lab_results TEXT,
    FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
    FOREIGN KEY (physician_id) REFERENCES physicians(physician_id)
);