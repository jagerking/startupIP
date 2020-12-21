# startupIP
## What is this?
Using Linux's crontab, we can force Linux to execute a Python program at startup using the `@reboot` keyword. This Python program will send an email from a gmail account of your choice to another email containing the system's IP address for use in ssh, for example. 
## How to use:
1. Give the shell script executable privlages:
```
$ sudo chmod +x PATH/TO/ip.sh
```
2. Open your system's crontab using:
``` 
$ sudo crontab -e
```
3. Add the following line to the crontab:
```
@reboot PATH/TO/FILE/ip.sh
```
4. Edit ipsample.py. Where indicated enter destination email address and sender gmail email address and password.
5. You may have to change your gmail account settings to allow Python to send the email. You will recieve an email about doing this if necessary.
