package com.ssafy.db.repository.studenthomework;

import com.ssafy.db.entity.NoticeFile;
import com.ssafy.db.entity.StudentHomeworkFile;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@Repository
public interface StudentHomeworkFileRepository extends JpaRepository<StudentHomeworkFile, Integer> {

    // 공지 ID로 모든 파일 조회
    @Query(value = "SELECT student_homework_file.* FROM ST_HW_FILE WHERE student_homework_file.st_hwid = :stHwId"
            , nativeQuery = true)
    List<MultipartFile> findStudentHomeworkFileByStHwId(Integer stHwId);

    // 파일 삭제
    @Transactional
    @Modifying
    @Query(value = "DELETE FROM student_homework_file WHERE student_homework_file.st_hwid = :stHwId", nativeQuery = true)
    void deleteStudentHomeworkFileByStHwId(Integer stHwId);
}
