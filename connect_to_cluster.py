#! /usr/bin/python

import pexpect #used for the server connection
import sys #to use some methods from sys module

#constants
user = "" #i guess our group id?
password = ""  #and the password we use to log in the cluster?


"""
this method is to connect the cluster via some commands
"""
def ssh_connect_command_line(command, user, host, password):

	#login form, ssh brucewilliam@cs.brandeis.edu
	
	#using the spawn method from pexpect module
	login_config = pexpect.spawn("ssh -l %s %s %s" % (user, host, command))

	#call expect method on login_config, using some info
	#parameter being a list of input
	temp = login_config.expect([pexpect.TIMEOUT, "Loggin in confirmed?", "Password: "]) #waits for input

	#now check the value of temp, 0 being timeout error, 1 being public key not accepted
	if temp == 0:
		print("Some error here!" + "\n")
		print("The messages are as follow:" + "\n")
		print(login_config.before, login_config.after)
		return

	#the public key here is not accepted
	if temp == 1:
		login_config.sendline("Yes")
		
		#now reassign values to login config and the temp variable
		login_config.expect("Password: ") #expect waits for inout
		temp = login_config.expect([pexpect.TIMEOUT, "Password: "])

		#check its value again
		if temp == 0:
			print("Some errors here!" + "\n")
			print("The messages are as follow:" + "\n")
			print(login_config.before, login_config.after)
			return

		#if nothing happens above, then return this login_config
		login_config.sendline(password) #the password for our group
		return login_config


def run():
	server = "" #the server host name for one in our group

	query = sys.argv[1] #the bunch of words we are searching

	for i in range(2, len(sys.argv)):
		query += " " + sys.argv[i]

	#we can print out the query if it works
	print(query)

	
