# flask_4_databases_mysql_vm

#### MySQL Setup on Azure/GCP VM:
 - For this portion of the assignment, I used Azure
 - Log into your Azure student account and create a new virtual machine.
 - Create a new resource group and give it a name.
 - Select **US EAST** for the region. Change the security type to **Standard**. Change the size to **B1ms**. 
 - Under the authentication type option, create a username and password.
 - On reviewing the configurations for the virtual machine, the price per hour came out to be 0.0207 USD.
 - Once the configurations are reviewed, press **create**.
 - In a new tab, log in to Google Shell. Type in ```ssh``` into the terminal.
 - Then, type in ```ssh [username that you created for Azure Virtual Machine]@[IP address of your Virtual Machine]```. You will see a message, **Are you sure you want to continue connecting (yes/no/[fingerprint])? Type in yes and then type in your password that you created for the Azure virtual machine.
 - If the username and password are correct, you will be connected to Ubuntu 20.04.6.
 - Type in ```sudo apt-get update```. You will see a message asking if you want to continue. Type in Y.
 - Type in ```sudo mysql``` to enter the MySQL connection.
 - To create a user for the MySQL connection, enter ```create user '<user>'@'%' IDENTIFIED BY '<password>';``` Choose a <user> and <password> and be sure to save it.
 - Next, type in ```select user from mysql.user;```. This will show a list of users and you should be able to see the user you created within this list.
 - To grant priviliges to your user, enter ```grant all privileges on *.* to '<user>'@'%' with grant option;```
 - In your Azure virtual machine, go to **Networking**. Click on **Add inbound security rule** and change the Service to MySQL. This will add port **3306** to the Destination Port Ranges.
 - Navigate back to Google Shell and in the terminal enter ```\quit``` which will exit you out of the MySQL connection.
 - Type in ```sudo nano /etc/mysql/mysql.conf.d/mysqld.cnf``` which will being you to the nano terminal. Click the downwards arrow until you reach **bind address** and change it to ```0.0.0.0```. Type Ctrl + O to save. Hit enter. Then type Ctrl + X to exit out of the nano terminal.
 - Back in the regular terminal, type in ```/etc/init.d/mysql restart```. Then you will be asked to enter the password for your virtual machine.
 - Open MySQL Workbench and create a new connection. Choose a new connection name.
 - For the Hostname, enter the IP address of your Azure virtual machine and under user, you will enter the user you created for the MySQL connection. Enter your password from <password> that you created when creating a user for the MySQL connection. Test the connection to ensure it is successful.

#### Creating a Simple Database with Tables:
 - In MySQL Workbench, I entered the following to create a database called stonybrooknyhospital
```
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
```

To populate the tables with fake data, I entered the following:

```
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
```

 - Click on **Database** and choose **Reverse Engineer** to create the ERD diagram.

 - ![image]()



