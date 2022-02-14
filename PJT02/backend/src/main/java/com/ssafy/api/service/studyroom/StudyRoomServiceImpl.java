package com.ssafy.api.service.studyroom;

import com.ssafy.api.request.studyroom.StudyRoomRegisterPostReq;
import com.ssafy.db.entity.Studyroom;
import com.ssafy.db.repository.studyroom.StudyRoomDetailRepository;
import com.ssafy.db.repository.studyroom.StudyRoomRepository;
import com.ssafy.db.repository.studyroom.StudyRoomRepositorySupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;


@Service("studyRoomService")
public class StudyRoomServiceImpl implements StudyRoomService {
    @Autowired
    StudyRoomRepository studyRoomRepository;
    @Autowired
    StudyRoomRepositorySupport studyRoomRepositorySupport;
    @Autowired
    StudyRoomDetailRepository studyRoomDetailRepository;
    @Override
    public Studyroom createStudyRoom(StudyRoomRegisterPostReq studyRoomRegisterPostReq) {
        Studyroom studyRoom = new Studyroom();
        studyRoom.setTchrId(studyRoomRegisterPostReq.getTchrId());
        studyRoom.setStudyName(studyRoomRegisterPostReq.getStudyName());
        studyRoom.setStudyDesc(studyRoomRegisterPostReq.getStudyDesc());
        return studyRoomRepository.save(studyRoom);
    }

    @Override
    public void deleteStudyRoom(String tchrId, String studyName) {
        studyRoomRepositorySupport.deleteStudyRoomByTchrIdAndStudyName(tchrId, studyName);
    }

    @Override
    public List<Object[]> findstudyNamebytchrId(String tchrId) {
        List<Object[]> list = studyRoomRepository.selectstudyIdAndstudyNamebytchrId(tchrId);
        return list;
    }

}
