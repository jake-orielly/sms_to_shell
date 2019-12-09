# SMS to Shell
This SMS to Shell is a Flask API that uses Twilio to allow users to trigger shell scripts via SMS.

# Setup
After cloning, create a text file in the project directory called "authorized_numbers.txt". Populate this file with the phone numbers you would like to give permission to executes scripts, each on its own line. The numbers must include the country code and be written with no spaces or punctuation. For example, if your number is "1(234) 567-8910", write it as "12345678910". Place any scripts you would like to be availible in the scripts directory. Start the API by running the command "flask run --host=0.0.0.0" in your terminal. You will need a twilio account for the next step (a free trial account is fine). In your twilio numbers page (https://www.twilio.com/console/phone-numbers/incoming), click the number you would like to send your SMS's to. Scroll down to "Messaging" > "A Message Comes In" and set the webhook to "yourserver:5000/sms" and save. You're now ready to go!

# Usage
Text the name of your script (without the .sh extension) to the your twilio number. You will recieve a response letting you know whether the execution of your script succeeded. 