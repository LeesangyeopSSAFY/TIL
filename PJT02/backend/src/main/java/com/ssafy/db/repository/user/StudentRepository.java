package com.ssafy.db.repository.user;


import com.ssafy.db.entity.Student;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public interface StudentRepository  extends JpaRepository<Student, String> {
                                                        //Entity클래스, PK 타입
 //Spring Boot의 Repository는 MyBatis의 DAO 역할: 실제로 DB에 접근하는 객체
    Optional<Student> findById(String stId);
    void deleteById(String stId);

}
