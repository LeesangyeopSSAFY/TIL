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
@ApiModel("TeacherModifyPutRequest")
public class TeacherModifyPutReq {
	@ApiModelProperty(name="교사 ID", example="tea_id")
	String tchr_id;
	@ApiModelProperty(name="교사 name", example="kimssafy")
	String tchr_name;
	@ApiModelProperty(name="교사 email", example="ssafy@ssafy.com")
	String tchr_email;
	@ApiModelProperty(name="교사 Password", example="1234")
	String tchr_password;
	@ApiModelProperty(name="교사 contact", example="010-1234-1234")
	String tchr_contact;
	@ApiModelProperty(name="교사 school", example="싸피중학교")
	String tchr_school;
	@ApiModelProperty(name = "교사 birthday", example = "20050305")
	String tchr_birthday;
}
