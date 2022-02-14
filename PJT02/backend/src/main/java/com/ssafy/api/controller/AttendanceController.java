package com.ssafy.api.controller;

import com.ssafy.api.service.Attendance.AttendanceService;
import io.swagger.annotations.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@Api(value = "출석 API", tags = {"Attendance"})
@RestController
@RequestMapping("/api/v1/attendance")
public class AttendanceController {
    @Autowired
    AttendanceService attendanceService;

    @GetMapping("/studentlist/{stId}")
    @ApiOperation(value = "학생 출석 개수 조회", notes = "<strong>학생ID</strong>를 통해 학생 출석인정 개수와 전체 수업개수를 확인한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<int[]>> studentList (
            @PathVariable @ApiParam(value = "학생Id",required = true) String stId){
        List<int[]> arr = attendanceService.countStudentAttendance(stId);
        return ResponseEntity.status(200).body(arr);
    }

    @GetMapping("/teacherlist/{tchrId}")
    @ApiOperation(value = "수업에 속하는 출석 개수 조회", notes = "<strong>교사ID</strong>를 통해 수업을 듣는 학생 출석인정 개수와 전체 수업개수를 확인한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "사용자 없음"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<int[]>> teacherList(
            @PathVariable @ApiParam(value = "교사Id",required = true) String tchrId){
        List<int[]> list =attendanceService.countAttendance(tchrId);
        return ResponseEntity.status(200).body(list);
    }
}
