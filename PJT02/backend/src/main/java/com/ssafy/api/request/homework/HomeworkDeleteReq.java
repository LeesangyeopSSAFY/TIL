package com.ssafy.api.request.homework;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("HomeworkDeleteReq")
public class HomeworkDeleteReq {
    @ApiModelProperty(name = "과제 ID", example = "1")
    Integer hwId;
    @ApiModelProperty(name = "선생님 ID", example = "tchr_id")
    String tchrId;
}
