package com.ssafy.api.request.homework;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;
import org.springframework.web.multipart.MultipartFile;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;

@Getter
@Setter
@ApiModel("HomeworkRegisterPostReq")
public class HomeworkRegisterPostReq {
    @ApiModelProperty(name = "교실 ID", example = "1")
    Integer studyId;
    @ApiModelProperty(name = "출제 교사 ID", example = "tchr_id")
    String tchrId;
    @ApiModelProperty(name = "과제 제목", example = "페르마의 마지막 정리")
    String hwTitle;
    @ApiModelProperty(name = "과제 내용", example = "증명하기")
    String hwContent;
    @ApiModelProperty(name = "제출 기한", example = "2022-02-18 12:00")
    String hwDeadline;
    @ApiModelProperty
    List<MultipartFile> hwFile;
}
