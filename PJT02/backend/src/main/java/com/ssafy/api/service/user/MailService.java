package com.ssafy.api.service.user;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class MailService {
    @Autowired
    private JavaMailSender javaMailSender;

    public void sendMail(String Id, String Email) {
        String userId = Id;
        String userEmail = Email;

        //단순 텍스트로 구성된 메일 메시지를 생성할 때 사용
        SimpleMailMessage simpleMailMessage = new SimpleMailMessage();
        //수신자 설정
        simpleMailMessage.setTo(userEmail);
        //메일 제목
        simpleMailMessage.setSubject("요청하신 아이디 찾기");
        //메일 내용
        simpleMailMessage.setText("회원님의 아이디는 : "+userId+"입니다.");
        //메일 발송
        javaMailSender.send(simpleMailMessage);
    }
}
