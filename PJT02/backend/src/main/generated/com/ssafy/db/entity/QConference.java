package com.ssafy.db.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.Generated;
import com.querydsl.core.types.Path;


@Generated("com.querydsl.codegen.EntitySerializer")
public class QConference extends EntityPathBase<Conference> {

    private static final long serialVersionUID = 846542477L;

    public static final QConference qConference = new QConference("conference");

    public final QBaseEntity _super = new QBaseEntity(this);

    public final NumberPath<Integer> confId = createNumber("conf_id", Integer.class);

    public final NumberPath<Integer> studyId = createNumber("study_id", Integer.class);

    public final StringPath tchrId = createString("tchr_id");

    public final StringPath confTitle = createString("conf_title");

    public final StringPath confInit = createString("conf_init");

    public final StringPath confDes = createString("conf_des");

    public final StringPath confStart = createString("conf_start");

    public final StringPath confEnd = createString("conf_end");

    public final NumberPath<Integer> confAtt = createNumber("conf_att", Integer.class);

    public QConference(String variable) {
        super(Conference.class, forVariable(variable));
    }

    public QConference(Path<? extends Conference> path) {
        super(path.getType(), path.getMetadata());
    }

    public QConference(PathMetadata metadata) {
        super(Conference.class, metadata);
    }

}

