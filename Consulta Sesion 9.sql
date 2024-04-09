CREATE TABLE cities (
 ciudad_id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(255),
 status boolean
 );
 
CREATE TABLE jobsJ(
 jobs_id INT AUTO_INCREMENT PRIMARY KEY,
 name VARCHAR(255),
 status boolean
 );

CREATE TABLE employees (
 employees_id INT AUTO_INCREMENT PRIMARY KEY,
 nombre VARCHAR(255),
 ciudad_id INT,
 jobs_id INT,
 salary DOUBLE,
 STATUS BOOLEAN DEFAULT 1,
 FOREIGN KEY (ciudad_id) REFERENCES cities(ciudad_id),
 FOREIGN KEY (jobs_id) REFERENCES jobsJ(jobs_id)
 );
