package com.ssafy.db.repository.conference;

import com.ssafy.db.entity.Attendance;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface AttendanceRepository extends JpaRepository<Attendance, Integer> {

    @Query(value = "SELECT attendance.* FROM attendance " +
            "WHERE st_Id=:stId AND conf_Id=:confId LIMIT 1",
    nativeQuery = true)
    Attendance findAttendanceByIds(String stId, Integer confId);

    //conference가 열린 수업 중 이번달 수업의 출석인정 개수와 전체 수업수
    @Query(value = "select count(case when att_pass ='1' then 1 end), (select count(study_id) \n" +
            "\t\t\t\t\t\t\t\t\t\t\t\t\tfrom studyroom_detail where st_id = :stId and study_id  in (select study_id\n" +
            "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tfrom conference\n" +
            "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\twhere date_format(conf_end, '%Y-%m') = date_format(now(), '%Y-%m')\n" +
            "                                                                                                                    group by study_id))\n" +
            "from attendance\n" +
            "where st_id = :stId and conf_id in (select conf_id\n" +
            "\t\t\t\t\t\t\t\t\t\tfrom conference\n" +
            "\t\t\t\t\t\t\t\t\t\twhere date_format(conf_end, '%Y-%m') = date_format(now(), '%Y-%m'))",nativeQuery = true)
    List<int[]> countStudentAttendance(String stId);

    //conference가 열린 수업 중 학생 참여수와 전체 학생수
    @Query(value = "select count(case when att_pass = '1' then 1 end), (select count(st_id) \n" +
            "\t\t\t\t\t\t\t\t\t\t\t\t\tfrom studyroom_detail \n" +
            "                                                    where tchr_id = :tchrId and study_id in (select study_id\n" +
            "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tfrom conference\n" +
            "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\twhere date_format(conf_end, '%Y-%m') = date_format(now(), '%Y-%m')\n" +
            "\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tgroup by study_id))\n" +
            "from attendance\n" +
            "where conf_id in ( select conf_id\n" +
            "\t\t\t\t\tfrom conference\n" +
            "                    where tchr_id = :tchrId and date_format(conf_end, '%Y-%m') = date_format(now(), '%Y-%m'))", nativeQuery = true)
    List<int[]> countAttendance(String tchrId);
}
