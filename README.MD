# Netflix Cookie Monster
## Check Netflix Login cookies
![Alt text](assets/art.png "Cookie Monster!")

Choose an option in the program in order to:

1) Load an existing cookie, created in Netscape Cookie File Format. The script will then parse the objects into a legal login cookie in json format, and subsequently check its validity by opening netflix.com.


2) Login with existing credentials, and export a login cookie for future usage. A usage which is undoubtedly suspect, but that's not for me to judge.

3) Check multiple cookie files, created in Netscape format, and ending in "*.txt". Place the files in the "cookies/" folder, and if valid files exist they will be stored in "valid cookies".


Launch preferably in a Linux terminal, although the script was created in Windows and should work fine (apart from botched escape sequences in powershell...).