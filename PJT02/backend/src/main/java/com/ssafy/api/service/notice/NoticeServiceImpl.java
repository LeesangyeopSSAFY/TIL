package com.ssafy.api.service.notice;

import com.ssafy.api.request.notice.NoticeRegisterPostReq;
import com.ssafy.api.request.notice.NoticeUpdatePutReq;
import com.ssafy.db.entity.Notice;
import com.ssafy.db.entity.NoticeFile;
import com.ssafy.db.repository.notice.NoticeFileRepository;
import com.ssafy.db.repository.notice.NoticeRepository;
import com.ssafy.db.repository.notice.NoticeRepositorySupport;
import org.apache.commons.lang3.RandomStringUtils;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.core.io.Resource;
import org.springframework.core.io.UrlResource;
import org.springframework.stereotype.Service;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.net.MalformedURLException;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.time.LocalDateTime;
import java.util.*;

@Service("noticeService")
public class NoticeServiceImpl implements NoticeService{
    @Autowired
    NoticeRepository noticeRepository;

    @Autowired
    NoticeFileRepository noticeFileRepository;

    @Autowired
    NoticeRepositorySupport noticeRepositorySupport;

    @Override // 공지사항 등록
    public Notice createNotice(NoticeRegisterPostReq noticeRegisterPostReq) {
        System.out.println("run service!!!!!!!!!");
        Notice notice = new Notice();
        notice.setStudyId(noticeRegisterPostReq.getStudyId());
        notice.setTchrId(noticeRegisterPostReq.getTchrId());
        notice.setNoticeTitle(noticeRegisterPostReq.getNoticeTitle());
        notice.setNoticeContent(noticeRegisterPostReq.getNoticeContent());
//        System.out.println(noticeRegisterPostReq.getNoticeFile());
        noticeRepository.save(notice);
        System.out.println(notice.getNoticeId());
        if (!noticeRegisterPostReq.getNoticeFile().get(0).isEmpty()) {
            List<MultipartFile> noticeFile = noticeRegisterPostReq.getNoticeFile();
            for (MultipartFile multipartFile : noticeFile) {
                NoticeFile newFile = new NoticeFile();
                newFile.setNoticeId(notice.getNoticeId());

                String sourceFileName = multipartFile.getOriginalFilename();
                File destinationNoticeFile;
                String destinationNoticeFileName;
                String noticePath = "D:/";

                destinationNoticeFileName = "tchr" + RandomStringUtils.randomAlphanumeric(8) + sourceFileName;
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

                noticeFileRepository.save(newFile);
            }
        }
        return notice;
    }

    @Override // 공지사항 삭제
    public void deleteNotice(Integer noticeId, String tchrId) {
        noticeRepositorySupport.deleteNoticeByNoticeIdAndTchrId(noticeId, tchrId);
    }

    @Override // 공지사항 상세 조회
    public Notice findBynoticeId(Integer NoticeId) {
        Notice notice = noticeRepositorySupport.findByNoticeId(NoticeId).get();
        return notice;
    }

    @Override
    public Notice updateNotice(NoticeUpdatePutReq noticeUpdatePutReq) {
        System.out.println(noticeUpdatePutReq.getNoticeId());
        System.out.println(noticeUpdatePutReq.getNoticeTitle());
        System.out.println(noticeUpdatePutReq.getNoticeContent());
        Notice notice = noticeRepositorySupport.findByNoticeId(noticeUpdatePutReq.getNoticeId()).get();
        notice.setNoticeTitle(noticeUpdatePutReq.getNoticeTitle());
        notice.setNoticeContent(noticeUpdatePutReq.getNoticeContent());
        notice.setNoticePosted(LocalDateTime.now());
        noticeRepository.save(notice);
        noticeFileRepository.deleteNoticeFileByNoticeId(noticeUpdatePutReq.getNoticeId());
        if (!noticeUpdatePutReq.getNoticeFile().get(0).isEmpty()) {
            List<MultipartFile> noticeFile = noticeUpdatePutReq.getNoticeFile();
            for (MultipartFile multipartFile : noticeFile) {
                NoticeFile newFile = new NoticeFile();
                newFile.setNoticeId(notice.getNoticeId());

                String sourceFileName = multipartFile.getOriginalFilename();
                File destinationNoticeFile;
                String destinationNoticeFileName;
                String noticePath = "D:/";

                destinationNoticeFileName = "tchr" + RandomStringUtils.randomAlphanumeric(8) + sourceFileName;
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
                noticeFileRepository.save(newFile);
            }
        }
        return notice;
    }

    @Override
    public List<Notice> findNoticeByStudyId(Integer studyId) {
        return noticeRepositorySupport.findNoticeByStudyId(studyId);
    }

    @Override
    public List<Notice> findNoticeByTchrId(String tchrId) {
        return noticeRepositorySupport.findNoticeByTchrId(tchrId);
    }

    @Override
    public List<Notice> findNoticeBystId(String stId) {
        return noticeRepository.findNoticeBystId(stId);
    }

    @Override
    public Resource loadAsResource(String fileName, String filePath) {
        try {
            System.out.println("loadAsResource run!!!!!!!!!!!!!!");
            Path file = Paths.get(filePath).resolve(fileName);
            System.out.println(file);
            System.out.println("file run!!!!!!!!!!!!!!");
            System.out.println(file.toUri());
            Resource resource = new UrlResource(file.toUri());
            if (resource.exists() || resource.isReadable()) {
                return resource;
            }
        } catch (MalformedURLException e) {
            e.printStackTrace();
        }
        return null;
    }
}
