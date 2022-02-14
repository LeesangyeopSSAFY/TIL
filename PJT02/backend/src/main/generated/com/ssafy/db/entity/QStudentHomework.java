package com.ssafy.db.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.Generated;
import com.querydsl.core.types.Path;


@Generated("com.querydsl.codegen.EntitySerializer")
public class QStudentHomework extends EntityPathBase<StudentHomework> {

    private static final long serialVersionUID = 846542477L;

    public static final QStudentHomework studenthomework = new QStudentHomework("studenthomework");

    public final QBaseEntity _super = new QBaseEntity(this);

    public final NumberPath<Integer> stHwId = createNumber("st_hwid", Integer.class);

    public final NumberPath<Integer> hwId = createNumber("hw_id", Integer.class);

    public final NumberPath<Integer> studyId = createNumber("study_id", Integer.class);

    public final StringPath tchrId =  createString("tchr_id");

    public final StringPath stId =  createString("st_id");

    public final StringPath stHwcontent = createString("st_hwcontent");

    public final StringPath stHwposted = createString("st_hwposted");

    public final NumberPath<Integer> stHwscore = createString("st_hwscore", Integer.class);

//    public final file

    public QStudentHomework(String variable) { super(StudentHomework.class, forVariable(variable)); }

    public QStudentHomework(Path<? extends StudentHomework> path) {
        super(path.getType(), path.getMetadata());
    }

    public QStudentHomework(PathMetadata metadata) {
        super(StudentHomework.class, metadata);
    }

}
