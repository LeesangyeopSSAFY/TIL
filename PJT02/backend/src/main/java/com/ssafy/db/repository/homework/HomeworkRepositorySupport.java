package com.ssafy.db.repository.homework;

import com.querydsl.jpa.impl.JPAQueryFactory;
import com.ssafy.db.entity.Homework;
import com.ssafy.db.entity.QHomework;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Repository;

import java.util.List;
import java.util.Optional;

@Repository
public class HomeworkRepositorySupport {
    @Autowired
    private JPAQueryFactory jpaQueryFactory;
    QHomework qHomework = QHomework.homework;

    public List<Homework> findHomeworkByStudyId(Integer studyId) {
        return jpaQueryFactory.select(qHomework).from(qHomework)
                .where(qHomework.studyId.eq(studyId)).fetch();
    }

    public List<Homework> findHomeworkByTchrId(String tchrId) {
        return jpaQueryFactory.select(qHomework).from(qHomework)
                .where(qHomework.tchrId.eq(tchrId)).fetch();
    }

    public Optional<Homework> findHomeworkByHwId(Integer hwId) {
        Homework homework = jpaQueryFactory.select(qHomework).from(qHomework)
                .where(qHomework.hwId.eq(hwId)).fetchOne();
        return Optional.ofNullable(homework);
    }

    public void deleteHomeworkByHwId(Integer hwId, String tchrId){
        jpaQueryFactory.delete(qHomework).where(qHomework.hwId.eq(hwId).and(qHomework.tchrId.eq(tchrId))).execute();
    }
}
