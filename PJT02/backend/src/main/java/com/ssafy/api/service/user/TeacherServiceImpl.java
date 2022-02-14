package com.ssafy.api.service.user;

import com.ssafy.api.request.user.TeacherModifyPutReq;
import com.ssafy.api.request.user.TeacherProfilePutReq;
import org.apache.commons.lang3.RandomStringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;

import com.ssafy.api.request.user.TeacherRegisterPostReq;
import com.ssafy.db.entity.Teacher;
import com.ssafy.db.repository.user.TeacherRepository;
import com.ssafy.db.repository.user.TeacherRepositorySupport;

import java.io.File;
import java.io.IOException;
import java.util.List;

@Service("teacherService")
public class TeacherServiceImpl implements TeacherService {
	@Autowired
	TeacherRepository teacherRepository;

	@Autowired
	TeacherRepositorySupport teacherRepositorySupport;

	@Autowired
	PasswordEncoder passwordEncoder;

	@Override
	public Teacher createTeacher(TeacherRegisterPostReq teacherRegisterInfo) {
		Teacher teacher = new Teacher();
		teacher.setTchrId(teacherRegisterInfo.getTchr_id());
		teacher.setTchrName(teacherRegisterInfo.getTchr_name());
		teacher.setTchrEmail(teacherRegisterInfo.getTchr_email());
		teacher.setTchrPassword(passwordEncoder.encode(teacherRegisterInfo.getTchr_password()));
		teacher.setTchrContact(teacherRegisterInfo.getTchr_contact());
		teacher.setTchrSchool(teacherRegisterInfo.getTchr_school());
		teacher.setTchrBirthday(teacherRegisterInfo.getTchr_birthday());
		return teacherRepository.save(teacher);
	}

	@Override
	public Teacher modifyTeacher(TeacherModifyPutReq teacherModifyInfo) {
		Teacher teacher = new Teacher();
		teacher.setTchrId(teacherModifyInfo.getTchr_id());
		teacher.setTchrName(teacherModifyInfo.getTchr_name());
		teacher.setTchrEmail(teacherModifyInfo.getTchr_email());
		teacher.setTchrPassword(passwordEncoder.encode(teacherModifyInfo.getTchr_password()));
		teacher.setTchrContact(teacherModifyInfo.getTchr_contact());
		teacher.setTchrSchool(teacherModifyInfo.getTchr_school());
		teacher.setTchrBirthday(teacherModifyInfo.getTchr_birthday());
		return teacherRepository.save(teacher);
	}

	@Override
	public Teacher findById(String tchrId) {
		Teacher teacher = teacherRepositorySupport.findById(tchrId).get();
		return teacher;
	}

	@Override
	public void deleteTeacher(String tchr_id) {
		teacherRepository.deleteById(tchr_id);
	}

	@Override
	public Teacher changeTeacherPassword(Teacher teacher) {
		teacher.setTchrPassword(passwordEncoder.encode(teacher.getTchrPassword()));
		return teacherRepository.save(teacher);
	}

	@Override
	public String findByName(String tchrName) {
		String tchrId = teacherRepositorySupport.findIdByName(tchrName);
		return tchrId;
	}

	@Override
	public List<Object[]> findstIdAndstName() {
		List<Object[]> list = teacherRepository.selectAllStudent();
		return list;
	}

	@Override
	public Teacher changeTeacherProfile(TeacherProfilePutReq teacherProfilePutReq) {
		Teacher teacher = teacherRepositorySupport.findById(teacherProfilePutReq.getTchrId()).get();

		if (teacherProfilePutReq.getTchrProfFile().get(0).isEmpty()) {
			System.out.println("!!!!!!!!!!!!!!");
			teacher.setTchrProfName(null);
			teacher.setTchrProfPath(null);
			teacher.setTchrOriginProfName(null);
			teacherRepository.save(teacher);
			return teacher;
		} else {
			System.out.println("????????????????");
			String sourceFileName = teacherProfilePutReq.getTchrProfFile().get(0).getOriginalFilename();
			File destinationProfile;
			String destinationProfileName;
			String teacherprofPath = "../frontend/src/assets/images/tchr_profiles/";

			destinationProfileName = "tchr" + RandomStringUtils.randomAlphanumeric(8) + sourceFileName;
			destinationProfile = new File(teacherprofPath + destinationProfileName);

			destinationProfile.getParentFile().mkdirs();
			try {
				teacherProfilePutReq.getTchrProfFile().get(0).transferTo(destinationProfile);
			} catch (IOException e) {
				e.printStackTrace();
			}

			teacher.setTchrProfName(destinationProfileName);
			teacher.setTchrOriginProfName(sourceFileName);
			teacher.setTchrProfPath("tchr_profiles/");
			teacherRepository.save(teacher);
			return teacher;
		}
	}
}

