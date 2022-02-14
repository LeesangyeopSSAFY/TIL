use `ssafy_web_db`;


CREATE TABLE `notice` (
  `notice_id` INT,
  `studyroom_id` INT,
  `notice_title` VARCHAR(50) NOT NULL,
  `notice_content` TEXT NOT NULL,
  `notice_posted` DATETIME DEFAULT current_timestamp,
  `notice_updated` DATETIME DEFAULT current_timestamp ON UPDATE current_timestamp,
  `notice_author` VARCHAR(13) NOT NULL,
  `notice_file` LONGBLOB,
  PRIMARY KEY (`notice_id`),
  FOREIGN KEY (`studyroom_id`)
  REFERENCES studyroom(`study_id`) ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;