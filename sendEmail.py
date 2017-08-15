import smtplib
to='703353105@qq.com'


mail_user='915932312@qq.com'
mail_pwd='dgobkatgefqfbeeb'
smtpserver=smtplib.SMTP("smtp.qq.com",587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(mail_user,mail_pwd)
header = 'To:' + to + '\n' + 'From: ' + mail_user + '\n' + 'Subject:testing \n'
print(header)
msg= header+ '\n this is test msg from mkyong.com \n\n'
smtpserver.sendmail(mail_user,to,msg)
print('done')
 