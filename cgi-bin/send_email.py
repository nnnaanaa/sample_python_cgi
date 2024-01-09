#!/usr/bin/env python
import cgi
import smtplib
from email.mime.text import MIMEText
 
# ヘッダーの設定
print("Content-type: text/html\n")

# POSTデータの取得
form = cgi.FieldStorage()
name = form.getvalue("name")
email = form.getvalue("email")
message = form.getvalue("message")

smtp_setting = {
    'host': 'smtp.lolipop.jp',
    'port': 465,
    'account': '',
    'password': ''
}
 
email_content = {
    'To': '',
    'From': '{}'.format(email),
    'Subject': 'お問い合わせ {}'.format(name),
    'Text': '{}'.format(message)
}
 
msg = MIMEText(email_content['Text'], 'plain', 'utf-8')
msg['Subject'] = email_content['Subject']
msg['From'] = email_content['From']
msg['To'] = email_content['To']
 
try:
    with smtplib.SMTP_SSL(smtp_setting['host'], smtp_setting['port'], timeout=10) as smtp:
        smtp.login(smtp_setting['account'], smtp_setting['password'])
        smtp.send_message(msg)
        smtp.quit()

    print("<h2>Email sent successfully</h2>")
except Exception as e:
    print(f"<h2>Error sending email: {str(e)}</h2>")
