package com.ssafy.api.response;

import com.ssafy.db.entity.StudentHomework;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@ApiModel("StudentHomeworkResponse")
public class StHwFindID {
    @ApiModelProperty(name = "학생 과제 ID", example = "null")
    Integer stHwId;
    @ApiModelProperty(name = "교수 과제 ID", example = "1")
    Integer hwId;
    @ApiModelProperty(name = "클래스 ID", example = "1")
    Integer studyId;
    @ApiModelProperty(name = "학생 점수", example = "1")
    Integer stHwscore;
    @ApiModelProperty(name = "출제 교사 ID", example = "tchr_id")
    String tchrId;
    @ApiModelProperty(name = "제출 학생 ID", example = "st_id")
    String stId;
    @ApiModelProperty(name = "제출과제 내용", example = "수학 과제 제출")
    String stHwContent;
    @ApiModelProperty(name = "과제 제출일자", example= "null")
    LocalDateTime stHwposted;
    public static StHwFindID of(StudentHomework studentHomework){
        StHwFindID res = new StHwFindID();
        res.setStHwId(studentHomework.getStHwId());
        res.setHwId(studentHomework.getHwId());
        res.setStudyId(studentHomework.getStudyId());
        res.setStHwscore(studentHomework.getStHwscore());
        res.setTchrId(studentHomework.getTchrId());
        res.setStId(studentHomework.getStId());
        res.setStHwContent(studentHomework.getStHwcontent());
        res.setStHwposted(studentHomework.getStHwposted());
        return res;
    }
}
