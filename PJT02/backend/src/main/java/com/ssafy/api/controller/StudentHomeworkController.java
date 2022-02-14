package com.ssafy.api.controller;

import com.ssafy.api.request.studenthomework.StudentHomeworkDeleteRes;
import com.ssafy.api.request.studenthomework.StudentHomeworkPutReq;
import com.ssafy.api.request.studenthomework.StudentHomeworkRegisterPostReq;
import com.ssafy.api.request.studenthomework.StudentHomeworkUpdatePutReq;
import com.ssafy.api.response.StHwFindID;
import com.ssafy.api.service.studenthomework.StudentHomeworkService;
import com.ssafy.common.model.response.BaseResponseBody;
import com.ssafy.db.entity.StudentHomework;
import io.swagger.annotations.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

/**
 * 유저 관련 API 요청 처리를 위한 컨트롤러 정의.
 */
@Api(value = "유저 API", tags = {"StudentHomework"})
@RestController
@RequestMapping("/api/v1/studenthomework")
public class StudentHomeworkController {
	@Autowired
	StudentHomeworkService studentHomeworkService;

	@PostMapping("/create")
	@ApiOperation(value = "학생 과제 제출", notes = "<strong>과제 id, 클래스 id, 선생 id, 학생 id, 과제 내용</strong>을 입력하여 과제를 제출한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<? extends BaseResponseBody> register(
			@ApiParam(value="과제 작성", required = true)
			@ModelAttribute
					StudentHomeworkRegisterPostReq studentHomeworkRegisterPostReq
			) throws Exception{
		studentHomeworkService.createStudentHomework(studentHomeworkRegisterPostReq);
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}

	@DeleteMapping("delete")
	@ApiOperation(value = "학생 과제 삭제", notes = "<strong>과제 id, 학생 id</strong>를 통해 삭제 한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<?> delete(@RequestBody StudentHomeworkDeleteRes studentHomeworkDeleteRes){
		Integer hwId = studentHomeworkDeleteRes.getHwId();
		String stId = studentHomeworkDeleteRes.getStId();
		studentHomeworkService.deleteStudentHomework(hwId, stId);
		return ResponseEntity.status(200).body("OK");
	}

//	@PutMapping("/modify/{stHwId}")
//	@ApiOperation(value = "학생 과제 수정", notes = "학생 과제를 수정한다.")
//	@ApiResponses({
//			@ApiResponse(code = 200, message = "성공"),
//			@ApiResponse(code = 401, message = "인증 실패"),
//			@ApiResponse(code = 404, message = "사용자 없음"),
//			@ApiResponse(code = 500, message = "서버 오류")
//	})
//	public ResponseEntity<? extends BaseResponseBody> modify(
//			@PathVariable @ApiParam(value = "학생 과제 수정") Integer stHwId,
//			@ModelAttribute @ApiParam(value="학생 과제 수정정보", required = true) StudentHomeworkUpdatePutReq studentHomeworkUpdatePutReq) {
//		StudentHomework studentHomework = studentHomeworkService.StudentHomeworkupdateNotice(stHwId, studentHomeworkUpdatePutReq);
//		if (studentHomework.getStHwId() != stHwId) return ResponseEntity.status(404).body(BaseResponseBody.of(404,"False"));
//		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
//	}

	@GetMapping("/teacher/list/{hwId}")
	@ApiOperation(value = "과제에 포함된 학생 과제 조회", notes = "과제 아이디를 통해 조회한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<List<StudentHomework>> hw_list(
			@PathVariable @ApiParam(value = "학생 과제 정보", required = true)Integer hwId) {
		List<StudentHomework> list = studentHomeworkService.findStudentHomeworkByHwId(hwId);
		return ResponseEntity.status(200).body(list);
	}

	@GetMapping("/student/list/{stId}")
	@ApiOperation(value = "학생이 제출한 과제 조회", notes = "학생 아이디를 통해 조회한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<List<StudentHomework>> st_list(
			@PathVariable @ApiParam(value = "학생 개별과제 정보", required = true)String stId) {
		List<StudentHomework> list = studentHomeworkService.findStudentHomeworkByStId(stId);
		return ResponseEntity.status(200).body(list);
	}

	@GetMapping("/detail/{stHwId}")
	@ApiOperation(value = "학생 과제 세부 조회", notes = "선택한 학생의 과제를 조회한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<StHwFindID> firndStHwId(
			@PathVariable @ApiParam(value = "학생기준 과제 상세 정보") Integer stHwId) {
		StudentHomework studentHomework = studentHomeworkService.findBystHwId(stHwId);
		return ResponseEntity.status(200).body(StHwFindID.of(studentHomework));
	}


	@PutMapping("/score")
	@ApiOperation(value = "학생 과제 점수 수정", notes = "제출한 과제ID, 채점점수를 통해 학생 과제 점수를 수정한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public  ResponseEntity<? extends BaseResponseBody> score(@RequestBody StudentHomeworkPutReq studentHomeworkPutReq){
		studentHomeworkService.updateScore(studentHomeworkPutReq);
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}
}
