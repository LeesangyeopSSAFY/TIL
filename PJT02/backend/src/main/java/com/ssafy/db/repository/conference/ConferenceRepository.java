package com.ssafy.db.repository.conference;

import com.ssafy.db.entity.Conference;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public interface ConferenceRepository extends JpaRepository<Conference, Integer> {

    @Query(value = "SELECT conference.* FROM conference WHERE tchr_id=:tchrId AND study_id=:studyId ORDER BY conf_id DESC LIMIT 1"
            ,nativeQuery = true)
    Conference findConference(Integer studyId, String tchrId);

    @Query(value = "SELECT conference.* FROM conference WHERE conf_id=:confId", nativeQuery = true)
    Conference findConferenceById(Integer confId);

    @Query(value = "SELECT conference.* FROM conference WHERE study_id=:studyId AND tchr_id=:tchrId AND DATE(conf_start)=:targetDate", nativeQuery = true)
    List<Conference> findConferenceByDate(Integer studyId, String tchrId, String targetDate);
}
