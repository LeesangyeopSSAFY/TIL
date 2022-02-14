package com.ssafy.db.entity;

import lombok.Getter;
import lombok.Setter;
import org.hibernate.dialect.Ingres9Dialect;

import javax.persistence.*;
import java.util.List;

@Entity
@Getter
@Setter
public class Attendance {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "att_id", updatable = false)
    Integer attId;
    @Column(name = "conf_id", updatable = false)
    Integer confId;
    @Column(name = "st_id", updatable = false)
    String stId;
    @Column(name = "att_pass")
    Integer attPass;
    @OneToMany
    @JoinColumn(name = "att_id",insertable = false, updatable = false)
    private List<AttendanceRecord> attendanceRecords;
}
