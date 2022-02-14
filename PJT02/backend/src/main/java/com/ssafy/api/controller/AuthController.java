package com.ssafy.api.controller;

import com.ssafy.api.request.user.StudentLoginPostReq;
import com.ssafy.api.request.user.TeacherLoginPostReq;
import com.ssafy.api.response.StudentLoginPostRes;
import com.ssafy.api.response.TeacherLoginPostRes;
import com.ssafy.api.response.UserLoginPostRes;
import com.ssafy.api.service.user.StudentService;
import com.ssafy.api.service.user.TeacherService;
import com.ssafy.db.entity.Teacher;
import com.ssafy.db.entity.Student;
import io.swagger.annotations.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;
import com.ssafy.common.model.response.BaseResponseBody;
import com.ssafy.common.util.JwtTokenUtil;

/**
 * 인증 관련 API 요청 처리를 위한 컨트롤러 정의.
 */
@Api(value = "인증 API", tags = {"Auth."})
@RestController
@RequestMapping("/api/v1/auth")
public class AuthController {
	@Autowired
	StudentService studentService;

	@Autowired
	TeacherService teacherService;

	@Autowired
	PasswordEncoder passwordEncoder;


	@PostMapping("/studentlogin")
	@ApiOperation(value = "로그인", notes = "<strong>아이디와 패스워드</strong>를 통해 로그인 한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공", response = UserLoginPostRes.class),
			@ApiResponse(code = 401, message = "인증 실패", response = BaseResponseBody.class),
			@ApiResponse(code = 404, message = "사용자 없음", response = BaseResponseBody.class),
			@ApiResponse(code = 500, message = "서버 오류", response = BaseResponseBody.class)
	})
	public ResponseEntity<StudentLoginPostRes> login(@RequestBody @ApiParam(value="로그인 정보", required = true) StudentLoginPostReq studentloginInfo) {
		String st_id = studentloginInfo.getSt_id();
		String st_password = studentloginInfo.getSt_password();
		Student student = studentService.findById(st_id);
		if(passwordEncoder.matches(st_password, student.getStPassword())){
			//패스워드가 맞는 경우 , 로그인 성공
			return ResponseEntity.ok(StudentLoginPostRes.of(200, "Success", JwtTokenUtil.getToken(st_id)));
		}
		return ResponseEntity.status(401).body(StudentLoginPostRes.of(401, "Invalid Password", null));

	}


	@PostMapping("/teacherlogin")
	@ApiOperation(value = "로그인", notes = "<strong>아이디와 패스워드</strong>를 통해 로그인 한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공", response = TeacherLoginPostRes.class),
			@ApiResponse(code = 401, message = "인증 실패", response = BaseResponseBody.class),
			@ApiResponse(code = 404, message = "사용자 없음", response = BaseResponseBody.class),
			@ApiResponse(code = 500, message = "서버 오류", response = BaseResponseBody.class)
	})
	public ResponseEntity<TeacherLoginPostRes> login(@RequestBody @ApiParam(value="로그인 정보", required = true) TeacherLoginPostReq teacherloginInfo) {
		String tchr_id = teacherloginInfo.getTchr_id();
		String tchr_password = teacherloginInfo.getTchr_password();
		Teacher teacher = teacherService.findById(tchr_id);
		if(passwordEncoder.matches(tchr_password, teacher.getTchrPassword())){
			//패스워드가 맞는 경우 , 로그인 성공
			return ResponseEntity.ok(TeacherLoginPostRes.of(200, "Success", JwtTokenUtil.getToken(tchr_id)));
		}
		return ResponseEntity.status(401).body(TeacherLoginPostRes.of(401, "Invalid Password", null));
	}
}