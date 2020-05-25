import socket, irctokens
import os


def ircregister(username, password):
    # define the variables
    d = irctokens.StatefulDecoder()
    e = irctokens.StatefulEncoder()
    s = socket.socket()

    #connecting to the server
    host = os.getenv("IRC_HOST") or "127.0.0.1"
    try :
        port = int(os.getenv("IRC_PORT"))
    except :
        port = 6667
    s.connect((host, port))

    #defining the send function with proper formatting
    def _send(line):
        print(f"> {line.format()}")
        e.push(line)
        while e.pending():
            e.pop(s.send(e.pending()))

    # registering the connection to the server

    _send(irctokens.build("USER", [username, "0", "*", username]))
    _send(irctokens.build("NICK", [username]))

    # go through the cases

    while True:
        lines = d.push(s.recv(1024))

        if lines == None:    #if nothing is received from server
            return "server error"
            break

        for line in lines:
            print(f"< {line.format()}")

            if line.command == "433": # if nickname already in use
                return "433"

            elif line.command == "005": # when 005 is received pass the nickserv register command command
                _send(irctokens.build("PRIVMSG", ["NickServ", f"REGISTER {password}"]))

            if line.command == "NOTICE" and line.params == [username, "Account created"]: # if Services respond with appropriate notice NOTICE
                _send(irctokens.build("QUIT"))
                return "success"

# register("hello", "test")
