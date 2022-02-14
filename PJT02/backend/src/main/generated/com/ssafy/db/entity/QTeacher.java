package com.ssafy.db.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.Generated;
import com.querydsl.core.types.Path;


/**
 * QUser is a Querydsl query type for User
 */
@Generated("com.querydsl.codegen.EntitySerializer")
public class QTeacher extends EntityPathBase<Teacher> {

    private static final long serialVersionUID = 846542477L;

    public static final QTeacher teacher = new QTeacher("teacher");

    public final QBaseEntity _super = new QBaseEntity(this);

    public final StringPath tchrId = createString("tchr_id");

    public final StringPath tchrName = createString("tchr_name");

    public final StringPath tchrEmail = createString("tchr_email");

    public final StringPath tchrPassword = createString("tchr_password");

    public final StringPath tchrContact = createString("tchr_contact");

    public final StringPath tchrSchool = createString("tchr_school");

    public QTeacher(String variable) {
        super(Teacher.class, forVariable(variable));
    }

    public QTeacher(Path<? extends Teacher> path) {
        super(path.getType(), path.getMetadata());
    }

    public QTeacher(PathMetadata metadata) {
        super(Teacher.class, metadata);
    }

}
