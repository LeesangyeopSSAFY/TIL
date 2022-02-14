package com.ssafy.api.request.studyroom;

import com.ssafy.db.entity.Teacher;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("StudyRoomRegisterPostRequest")
public class StudyRoomRegisterPostReq {
    @ApiModelProperty(name = "선생님 ID", example = "ssafy_web")
    String tchrId;
    @ApiModelProperty(name = "수업 Name", example = "수학")
    String studyName;
    @ApiModelProperty(name = "수업 Description", example = "수업에 대한 설명 작성")
    String studyDesc;
}
