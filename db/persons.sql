CREATE DATABASE Persons;
use Persons;

CREATE TABLE `persons` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `address` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert into `persons`(`id`,`name`,`address`) values
(1,'Josip Jovanovic','Earth'),
(2,'Rahul Kumar','Mars');