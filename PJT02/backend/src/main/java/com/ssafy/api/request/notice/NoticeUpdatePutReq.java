package com.ssafy.api.request.notice;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;
import org.springframework.web.multipart.MultipartFile;

import java.util.List;

@Getter
@Setter
@ApiModel("NoticeUpdatePutRequest")
public class NoticeUpdatePutReq {
    @ApiModelProperty(name = "noticeId", example = "null")
    Integer noticeId;
    @ApiModelProperty(name = "noticeTitle", example = "공지사항입니다.")
    String noticeTitle;
    @ApiModelProperty(name = "noticeContent", example = "공지사항 내용")
    String noticeContent;
    @ApiModelProperty
    List<MultipartFile> noticeFile;
}
