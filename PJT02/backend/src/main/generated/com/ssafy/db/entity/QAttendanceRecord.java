package com.ssafy.db.entity;

import static com.querydsl.core.types.PathMetadataFactory.*;

import com.querydsl.core.types.dsl.*;

import com.querydsl.core.types.PathMetadata;
import javax.annotation.Generated;
import com.querydsl.core.types.Path;


@Generated("com.querydsl.codegen.EntitySerializer")
public class QAttendanceRecord extends EntityPathBase<AttendanceRecord> {

    private static final long serialVersionUID = 846542477L;

    public static final QAttendanceRecord qAttendanceRecord = new QAttendanceRecord("attendancerecord");

    public final QBaseEntity _super = new QBaseEntity(this);

    public final NumberPath<Integer> noticeId = createNumber("notice_id", Integer.class);

    public final NumberPath<Integer> studyId = createNumber("study_id", Integer.class);

    public final StringPath tchrId = createString("tchr_id");

    public final StringPath noticeContent = createString("notice_content");

    public final StringPath noticeTitle = createString("notice_title");

    public final StringPath noticePosted = createString("notice_posted");

    public QAttendanceRecord(String variable) {
        super(AttendanceRecord.class, forVariable(variable));
    }

    public QAttendanceRecord(Path<? extends AttendanceRecord> path) {
        super(path.getType(), path.getMetadata());
    }

    public QAttendanceRecord(PathMetadata metadata) {
        super(AttendanceRecord.class, metadata);
    }

}

