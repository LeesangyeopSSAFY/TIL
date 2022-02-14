package com.ssafy.api.request.studyroomdetail;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("StudyRoomDetailDeleteRequest")
public class StudyRoomDetailDeleteReq {
    @ApiModelProperty(name = "수업 ID", example = "1")
    int studyId;
    @ApiModelProperty(name = "삭제할 학생 ID", example = "st_id1")
    String stId;

}
