CREATE DATABASE Persons;
use Persons;

CREATE TABLE `persons` (
  `id` int unsigned NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `email` varchar(100) NOT NULL,
  `phone` int unsigned NOT NULL,
  `address` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

insert into `persons`(`id`,`name`,`email`,`phone`,`address`) values
(1,'Josip Jovanovic','sroy@gmail.com',2147483647,'Earth'),
(2,'Rahul Kumar','rahul@gmail.com',34256780,'Mars');