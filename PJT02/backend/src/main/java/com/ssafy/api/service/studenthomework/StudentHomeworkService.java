package com.ssafy.api.service.studenthomework;

import com.ssafy.api.request.studenthomework.StudentHomeworkPutReq;
import com.ssafy.api.request.studenthomework.StudentHomeworkRegisterPostReq;
import com.ssafy.api.request.studenthomework.StudentHomeworkUpdatePutReq;
import com.ssafy.db.entity.StudentHomework;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

/**
 *	유저 관련 비즈니스 로직 처리를 위한 서비스 인터페이스 정의.
 */
public interface StudentHomeworkService {
	// 학생 과제 등록
	StudentHomework createStudentHomework(StudentHomeworkRegisterPostReq studentHomeworkRegisterPostReq);
	// 과제 삭제(과제 ID와 학생 ID로 삭제)
	@Transactional
	void deleteStudentHomework(Integer hwId, String stId);
	//학생 과제 수정
	StudentHomework StudentHomeworkupdateNotice(Integer stHwId, StudentHomeworkUpdatePutReq StudentHomeworkUpdatePutReq);

    //학생 과제 조회 (학생ID에 따라, 과제ID에 따라, 학생 조회)
	List<StudentHomework> findStudentHomeworkByHwId(Integer hwId);
	List<StudentHomework> findStudentHomeworkByStId(String stId);

	// 공지사항 상세 조회
	StudentHomework findBystHwId(Integer stHwId);

	@Transactional
	void updateScore(StudentHomeworkPutReq studentHomeworkPutReq);

}
