package com.ssafy.api.request.studenthomework;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@Getter
@Setter
@ApiModel("StudentHomeworkRegisterPostReq")
public class StudentHomeworkRegisterPostReq {
    @ApiModelProperty(name = "교수 과제 ID", example = "1")
    Integer hwId;
    @ApiModelProperty(name = "클래스 ID", example = "1")
    Integer studyId;
    @ApiModelProperty(name = "출제 교사 ID", example = "tchr_id")
    String tchrId;
    @ApiModelProperty(name = "제출 학생 ID", example = "st_id")
    String stId;
    @ApiModelProperty(name = "제출과제 내용", example = "수학 과제 제출")
    String stHwContent;
    @ApiModelProperty
    List<MultipartFile> stHwFile;
}
