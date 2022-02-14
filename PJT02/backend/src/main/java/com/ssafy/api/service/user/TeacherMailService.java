package com.ssafy.api.service.user;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

/**
 *	유저 관련 비즈니스 로직 처리를 위한 서비스 구현 정의.
 */
@Service("teacherMailService")
public class TeacherMailService {
	@Autowired
	private JavaMailSender javaMailSender;

	public void sendMail(String Id, String Mail){
		String userId = Id;
		String userEmail = Mail;

		SimpleMailMessage Message = new SimpleMailMessage();	// 메일 내용 설정
		Message.setTo(userEmail);								// 수신자 설정
		Message.setSubject("요청하신 아이디 찾기");			// 메일 제목 설정
		Message.setText("회원님의 아이디는 : "+userId+"입니다.");			// 내용 설정
		javaMailSender.send(Message);
	}
}
