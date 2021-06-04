% rebase('layout.tpl', title='Home Page', year=year)
<div class="jumbotron">
    <h1>Balanced meals</h1>
    <p class="lead">A balanced diet is based on three traditional meals. Eat right and stay in shape with 23Food.</p>
    <p><a href="http://bottlepy.org/docs/dev/index.html" class="btn btn-primary btn-large">Catalog &raquo;</a></p>
</div>

<div class="row">
    <div class="col-md-4">
        <h2>Breakfasts</h2>
        <p>Breakfast is the most important meal. We can make your morning better and energize you for the whole day. If you order breakfast from 9: 00 to 12: 00, you will receive a 25% discount.</p>
        <img src="static/image/img1.jpg" width = "350" height = "200">
        <br>
        <br>
        <br>
        <br>
        <p>Lunch promo code, only today from 12:00 to 16:00.</p>
        <p>Promo code:LUNCHMURCH</p>
        <img src = "static/image/gif1.gif" widht = "150" height = "250">

        
    </div>
    <div class="col-md-4">
        <h2>Lunches</h2>
        <p>So as not to waste the most productive hours on the road and in queues. Instead of the usual couple of establishments on 23Food.There are more than a dozen options for food — something for everyone.</p>
        <img src="static/image/img3.jpg" width = "350" height = "200">

    </div>

    <div class="col-md-4">
        <h2>Dinners</h2>
        <p>If you need to beat the deadlines sooner. Dinner with delivery will help you to cheer up, not be distracted by the search for food and feel more confident in the evenings in the office, home etc.</p>
        <img src="static/image/img2.jpg" width = "350" height = "200">

    </div>
</div>
<h3> Ask a Question </h3>
<form action="/home" method="post">
        <p><textarea rows="2" cols="50" name="QUEST" placeholder="Your question"></textarea></p> 
        <p><input type="text" size="50" name="ADRESS" placeholder="Your email"></p>
        <p><input type="submit" class="btn btn-default" value="Send"></p>
</form>
 
<style>
    .lognText{
        padding: 9px;
        border: 1px solid #808080;
        border-radius: 5px;
        position: absolute;
        font-size: 20px;
        width: 150px;
        height: 500px;
        top: 20%;
        left: 90%;
        text-align: center;
    }

</style>

<style>
    .lognLab{
        position: absolute;
        font-size: 20px;
        width: 100px;
        top: 10%;
        left: 90%;
        text-align: center;
    }

</style>

%with open("log.txt",encoding="utf-8") as file:
    %logs=file.read()
<p><label class=lognLab ;>Users</label><textarea class=lognText>{{logs}}</textarea></p>