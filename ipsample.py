import socket;
import smtplib;

ip = socket.gethostbyname(socket.gethostname());

#replace the x's with your info!
#remember to allow third party api's to use your senderAddress gmail account!
senderAddress = "xxx@gmail.com";
recieverAddress = "xxxxx";
senderPassword = "xxxxx";
subject = "Raspberry Pi Local IP";
body = "The IP address is: " + ip;

smtp_server = smtplib.SMTP_SSL("smtp.gmail.com", 465);
smtp_server.login(senderAddress, senderPassword);
message = f"Subject: {subject}\n\n{body}";
smtp_server.sendmail(senderAddress, recieverAddress, message);
smtp_server.close();

