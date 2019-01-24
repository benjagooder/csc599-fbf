# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from flask import Flask, request, render_template
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/index/')
def index():
    #pages = current_wiki.index()
    #return render_template('index.html', pages=pages)
    return "This should be a list of all of the pages created thus far"

@app.route('/<path:url>/')
def display(url):
    #page = current_wiki.get_or_404(url)
    #return render_template('page.html', page=page)
    with open("romeInput.txt", "r") as f:
        content = f.read()
    return content

@app.route("/lists", methods=['GET'])
def demo():
    # Turn the text outcome from ANTLR back into parsed array of dictionaries
    with open("romeOutput.txt", "r") as file:
        goldenGoose = eval(file.readline())

    uniqueTitles = []
    myDict = {}
    # Scrub through for multiple entries on the same list
    for listTitle in goldenGoose:
        if listTitle[0] not in uniqueTitles:
            myDict[listTitle[0]] = []


    # Scrub through the posts
    for title in myDict:
        for entry in goldenGoose:
            if entry[0] is title:
                myDict[title].append(entry[1])

    return render_template('rome.html', myDict = myDict)


@app.route("/sms", methods=['POST'])
def postSMS():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    resp = MessagingResponse()

    from_number = request.form['From']
    to_number = request.form['To']
    body = request.form['Body']

    ## Execute ANTLR on the current input file
    if (body == "runrunrunrunrunrun"):
        # Need to execute run2.bat here
        os.system("C:/Users/user/Rome/run.bat")
        #resp.message("Running current input queue through ANTLR")
    else:
        # Write the sms message sent to us to a text file
        f = open("romeInput.txt", "a+")
        f.write(body + "\n")
        f.close()

    # Add a message response to the user
    #resp.message("Thank you for your message!")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
