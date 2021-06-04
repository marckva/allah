from bottle import post, request
import re
@post('/home', method='post')

def my_form():
    mail = request.forms.get('ADRESS')
    question = request.forms.get('QUEST')

    regex = '^(\w|\.|\-|\_)+[@](\w|\.|\-|\_)+[^.]\.\w{2,3}$'
    if len(mail) == 0 or len(question) == 0:
        return "Empty from!"
    else:
        if(re.search(regex, mail)):
             return "Thanks! The answer will be sent to the mail %s" % mail
        else:
            return "Mail doesnt match"