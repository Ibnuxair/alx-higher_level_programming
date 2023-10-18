-- a script that creates the MySQL server user user_0d_1
-- Grant all privileges to user_0d_1
-- Flush privileges to apply the changes
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost' WITH GRANT OPTION;
FLUSH PRIVILEGES;
