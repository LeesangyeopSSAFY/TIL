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
public class QNotice extends EntityPathBase<Notice> {

    private static final long serialVersionUID = 846542477L;

    public static final QNotice qnotice = new QNotice("notice");

    public final QBaseEntity _super = new QBaseEntity(this);

    public final NumberPath<Integer> noticeId = createNumber("notice_id", Integer.class);

    public final NumberPath<Integer> studyId = createNumber("study_id", Integer.class);

    public final StringPath tchrId = createString("tchr_id");

    public final StringPath noticeContent = createString("notice_content");

    public final StringPath noticeTitle = createString("notice_title");

    public final StringPath noticePosted = createString("notice_posted");

    public QNotice(String variable) {
        super(Notice.class, forVariable(variable));
    }

    public QNotice(Path<? extends Notice> path) {
        super(path.getType(), path.getMetadata());
    }

    public QNotice(PathMetadata metadata) {
        super(Notice.class, metadata);
    }

}

