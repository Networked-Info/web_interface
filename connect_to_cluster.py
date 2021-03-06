#! /usr/bin/python

import pexpect #used for the server connection
import sys #to use some methods from sys module

#constants
# user = "cs132g1" #i guess our group id?
# host = "xcn00.cs-i.brandeis.edu"
# command = "yarn app.jar inputdir outputdir"

"""
this method is to connect the cluster via some commands
"""
# def ssh_connect_command_line(user, server, command):

	#login form, ssh brucewilliam@cs.brandeis.edu
	
	#using the spawn method from pexpect module
	# login_config = pexpect.spawn("ssh -i %s %s@%s %s" % ("~/.ssh/id_rsa_cs132g1", user, host, command))
 #  puts login_config

	#call expect method on login_config, using some info
	#parameter being a list of input
	# temp = login_config.expect([pexpect.TIMEOUT, "Loggin in confirmed?", "Password: "]) #waits for input

	#now check the value of temp, 0 being timeout error, 1 being public key not accepted
	# if temp == 0:
	# 	print("Some error here!" + "\n")
	# 	print("The messages are as follow:" + "\n")
	# 	print(login_config.before, login_config.after)
	# 	return

	#the public key here is not accepted
	# if temp == 1:
	# 	login_config.sendline("Yes")
		
	# 	#now reassign values to login config and the temp variable
	# 	login_config.expect("Password: ") #expect waits for inout
	# 	temp = login_config.expect([pexpect.TIMEOUT, "Password: "])

	# 	#check its value again
	# 	if temp == 0:
	# 		print("Some errors here!" + "\n")
	# 		print("The messages are as follow:" + "\n")
	# 		print(login_config.before, login_config.after)
	# 		return

	# 	#if nothing happens above, then return this login_config
	# 	login_config.sendline(password) #the password for our group
	# 	return login_config

  # return outputstream on cluster


def run():
	user = "cs132g1" #i guess our group id?
	server = "xcn00.cs-i.brandeis.edu" #the server host name for one in our group, like cs.brandeis.edu
	appname = "spark-query.jar"
	ssh_key = "~/.ssh/id_rsa_xcn00"
	command = "yarn jar spark-query.jar /data/wiki_csv wiki0.csv /user/cs132g1/output"

	# query = sys.argv[1] #the bunch of words we are searching

	# for i in range(2, len(sys.argv)):
	# 	query += " " + sys.argv[i]

	# #we can print out the query if it works
	# print(query)

	login_config = pexpect.run("ssh -i %s %s@%s %s" % (ssh_key, user, server, command))
	print(login_config)

  # get("/") {
  #   query = response("query")
  # }

  # python scapture some output stream on the cluster

  # puts login_config

	#then generate the command, i think it's path + which file to run
	# command = ""

	#then start
	# start = ssh_connect_command_line(user, server, password, command)
	# start.expect(pexpect.EOF, timeout = 600)
	# output = start.before

	# print(output) # we can see what results is generated here

 #  request("output") = output
 #  render page

	# file = open('output.txt', 'w')
	# file.write(output)
	# file.close()


#then run
if __name__ == "__main__":
	run()