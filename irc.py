from flaskapp import register
import irctokens, socket

ircsock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = "127.0.0.1"
username = register.username # collect from flask
password = register.username #collect from flask

ircsock.connect((server, 6667))
ircsock.send(bytes("USER "+ username + " " + username + " " + username + " " + username + "\r\n", "UTF-8"))
ircsock.send(bytes("NICK "+ username + "\r\n", "UTF-8"))
ircsock.send(bytes(f"PRIVMSG NickServ@localhost :REGISTER {password}\r\n" ))
ircsock.send(bytes("QUIT \n", "UTF-8"))




