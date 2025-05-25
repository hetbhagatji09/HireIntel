package com.example.Backend.Model.Controller;

import org.springframework.core.io.ByteArrayResource;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;
import org.springframework.web.multipart.MultipartFile;

import java.io.IOException;

@RestController
@RequestMapping("/api/resume")
public class ResumeController {
    @PostMapping("/analyze")
    public ResponseEntity<String> analyzeResume(
            @RequestPart("resume") MultipartFile resume,
            @RequestParam("jobDescription") String jobDescription
    ) throws IOException {

        // Prepare multipart request to n8n agent
        String n8nWebhookUrl = "https://n8n.yourdomain.com/webhook/analyze-resume";

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.MULTIPART_FORM_DATA);

        MultiValueMap<String, Object> body = new LinkedMultiValueMap<>();
        body.add("resume", new ByteArrayResource(resume.getBytes()) {
            @Override
            public String getFilename() {
                return resume.getOriginalFilename();
            }
        });
        body.add("jobDescription", jobDescription);

        HttpEntity<MultiValueMap<String, Object>> requestEntity = new HttpEntity<>(body, headers);

        RestTemplate restTemplate = new RestTemplate();
        ResponseEntity<String> response = restTemplate.postForEntity(n8nWebhookUrl, requestEntity, String.class);

        return ResponseEntity.ok(response.getBody());
    }
}
