package com.ssafy.api.service.studenthomework;

import com.ssafy.api.request.studenthomework.StudentHomeworkPutReq;
import com.ssafy.api.request.studenthomework.StudentHomeworkRegisterPostReq;
import com.ssafy.api.request.studenthomework.StudentHomeworkUpdatePutReq;
import com.ssafy.db.entity.StudentHomework;
import com.ssafy.db.entity.StudentHomeworkFile;
import com.ssafy.db.repository.studenthomework.StudentHomeworkFileRepository;
import com.ssafy.db.repository.studenthomework.StudentHomeworkRepository;
import com.ssafy.db.repository.studenthomework.StudentHomeworkRepositorySupport;
import org.apache.commons.lang3.RandomStringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.time.LocalDateTime;
import java.util.List;
import java.util.Objects;

@Service("StudentHomeworkService")
public class StudentHomeworkServiceImpl implements StudentHomeworkService{
    @Autowired
    StudentHomeworkRepository studenthomeworkRepository;

    @Autowired
    StudentHomeworkFileRepository studentHomeworkFileRepository;

    @Autowired
    StudentHomeworkRepositorySupport studenthomeworkRepositorySupport;

    @Override
    public StudentHomework createStudentHomework(StudentHomeworkRegisterPostReq studentHomeworkRegisterPostReq) {
        StudentHomework studenthomework = studenthomeworkRepositorySupport.findByIds(studentHomeworkRegisterPostReq.getStId(), studentHomeworkRegisterPostReq.getHwId());
//        studenthomework.setHwId(studentHomeworkRegisterPostReq.getHwId());
//        studenthomework.setStudyId(studentHomeworkRegisterPostReq.getStudyId());
//        studenthomework.setTchrId(studentHomeworkRegisterPostReq.getTchrId());
//        studenthomework.setStId(studentHomeworkRegisterPostReq.getStId());
        studenthomework.setStHwcontent(studentHomeworkRegisterPostReq.getStHwContent());
        studenthomework.setStHwposted(LocalDateTime.now());
        studenthomeworkRepository.save(studenthomework);
        if (!studentHomeworkRegisterPostReq.getStHwFile().get(0).isEmpty()){
            List<MultipartFile> sthwFile = studentHomeworkRegisterPostReq.getStHwFile();
            for (MultipartFile multipartFile : sthwFile) {
                StudentHomeworkFile newFile = new StudentHomeworkFile();
                newFile.setStHwId(studenthomework.getStHwId());

                String sourceFileName = multipartFile.getOriginalFilename();
                File destinationNoticeFile;
                String destinationNoticeFileName;
                String noticePath = "D:/";
                LocalDateTime nowtime = LocalDateTime.now();

                destinationNoticeFileName = nowtime + RandomStringUtils.randomAlphanumeric(8) + sourceFileName;
                destinationNoticeFile = new File(noticePath + destinationNoticeFileName);

                destinationNoticeFile.getParentFile().mkdirs();
                try {
                    multipartFile.transferTo(destinationNoticeFile);
                } catch (IOException e) {
                    e.printStackTrace();
                }

                newFile.setFileName(destinationNoticeFileName);
                newFile.setFileOriginName(sourceFileName);
                newFile.setFilePath(noticePath);
                studentHomeworkFileRepository.save(newFile);

            }
        }
        return studenthomework;
    }

    @Override
    public void deleteStudentHomework(Integer hwId, String stId) {
        studenthomeworkRepositorySupport.deleteStudentHomeworkByStHwIdAndStId(hwId, stId);
    }

    @Override
    public StudentHomework StudentHomeworkupdateNotice(Integer stHwId, StudentHomeworkUpdatePutReq StudentHomeworkUpdatePutReq) {
        StudentHomework studenthomework = new StudentHomework();
        studenthomework.setStHwId(StudentHomeworkUpdatePutReq.getStHwId());
//        studenthomework.setHwId(StudentHomeworkUpdatePutReq.getHwId());
//        studenthomework.setStudyId(StudentHomeworkUpdatePutReq.getStudyId());
//        studenthomework.setTchrId(StudentHomeworkUpdatePutReq.getTchrId());
//        studenthomework.setStId(StudentHomeworkUpdatePutReq.getStId());
        studenthomework.setStHwcontent(StudentHomeworkUpdatePutReq.getStHwContent());
        studenthomework.setStHwposted(LocalDateTime.now());
        if (!Objects.equals(StudentHomeworkUpdatePutReq.getStHwId(), stHwId)) return studenthomework;
        studenthomeworkRepository.save(studenthomework);
        studentHomeworkFileRepository.deleteStudentHomeworkFileByStHwId(stHwId);
        if (!StudentHomeworkUpdatePutReq.getStHwFile().get(0).isEmpty()){
            List<MultipartFile> sthwFile = StudentHomeworkUpdatePutReq.getStHwFile();
            for (MultipartFile multipartFile : sthwFile) {
                StudentHomeworkFile newFile = new StudentHomeworkFile();
                newFile.setStHwId(studenthomework.getStHwId());

                String sourceFileName = multipartFile.getOriginalFilename();
                File destinationNoticeFile;
                String destinationNoticeFileName;
                String noticePath = "D:/";
                LocalDateTime nowtime = LocalDateTime.now();

                destinationNoticeFileName = nowtime + RandomStringUtils.randomAlphanumeric(8) + sourceFileName;
                destinationNoticeFile = new File(noticePath + destinationNoticeFileName);

                destinationNoticeFile.getParentFile().mkdirs();
                try {
                    multipartFile.transferTo(destinationNoticeFile);
                } catch (IOException e) {
                    e.printStackTrace();
                }

                newFile.setFileName(destinationNoticeFileName);
                newFile.setFileOriginName(sourceFileName);
                newFile.setFilePath(noticePath);
                studentHomeworkFileRepository.save(newFile);

            }
        }
        return studenthomework;
    }

    @Override
    public List<StudentHomework> findStudentHomeworkByHwId(Integer hwId) {
        return studenthomeworkRepositorySupport.findStudentHomeworkByHwId(hwId);
    }

    @Override
    public List<StudentHomework> findStudentHomeworkByStId(String stId) {
        return studenthomeworkRepositorySupport.findStudentHomeworkByStId(stId);
    }

    @Override
    public StudentHomework findBystHwId(Integer stHwId) {
        StudentHomework studentHomework = studenthomeworkRepositorySupport.findBystHwId(stHwId).get();
        return studentHomework;
    }

    @Override
    public void updateScore(StudentHomeworkPutReq studentHomeworkPutReq) {
        int stHwId = studentHomeworkPutReq.getStHwId();
        int stScore = studentHomeworkPutReq.getStHwscore();
        StudentHomework studentHomework = findBystHwId(stHwId);
        studentHomework.setStHwscore(stScore);
        studenthomeworkRepository.save(studentHomework);
    }
}
