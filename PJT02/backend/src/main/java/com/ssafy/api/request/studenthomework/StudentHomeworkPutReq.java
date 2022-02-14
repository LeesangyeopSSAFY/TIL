package com.ssafy.api.request.studenthomework;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;
import org.springframework.web.bind.annotation.GetMapping;

@Getter
@Setter
@ApiModel("StudentHomeworkPutRequest")
public class StudentHomeworkPutReq {
    @ApiModelProperty(name = "학생 과제 ID", example = "1")
    int stHwId;
    @ApiModelProperty(name = "과제 점수", example = "100")
    int stHwscore;
}
