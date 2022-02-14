package com.ssafy.api.request.user;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("StudentLoginPostRequest")
public class StudentLoginPostReq {
    @ApiModelProperty(name = "학생 ID", example = "ssafy_web")
    String st_id;
    @ApiModelProperty(name = "학생 Password", example = "1234")
    String st_password;
}
