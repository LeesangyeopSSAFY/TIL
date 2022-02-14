package com.ssafy.db.repository.studyroom;

import com.ssafy.db.entity.*;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;

@Repository
public interface StudyRoomDetailRepository extends JpaRepository<StudyroomDetail, Integer> {
    //@Query(value = "select d.study_id AS study_id, d.st_id AS st_id, s.student AS st_name from studyroom_detail AS d inner join student AS s on d.st_id=s.st_id where d.study_id= :studyId", nativeQuery = true)
    @Query(value = "select d.study_id AS study_id, d.st_id AS st_id, s.st_name AS st_name s.st_prof_name AS st_prof_name, s.st_origin_prof_name AS st_origin_prof_name, s.st_prof_path AS st_prof_path" +
            "from studyroom_detail AS d " +
            "inner join student AS s on d.st_id=s.st_id where d.study_id= :studyId", nativeQuery = true)
    List<Object[]> findStudyroombystudyId(int studyId);

@Query(value = "select st.study_id, st.tchr_id, st.study_name, st.study_desc, c.conf_id, c.conf_title, date_format(c.conf_init, '%Y-%m-%d %H:%i:%s'), date_format(c.conf_des, '%Y-%m-%d %H:%i:%s'),  date_format(c.conf_start, '%Y-%m-%d %H:%i:%s'),  date_format(c.conf_end, '%Y-%m-%d %H:%i:%s'),  date_format(c.conf_att, '%Y-%m-%d %H:%i:%s')\n" +
            "from studyroom as st, conference as c\n" +
            "left join studyroom_detail as sd\n" +
            "on sd.study_id = c.study_id\n" +
            "where sd.st_id = :stId and (st.study_id, st.tchr_id, c.conf_start) in (select conf.study_id, conf.tchr_id, max(conf_start)\n"+
            "from conference as conf\n"+
            "group by conf.study_id)",nativeQuery = true)
    List<Object[]> findStudyroomAndconbystId(String stId);
    //    @Query(value = "select st.study_id, st.tchr_id, st.study_name, st.study_desc, c.conf_id, c.conf_title, c.conf_init, c.conf_des, c.conf_start, c.conf_end, c.conf_att\n" +
//            "from studyroom as st\n" +
//            "left join studyroom_detail as sd\n" +
//            "on st.study_id = sd.study_id\n" +
//            "left join conference as c\n" +
//            "on st.study_id = c.study_id and st.tchr_id = c.tchr_id\n" +
//            "where sd.st_id = :stId\n"+
//    List<Object[]> findStudyroomAndconbystId(String stId);

    @Query(value = "select st_id, st_name, st_email, st_contact, st_school, st_birthday, st_prof_name, st_origin_prof_name, st_prof_path\n" +
            "from student\n" +
            "where student.st_id in (select studyroom_detail.st_id\n" +
            "\t\t\t\tfrom studyroom_detail\n" +
            "                where studyroom_detail.study_id =:studyId)", nativeQuery = true)
    List<Object[]> findstudentbystudyId(int studyId);
}
