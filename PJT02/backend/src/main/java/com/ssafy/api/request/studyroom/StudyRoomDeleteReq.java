package com.ssafy.api.request.studyroom;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("StudyRoomDeleteRequest")
public class StudyRoomDeleteReq {
    @ApiModelProperty(name = "선생님 ID", example = "test1")
    String tchrId;
    @ApiModelProperty(name = "교실 이름", example = "수학")
    String studyName;
}
