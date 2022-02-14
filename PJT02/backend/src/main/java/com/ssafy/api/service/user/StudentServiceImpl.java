package com.ssafy.api.service.user;

import com.ssafy.api.request.user.StudentProfilePutReq;
import com.ssafy.api.request.user.StudentRegisterPostReq;
import com.ssafy.api.request.user.StudentUpdatePutReq;
import com.ssafy.db.entity.Student;
import com.ssafy.db.entity.Teacher;
import com.ssafy.db.repository.user.StudentRepository;
import com.ssafy.db.repository.user.StudentRepositorySupport;
import org.apache.commons.lang3.RandomStringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Lazy;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import java.io.File;
import java.io.IOException;
import java.util.List;

@Service("studentService")
public class StudentServiceImpl implements StudentService{
    @Autowired
    StudentRepository studentRepository;

    @Autowired
    StudentRepositorySupport studentRepositorySupport;


    @Lazy
    @Autowired
    PasswordEncoder passwordEncoder;

    @Override
    public Student createStudent(StudentRegisterPostReq studentRegisterInfo) {
        Student student = new Student();
        student.setStId(studentRegisterInfo.getSt_id());
        student.setStName(studentRegisterInfo.getSt_name());
        student.setStEmail(studentRegisterInfo.getSt_email());
        student.setStPassword(passwordEncoder.encode(studentRegisterInfo.getSt_password()));
        student.setStContact(studentRegisterInfo.getSt_contact());
        student.setStSchool(studentRegisterInfo.getSt_school());
        student.setStBirthday(studentRegisterInfo.getSt_birthday());
        return studentRepository.save(student);
    }

    @Override
    public Student findById(String stId) {
        Student student = studentRepositorySupport.findById(stId).get();
        return student;
    }

    @Override
    public void deleteStudent(String st_id) {
        studentRepository.deleteById(st_id);
    }

    @Override
    public Student updateStudent(StudentUpdatePutReq studentUpdatePutReq) {
        Student student = new Student();
        student.setStId(studentUpdatePutReq.getSt_id());
        student.setStName(studentUpdatePutReq.getSt_name());
        student.setStEmail(studentUpdatePutReq.getSt_email());
        student.setStPassword(passwordEncoder.encode(studentUpdatePutReq.getSt_password()));
        student.setStContact(studentUpdatePutReq.getSt_contact());
        student.setStSchool(studentUpdatePutReq.getSt_school());
        student.setStBirthday(studentUpdatePutReq.getSt_birthday());
        return studentRepository.save(student);
    }

    @Override
    public String findstIdBystName(String stName) {
        String StId = studentRepositorySupport.findstIdBystName(stName);
        return StId;
    }

    @Override
    public Student changeStudentPassword(Student student) {
        student.setStPassword(passwordEncoder.encode(student.getStPassword()));
        return studentRepository.save(student);
    }

    @Override
    public Student changeStudentProfile(StudentProfilePutReq studentProfilePutReq) {
        Student student = studentRepositorySupport.findById(studentProfilePutReq.getStId()).get();

        if (studentProfilePutReq.getStProfFile().get(0).isEmpty()) {
            System.out.println("!!!!!!!!!!!!!!");
            student.setStProfName(null);
            student.setStProfPath(null);
            student.setStOriginProfName(null);
            studentRepository.save(student);
            return student;
        } else {
            System.out.println("????????????????");
            String sourceFileName = studentProfilePutReq.getStProfFile().get(0).getOriginalFilename();
            File destinationProfile;
            String destinationProfileName;
            String studentprofPath = "../frontend/src/assets/images/st_profiles/";

            destinationProfileName = "st" + RandomStringUtils.randomAlphanumeric(8) + sourceFileName;
            destinationProfile = new File(studentprofPath + destinationProfileName);

            destinationProfile.getParentFile().mkdirs();
            try {
                studentProfilePutReq.getStProfFile().get(0).transferTo(destinationProfile);
            } catch (IOException e) {
                e.printStackTrace();
            }

            student.setStProfName(destinationProfileName);
            student.setStOriginProfName(sourceFileName);
            student.setStProfPath("st_profiles/");
            studentRepository.save(student);
            return student;
        }
    }

}
