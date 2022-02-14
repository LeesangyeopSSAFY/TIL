package com.ssafy.api.request.user;

import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

/**
 * 유저 회원가입 API ([POST] /api/v1/users) 요청에 필요한 리퀘스트 바디 정의.
 */
@Getter
@Setter
@ApiModel("TeacherLoginPostRequest")
public class TeacherLoginPostReq {
	@ApiModelProperty(name = "교수 ID", example = "Teacher_web")
	String tchr_id;
	@ApiModelProperty(name = "교수 Password", example = "Teacher_password")
	String tchr_password;
}
