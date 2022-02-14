package com.ssafy.api.request.studenthomework;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@Getter
@Setter
@ApiModel("StudentHomeworkUpdatePutRequest")
public class StudentHomeworkUpdatePutReq {
    @ApiModelProperty(name = "학생 과제 ID", example = "null")
    Integer stHwId;
    @ApiModelProperty(name = "제출과제 내용", example = "도덕 과제 제출")
    String stHwContent;
    @ApiModelProperty
    List<MultipartFile> stHwFile;
}