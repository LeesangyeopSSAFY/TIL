package com.ssafy.db.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;
import java.time.LocalDateTime;

@Getter
@Setter
@Entity
public class AttendanceRecord {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "rec_id", updatable = false)
    Integer recId;
    @Column(name = "att_id", updatable = false)
    Integer attId;
    @Column(name = "conf_id", updatable = false)
    Integer confId;
    @Column(name = "st_id", updatable = false)
    String stId;
    @Column(name = "rec_in")
    LocalDateTime recIn;
    @Column(name = "rec_out")
    LocalDateTime recOut;

//    @ManyToOne
//    @JoinColumn(name = "conf_id", insertable = false, updatable = false)
//    private Conference conference;
}
