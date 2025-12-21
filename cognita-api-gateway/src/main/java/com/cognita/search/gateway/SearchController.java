package com.cognita.search.gateway;

import org.springframework.web.bind.annotation.*;
import java.util.Map;

@RestController
@RequestMapping("/api")
@CrossOrigin(origins = "http://localhost:5173")
public class SearchController {

    private final VectorOrchestrationService vectorService;

    public SearchController(VectorOrchestrationService vectorService) {
        this.vectorService = vectorService;
    }

    @PostMapping("/query")
    public Map<String, Object> query(@RequestBody Map<String, String> payload) {
        String text = payload.get("text");
        if (text == null || text.isBlank()) {
            throw new IllegalArgumentException("Query text cannot be empty");
        }
        return vectorService.query(text);
    }

    @GetMapping("/health")
    public String health() {
        return "Cognita Gateway is running";
    }
}
