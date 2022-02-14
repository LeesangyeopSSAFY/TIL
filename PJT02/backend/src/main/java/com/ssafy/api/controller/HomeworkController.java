package com.ssafy.api.controller;

import com.ssafy.api.request.homework.HomeworkDeleteReq;
import com.ssafy.api.request.homework.HomeworkModifyReq;
import com.ssafy.api.request.homework.HomeworkRegisterPostReq;
import com.ssafy.api.response.HomeworkInfoRes;
import com.ssafy.api.service.homework.HomeworkService;
import com.ssafy.common.model.response.BaseResponseBody;
import com.ssafy.db.entity.Homework;
import io.swagger.annotations.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.http.HttpHeaders;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.util.List;

@Api(value = "과제 API", tags = {"Homework"})
@RestController
@RequestMapping("/api/v1/homework")
public class HomeworkController {
    @Autowired
    HomeworkService homeworkService;

    @PostMapping("/create")
    @ApiOperation(value = "과제 출제", notes = "<strong>과제 제목, 내용, 기한, 첨부</strong>를 통해 개설한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<? extends BaseResponseBody> regist(
            @ApiParam(value = "과제 출제 정보", required = true)
            @ModelAttribute
                    HomeworkRegisterPostReq homeworkRegisterPostReq
    ) {
        homeworkService.createHomework(homeworkRegisterPostReq);
        return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
    }

    @GetMapping("/teacher/{tchrId}")
    @ApiOperation(value = "교사가 출제한 과제 조회", notes = "<strong>교사아이디</strong>를 통해 조회 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<Homework>> tchr_list(
            @PathVariable @ApiParam(value = "과제 출제 정보", required = true)String tchrId){
        List<Homework> list = homeworkService.findHomeworkByTchrId(tchrId);
        return ResponseEntity.status(200).body(list);
    }

    @GetMapping("/study/{studyId}")
    @ApiOperation(value = "수업에 포함된 과제 조회", notes = "<strong>수업아이디</strong>를 통해 조회 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<Homework>> study_list(
            @PathVariable @ApiParam(value = "과제 출제 정보", required = true)Integer studyId) {
        List<Homework> list = homeworkService.findHomeworkByStudyId(studyId);
        return ResponseEntity.status(200).body(list);
    }

    @GetMapping("/detail/{hwId}")
    @ApiOperation(value = "과제의 상세 내용 조회", notes = "<strong></strong>를 통해 조회 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<HomeworkInfoRes> homework_detail(
            @PathVariable @ApiParam(value = "과제 상세 정보") Integer hwId) {
        Homework homework = homeworkService.findHomeworkByHwId(hwId);
        return ResponseEntity.status(200).body(HomeworkInfoRes.of(homework));
    }

    @DeleteMapping("/delete")
    @ApiOperation(value = "과제 삭제", notes = "<strong>과제, 교사 ID</strong>을 통해 (교사가) 과제를 삭제 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<?> delete(@RequestBody HomeworkDeleteReq homeworkDeleteReq){
        Integer hwId = homeworkDeleteReq.getHwId();
        String tchrId = homeworkDeleteReq.getTchrId();
        homeworkService.deleteHomework(hwId, tchrId);
        return ResponseEntity.status(200).body("OK");
    }

    @PostMapping("/modify")
    @ApiOperation(value = "과제 수정", notes = "<strong>과제 ID</strong>을 통해 과제를 수정한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public  ResponseEntity<? extends BaseResponseBody> modifyHomework(
            @ApiParam(value = "과제 수정")
            @ModelAttribute HomeworkModifyReq homeworkModifyReq) {
        Homework homework = homeworkService.updateHomework(homeworkModifyReq);
//        if (homework.getHwId() != hwId) return ResponseEntity.status(404).body(BaseResponseBody.of(404,"False"));
        return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
    }

    @GetMapping("/student/{stId}")
    @ApiOperation(value = "학생이 속한 수업의 과제 조회", notes = "<strong>학생아이디</strong>를 통해 조회 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<Homework>> student_list(
            @PathVariable @ApiParam(value = "학생ID", required = true)String stId){
        List<Homework> list = homeworkService.findHomeworkBystId(stId);
        return ResponseEntity.status(200).body(list);
    }

    @GetMapping("/student/rate/{stId}")
    @ApiOperation(value = "학생이 제출한 과제중 미채점 과제 수와 채점 된 과제 수, 미제출 과제 중 기한 지난과제, 기한 남은 과제 수", notes = "<strong>학생아이디</strong>를 통해 조회 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<int[]>> rate(@PathVariable String stId){
        List<int[]> list = homeworkService.countBystId(stId);
        return ResponseEntity.status(200).body(list);
    }

    @GetMapping("/teacher/rate/{tchrId}")
    @ApiOperation(value = "교사의 수업 과제의 제출한 과제중 미채점된 과제, 채점된 과제, 미제출한 과제중 마감 남은 과제, 마감 지난 과제", notes = "<strong>교사아이디</strong>를 통해 조회 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<int[]>> homeworkrate(@PathVariable String tchrId){
        List<int[]> list = homeworkService.countBytchrId(tchrId);
        return ResponseEntity.status(200).body(list);
    }

    @GetMapping("/download-file")
    @ApiOperation(value = "파일 다운", notes = "<strong>파일 정보</strong>를 통해 파일을 다운로드 한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<Resource> download(
            @ApiParam(value = "파일 정보", required = true)
            @RequestParam
                    String fileName,
            @RequestParam
                    String filePath
    ) throws IOException {
        Resource file = homeworkService.loadAsResource(fileName, filePath);

        return ResponseEntity.ok().header(
                HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + file.getFilename() + "\""
        ).body(file);
    }
}
