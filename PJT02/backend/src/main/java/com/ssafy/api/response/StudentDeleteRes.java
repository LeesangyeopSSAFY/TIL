package com.ssafy.api.response;

import com.ssafy.common.model.response.BaseResponseBody;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
@ApiModel("StudentDeleteResponse")
public class StudentDeleteRes extends BaseResponseBody {
    @ApiModelProperty(name ="학생 ID")
    String st_id;

    public static StudentDeleteRes of(String st_id){
        StudentDeleteRes res = new StudentDeleteRes();
        res.setSt_id(st_id);
        return res;
    }
}
