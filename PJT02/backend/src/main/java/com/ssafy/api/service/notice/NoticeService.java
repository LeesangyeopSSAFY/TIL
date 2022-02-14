package com.ssafy.api.service.notice;

import com.ssafy.api.request.notice.NoticeUpdatePutReq;
import com.ssafy.db.entity.Notice;
import com.ssafy.api.request.notice.NoticeRegisterPostReq;
import org.springframework.core.io.Resource;
import org.springframework.transaction.annotation.Transactional;

import java.io.IOException;
import java.util.*;

/**
 *	유저 관련 비즈니스 로직 처리를 위한 서비스 인터페이스 정의.
 */
public interface NoticeService {
	// 공지사항 등록, 첨부파일 등록
	Notice createNotice(NoticeRegisterPostReq noticeRegisterPostReq) throws IOException;
	// 공지사항 삭제(공지사항 ID와 교수 ID로 삭제)
	@Transactional
	void deleteNotice(Integer noticeId, String tchrId);
	// 공지사항 상세 조회
	Notice findBynoticeId(Integer NoticeId);

    // 공지사항 조회 (수업ID에 따라, 교사ID에 따라, 공지사항 조회)
	List<Notice> findNoticeByStudyId(Integer studyId);
	List<Notice> findNoticeByTchrId(String tchrId);
	List<Notice> findNoticeBystId(String stId);

	//공지사항 수정
	Notice updateNotice(NoticeUpdatePutReq noticeUpdatePutReq) throws IOException;

	Resource loadAsResource(String fileName, String filePath);
}
