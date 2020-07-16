# Liberta Casa

This has a series of little enhancements I have taken up as pet projects.

### Registration Page

##### Theoreticals

It includes the following technologies: oragono IRCd, flask, a python bot using irctokens

It consists of the following flow.

1. A user shall go on to the [registration](https://liberta.casa/register.html) . They will enter the details and click on Register.
   * The Website is generated using `flask` and the form is generated using `wtforms, flask_wtf`. 
   * It shall capture the username and password entered by the user and POST it to the same route.
   * The username and password already have validators to ensure they fit within the parameters if the oragono ircd services. eg. NICKLEN 32
2. The bot will be triggered and it shall carry the information provided as arguments by connecting to the IRCd.
3. It will use the `USER` ,`NICK ` commands to register the connection on the IRCd then assign the nickname same as that passed on by the flask route. 
   * If no lines are recieved it shall throw a server error.
   * If the nickname is already in use then the received the `433` code will be captured and translated back to the user as suggestion to retry with a different username 
   * If the `NICK` command is successful it shall proceed to the next step
4. Using the `PRIVMSG` command the bot shall register for the user and it shall read for `NOTICE` indicating successful account creation and carry that back to the flask app and be shown to the user.
5. TODO: If this fails add and unconditional which exits or it will be an infinite loop.
6. After this success the bot shall Die  and the user will be redirected to the page which contains Rules and FAQs about login and features.

### Verification Page

this has been added to engage email verification during registration to prevent registration spam.
it follows the same exact procedure.


#### Known Drawbacks

CSFR token used to prevent cross site forgery attacks
the ip that connects during registration is localhost itself which prevents checks agains abuse in a way. If there is a way to capture the ip from the website visit and post it to the route and incorporate it somehow then it can be done.
