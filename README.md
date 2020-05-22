# liberta-casa

The goal here is to make the procedure for registration to an ircd absolutely noob friendly whilst still using the services.

This is the rough procedure. 
1. The user will go to the registration page. [Placeholder](https://liberta.casa/register.html). They
  will submit their username and they will type out the password. Both of these fields have validation
  checks dependent on the ircd which are hardcoded. Then they shall click on Register. 

2. That will trigger a POST to the same route. upon detection it will capture the fields and it shall trigger a connection
  by the bot. The bot will connect to the ircd and pass the commands to set it's details based on the username provided using
  USER and NICK commands. If the nick is already in use, the Error code returned will be converted to a username already taken
  alert on the webpage. prompting them to retry. If the nick is not in use then the bot will pass the PRIVMSG to services to
  `REGISTER password` where the password will be replaced by the one captured by flask webapp. The reply code for successful
  registration shall be checked for and upon recieving it it shall display a message for the user to login using SASL.
