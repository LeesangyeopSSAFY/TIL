package com.ssafy.api.service.studyroom;

import com.ssafy.api.request.studyroom.StudyRoomRegisterPostReq;
import com.ssafy.db.entity.Studyroom;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

public interface StudyRoomService {
    //수업 등록
    Studyroom createStudyRoom(StudyRoomRegisterPostReq studyRoomRegisterPostReq);
    //수업 삭제
    @Transactional
    void deleteStudyRoom(String tchrId, String studyName);
    //사이드바에 보일 선생님 수업 list 검색 : 선생님아이디
    List<Object[]> findstudyNamebytchrId(String tchrId);
}
