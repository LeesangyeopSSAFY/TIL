package com.ssafy.api.response;

import com.ssafy.db.entity.Notice;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

import java.time.LocalDateTime;

@Getter
@Setter
@ApiModel("NoticeResponse")
public class NoticeFindID {
    @ApiModelProperty(name="Notice ID")
    Integer noticeId;
    @ApiModelProperty(name = "클래스 ID", example = "1")
    Integer studyId;
    @ApiModelProperty(name="tchr ID")
    String tchrId;
    @ApiModelProperty(name="Notice Title")
    String noticeTitle;
    @ApiModelProperty(name="Notice content")
    String noticeContent;
    @ApiModelProperty(name="Notice Posted")
    LocalDateTime noticePosted;
    public static NoticeFindID of(Notice notice){
        NoticeFindID res = new NoticeFindID();
        res.setNoticeId(notice.getNoticeId());
        res.setStudyId(notice.getStudyId());
        res.setNoticeTitle(notice.getNoticeTitle());
        res.setTchrId(notice.getTchrId());
        res.setNoticeContent(notice.getNoticeContent());
        res.setNoticePosted(notice.getNoticePosted());
        return res;
    }
}
