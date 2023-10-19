-- Use the hbtn_0d_usa database
USE hbtn_0d_usa;

-- Find the state_id for California
SELECT id INTO @california_id FROM states WHERE name = 'California';

-- List all cities in California
SELECT * FROM cities WHERE state_id = @california_id ORDER BY id;
