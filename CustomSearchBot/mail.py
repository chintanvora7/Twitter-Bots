#This is the Reply module of the framework. Here the reply are packaged in an email and sent to user using the smtp library
import smtplib
'''
fromaddr = 'cmvora@gmail.com'
toaddrs  = ['cvora@umd.edu']
msg = 'There was a terrible error that occured and I wanted you to know!'


# Credentials (if needed)
username = 'cmvora'
password = 'Chintan5493'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
'''

#This function helps in sending out an email. Please add the bot password and account details below
def send_email(content):

	gmail_user = "cmvora@gmail.com"
	gmail_pwd = "****" #Please add password in the Double quotes here
	FROM = 'cmvora@gmail.com'
	TO = ['cvora@umd.edu'] #must be a list
	SUBJECT = "Testing sending using gmail"			#This is the subject of the email
	TEXT = "Testing sending mail using gmail servers"	#This is the body text of the email
	TEXT = content
	# Prepare actual message
	message = """\From: %s\nTo: %s\nSubject: %s\n\n%s
	""" % (FROM, ", ".join(TO), SUBJECT, TEXT)
	try:
		#server = smtplib.SMTP(SERVER) 
		server = smtplib.SMTP("smtp.gmail.com", 587) #or port 465 doesn't seem to work!
		server.ehlo()
		server.starttls()
		server.login(gmail_user, gmail_pwd)
		server.sendmail(FROM, TO, message)
		#server.quit()
		server.close()
		print 'successfully sent the mail'
		return True
	except Exception,e:
		print "failed to send mail due to:"
		print e
		return False

#This is a run function which calls the email function and returns True/False if email is sent/not sent
def run(content):
	result = send_email(content)
	return result

#This is an extra unit test module.
def test():
	s1 = "Hi\n"
	s2 = "This is a test if new line works"
	s3 = "\n"
	s4 = "This should be in the next line"
	s5 = s1+s2+s3+s4
	send_email(s5)	
