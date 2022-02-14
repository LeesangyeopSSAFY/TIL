package com.ssafy.api.request.conference;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;
import java.time.LocalTime;

@Getter
@Setter
@ApiModel("ConferenceRegisterReq")
public class ConferenceRegisterReq {
    @ApiModelProperty(name = "study_id", example = "")
    Integer studyId;
    @ApiModelProperty(name = "tchr_id", example = "")
    String tchrId;
    @ApiModelProperty(name = "conf_title", example = "")
    String confTitle;
    @ApiModelProperty(name = "conf_start", example = "")
    String confStart;
    @ApiModelProperty(name = "conf_end", example = "")
    String confEnd;
    @ApiModelProperty(name = "conf_att", example = "")
    Integer confAtt;
}
