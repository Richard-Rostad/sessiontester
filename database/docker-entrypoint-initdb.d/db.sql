CREATE DATABASE sessiondb;
CREATE USER 'sessions'@'%' IDENTIFIED BY 'sessions';
GRANT ALL PRIVILEGES ON sessiondb.* TO 'sessions'@'%';
