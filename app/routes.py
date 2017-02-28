from flask import Flask, render_template, request, flash
from forms import ContactForm
from flask_mail import Mail, Message


mail = Mail()

app = Flask(__name__)
app.secret_key = "youcantguess"

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USE_SSL"] = True
app.config["MAIL_USERNAME"] = 'contact@example.com'
app.config["MAIL_PASSWORD"] = 'your-password'

mail.init_app(app)


@app.route('/')
@app.route('/contact', methods =['GET', 'POST'])
def contact():
	form = ContactForm()
	if request.method == 'POST':
		if form.validate() == False:
			flash('All fields are required')
			return render_template('contact.html',  form = form)
		else:
			msg = Message(form.subject.data, sender ='contact@example.com', recipients=['your_email@example.com'])
			msg.body = """
			From: %s <%s>
			%s
			""" % (form.name.data, form.email.data, form.message.data)
			mail.send(msg)

			return 'form posted'
	elif request.method == 'GET':
		return render_template('contact.html',  form=form)



if __name__ == '__main__':
	app.run()

