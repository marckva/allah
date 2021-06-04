from bottle import post, request, route, run, redirect,put
import re
import pdb
import json
@post('/Reg', method="post")
def Reg_form():
    logins=[]
    f=open("serf.txt","a")
    f.close()
    login = request.forms.get('Login')
    pas = request.forms.get('Password')
    pas1 = request.forms.get('Password confirmation')
    mail = request.forms.get('email')
    for line in open("serf.txt","r"):
        if "Login:" in line:
            string1, separator, string2 = line.partition(': ')
            logins.append(string2)
    print (logins)
    if (login+"\n") in logins:#Проверка на существующий логин
        return  ('''<h2 align=center>This login already exists. Try again.  </h2>'''+"<br>"+'''
        <style>
            h2
            {
            font-size: 200%;
            font-family: Verdana, Arial, Helvetica, sans-serif;
            color: #808080;
            }
            .h4 {
            border-radius: 12px;
            background: wight;
            border-color: #cccccc;
            color: black;
            font-size: 9pt;
            height: 70px;
            width: 200px;
            position: relative;
            top: 50%;
            left: 50%;
            transform: translate(-50%,0);
            }
        </style>
            <p><a href="/Reg"><input class=h4  type="submit" value="Back"></a></p>''')
    else:
        if (pas==pas1):#Проверка на пароли
            match = re.search (r'[a-zA-Z0-9+-]+[@][a-zA-Z0-9-.]+[^.].[a-zA-Z0-9-.]{2,3}$', mail)
            if match!=None: #Проверка на почту
                g=open("log.txt","a")
                g.writelines(login)
                g.writelines("\n")
                g.close()
                t=open("pass.txt","a")
                t.writelines(pas)
                t.writelines("\n")
                t.close()
                f=open("serf.txt","a")
                f.writelines("****************************************************************"+"\n")#Запись данных в файлы
                f.writelines("Login: "+login)
                f.writelines("\n")
                f.writelines("Password: "+pas)
                f.writelines("\n")
                f.writelines("Email: "+mail)
                f.writelines("\n")
                f.close()
                return  ('''<h2 align=center>You have successfully registered </h2>'''+"<br>"+'''
                <style>

                    h2
                    {
                    font-size: 200%;
                    font-family: Verdana, Arial, Helvetica, sans-serif;
                    color: #808080;
                    }
                    .h4 {
                    border-radius: 12px;
                    background: wight;
                    border-color: #cccccc;
                    color: black;
                    font-size: 9pt;
                    height: 70px;
                    width: 200px;
                    position: relative;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%,0);
                    }
                </style>
                    <p><a href="/home"><input class=h4  type="submit" value="Back"></a></p>''')
            elif (match==None):
                return  ('''<h2 align=center>Wrong mail. Try again.  </h2>'''+"<br>"+'''
                <style>

                    h2
                    {
                    font-size: 200%;
                    font-family: Verdana, Arial, Helvetica, sans-serif;
                    color: #808080;
                    }
                    .h4 {
                    border-radius: 12px;
                    background: wight;
                    border-color: #cccccc;
                    color: black;
                    font-size: 9pt;
                    height: 70px;
                    width: 200px;
                    position: relative;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%,0);
                    }
                </style>
                    <p><a href="/Reg"><input class=h4  type="submit" value="Back"></a></p>''')
        elif (pas!=pas1):
                return  ('''<h2 align=center>Password mismatch. Try again.  </h2>'''+"<br>"+'''
                <style>

                    h2
                    {
                    font-size: 200%;
                    font-family: Verdana, Arial, Helvetica, sans-serif;
                    color: #808080;
                    }
                    .h4 {
                    border-radius: 12px;
                    background: wight;
                    border-color: #cccccc;
                    color: black;
                    font-size: 9pt;
                    height: 70px;
                    width: 200px;
                    position: relative;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%,0);
                    }
                </style>
                    <p><a href="/Reg"><input class=h4  type="submit" value="Back"></a></p>''')