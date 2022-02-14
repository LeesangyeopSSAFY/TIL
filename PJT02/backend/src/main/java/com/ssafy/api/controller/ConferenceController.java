package com.ssafy.api.controller;

import com.ssafy.api.request.conference.ConferenceRegisterReq;
import com.ssafy.api.service.conference.ConferenceService;
import com.ssafy.common.model.response.BaseResponseBody;
import com.ssafy.db.entity.Conference;
import io.swagger.annotations.*;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Api(value = "화상 및 출결 API", tags = {"Conference"})
@RestController
@RequestMapping("/api/v1/conference")
public class ConferenceController {
    @Autowired
    ConferenceService conferenceService;

    @PostMapping("/create")
    @ApiOperation(value = "수업 시작/종료/인정시간 입력", notes = "<strong>화상 정보</strong>를 입력하여 화상을 개설한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "잘못된 요청"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<? extends BaseResponseBody> register(
            @ApiParam(value = "화상 개설", required = true)
            @RequestBody
            ConferenceRegisterReq conferenceRegisterReq
    ) {
        conferenceService.createConference(conferenceRegisterReq);
        return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
    }

    @GetMapping("/info")
    @ApiOperation(value = "마지막 화상정보 조회", notes = "<strong>수업 ID, 교사 ID</strong>를 입력하여 화상을 조회한다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "잘못된 요청"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<Conference> getinfo(
            @ApiParam(value = "화상정보 조회", required = true)
            @RequestParam
            Integer studyId, String tchrId
    ) {
        Conference conference = conferenceService.findConference(studyId, tchrId);
        return ResponseEntity.status(200).body(conference);
    }

    @PostMapping("/enter")
    @ApiOperation(value = "수업 입실", notes = "수업에 입장하여 출석기록을 남긴다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "잘못된 요청"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<? extends BaseResponseBody> conferencein(
            @ApiParam(value = "수업 입장", required = true)
            @RequestParam
            String stId, Integer confId
    ) {
        conferenceService.enterConference(stId, confId);
        return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
    }

    @PutMapping("/exit")
    @ApiOperation(value = "수업 퇴실", notes = "수업에서 퇴장하여 출석기록을 남긴다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "잘못된 요청"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<? extends BaseResponseBody> conferenceout(
            @ApiParam(value = "수업 퇴장", required = true)
            @RequestParam
            String stId, Integer confId
    ) {
        System.out.println("!!!!!!!!!!!!!!!!!!in exit controller");
        conferenceService.exitConference(stId, confId);
        return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
    }

    @GetMapping("/infobydate")
    @ApiOperation(value = "일자별 수업 리스트", notes = "날짜에 따라 수업 기록을 가져온다.")
    @ApiResponses({
            @ApiResponse(code = 200, message = "성공"),
            @ApiResponse(code = 401, message = "인증 실패"),
            @ApiResponse(code = 404, message = "잘못된 요청"),
            @ApiResponse(code = 500, message = "서버 오류")
    })
    public ResponseEntity<List<Conference>> conferenceinfobydate(
            @ApiParam(value = "일자별 수업", required = true)
            @RequestParam
                    Integer studyId, String tchrId, String targetDate
    ) {
        List<Conference> list = conferenceService.findConferenceByDate(studyId, tchrId, targetDate);
        return ResponseEntity.status(200).body(list);
    }

}
