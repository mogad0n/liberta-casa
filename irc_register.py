import socket, irctokens


def ircregister(username, password, email):
    # define the variables
    d = irctokens.StatefulDecoder()
    e = irctokens.StatefulEncoder()
    s = socket.socket()

    #connecting to the server
    s.connect(("127.0.0.1", 6667))

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
                _send(irctokens.build("PRIVMSG", ["NickServ", f"REGISTER {password} {email}"]))

            if line.command == "NOTICE" and line.params == [username, f"Account created, pending verification; verification code has been sent to {email}"]: # if Services respond with appropriate notice NOTICE
                _send(irctokens.build("QUIT"))
                return "success"

# register("hello", "test")
