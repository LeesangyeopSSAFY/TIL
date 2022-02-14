package com.ssafy.api.service.user; //비즈니스 로직 처리를 위한 서비스

import com.ssafy.api.request.user.StudentProfilePutReq;
import com.ssafy.api.request.user.StudentRegisterPostReq;
import com.ssafy.api.request.user.StudentUpdatePutReq;
import com.ssafy.api.request.user.TeacherProfilePutReq;
import com.ssafy.db.entity.Student;
import com.ssafy.db.entity.Teacher;

import java.util.List;

/**
 *	유저 관련 비즈니스 로직 처리를 위한 서비스 인터페이스 정의.
 */
public interface StudentService {
	Student createStudent(StudentRegisterPostReq studentRegisterInfo);
	Student findById(String stId);
	void deleteStudent(String st_id);
	Student updateStudent(StudentUpdatePutReq studentUpdatePutReq);
	Student changeStudentPassword(Student student);
	String findstIdBystName(String stName);

	Student changeStudentProfile(StudentProfilePutReq studentProfilePutReq);
}
