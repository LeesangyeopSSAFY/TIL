use `ssafy_web_db`;


CREATE TABLE `homework` (
  `hw_id` INT,
  `studyroom_id` INT,
  `hw_title` VARCHAR(50) NOT NULL,
  `hw_content` TEXT,
  `hw_deadline` DATETIME NOT NULL,
  `hw_posted` DATETIME DEFAULT current_timestamp,
  `hw_updated` DATETIME DEFAULT current_timestamp ON UPDATE current_timestamp,
  `hw_author` VARCHAR(13) NOT NULL,
  `hw_file` LONGBLOB,
  PRIMARY KEY (`hw_id`),
  FOREIGN KEY (`studyroom_id`)
  REFERENCES studyroom(`study_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;