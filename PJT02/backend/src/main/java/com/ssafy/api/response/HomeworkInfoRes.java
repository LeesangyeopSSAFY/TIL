package com.ssafy.api.response;

import com.ssafy.db.entity.Homework;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDate;
import java.time.LocalDateTime;

@Getter
@Setter
@ApiModel("HomeworkInfoRes")
public class HomeworkInfoRes {
    @ApiModelProperty(name = "hw_id")
    Integer hwId;
    @ApiModelProperty(name = "study_id")
    Integer studyId;
    @ApiModelProperty(name = "tchr_id")
    String tchrId;
    @ApiModelProperty(name = "hw_title")
    String hwTitle;
    @ApiModelProperty(name = "hw_content")
    String hwContent;
    @ApiModelProperty(name = "hw_deadline")
    LocalDateTime hwDeadline;
    @ApiModelProperty(name = "hw_posted")
    LocalDateTime hwPosted;
//    @ApiModelProperty(name = "hw_file")
    public static HomeworkInfoRes of(Homework homework) {
        HomeworkInfoRes res = new HomeworkInfoRes();
        res.setHwId(homework.getHwId());
        res.setStudyId(homework.getStudyId());
        res.setTchrId(homework.getTchrId());
        res.setHwTitle(homework.getHwTitle());
        res.setHwContent(homework.getHwContent());
        res.setHwDeadline(homework.getHwDeadline());
        res.setHwPosted(homework.getHwPosted());
        return res;
    }
}
