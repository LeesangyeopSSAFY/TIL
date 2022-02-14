package com.ssafy.db.repository.conference;

import com.ssafy.db.entity.*;
import com.querydsl.jpa.impl.JPAQueryFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class ConferenceRepositorySupport {
    @Autowired
    private JPAQueryFactory jpaQueryFactory;
    QConference qConference = QConference.conference;
    QAttendance qAttendance = QAttendance.attendance;
    QAttendanceRecord qAttendanceRecord = QAttendanceRecord.attendanceRecord;

    public Attendance enterConference(String stId, Integer confId) {
        Attendance att = (Attendance) jpaQueryFactory.select(qAttendance).from(qAttendance)
                .where(qAttendance.stId.eq(stId).and(qAttendance.confId.eq(confId))).fetch();
        return att;
    }
}
