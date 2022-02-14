package com.ssafy.api.request.studenthomework;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("StudentHomeworkDeleteRequest")
public class StudentHomeworkDeleteRes {
    @ApiModelProperty(name = "과제 ID", example = "1")
    Integer hwId;
    @ApiModelProperty(name = "학생 ID", example = "st_id")
    String stId;
}
