package com.ssafy.api.service.Attendance;

import com.ssafy.db.repository.conference.AttendanceRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service("AttendanceService")
public class AttendanceServiceImpl implements AttendanceService {
    @Autowired
    AttendanceRepository attendanceRepository;
    @Override
    public List<int[]> countStudentAttendance(String stId) {
        List<int[]> arr = attendanceRepository.countStudentAttendance(stId);
        return arr;
    }

    @Override
    public List<int[]> countAttendance(String tchrId) {
        List<int[]> list = attendanceRepository.countAttendance(tchrId);
        return list;
    }
}
