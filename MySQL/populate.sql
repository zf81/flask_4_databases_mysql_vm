INSERT INTO physicians (physician_name, phys_specialty) VALUES 
('Dr. Carmen Waters', 'Oncology'),
('Dr. Kristen Moore', 'Urology'),
('Dr. Iris Crocitto', 'Endocrinology');

INSERT INTO patients (first_name, last_name, date_of_birth, onc_physician_id) VALUES
('Deanna', 'Morgan', '1992-07-13', 1), 
('Preston', 'Floyd', '1979-10-09', 2), 
('Georgia', 'Sanchez', '1988-06-21', 3); 

INSERT INTO patientlabs (patient_id, physician_id, lab_name, lab_date, lab_results) VALUES
(1, 1, 'Complete Blood Count', '2023-07-30', 'Low WBC'),
(2, 2, 'PSA', '2023-05-10', 'WNL'),
(3, 3, 'TSH', '2023-11-17', 'Elevated TSH');