package com.ssafy.db.repository.user;

import com.ssafy.db.entity.Teacher;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface TeacherRepository extends JpaRepository<Teacher, String> {
    // 아래와 같이, Query Method 인터페이스(반환값, 메소드명, 인자) 정의를 하면 자동으로 Query Method 구현됨.
    Optional<Teacher> findById(String tchrId);
    void deleteById(String tchrId);

    @Query(value = "SELECT st_id, st_name FROM student", nativeQuery = true)
    List<Object[]> selectAllStudent();
}