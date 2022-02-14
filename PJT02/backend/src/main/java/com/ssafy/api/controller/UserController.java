package com.ssafy.api.controller;

import com.ssafy.api.request.user.*;
import com.ssafy.api.response.StudentFindID;
import com.ssafy.api.response.TeacherFindID;
import com.ssafy.api.service.user.MailService;
import com.ssafy.api.service.user.StudentService;
import com.ssafy.api.service.user.TeacherMailService;
import com.ssafy.api.service.user.TeacherService;
import com.ssafy.db.entity.Student;
import com.ssafy.db.entity.Teacher;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.*;

import com.ssafy.common.model.response.BaseResponseBody;

import io.swagger.annotations.Api;
import io.swagger.annotations.ApiOperation;
import io.swagger.annotations.ApiParam;
import io.swagger.annotations.ApiResponse;
import io.swagger.annotations.ApiResponses;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

/**
 * 유저 관련 API 요청 처리를 위한 컨트롤러 정의.
 */
@Api(value = "유저 API", tags = {"User"})
@RestController
@RequestMapping("/api/v1")
public class UserController {

	@Autowired
	StudentService studentService;

	@Autowired
	MailService mailService;

	@Autowired
	PasswordEncoder passwordEncoder;

	@Autowired
	TeacherMailService teachermailService;

	@Autowired
	TeacherService teacherService;


	@PostMapping("/teacher/signup")
	@ApiOperation(value = "교사 회원 가입", notes = "<strong>아이디,패스워드,이름, 연락처, 이메일, 학교이름</strong>를 통해 회원가입 한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<? extends BaseResponseBody> register(
			@RequestBody @ApiParam(value="회원가입 정보", required = true)  TeacherRegisterPostReq teacherRegisterInfo) {
		//임의로 리턴된 User 인스턴스. 현재 코드는 회원 가입 성공 여부만 판단하기 때문에 굳이 Insert 된 유저 정보를 응답하지 않음.
		Teacher teacher = teacherService.createTeacher(teacherRegisterInfo);
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}


	@PostMapping("/student/signup")
	@ApiOperation(value = "학생 회원 가입", notes = "<strong>아이디,패스워드,이름, 연락처, 이메일, 학교이름</strong>를 통해 회원가입 한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<? extends BaseResponseBody> register(
			@RequestBody @ApiParam(value="회원가입 정보", required = true) StudentRegisterPostReq studentRegisterInfo) {

		//임의로 리턴된 User 인스턴스. 현재 코드는 회원 가입 성공 여부만 판단하기 때문에 굳이 Insert 된 유저 정보를 응답하지 않음.
		Student student = studentService.createStudent(studentRegisterInfo);
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}


	@PutMapping("/teacher/modify")
	@ApiOperation(value = "교사 정보 수정", notes = "<strong>아이디,패스워드,이름, 연락처, 이메일, 학교이름</strong>를 통해 정보를 수정한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<? extends BaseResponseBody> modify(
			@RequestBody @ApiParam(value="회원가입 정보", required = true) TeacherModifyPutReq teacherModifyInfo) {
		//임의로 리턴된 User 인스턴스. 현재 코드는 회원 가입 성공 여부만 판단하기 때문에 굳이 Insert 된 유저 정보를 응답하지 않음.
		Teacher t = teacherService.findById(teacherModifyInfo.getTchr_id());
		boolean check = passwordEncoder.matches(teacherModifyInfo.getTchr_password(), t.getTchrPassword());
		if(!check) return ResponseEntity.status(404).body(BaseResponseBody.of(404,"False"));
		else{
			Teacher teacher = teacherService.modifyTeacher(teacherModifyInfo);
		}
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}


	@PostMapping("/teacher/profile")
	@ApiOperation(value = "교사 프로필 사진 수정", notes = "<strong>교사ID, 프로필 이미지</strong>를 통해 정보를 수정한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<? extends BaseResponseBody> teacherprof(
			@ModelAttribute
					TeacherProfilePutReq teacherProfilePutReq
	) {
		teacherService.changeTeacherProfile(teacherProfilePutReq);
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}


	@PutMapping("/student/modify")
	@ApiOperation(value = "학생 회원 정보 수정", notes = "회원 정보를 수정한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<? extends BaseResponseBody> modify(
			@RequestBody @ApiParam(value="회원수정 정보", required = true) StudentUpdatePutReq studentUpdatePutReq) {

		Student st = studentService.findById(studentUpdatePutReq.getSt_id());
		boolean check = passwordEncoder.matches(studentUpdatePutReq.getSt_password(), st.getStPassword());
		if(!check) return ResponseEntity.status(404).body(BaseResponseBody.of(404,"False"));
		else {
			Student student = studentService.updateStudent(studentUpdatePutReq);
			return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
		}
	}


	@PostMapping("/student/profile")
	@ApiOperation(value = "학생 프로필 사진 수정", notes = "<strong>학생ID, 프로필 이미지</strong>를 통해 정보를 수정한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<? extends BaseResponseBody> studentprof(
			@ModelAttribute
					StudentProfilePutReq studentProfilePutReq
	) {
		studentService.changeStudentProfile(studentProfilePutReq);
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}


	@DeleteMapping("/teacher/withdrawal/{tchrId}")
	@ApiOperation(value = "교사 회원 정보 삭제", notes = "회원 정보를 삭제한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<?> removeteacher(@ApiParam(value = "삭제할 교사 아이디", required = true)@PathVariable String tchrId){
		teacherService.deleteTeacher(tchrId);
		return ResponseEntity.status(200).body(200);
	}


	@DeleteMapping("/student/withdrawal/{stId}")
	@ApiOperation(value = "학생 회원 정보 삭제", notes = "회원 정보를 삭제한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<?> removestudent(@ApiParam(value = "삭제할 학생 아이디", required = true)@PathVariable String stId){
		studentService.deleteStudent(stId);
		return ResponseEntity.status(200).body("OK");
	}

	@PostMapping("/findId")
	@ApiOperation(value = "회원 아이디 찾기", notes = "<strong>회원 이메일로</strong> 아이디를 포함한 메일을 전송한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<?> findId(@RequestBody StudentFindIdPostReq studentFindIdPostReq){
		String stName = studentFindIdPostReq.getStName();
		String stEmail = studentFindIdPostReq.getStEmail();
		//이름 정보로 회원 Id 찾고, Mail 보내기
		String stId = studentService.findstIdBystName(stName);
		mailService.sendMail(stId, stEmail);
		return ResponseEntity.status(200).body(stId);
	}

	@PostMapping("/findteacherId")
	@ApiOperation(value = "교사 아이디 찾기", notes = "<strong>회원 이메일로</strong>아이디를 포함한 메일을 전송한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<?> findteacherId(
			@RequestBody TeacherFindIdPostReq teacherFindIdPostReq) {
		String tchrName = teacherFindIdPostReq.getTchrName();
		String tchrEmail = teacherFindIdPostReq.getTchrEmail();

		String tchrId = teacherService.findByName(tchrName);
		teachermailService.sendMail(tchrId, tchrEmail);
		return ResponseEntity.status(200).body(200);
	}

	@PutMapping("/findPassword")
	@ApiOperation(value = "회원 비밀번호 변경", notes = "회원 아이디로 비밀번호를 변경한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public  ResponseEntity<? extends BaseResponseBody> findPassword(@RequestParam String stId, @RequestParam String stPassword) {

		//1. 회원 아이디에 해당하는 회원 정보 가져오기
		Student student = studentService.findById(stId);
		//2. 변경할 비밀번호
		student.setStPassword(stPassword);
		Student updateStudent = studentService.changeStudentPassword(student);
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}

	@PutMapping("/findTeacherPassword")
	@ApiOperation(value = "교사 비밀번호 변경", notes = "교사 아이디로 비밀번호를 변경한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public  ResponseEntity<? extends BaseResponseBody> findTeacherPassword(@RequestParam String tchrId, @RequestParam String tchrPassword) {

		//1. 교사 아이디에 해당하는 회원 정보 가져오기
		Teacher teacher = teacherService.findById(tchrId);
		//2. 변경할 비밀번호
		teacher.setTchrPassword(tchrPassword);
		Teacher modifyTeacher = teacherService.changeTeacherPassword(teacher);
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}

	@GetMapping("/student/{stId}")
	@ApiOperation(value = "학생 회원 본인 정보 조회", notes = "로그인한 학생 본인의 정보를 응답한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<StudentFindID> findStudentId(@RequestParam String stId) {
		Student student = studentService.findById(stId);
		return ResponseEntity.status(200).body(StudentFindID.of(student));
	}

	@GetMapping("/teacher/{tchrId}")
	@ApiOperation(value = "교수 회원 본인 정보 조회", notes = "로그인한 교수 본인의 정보를 응답한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<TeacherFindID> findTeaId(@RequestParam String tchrId) {
		Teacher teacher = teacherService.findById(tchrId);
		return ResponseEntity.status(200).body(TeacherFindID.of(teacher));
	}

	@GetMapping("/teacher/studentlist")
	@ApiOperation(value = "학생 조회", notes = "학생 리스트를 조회 한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<List<Object[]>> list(){
		List<Object[]> list = teacherService.findstIdAndstName();
		return ResponseEntity.status(200).body(list);
	}
}
