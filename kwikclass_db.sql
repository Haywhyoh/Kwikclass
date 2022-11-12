CREATE DATABASE kwikclass_db;
CREATE USER 'kwikclass_admin'@'localhost' IDENTIFIED BY 'Mydreams98';
GRANT ALL PRIVILEGES ON kwikclass_db.* TO 'kwikclass_admin'@'localhost' WITH GRANT OPTION;
