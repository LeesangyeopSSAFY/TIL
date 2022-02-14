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
public class QStudyroom extends EntityPathBase<Studyroom> {

    private static final long serialVersionUID = 846542477L;

    public static final QStudyroom studyroom = new QStudyroom("studyroom");

    public final QBaseEntity _super = new QBaseEntity(this);

    public final NumberPath<Integer> studyId = createNumber("study_id", Integer.class);

    public final StringPath tchrId = createString("tchr_id");

    public final StringPath studyName = createString("study_name");

    public final StringPath studyDesc = createString("study_desc");

    public QStudyroom(String variable) {
        super(Studyroom.class, forVariable(variable));
    }

    public QStudyroom(Path<? extends Studyroom> path) {
        super(path.getType(), path.getMetadata());
    }

    public QStudyroom(PathMetadata metadata) {
        super(Studyroom.class, metadata);
    }

}
