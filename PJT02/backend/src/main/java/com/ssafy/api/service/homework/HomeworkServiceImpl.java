package com.ssafy.api.service.homework;

import com.ssafy.api.request.homework.HomeworkModifyReq;
import com.ssafy.api.request.homework.HomeworkRegisterPostReq;
import com.ssafy.db.entity.Homework;
import com.ssafy.db.entity.HomeworkFile;
import com.ssafy.db.repository.homework.HomeworkFileRepository;
import com.ssafy.db.repository.homework.HomeworkRepository;
import com.ssafy.db.repository.homework.HomeworkRepositorySupport;
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
import java.util.List;
import java.util.Objects;

@Service("homeworkService")
public class HomeworkServiceImpl implements HomeworkService{
    @Autowired
    HomeworkRepository homeworkRepository;

    @Autowired
    HomeworkFileRepository homeworkFileRepository;

    @Autowired
    HomeworkRepositorySupport homeworkRepositorySupport;

    @Override
    public Homework createHomework(HomeworkRegisterPostReq homeworkRegisterPostReq) {
        Homework homework = new Homework();
        String[] dl = homeworkRegisterPostReq.getHwDeadline().split("[/ :]");
        LocalDateTime deadline = LocalDateTime.of(
                Integer.parseInt(dl[0]),
                Integer.parseInt(dl[1]),
                Integer.parseInt(dl[2]),
                Integer.parseInt(dl[3]),
                Integer.parseInt(dl[4]),
                Integer.parseInt(dl[5]));
        homework.setHwTitle(homeworkRegisterPostReq.getHwTitle());
        homework.setHwContent(homeworkRegisterPostReq.getHwContent());
        homework.setHwDeadline(deadline);
        homework.setTchrId(homeworkRegisterPostReq.getTchrId());
        homework.setStudyId(homeworkRegisterPostReq.getStudyId());
        homeworkRepository.save(homework);
        if (!homeworkRegisterPostReq.getHwFile().get(0).isEmpty()) {
            List<MultipartFile> hwFile = homeworkRegisterPostReq.getHwFile();
            for (MultipartFile multipartFile : hwFile) {
                HomeworkFile newFile = new HomeworkFile();
                newFile.setHwId(homework.getHwId());

                String sourceFileName = multipartFile.getOriginalFilename();
                File destinationHomeworkFile;
                String destinationHomeworkFileName;
                String homeworkPath = "D:/";

                destinationHomeworkFileName = "stu" + RandomStringUtils.randomAlphanumeric(8) + sourceFileName;
                destinationHomeworkFile = new File(homeworkPath + destinationHomeworkFileName);

                destinationHomeworkFile.getParentFile().mkdirs();
                try {
                    multipartFile.transferTo(destinationHomeworkFile);
                } catch (IOException e) {
                    e.printStackTrace();
                }

                newFile.setFileName(destinationHomeworkFileName);
                newFile.setFileOriginName(sourceFileName);
                newFile.setFilePath(homeworkPath);
                homeworkFileRepository.save(newFile);
            }
        }
        return homework;
    }

    @Override
    public void deleteHomework(Integer hwId, String tchrId) {
        homeworkRepositorySupport.deleteHomeworkByHwId(hwId, tchrId);
    }

    @Override
    public List<int[]> countBystId(String stId) {
        return homeworkRepository.countBystId(stId);
    }

    @Override
    public List<int[]> countBytchrId(String tchrId) {
        return homeworkRepository.counthomeworkBytchrId(tchrId);
    }

    @Override
    public List<Homework> findHomeworkBystId(String stId) {
        return homeworkRepository.findHomeworkBystId(stId);
    }

    @Override
    public List<Homework> findHomeworkByStudyId(Integer studyId) {
        return homeworkRepositorySupport.findHomeworkByStudyId(studyId);
    }

    @Override
    public List<Homework> findHomeworkByTchrId(String tchrId) {
        return homeworkRepositorySupport.findHomeworkByTchrId(tchrId);
    }

    @Override
    public Homework findHomeworkByHwId(Integer hwId) {
        Homework hw = homeworkRepositorySupport.findHomeworkByHwId(hwId).get();
        return hw;
    }

    @Override
    public Homework updateHomework(HomeworkModifyReq homeworkModifyReq) {
        Homework homework = homeworkRepositorySupport.findHomeworkByHwId(homeworkModifyReq.getHwId()).get();
        String[] dl = homeworkModifyReq.getHwDeadline().split("[/ :]");
        LocalDateTime deadline = LocalDateTime.of(
                Integer.parseInt(dl[0]),
                Integer.parseInt(dl[1]),
                Integer.parseInt(dl[2]),
                Integer.parseInt(dl[3]),
                Integer.parseInt(dl[4]),
                Integer.parseInt(dl[5]));
        homework.setHwTitle(homeworkModifyReq.getHwTitle());
        homework.setHwContent(homeworkModifyReq.getHwContent());
        homework.setHwDeadline(deadline);
        homework.setHwPosted(LocalDateTime.now());
        homeworkRepository.save(homework);
        homeworkFileRepository.deleteHomeworkFileByHwId(homeworkModifyReq.getHwId());
        if (!homeworkModifyReq.getHwFile().get(0).isEmpty()) {
            List<MultipartFile> hwFile = homeworkModifyReq.getHwFile();
            for (MultipartFile multipartFile : hwFile) {
                HomeworkFile newFile = new HomeworkFile();
                newFile.setHwId(homework.getHwId());

                String sourceFileName = multipartFile.getOriginalFilename();
                File destinationHomeworkFile;
                String destinationHomeworkFileName;
                String homeworkPath = "D:/";

                destinationHomeworkFileName = "stu" + RandomStringUtils.randomAlphanumeric(8) + sourceFileName;
                destinationHomeworkFile = new File(homeworkPath + destinationHomeworkFileName);

                destinationHomeworkFile.getParentFile().mkdirs();
                try {
                    multipartFile.transferTo(destinationHomeworkFile);
                } catch (IOException e) {
                    e.printStackTrace();
                }

                newFile.setFileName(destinationHomeworkFileName);
                newFile.setFileOriginName(sourceFileName);
                newFile.setFilePath(homeworkPath);
                homeworkFileRepository.save(newFile);
            }
        }

        return homework;
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
