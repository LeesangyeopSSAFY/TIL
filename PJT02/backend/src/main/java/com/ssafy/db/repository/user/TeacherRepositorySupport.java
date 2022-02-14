package com.ssafy.db.repository.user;

import com.querydsl.core.Tuple;
import com.querydsl.jpa.impl.JPAQueryFactory;
import com.ssafy.db.entity.QStudent;
import com.ssafy.db.entity.QTeacher;
import com.ssafy.db.entity.Teacher;

import java.util.List;
import java.util.Optional;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;


/**
 * 유저 모델 관련 디비 쿼리 생성을 위한 구현 정의.
 */
@Repository
public class TeacherRepositorySupport {
    @Autowired
    private JPAQueryFactory jpaQueryFactory;

    QTeacher qTeacher = QTeacher.teacher;

    QStudent qStudent = QStudent.student;

    public Optional<Teacher> findById(String tchrId) {
        Teacher teacher = jpaQueryFactory.select(qTeacher).from(qTeacher)
                .where(qTeacher.tchrId.eq(tchrId)).fetchOne();
        return Optional.ofNullable(teacher);
    }

    public String findIdByName(String tchrName){
        return jpaQueryFactory.select(qTeacher.tchrId).from(qTeacher)
                .where(qTeacher.tchrId.eq(tchrName)).fetchOne();
    }
}
