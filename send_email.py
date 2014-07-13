#!/usr/bin/env python
 
from time import sleep
import os
import random
import smtplib
import subprocess
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(23, GPIO.IN)

print "please wait..."
server = smtplib.SMTP('smtp.gmail.com', 587)

#server.ehlo()
#server.starttls()
#server.login()

nouns = ['monkey','cow','buttefly','penguin','elephant','caterpillar','world','ball','chair','hot wheels car','kipa','sock','duck','race car','monster truck','nose']
verbs = ['jumped at','mooed at','quacked at','did crazy things to','bonked','flipped','licked','fell on','spun','looked at']
adj = ['crazy','silly','happy','giant','tiny','weird','dizzy','windy','pink','fast','speedy','super slow','super','rediculous','inredible','unbeleivable','fuzzy']

def sendmail(fro, to, subject, body):
    msg = "\r\n".join([
        "From: " + fro,
        "To: " + to,
        "Subject: " + subject,
        "",
        body 
        ])
    server.sendmail(fro, [to], msg)

def make_msg():
    return 'The ' + random.choice(adj) + ' ' + random.choice(nouns) + ' ' + random.choice(verbs) + ' the ' + random.choice(adj) + ' ' +random.choice(nouns)

#Send the mail
def send():
    print "sending..."
    sendmail("test@example.com", random.choice(emails), msg, "the button was pushed")
    print "sent"

def talk():
    subprocess.call(['./goog_speak.sh', make_msg()])
    #subprocess.Popen(['festival', '--tts'], stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE).communicate(input=make_msg())

print "ready."

while True:
    if ( GPIO.input(23) == False ):
        talk()
        sleep(1)
    sleep(0.01)
 
