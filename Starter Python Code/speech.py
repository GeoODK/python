import speech

while True:
    phrase = speech.input()
    speech.say("You said %s" % phrase)
    if phrase == "turn off":
        break