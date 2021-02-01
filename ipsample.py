import socket;
import smtplib;
import fcntl
import struct

ip = socket.gethostbyname(socket.gethostname());

remote_server = "google.com"
def get_my_ip_address(remote_server):
    """
    Return the/a network-facing IP number for this system.
    """
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s: 
        s.connect((remote_server, 80))
        return s.getsockname()[0]

ip2 =get_my_ip_address(remote_server)

#replace the x's with your info!
#remember to allow third party api's to use your senderAddress gmail account!
senderAddress = "xxx";
recieverAddress = "xxx";
senderPassword = "xxx";
subject = "Raspberry Pi Local IP";
body = "The IP address is: " + ip + " | "+ ip2;

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465);
smtp_server.login(senderAddress, senderPassword);
message = f"Subject: {subject}\n\n{body}";
smtp_server.sendmail(senderAddress, recieverAddress, message);
smtp_server.close();

