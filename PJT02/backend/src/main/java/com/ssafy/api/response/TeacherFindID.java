package com.ssafy.api.response;

import com.ssafy.db.entity.Teacher;
import io.swagger.annotations.ApiModel;
import io.swagger.annotations.ApiModelProperty;
import lombok.Getter;
import lombok.Setter;

import javax.persistence.Column;

@Getter
@Setter
@ApiModel("TeacherFindID")
public class TeacherFindID {
    @ApiModelProperty(name="Teacher ID")
    String tchrId;
    @ApiModelProperty(name="Teacher Name")
    String tchrName;
    @ApiModelProperty(name="Teacher email")
    String tchrEmail;
    @ApiModelProperty(name="Teacher concat")
    String tchrConcat;
    @ApiModelProperty(name="Teacher birthday")
    String tchrBirthday;
    @ApiModelProperty(name="Teacher school")
    String tchrSchool;
    @ApiModelProperty(name="Teacher password")
    String tchrPassword;
    @ApiModelProperty(name="tchr ProfName")
    String tchrProfName;
    @ApiModelProperty(name="tchr OriginProfName")
    String tchrOriginProfName;
    @ApiModelProperty(name="tchr ProfPath")
    String tchrProfPath;
    public static TeacherFindID of(Teacher teacher){
        TeacherFindID res = new TeacherFindID();
        res.setTchrId(teacher.getTchrId());
        res.setTchrName(teacher.getTchrName());
        res.setTchrEmail(teacher.getTchrEmail());
        res.setTchrConcat(teacher.getTchrContact());
        res.setTchrBirthday(teacher.getTchrBirthday());
        res.setTchrSchool(teacher.getTchrSchool());
        res.setTchrPassword(teacher.getTchrPassword());
        res.setTchrProfName(teacher.getTchrProfName());
        res.setTchrOriginProfName(teacher.getTchrOriginProfName());
        res.setTchrProfPath(teacher.getTchrProfPath());
        return res;
    }
}
