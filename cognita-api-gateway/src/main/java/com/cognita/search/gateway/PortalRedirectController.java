package com.cognita.search.gateway;

import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.servlet.view.RedirectView;

@RestController
public class PortalRedirectController {

    @GetMapping("/")
    public RedirectView home() {
        return new RedirectView("http://localhost:5173");
    }
}
