package com.ssafy.db.repository.homework;

import com.ssafy.db.entity.Homework;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface HomeworkRepository extends JpaRepository<Homework, Integer> {
//    List<Homework> findHomeworkByStudyId (Integer studyId);
//    List<Homework> findHomeworkByTchrId(String tchrId);
//    Optional<Homework> findHomeworkByHwId(Integer hwId);
//    void deleteHomeworkByHwId(Integer hwId);

    @Query(value = "select homework.* from homework where homework.study_id in " +
            "( select study_id from studyroom_detail where st_id = :stId)",nativeQuery = true)
    List<Homework> findHomeworkBystId(String stId);

    @Query(value = "select count(case when st_hwcontent is not null and st_hwscore is null then 1 end), count(case when st_hwcontent is not null and st_hwscore is not null then 1 end), count(case when st_hwcontent is null and hw_deadline <= now() then 1 end), count(case when st_hwcontent is null and hw_deadline > now() then 1 end)\n" +
            "from student_homework\n" +
            "join homework\n" +
            "on student_homework.hw_id = homework.hw_id\n" +
            "where student_homework.st_id = :stId", nativeQuery = true)
    List<int[]> countBystId(String stId);


    @Query(value = "select count(case when st_hwcontent is not null and st_hwscore is null then 1 end), count(case when st_hwcontent is not null and st_hwscore is not null then 1 end), count(case when st_hwcontent is null and  hw_deadline > now() then 1 end), count(case when st_hwcontent is null and hw_deadline <= now() then 1 end)\n" +
            "from student_homework\n" +
            "left join homework\n" +
            "on student_homework.hw_id = homework.hw_id\n" +
            "where student_homework.tchr_id = :tchrId and (month(now()) = month(homework.hw_deadline) or month(now()) = month(homework.hw_posted))", nativeQuery = true)
    List<int[]> counthomeworkBytchrId(String tchrId);
}
