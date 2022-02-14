package com.ssafy.db.entity;

import lombok.Getter;
import lombok.Setter;
import org.hibernate.annotations.CreationTimestamp;
import org.springframework.data.annotation.LastModifiedDate;

import javax.persistence.*;
import java.io.Serializable;
import java.time.LocalDateTime;
import java.util.List;

@Entity
@Getter
@Setter
public class Notice implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name= "notice_id", updatable = false)
    Integer noticeId;
    @Column(name= "study_id", updatable = false)
    Integer studyId;
    @Column(name= "tchr_id", updatable = false)
    String tchrId;


    @Column(name= "notice_title")    // 제목
    String noticeTitle;
    @Column(name= "notice_content")  // 내용
    String noticeContent;
    @CreationTimestamp
    @LastModifiedDate
    @Column(name= "notice_posted")  // 최종 수정일
    LocalDateTime noticePosted;

    @OneToMany
    @JoinColumn(name = "notice_id",insertable = false, updatable = false)
    private List<NoticeFile> noticeFile;
}
