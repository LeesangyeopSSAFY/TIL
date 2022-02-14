package com.ssafy.db.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;
import java.time.LocalTime;
import java.util.List;

@Entity
@Getter
@Setter
public class Conference {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "conf_id", updatable = false)
    Integer confId;
    @Column(name = "study_id", updatable = false)
    Integer studyId;
    @Column(name = "tchr_id", updatable = false)
    String tchrId;
    @Column(name = "conf_title", updatable = false)
    String confTitle;
    @Column(name = "conf_init", updatable = false)
    LocalDateTime confInit;
    @Column(name = "conf_des", updatable = false)
    LocalDateTime confDes;
    @Column(name = "conf_start", updatable = false)
    LocalDateTime confStart;
    @Column(name = "conf_end", updatable = false)
    LocalDateTime confEnd;
    @Column(name = "conf_att", updatable = false)
    Integer confAtt;
    @OneToMany
    @JoinColumn(name = "conf_id",insertable = false, updatable = false)
    private List<Attendance> attendances;

}
