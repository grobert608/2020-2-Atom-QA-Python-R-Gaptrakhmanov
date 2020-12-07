CREATE DATABASE IF NOT EXISTS MYSQL_DB;
CREATE USER IF NOT EXISTS `test_qa`@`%` IDENTIFIED BY 'qa_test';
GRANT USAGE ON *.* TO `test_qa`@`%`;
GRANT ALL PRIVILEGES ON `MYSQL_DB`.* TO `test_qa`@`%`;
USE MYSQL_DB;
CREATE TABLE IF NOT EXISTS `test_users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `username` varchar(16) DEFAULT NULL,
  `password` varchar(255) NOT NULL,
  `email` varchar(64) NOT NULL,
  `access` smallint DEFAULT NULL,
  `active` smallint DEFAULT NULL,
  `start_active_time` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `ix_test_users_username` (`username`)
)
;