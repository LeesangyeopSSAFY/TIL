package com.ssafy.api.service.user;

import com.ssafy.api.request.user.TeacherModifyPutReq;
import com.ssafy.api.request.user.TeacherProfilePutReq;
import com.ssafy.api.request.user.TeacherRegisterPostReq;
import com.ssafy.db.entity.Teacher;

import java.util.List;

/**
 *	유저 관련 비즈니스 로직 처리를 위한 서비스 인터페이스 정의.
 */
public interface TeacherService {
	Teacher createTeacher(TeacherRegisterPostReq teacherRegisterInfo);
	Teacher modifyTeacher(TeacherModifyPutReq teacherModifyInfo);
	Teacher findById(String tchrId);
	Teacher changeTeacherPassword(Teacher teacher);
	void deleteTeacher(String tchr_id);
	String findByName(String tchrName);
	List<Object[]> findstIdAndstName();

	Teacher changeTeacherProfile(TeacherProfilePutReq teacherProfilePutReq);
}
