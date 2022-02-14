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
@ApiModel("HomeworkModifyReq")
public class HomeworkModifyReq {
    @ApiModelProperty(name = "과제 id")
    Integer hwId;
//    @ApiModelProperty(name = "교실 ID", example = "1")
//    Integer studyId;
//    @ApiModelProperty(name = "출제 교사 ID", example = "tchr_id")
//    String tchrId;
    @ApiModelProperty(name = "과제 제목")
    String hwTitle;
    @ApiModelProperty(name = "과제 내용")
    String hwContent;
    @ApiModelProperty(name = "제출 기한")
    String hwDeadline;
    @ApiModelProperty(name = "작성일자", example= "")
    LocalDateTime hwPosted;
    @ApiModelProperty
    List<MultipartFile> hwFile;
}
