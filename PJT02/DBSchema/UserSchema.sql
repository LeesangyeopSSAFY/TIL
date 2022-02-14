use `ssafy_web_db`;

drop table student;
drop table teacher;

CREATE TABLE `student` (
  `st_id` varchar(20) NOT NULL,
  `st_name` varchar(10) NOT NULL,
  `st_email` varchar(72) NOT NULL,
  `st_password` varchar(255) NOT NULL,
  `st_contact` varchar(13) DEFAULT NULL,
  `st_signup_date` DATETIME not null DEFAULT CURRENT_TIMESTAMP,
  `st_birthday` DATE DEFAULT NULL,
  `st_school` varchar(20) DEFAULT NULL,
  `st_img` longblob DEFAULT NULL,
  PRIMARY KEY (`st_id`),
  unique key (`st_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

CREATE TABLE `teacher` (
  `tchr_id` varchar(20) NOT NULL,
  `tchr_name` varchar(10) NOT NULL,
  `tchr_email` varchar(72) NOT NULL,
  `tchr_password` varchar(255) NOT NULL,
  `tchr_contact` varchar(13) DEFAULT NULL,
  `tchr_signup_date` DATETIME not null DEFAULT CURRENT_TIMESTAMP,
  `tchr_birthday` DATE DEFAULT NULL,
  `tchr_school` varchar(20) DEFAULT NULL,
  `tchr_img` longblob DEFAULT NULL,
  PRIMARY KEY (`tchr_id`),
  unique key (`tchr_email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
