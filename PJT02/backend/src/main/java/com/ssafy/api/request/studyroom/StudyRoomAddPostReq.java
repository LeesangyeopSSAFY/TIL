package com.ssafy.api.request.studyroom;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("StudyRoomAddPostRequest")
public class StudyRoomAddPostReq {
    @ApiModelProperty(name = "수업 ID", example = "수학")
    Integer studyId;
    @ApiModelProperty(name = "교사 ID", example = "test_id")
    String tchrId;
    @ApiModelProperty(name = "추가할 학생 ID", example = "st_id")
    String stId;
}
