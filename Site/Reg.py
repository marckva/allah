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
                return  ('''<h2 align=center>etot login yje ispolsovalsia. poprobyite eshe raz. </h2>'''+"<br>"+'''
                <style>
                body {
                  background: #ffffff;
                }
                .gradient-button {
                  text-decoration: none;
                  display: inline-block;
                  color: white;
                  padding: 20px 80px;
                  margin: 10px 20px;
                  border-radius: 10px;
                  font-family: 'Montserrat', sans-serif;
                  text-transform: uppercase;
                  letter-spacing: 2px;
                  background-image: linear-gradient(to right, #9EEFE1 0%, #4830F0 51%, #9EEFE1 100%);
                  background-size: 200% auto;
                  box-shadow: 0 0 20px rgba(0, 0, 0, .1);
                  transition: .5s;
                }
                .gradient-button:hover {
                  background-position: right center;
                }
                </style>
                ''')
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
                return  ('''<h2 align=center>vi yspeshno zaregestrirovalis`  </h2>'''+"<br>"+'''
                <style>
                body {
                  background: #ffffff;
                }
                .gradient-button {
                  text-decoration: none;
                  display: inline-block;
                  color: white;
                  padding: 20px 80px;
                  margin: 10px 20px;
                  border-radius: 10px;
                  font-family: 'Montserrat', sans-serif;
                  text-transform: uppercase;
                  letter-spacing: 2px;
                  background-image: linear-gradient(to right, #9EEFE1 0%, #4830F0 51%, #9EEFE1 100%);
                  background-size: 200% auto;
                  box-shadow: 0 0 20px rgba(0, 0, 0, .1);
                  transition: .5s;
                }
                .gradient-button:hover {
                  background-position: right center;
                }
                </style>
                <div class="holder">
                    <p><a href="/Reg"class="gradient-button">Back</a></p>
                </div>''')
            elif (match==None):
                return  ('''<h2 align=center>email ne podhodit. poprobyite eshe raz. </h2>'''+"<br>"+'''
                <style>
                body {
                  background: #ffffff;
                }
                .gradient-button {
                  text-decoration: none;
                  display: inline-block;
                  color: white;
                  padding: 20px 80px;
                  margin: 10px 20px;
                  border-radius: 10px;
                  font-family: 'Montserrat', sans-serif;
                  text-transform: uppercase;
                  letter-spacing: 2px;
                  background-image: linear-gradient(to right, #9EEFE1 0%, #4830F0 51%, #9EEFE1 100%);
                  background-size: 200% auto;
                  box-shadow: 0 0 20px rgba(0, 0, 0, .1);
                  transition: .5s;
                }
                .gradient-button:hover {
                  background-position: right center;
                }
                </style>
                ''')
        elif (pas!=pas1):
                return  ('''<h2 align=center>parol ne sovpadaet. Try again.  </h2>'''+"<br>"+'''
                <style>
                body {
                  background: #ffffff;
                }
                .gradient-button {
                  text-decoration: none;
                  display: inline-block;
                  color: white;
                  padding: 20px 80px;
                  margin: 10px 20px;
                  border-radius: 10px;
                  font-family: 'Montserrat', sans-serif;
                  text-transform: uppercase;
                  letter-spacing: 2px;
                  background-image: linear-gradient(to right, #9EEFE1 0%, #4830F0 51%, #9EEFE1 100%);
                  background-size: 200% auto;
                  box-shadow: 0 0 20px rgba(0, 0, 0, .1);
                  transition: .5s;
                }
                .gradient-button:hover {
                  background-position: right center;
                }
                </style>
               ''')