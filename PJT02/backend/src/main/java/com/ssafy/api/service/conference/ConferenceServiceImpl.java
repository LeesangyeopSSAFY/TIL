package com.ssafy.api.service.conference;

import com.ssafy.api.request.conference.ConferenceRegisterReq;
import com.ssafy.db.entity.Attendance;
import com.ssafy.db.entity.AttendanceRecord;
import com.ssafy.db.entity.Conference;
import com.ssafy.db.repository.conference.AttendanceRecordRepository;
import com.ssafy.db.repository.conference.AttendanceRepository;
import com.ssafy.db.repository.conference.ConferenceRepository;
import com.ssafy.db.repository.conference.ConferenceRepositorySupport;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.time.Duration;
import java.time.LocalDateTime;
import java.time.temporal.ChronoUnit;
import java.util.List;

@Service("ConferenceService")
public class ConferenceServiceImpl implements ConferenceService{
    @Autowired
    ConferenceRepository conferenceRepository;

    @Autowired
    ConferenceRepositorySupport conferenceRepositorySupport;

    @Autowired
    AttendanceRepository attendanceRepository;

    @Autowired
    AttendanceRecordRepository attendanceRecordRepository;

    @Override
    public Conference createConference(ConferenceRegisterReq conferenceRegisterReq) {
        Conference conference = new Conference();

        LocalDateTime now = LocalDateTime.now();

        String[] confst, confed;
        confst = conferenceRegisterReq.getConfStart().split(":");
        confed = conferenceRegisterReq.getConfEnd().split(":");

        LocalDateTime conferencestart = LocalDateTime.of(now.getYear(), now.getMonth(), now.getDayOfMonth(), Integer.parseInt(confst[0]), Integer.parseInt(confst[1]));
        LocalDateTime conferenceend = LocalDateTime.of(now.getYear(), now.getMonth(), now.getDayOfMonth(), Integer.parseInt(confed[0]), Integer.parseInt(confed[1]));

        conference.setStudyId(conferenceRegisterReq.getStudyId());
        conference.setTchrId(conferenceRegisterReq.getTchrId());
        conference.setConfTitle(conferenceRegisterReq.getConfTitle());
        conference.setConfStart(conferencestart);
        conference.setConfEnd(conferenceend);
        conference.setConfAtt(conferenceRegisterReq.getConfAtt());
        conferenceRepository.save(conference);
        return conference;
    }

    @Override
    public Conference findConference(Integer studyId, String tchrId) {
        return conferenceRepository.findConference(studyId, tchrId);
    }

    @Override
    public Attendance findAttendance(String stId, Integer confId) {
        return attendanceRepository.findAttendanceByIds(stId, confId);
    }

    @Override
    public AttendanceRecord findAttendanceRecord(String stId, Integer confId) {
        return attendanceRecordRepository.findAttendanceRecordByIds(stId, confId);
    }

    @Override
    public void enterConference(String stId, Integer confId) {
        Attendance attendance = findAttendance(stId, confId);
        if (attendance != null) {
        LocalDateTime now = LocalDateTime.now();

        AttendanceRecord attendanceRecord = new AttendanceRecord();
        attendanceRecord.setAttId(attendance.getAttId());
        attendanceRecord.setStId(stId);
        attendanceRecord.setConfId(confId);
        attendanceRecord.setRecIn(now);

        attendanceRecordRepository.save(attendanceRecord);
        }
    }

    @Override
    public void exitConference(String stId, Integer confId) {
        System.out.println("!!!!!!!!!!!in exit login");
        AttendanceRecord attendanceRecord = findAttendanceRecord(stId, confId);
        System.out.println(attendanceRecord.getRecId());
        System.out.println(attendanceRecord.getRecId());
        LocalDateTime now = LocalDateTime.now();
        attendanceRecord.setRecOut(now);

        List<AttendanceRecord> attendanceRecords = attendanceRecordRepository.findAllAttendanceRecordByIds(stId, confId);

        if (attendanceRecords != null) {
            Conference conference = conferenceRepository.findConferenceById(confId);
            LocalDateTime st, ed, confIn, confOut;
            long atttime = 0;  // 출석시간
            st = conference.getConfStart();
            ed = conference.getConfEnd();
            for (AttendanceRecord record : attendanceRecords) {
                if (record.getRecOut() == null) {
                    continue;
                }
                confIn = record.getRecIn();
                confOut = record.getRecOut();
                if (confIn.isBefore(st)) {
                    confIn = st;
                }
                if (confOut.isAfter(ed)) {
                    confOut = ed;
                }
//                System.out.println(Duration.between(confOut, confIn).getSeconds());
//                System.out.println(ChronoUnit.SECONDS.between(confOut, confIn));
                atttime += Duration.between(confIn, confOut).getSeconds();

            }
//            System.out.println(conference.getConfAtt());
//            System.out.println(atttime);
//            System.out.println(60L *conference.getConfAtt());
            if (60L *conference.getConfAtt() <= atttime) {
                Attendance attendance = findAttendance(stId, confId);
                attendance.setAttPass(1);
                attendanceRepository.save(attendance);
            }
            attendanceRecordRepository.save(attendanceRecord);

        }

    };

    @Override
    public List<Conference> findConferenceByDate(Integer studyId, String tchrId, String targetDate) {
        String year, month, day;
        String[] date = targetDate.split("-");
        year = date[0]; month = date[1]; day = date[2];

        return conferenceRepository.findConferenceByDate(studyId, tchrId, targetDate);
    }


}
