use `ssafy_web_db`;
<<<<<<< HEAD

DROP TABLE `notice`;
DROP TABLE `homework`;
DROP TABLE `studyroom`;
CREATE TABLE `studyroom` (
  `study_id` INT,
  `study_name` VARCHAR(20),
  `study_descruption` TEXT,
  PRIMARY KEY (`study_id`)
);
=======
-- 수업 관리자 테이블에 등록된 관리자 있는 지 확인
-- 없다면 teacher 넣기
-- 수업 테이블 생성
create table `studyroom` (
	`study_id` smallint auto_increment,  -- 수업 id번호
	`tchr_id` varchar(20) NOT NULL, 	-- 선생님 id
    `study_name` varchar(15),			-- 수업 이름
    `study_desc` varchar(50),			-- 수업 설명
    primary key(`study_id`),
    foreign key(`tchr_id`) references teacher (`tchr_id`)
    on update cascade on delete cascade
)ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
-- study id는 1부터 자동 증가
alter table `studyroom` auto_increment = 1;
-- 수업 생성 study id 포함
-- insert into studyroom(tchr_id, study_name, study_desc) values ('test1', '수학A', '2학년 A반');
-- 키 값을 이용한 update나 delete만을 허용해서 오류 발생, 일시적인 safe 모드 해제
set sql_safe_updates = 0;
>>>>>>> feature/studyroom
