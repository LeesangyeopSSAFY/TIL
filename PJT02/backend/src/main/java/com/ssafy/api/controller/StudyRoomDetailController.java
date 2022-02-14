package com.ssafy.api.controller;

import com.ssafy.api.request.studyroom.StudyRoomAddPostReq;
import com.ssafy.api.request.studyroomdetail.StudyRoomDetailDeleteReq;
import com.ssafy.api.service.studyroom.StudyRoomDetailService;
import com.ssafy.common.model.response.BaseResponseBody;
import com.ssafy.db.entity.Studyroom;
import io.swagger.annotations.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Api(value = "수업Detail API",tags = {"StudyRoomDetail"})
@RestController
@RequestMapping("api/v1/studyRoomDetail")
public class StudyRoomDetailController {
    @Autowired
    StudyRoomDetailService studyRoomDetailService;

    @GetMapping("/student/list/{stId}")
    @ApiOperation(value = "학생 수업 조회", notes = "<strong>학생아이디</strong>를 통해 조회 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<Studyroom>> studentlist(
            @PathVariable @ApiParam(value = "학생수업 정보", required = true)String stId){
        List<Studyroom> list = studyRoomDetailService.findStudyroombystId(stId);
        return ResponseEntity.status(200).body(list);
    }

    @GetMapping("/student/studylist/{studyId}")
    @ApiOperation(value = "학생 수업 조회", notes = "<strong>학생아이디</strong>를 통해 조회 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<Object[]>> studylistlist(
            @PathVariable @ApiParam(value = "학생 리스트 정보", required = true)int studyId){
        List<Object[]> list = studyRoomDetailService.findStudyroombystudyId(studyId);
        return ResponseEntity.status(200).body(list);
    }

    @PostMapping("/teacher/add")
    @ApiOperation(value = "학생 추가", notes = "<strong>수업ID, 교사ID, 학생 ID</strong>를 통해 수업에 학생을 추가한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<? extends BaseResponseBody> add(
            @RequestBody @ApiParam(value = "수업개설 정보", required = true) StudyRoomAddPostReq studyRoomAddPostReq){
        studyRoomDetailService.addStudent(studyRoomAddPostReq);
        return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
    }

    @GetMapping("/student/studylistwithconference/{stId}")
    @ApiOperation(value = "학생 수업 조회", notes = "<strong>학생아이디</strong>를 통해 조회 한다.")

    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<Object[]>> studyroomlistwithcoference(
            @PathVariable @ApiParam(value = "학생 ID 정보", required = true) String stId) {
        List<Object[]> list = studyRoomDetailService.findStudyroomAndconbystId(stId);

        return ResponseEntity.status(200).body(list);
    }

    @DeleteMapping("/teacher/deletestudent")
    @ApiOperation(value = "학생 삭제", notes = "<strong>수업ID, 학생 ID</strong>를 통해 수업에서 학생을 삭제한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<? extends BaseResponseBody> delete(
            @RequestBody @ApiParam(value = "수업ID, 학생ID", required = true) StudyRoomDetailDeleteReq studyRoomDetailDeleteReq) {
        studyRoomDetailService.deleteStudent(studyRoomDetailDeleteReq);
        return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
    }

    @GetMapping("/teacher/studentList/{studyId}")
    @ApiOperation(value = "우리반 조회", notes = "<strong>수업ID</strong>를 통해 수업에 해당하는 학생들을 조회한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<Object[]>> list(
            @PathVariable @ApiParam(value = "수업ID 정보", required = true) int studyId) {
        List<Object[]> list = studyRoomDetailService.findStudentbystudyId(studyId);
        return ResponseEntity.status(200).body(list);
    }
}
