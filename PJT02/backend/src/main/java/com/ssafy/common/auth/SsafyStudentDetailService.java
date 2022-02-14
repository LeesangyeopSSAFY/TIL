package com.ssafy.common.auth;

import com.ssafy.api.service.user.StudentService;
import com.ssafy.db.entity.Student;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.stereotype.Component;

/**
 * 현재 액세스 토큰으로 부터 인증된 유저의 상세정보(활성화 여부, 만료, 롤 등) 관련 서비스 정의.
 */
@Component
public class SsafyStudentDetailService implements UserDetailsService {
	@Autowired
	StudentService studentService;

    @Override
    public UserDetails loadUserByUsername(String userId) throws UsernameNotFoundException {
		Student student = studentService.findById(userId);
    		if(student != null) {
    			SsafyStudentDetails studentDetails = new SsafyStudentDetails(student);
    			return studentDetails;
    		}
    		return null;
    }
}
