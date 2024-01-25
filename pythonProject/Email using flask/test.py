from flask import Flask
from flask_mail import Mail,Message

app=Flask(__name__)

app.config['MAIL_SERVER']='SMTP.GMAIL.COM'
app.config['MAIL_PORT']=465
app.config['MAIL_USERNAME']='klucse2000031425@gmail.com'
app.config['MAIL_PASSWORD']='123456789'
app.config['MAIL_USE_TLS']=False
app.config['MAIL_USE_SSL']=True
mail=Mail(app)


@app.route("/")
def index():
    msg=Message('Hello',
                sender='klucse2000031425@gmail.com',
                recipients=['klucse2000031425@gmail.com'])
    msg.body='hello!! This message was sent from flask mail'
    mail.send(msg)
    return 'Sent'
if __name__=='__main__':
    app.run(debug=True)