package com.ssafy.db.repository.studenthomework;

import com.querydsl.jpa.impl.JPAQueryFactory;
import com.ssafy.db.entity.QNotice;
import com.ssafy.db.entity.QStudentHomework;
import com.ssafy.db.entity.StudentHomework;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;


@Repository
public class StudentHomeworkRepositorySupport {
    @Autowired
    private JPAQueryFactory jpaQueryFactory;
    QStudentHomework qStudentHomework = QStudentHomework.studentHomework;

    public void deleteStudentHomeworkByStHwIdAndStId(Integer hwId, String stId) {
        jpaQueryFactory.delete(qStudentHomework).where(qStudentHomework.hwId.eq(hwId).and(qStudentHomework.stId.eq(stId))).execute();  //excute 추가
    }

    public List<StudentHomework> findStudentHomeworkByHwId(Integer hwId){
        return jpaQueryFactory.select(qStudentHomework).from(qStudentHomework)
                .where(qStudentHomework.hwId.eq(hwId)).fetch();
    }

    public List<StudentHomework> findStudentHomeworkByStId(String stId) {
        return jpaQueryFactory.select(qStudentHomework).from(qStudentHomework)
                .where(qStudentHomework.stId.eq(stId)).fetch();
    }

    public Optional<StudentHomework> findBystHwId(Integer stHwId){
        StudentHomework studentHomework = jpaQueryFactory.select(qStudentHomework).from(qStudentHomework)
                .where(qStudentHomework.stHwId.eq(stHwId)).fetchOne();
        return Optional.ofNullable(studentHomework);
    }

    public StudentHomework findByIds(String stId, Integer hwId) {
        StudentHomework studentHomework = jpaQueryFactory.select(qStudentHomework).from(qStudentHomework)
                .where(qStudentHomework.hwId.eq(hwId).and(qStudentHomework.stId.eq(stId))).fetchOne();
        return  studentHomework;
    }
}
