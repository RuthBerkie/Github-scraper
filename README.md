This script is an automated security tool that scans a user's public GitHub profile to find exposed passwords.

     * It launches a controlled Google Chrome browser via Selenium, 
     * finds all repositories belonging to that user, 
     * opens any Python (.py) or JavaScript (.js) files. 

It then reads through the plain text code line-by-line and prints an immediate alert to your console if the word "password" is discovered.
