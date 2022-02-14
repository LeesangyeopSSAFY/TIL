package com.ssafy.db.repository.studyroom;

import com.ssafy.db.entity.Studyroom;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import org.springframework.transaction.annotation.Transactional;

import java.util.List;
import java.util.Optional;

@Repository
public interface StudyRoomRepository  extends JpaRepository<Studyroom, Integer> {

    @Query(value = "select study_id, study_name from studyroom where tchr_id = :tchrId", nativeQuery = true)
    public List<Object[]> selectstudyIdAndstudyNamebytchrId(String tchrId);
}