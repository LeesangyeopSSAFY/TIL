package com.ssafy.db.repository.studenthomework;

import com.ssafy.db.entity.StudentHomework;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.Optional;

@Repository
public interface StudentHomeworkRepository extends JpaRepository<StudentHomework, Integer> {
    Optional<StudentHomework> findBystHwId(Integer StHwId);
    @Transactional
    void deleteStudentHomeworkByStHwIdAndStId(Integer stHwId, String stId);
}
