package com.ssafy.api.request.user;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("UserFindIdPostRequest")
public class StudentFindIdPostReq {
    @ApiModelProperty(name = "ID를 찾을 사용자 이름", example = "ssafy")
    String stName;
    @ApiModelProperty(name = "ID 정보를 받을 이메일", example = "본인 이메일 입력")
    String stEmail;
}
