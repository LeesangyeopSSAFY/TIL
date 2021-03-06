package com.ssafy.api.service.studyroom;

import com.ssafy.api.request.studyroom.StudyRoomAddPostReq;
import com.ssafy.api.request.studyroomdetail.StudyRoomDetailDeleteReq;
import com.ssafy.db.entity.Studyroom;

import java.util.List;

public interface StudyRoomDetailService {
    //νμ μΆκ°
    void addStudent(StudyRoomAddPostReq studyRoomAddPostReq);
    List<Studyroom> findStudyroombystId(String stId);
    List<Object[]> findStudyroombystudyId(int studyId);
//    List<Tuple> findstIdAndstName();
    List<Object[]> findStudyroomAndconbystId(String stId);

    void deleteStudent(StudyRoomDetailDeleteReq studyRoomDetailDeleteReq);

    List<Object[]> findStudentbystudyId(int studyId);
}
