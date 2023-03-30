# Browsers
## Notes

## Security
### Is it safe to access any url?
In modern browsers, each tab runs on an independent process or [sandboxed](https://wiki.mozilla.org/Security/Sandbox/Process_model), therefore js scripts cannot access or modify memory spaces outside of the process

It cannot acces neither *localStorage* nor *Cookies* associated to another domain, due to the [Same Origin](https://en.wikipedia.org/wiki/Same-origin_policy#Origin_determination_rules) policy.

The main problem would be to download & execute a binary file or inserting personal info.

#### Browsers exploits / Beef Project
From another point of view, on 2023 no one is targeting cookies, there is much bigger risk for browsers, for example [Beef Project](https://beefproject.com/)

Is it possible to create malicious urls with beefproject.com and take control of the PC/mobile
