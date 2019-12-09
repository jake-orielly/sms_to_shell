from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route('/sms', methods=['GET', 'POST'])
def sms_reply():
    'Execute a shell script upon recieving sms from authorized user.'
    # Start our TwiML response
    resp = MessagingResponse()
    number = request.values.get('From')
    if (number_is_authorized(number)):
        files = os.listdir('scripts')
        scripts = [name.replace('.sh','') for name in files]
        script_name = request.values.get('Body')
        if (script_name in scripts):
            result = os.system('sh ./scripts/' + script_name + '.sh')
            if (result is 0):
                resp.message(script_name + '.sh ran successfully')
            else:
                resp.message(script_name + '.sh returned exit code ' + str(result))
        else:
            resp.message('Error: script ' + script_name + '.sh was not found')
        return str(resp)
    else:
        resp.message('Authorization Error: Unrecognized number')
        return str(resp)

if __name__ == '__main__':
    app.run(debug=True)


def number_is_authorized(num):
    stream = os.popen('cat authorized_numbers.txt')
    file_contents = stream.read()
    numbers = file_contents.split('\n')
    num = num.replace('+','')
    return num in numbers