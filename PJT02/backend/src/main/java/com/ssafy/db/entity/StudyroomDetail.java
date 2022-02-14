package com.ssafy.db.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.io.Serializable;
import java.util.List;

@Entity
@Getter
@Setter
public class StudyroomDetail implements Serializable {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name= "studyroom_detail_id", updatable = false)
    Integer studyroomDetailId;
    @Column(name = "study_id")
    Integer studyId;
    @Column(name = "tchr_id")
    String tchrId;
    @Column(name ="st_id")
    String stId;

    //Studyroom과 1:1 관계
//    @OneToOne
//    @JoinColumn(name ="study_id",insertable = false, updatable = false)
//    private Studyroom studyroom;
//    //Student와 1:N 관계
//    @ManyToMany(cascade=CascadeType.ALL)
//    @JoinColumn(name = "st_id",insertable = false, updatable = false)
//    private List<Student> students;
}
