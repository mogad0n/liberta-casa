# Liberta Casa

This has a series of little enhancements I have taken up as pet projects.

### Registration Page

##### Theoreticals

It includes the following technologies: oragono, flask, a python bot.

It consists of the following flow.

1. A user shall go on to the [registration](https://liberta.casa/register.html) (placeholder). They will enter the details and click on Register.
   * The Website is generated using `flask` and the form is generated using `wtforms, flask_wtf`. 
   * It shall capture the username and password entered by the user and POST it to the same route.
   * The username and password already have validators to ensure they fit within the parameters if the oragono ircd services. eg. NICKLEN 32
2. The bot will be triggered and it shall carry the information provided as arguments by connecting to the IRCd.
3. It will use the `USER` ,`NICK ` commands to register the connection on the IRCd then assign the nickname same as that passed on by the flask route. 
   * If the nickname is already in use then the received the `433` code will be captured and translated back to the user as suggestion to retry with a different username and while the password should be discarded?
   * If the `NICK` command is successful it shall proceed to the next step
4. Using the `PRIVMSG` command the bot shall register for the user and then ? should it capture the registration success NOTICE from the services to confirm back to the user? are there cases where it may not succeed?
5. After this the bot shall Die as if it never existed  and the user will be redirected to the page which contains Rules and FAQs about login and features.

