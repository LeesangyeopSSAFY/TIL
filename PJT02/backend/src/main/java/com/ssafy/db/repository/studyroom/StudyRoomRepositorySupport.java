package com.ssafy.db.repository.studyroom;

import com.querydsl.core.Tuple;
import com.querydsl.core.types.Projections;
import com.querydsl.jpa.impl.JPAQueryFactory;
import com.ssafy.db.entity.QStudyroom;

import com.ssafy.db.entity.QStudyroomDetail;
import com.ssafy.db.entity.Studyroom;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;


@Repository
public class StudyRoomRepositorySupport {
    @Autowired
    private JPAQueryFactory jpaQueryFactory;
    QStudyroom qStudyRoom = QStudyroom.studyroom;
    public List<String> findStudyNameByTchrId(String tchrId) {
        return jpaQueryFactory.select(qStudyRoom.studyName).from(qStudyRoom)
                .where(qStudyRoom.tchrId.eq(tchrId)).fetch();
    }

    public void deleteStudyRoomByTchrIdAndStudyName(String tchrId, String studyName){
        jpaQueryFactory.delete(qStudyRoom).where(qStudyRoom.tchrId.eq(tchrId).and(qStudyRoom.studyName.eq(studyName))).execute();
    }
}