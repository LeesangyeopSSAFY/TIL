package com.ssafy.api.controller;

import com.ssafy.api.request.notice.NoticeDeleteRes;
import com.ssafy.api.request.notice.NoticeRegisterPostReq;
import com.ssafy.api.request.notice.NoticeUpdatePutReq;
import com.ssafy.api.response.NoticeFindID;
import com.ssafy.api.service.notice.NoticeService;
import com.ssafy.common.model.response.BaseResponseBody;
import com.ssafy.db.entity.Notice;
import io.swagger.annotations.*;
import org.kurento.client.internal.server.Param;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.autoconfigure.web.ServerProperties;
import org.springframework.core.io.InputStreamResource;
import org.springframework.core.io.Resource;
import org.springframework.http.ContentDisposition;
import org.springframework.http.HttpHeaders;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.List;

/**
 * 유저 관련 API 요청 처리를 위한 컨트롤러 정의.
 */
@Api(value = "유저 API", tags = {"Notice"})
@RestController
@RequestMapping("/api/v1/notice")
public class NoticeController {
	@Autowired
	NoticeService noticeService;

	@PostMapping("/create")
	@ApiOperation(value = "교사 공지사항 입력", notes = "<strong>클래스 id, 선생 id, 공지사항 제목, 공지사항 내용</strong>을 입력하여 공지사항을 등록한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "잘못된 요청"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<? extends BaseResponseBody> register(
			@ApiParam(value="공지사항 작성", required = true)
			@ModelAttribute
					NoticeRegisterPostReq noticeRegisterPostReq
	) throws Exception{
		System.out.println("!!!!!!!!!!!!!!!!!!!!!!!!!!!");
		noticeService.createNotice(noticeRegisterPostReq);
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}

	@DeleteMapping("/delete")
	@ApiOperation(value = "공지사항 삭제", notes = "<strong>공지사항, 교사 아이디</strong>를 통해 삭제 한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<?> delete(@RequestBody NoticeDeleteRes noticeDeleteRes){
		Integer noticeId = noticeDeleteRes.getNoticeId();
		String tchrId = noticeDeleteRes.getTchrId();
		noticeService.deleteNotice(noticeId, tchrId);
		return ResponseEntity.status(200).body("OK");
	}

	@GetMapping("/{noticeId}")
	@ApiOperation(value = "공지사항 정보 조회", notes = "선택한 공지사항의 정보를 조회한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<NoticeFindID> findNoticetId(
			@PathVariable @ApiParam(value = "공지 상세 정보") Integer noticeId) {
		Notice notice = noticeService.findBynoticeId(noticeId);
		return ResponseEntity.status(200).body(NoticeFindID.of(notice));
	}

	@PostMapping("/modify")
	@ApiOperation(value = "공지사항 수정", notes = "공지사항을 수정한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<? extends BaseResponseBody> modify(
			@ApiParam(value = "공지사항 수정", required = true)
			@ModelAttribute NoticeUpdatePutReq noticeUpdatePutReq
	) throws IOException {
		System.out.println("This is notice modify request!!!!!!!!!!!!!!!!!!");
		Notice notice = noticeService.updateNotice(noticeUpdatePutReq);
//		if(notice.getNoticeId() != noticeId) return ResponseEntity.status(404).body(BaseResponseBody.of(404,"False"));
		return ResponseEntity.status(200).body(BaseResponseBody.of(200, "Success"));
	}

	@GetMapping("/study/list/{studyId}")
	@ApiOperation(value = "수업에 포함된 공지사항 조회", notes = "수업 아이디를 통해 조회한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<List<Notice>> study_list(
			@PathVariable @ApiParam(value = "공지사항 정보", required = true)Integer studyId) {
		List<Notice> list = noticeService.findNoticeByStudyId(studyId);
		return ResponseEntity.status(200).body(list);
	}

	@GetMapping("/teacher/list/{tchrId}")
	@ApiOperation(value = "교사가 출제한 공지사항 조회", notes = "<strong>교사아이디</strong>를 통해 조회 한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<List<Notice>> tchr_list(
			@PathVariable @ApiParam(value = "공지사항 정보", required = true)String tchrId){
		List<Notice> list = noticeService.findNoticeByTchrId(tchrId);
		return ResponseEntity.status(200).body(list);
	}

	@GetMapping("/student/list/{stId}")
	@ApiOperation(value = "학생이 속한 수업의 과제 조회", notes = "<strong>학생아이디</strong>를 통해 조회 한다.")
	@ApiResponses({
			@ApiResponse(code = 200, message = "성공"),
			@ApiResponse(code = 401, message = "인증 실패"),
			@ApiResponse(code = 404, message = "사용자 없음"),
			@ApiResponse(code = 500, message = "서버 오류")
	})
	public ResponseEntity<List<Notice>> student_list(
			@PathVariable @ApiParam(value = "학생ID", required = true) String stId) {
		List<Notice> list = noticeService.findNoticeBystId(stId);
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
		Resource file = noticeService.loadAsResource(fileName, filePath);

		return ResponseEntity.ok().header(
				HttpHeaders.CONTENT_DISPOSITION, "attachment; filename=\"" + file.getFilename() + "\""
		).body(file);
	}
}
