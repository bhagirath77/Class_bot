## A bot that can attend your online classes
This bot works if your online classes are on the google meet platform.

First of all, you will have to add your credentials inside the code at two places i.e. your mail id and password which can be seen on the 48th line of the code.

After that , you will have to create an SQLite database which will hold the classroom codes for all the classes as per the schedules. 
The database can be easily created without coding using DB browser.
[Here](https://sqlitebrowser.org/) is the link from where you can download it. 
The table that you create should look something like this, 


![37-1](https://user-images.githubusercontent.com/61153266/120939110-028db400-c734-11eb-806e-a1fe4d8b488c.png)

Once this is done, you can run the code on a virtual machine and it will attend all your online classes.What the bot will do is that:

Open a chrome broswer.

Login to your gmail account.

Open google meet website.

Enter the classroon code.

Turn on your camera and mic and then proceed to join the class.

Leave the class on time .

And then it will join the next class as per the timetable and follow the same process over and over again.
