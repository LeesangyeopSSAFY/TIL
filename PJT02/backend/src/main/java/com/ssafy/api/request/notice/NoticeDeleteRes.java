package com.ssafy.api.request.notice;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("NoticeDeleteRequest")
public class NoticeDeleteRes {
    @ApiModelProperty(name = "공지사항 ID", example = "test1")
    Integer noticeId;
    @ApiModelProperty(name = "선생님 ID", example = "tchr_id")
    String tchrId;
}
