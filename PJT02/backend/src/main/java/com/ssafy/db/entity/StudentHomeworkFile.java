package com.ssafy.db.entity;

import lombok.Getter;
import lombok.Setter;

import javax.persistence.*;

@Entity
@Getter
@Setter
public class StudentHomeworkFile {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name= "file_id")
    Integer fileId;

    @Column(name= "st_hwid")
    Integer stHwId;

    @Column(name= "file_origin_name")
    String fileOriginName;

    @Column(name= "file_name")
    String fileName;

    @Column(name= "file_path")
    String filePath;
}
