-- script that lists all the tables of a database in my MySQL server.
USE mysql;
SELECT table_name AS "Tables_in_mysql"
FROM information_schema.tables
WHERE table_schema = 'mysql';
