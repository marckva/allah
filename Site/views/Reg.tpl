% rebase('layout.tpl', title='Home Page')
<form method="post" action="/Reg" class="form">

<style>

.center {
    position: absolute;
    top: 15%;
    left: 10%;
}

body {
    background: #F6F9F9;
}

.form label {
    width: 180px;
    float: left;
}

.form label {
    width: 180px;
    float: left;                
    color: #999;
}

.form input {
    width: 400px;
}

.form textarea {
    width: 400px;
}

.form textarea {
    width: 400px;
    max-width: 400px;
    min-width: 400px;
    line-height: 150%;
}

.confirm {
    float: none !important;
}

.form input[type="checkbox"] {
    width: auto;
}

.form input, .form textarea, .form select {
    padding: 9px;
    border: 1px solid #E5E5E5;
    border-radius: 5px;
}

</style>
<style>
    .lognLab{
        position: absolute;
        font-size: 20px;
        width: 150px;
        top: -20%;
        left: 0%;
        text-align: center;
    }

</style>
<body>
    <div  class=center id=left>
     <p>
     <label for="Reg"><span class=lognLab>Registratision</label>            <!--Labels-->
     </p>
     <p>
     <label for="Login"><span class="formTextRed">*</span> Login:</label>
     <input type="text" name="Login" id="lastname" />
     </p>
     <p>
     <label for="Password"><span class="formTextRed">*</span> Password:</label> <!--textarea-->
     <input type="text" name="Password" id="firstname" />
     </p>
     <p>
     <label for="Password confirmation">* Confirm your password:</label>
     <input type="text" name="Password confirmation" id="middlename" />
     </p>
     <p>
     <label for="email"><span class="formTextRed">*</span> Email:</label>
     <input type="text" name="email" id="email" />
     </p>
     <p class="submit">
     <input type="submit" value="Send"/>                                    <!--Button-->
     </p>
    </div>
</body>
 </form>
