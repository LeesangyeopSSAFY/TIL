package com.ssafy.api.service.Attendance;

import java.util.List;

public interface AttendanceService {
    //출석 카운트
    List<int[]> countStudentAttendance(String stId);
    List<int[]> countAttendance(String tchrId);
}
