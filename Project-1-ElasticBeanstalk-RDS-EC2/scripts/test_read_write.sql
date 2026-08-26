-- Simple read/write test script to run once connected to the RDS instance
CREATE TABLE IF NOT EXISTS connection_test (
    id INT AUTO_INCREMENT PRIMARY KEY,
    message VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO connection_test (message) VALUES ('EC2 successfully connected to RDS via Elastic Beanstalk VPC');

SELECT * FROM connection_test;
