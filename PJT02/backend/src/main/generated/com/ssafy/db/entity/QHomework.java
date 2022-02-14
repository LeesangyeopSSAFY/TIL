package com.ssafy.db.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.Generated;
import com.querydsl.core.types.Path;


@Generated("com.querydsl.codegen.EntitySerializer")
public class QHomework extends EntityPathBase<Studyroom> {

    private static final long serialVersionUID = 846542477L;

    public static final QHomework homework = new QHomework("homework");

    public final QBaseEntity _super = new QBaseEntity(this);

    public final NumberPath<Integer> hwId = createNumber("hw_id", Integer.class);

    public final NumberPath<Integer> studyId = createNumber("study_id", Integer.class);

    public final StringPath tchrId =  createString("tchr_id");

    public final StringPath hwTitle = createString("hw_title");

    public final StringPath hwContent = createString("hw_cntent");

    public final StringPath hwDeadline = createString("hw_deadline");

    public final DatePath hwPosted = createDate("hw_posted");

    // file

    public QHomework(String variable) { super(Homework.class, forVariable(variable)); }

    public QHomework(Path<? extends Homework> path) {
        super(path.getType(), path.getMetadata());
    }

    public QHomework(PathMetadata metadata) {
        super(Homework.class, metadata);
    }

}
