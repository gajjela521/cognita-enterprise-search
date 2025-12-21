package com.cognita.search.gateway;

import org.springframework.stereotype.Service;
import org.springframework.web.client.RestTemplate;

import org.springframework.http.ResponseEntity;
import org.springframework.http.HttpEntity;
import org.springframework.http.HttpHeaders;
import org.springframework.http.MediaType;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

@Service
public class VectorOrchestrationService {

    private final RestTemplate restTemplate;
    private final String VECTOR_SERVICE_URL = "http://localhost:5001/query";

    public VectorOrchestrationService() {
        this.restTemplate = new RestTemplate();
    }

    public Map<String, Object> query(String queryText) {
        Map<String, Object> requestBody = new HashMap<>();
        requestBody.put("text", queryText);
        requestBody.put("k", 5);

        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_JSON);

        HttpEntity<Map<String, Object>> request = new HttpEntity<>(requestBody, headers);

        try {
            ResponseEntity<Map> response = restTemplate.postForEntity(VECTOR_SERVICE_URL, request, Map.class);
            return response.getBody();
        } catch (Exception e) {
            throw new RuntimeException("Failed to query Vector Service: " + e.getMessage());
        }
    }
}
