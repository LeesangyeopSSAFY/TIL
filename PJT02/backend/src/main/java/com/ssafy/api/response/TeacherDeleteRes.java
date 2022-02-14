package com.ssafy.api.response;

import com.ssafy.common.model.response.BaseResponseBody;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("TeacherDeleteResponse")
public class TeacherDeleteRes extends BaseResponseBody {
	@ApiModelProperty(name ="학생 ID")
	String tchr_id;

	public static TeacherDeleteRes of(String tchr_id){
		TeacherDeleteRes res = new TeacherDeleteRes();
		res.setTchr_id(tchr_id);
		return res;
	}
}
