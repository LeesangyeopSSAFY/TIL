package com.ssafy.db.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.Generated;
import com.querydsl.core.types.Path;


@Generated("com.querydsl.codegen.EntitySerializer")
public class QAttendance extends EntityPathBase<Attendance> {

    private static final long serialVersionUID = 846542477L;

    public static final QAttendance qAttendance = new QAttendance("attendance");

    public final QBaseEntity _super = new QBaseEntity(this);

    public final NumberPath<Integer> attId = createNumber("att_id", Integer.class);

    public final NumberPath<Integer> confId = createNumber("conf_id", Integer.class);

    public final StringPath stId = createString("st_id");

    public final BooleanPath attPass = createString("att_pass");

    public QAttendance(String variable) {
        super(Attendance.class, forVariable(variable));
    }

    public QAttendance(Path<? extends Attendance> path) {
        super(path.getType(), path.getMetadata());
    }

    public QAttendance(PathMetadata metadata) {
        super(Attendance.class, metadata);
    }

}

