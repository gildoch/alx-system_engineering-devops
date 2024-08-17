
### Postmortem Documentation

**1. Issue Summary:**
- **Duration:** The outage lasted from 07:30 to 08:15 GMT on Friday, 24 Mar 2017.
- **Impact:** The website www.gch.com was down, resulting in a 500 Internal Server Error. 100% of users were affected and unable to access the site.
- **Root Cause:** A typo in the `wp-settings.php` file, where `.phpp` was mistakenly used instead of `.php`, caused Apache to fail, leading to the 500 error.

**2. Timeline:**
- **07:30 GMT:** Issue detected when users reported inability to access www.gch.com.
- **07:35 GMT:** Monitoring alerts confirmed the 500 Internal Server Error across the site.
- **07:40 GMT:** Initial investigation began, checking Apache configuration files and server logs.
- **07:45 GMT:** Used `strace` to trace the execution flow, identifying an issue with the `wp-settings.php` file.
- **07:50 GMT:** Found that the `wp-settings.php` file contained a typo: `.phpp` instead of `.php`.
- **07:55 GMT:** Corrected the typo using `sed` command.
- **08:00 GMT:** Website functionality restored; tested and confirmed that the 500 error was resolved.
- **08:05 GMT:** Automated the fix using Puppet to prevent recurrence.
- **08:15 GMT:** Incident closed after final verification of all services.

**3. Root Cause and Resolution:**
- **Root Cause:** The `wp-settings.php` file, crucial for WordPress operations, was inadvertently edited with a typo (`.phpp` instead of `.php`). This error caused Apache to fail when processing the file, resulting in the 500 Internal Server Error.
- **Resolution:** The error was resolved by locating the typo using `grep`, and correcting it with the `sed` command. To prevent future occurrences, a Puppet script was deployed to automate the detection and correction of similar typos.

**4. Corrective and Preventative Measures:**
- **Improvements:** 
  - **Automate Typo Detection:** Implement a Puppet script to continually monitor and correct typos in critical files.
  - **Enhance Code Review:** Introduce a stricter review process for changes to key files like `wp-settings.php`.
  - **Monitoring Enhancements:** Set up additional monitoring for unauthorized file changes.

- **Tasks:**
  - **Deploy Puppet Automation:** Ensure the Puppet script is fully operational across all relevant environments.
  - **Implement File Integrity Monitoring:** Add tools to detect and alert on unauthorized or unintended file changes.
  - **Conduct Regular Audits:** Schedule periodic audits of critical configuration and code files.