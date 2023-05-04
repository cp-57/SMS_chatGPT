# SMS_chatGPT
Communicate with chatGPT via SMS using Twilio, Flask, and OpenAI API.

Suggested Steps:
1. Create a PythonAnywhere account for free: https://www.pythonanywhere.com/
2. Create a free Twilio account and set up a phone #.
3. Create an OpenAI account and obtain an API key. You will likely need to have a paid account to use the API.
4. Create a new web app on PythonAnywhere
5. Add the provided "app.py" code from this repository into the working directory of the web app. 
6. Log in to your PythonAnywhere account and navigate to the "Web" tab for your app.
7. Initialize OpenAI key: Scroll down to the "Environment" section and click the "Add a new variable" button.
In the "Name" field, enter OPENAI_API_KEY.
In the "Value" field, enter your actual API key.
Click the "Add" button to save the environment variable.
8. Create a new virtual environment using a bash console on PythonAnywhere. Then download Twilio, openAI, and flask packages using pip.
9. Go to the "Web" page of PythonAnywhere. Scroll down to virtual environments. Here, put the path to your newly created virtual environment. (i.e 
/home/username/.virtualenvs/name_of_your_virtual_environment)
10. Reload web app using the green button at the top of the "Web" page on PythonAnywhere.
11. Next go to the Twilio console. On the left column, click on Phone Numbers -> Active numbers. Then, click on the phone number you will use.
Go down to "Messaging Configuration". Next to the box that says "A Message Comes In" put the url pertaining to your /sms part of your website (i.e. 
https://your_username.pythonanywhere.com/sms)
12. The number should be set up and working!

Note: Under the Twilio free trial, each number you want to communicate with from the Twilio number will need to be "verified". Type in "verified" into the 
search box at the top of the page to find "Verified Numbers". Input any phone numbers you'd like to use with the chatGPT SMS.
