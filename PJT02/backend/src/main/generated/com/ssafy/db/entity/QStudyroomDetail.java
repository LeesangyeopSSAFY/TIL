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
public class QStudyroomDetail extends EntityPathBase<StudyroomDetail> {

    private static final long serialVersionUID = 846542477L;

    public static final QStudyroomDetail studyroomDetail = new QStudyroomDetail("studyroomDetail");

    public final QBaseEntity _super = new QBaseEntity(this);

    public final NumberPath<Integer> studyroomDetailId = createNumber("studyroom_detail_id", Integer.class);

    public final NumberPath<Integer> studyId = createNumber("study_id", Integer.class);

    public final StringPath tchrId = createString("tchr_id");

    public final StringPath stId = createString("st_id");

    public QStudyroomDetail(String variable) {
        super(StudyroomDetail.class, forVariable(variable));
    }

    public QStudyroomDetail(Path<? extends StudyroomDetail> path) {
        super(path.getType(), path.getMetadata());
    }

    public QStudyroomDetail(PathMetadata metadata) {
        super(StudyroomDetail.class, metadata);
    }
}

