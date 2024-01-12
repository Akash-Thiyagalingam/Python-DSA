from flask import Flask, render_template, flash, request, session, send_file

import mysql.connector
import sys

app = Flask(__name__)
app.config['DEBUG']
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'


@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/Home")
def Home():
    return render_template('index.html')


@app.route("/AdminLogin")
def AdminLogin():
    return render_template('AdminLogin.html')


@app.route("/NewOwner")
def NewOwner():
    return render_template('NewOwner.html')


@app.route("/OwnerLogin")
def OwnerLogin():
    return render_template('OwnerLogin.html')


@app.route("/UserLogin")
def UserLogin():
    return render_template('UserLogin.html')


@app.route("/NewUser")
def NewUser():
    return render_template('NewUser.html')


@app.route("/NewVehicle")
def NewVehicle():
    return render_template('NewVehicle.html')


@app.route("/AdminHome")
def AdminHome():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AdminHome.html', data=data)


@app.route("/AOwnerInfo")
def AOwnerInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM regtb  ")
    data = cur.fetchall()
    return render_template('AOwnerInfo.html', data=data)


@app.route("/ASalesInfo")
def ASalesInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb  ")
    data = cur.fetchall()
    return render_template('ASalesInfo.html', data=data)


@app.route("/AProductInfo")
def AProductInfo():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('AProductInfo.html', data=data)


@app.route("/adminlogin", methods=['GET', 'POST'])
def adminlogin():
    if request.method == 'POST':
        if request.form['uname'] == 'admin' and request.form['password'] == 'admin':

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb ")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('AdminHome.html', data=data)

        else:
            flash("UserName Or Password Incorrect!")
            return render_template('AdminLogin.html')


@app.route("/ARemove")
def ARemove():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  ")
    data = cur.fetchall()
    return render_template('ProductInfo.html', data=data)


@app.route("/newuser", methods=['GET', 'POST'])
def newuser():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']

        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO regtb VALUES ('','" + fname + "','"+ lname +"','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('User Register successfully')

    return render_template('UserLogin.html')


@app.route("/newowner", methods=['GET', 'POST'])
def newowner():
    if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        mobile = request.form['mobile']
        email = request.form['email']
        address = request.form['address']
        uname = request.form['uname']
        password = request.form['password']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO ownertb VALUES ('','"+ fname +"','" + lname + "','" + email + "','" + mobile + "','" + address + "','" + uname + "','" + password + "')")
        conn.commit()
        conn.close()
        flash('Owner Register successfully')

    return render_template('OwnerLogin.html')


@app.route("/ownerlogin", methods=['GET', 'POST'])
def ownerlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['dname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from ownertb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('OwnerLogin.html')
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM ownertb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")
            return render_template('OwnerHome.html', data=data)


@app.route("/OwnerHome")
def OwnerHome():
    dname = session['dname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM ownertb where username='" + dname + "'  ")
    data = cur.fetchall()
    return render_template('OwnerHome.html', data=data)





@app.route("/newproduct", methods=['GET', 'POST'])
def newproduct():
    if request.method == 'POST':
        dname = session['dname']
        vanme = request.form['vanme']
        vtype = request.form['vtype']
        year = request.form['year']
        gbox = request.form['gbox']
        powerps = request.form['powerps']
        futype = request.form['futype']
        brand = request.form['brand']
        Amount = request.form['Amount']
        file1 = request.files['file1']
        file1.save("static/upload/" + file1.filename)

        import random
        file = request.files['file']
        fnew = random.randint(1111, 9999)
        savename = str(fnew) + ".png"
        file.save("static/upload/" + savename)
        Address = request.form['Address']
        lat = request.form['lat']
        lon = request.form['lon']
        city = request.form['city']






        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO  protb VALUES ('','" + vanme + "','" + vtype + "','" + year + "','" + gbox + "','" + powerps + "','" + futype + "','" +
            brand + "','" + Amount + "','" + file1.filename + "','" + savename + "','" + dname + "','"+Address+"','"+ lat +"','"+ lon +"','"+ city +"')")
        conn.commit()
        conn.close()

    flash('vehicle Register successfully')
    return render_template('NewVehicle.html')


@app.route("/DVehicleInfo")
def DVehicleInfo():
    dname = session['dname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb where DName='" + dname + "' ")
    data = cur.fetchall()
    return render_template('DVehicleInfo.html', data=data)


@app.route("/DRemove")
def DRemove():
    id = request.args.get('id')
    dname = session['dname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cursor = conn.cursor()
    cursor.execute(
        "delete from protb where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Product  info Remove Successfully!')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb where DName='" + dname + "' ")
    data = cur.fetchall()
    return render_template('DRemove.html', data=data)




@app.route("/DBookInfo")
def DBookInfo():
    dname = session['dname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where DName='" + dname + "' and Status='waiting' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where DName='" + dname + "' and Status!='waiting' ")
    data1 = cur.fetchall()
    return render_template('DBookInfo.html', data=data,data1=data1)


@app.route("/Accept")
def Accept():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cursor = conn.cursor()
    cursor.execute(
        "update   booktb set status='Accept' where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Booking Status  Update  Successfully!')

    dname = session['dname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where DName='" + dname + "' and Status='waiting' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where DName='" + dname + "' and Status!='waiting' ")
    data1 = cur.fetchall()
    return render_template('DBookInfo.html', data=data, data1=data1)


@app.route("/Reject")
def Reject():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cursor = conn.cursor()
    cursor.execute(
        "update   booktb set status='Reject' where id='" + id + "'")
    conn.commit()
    conn.close()

    flash('Booking Status  Update  Successfully!')

    dname = session['dname']
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where DName='" + dname + "' and Status='waiting' ")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM booktb where DName='" + dname + "' and Status!='waiting' ")
    data1 = cur.fetchall()
    return render_template('DBookInfo.html', data=data, data1=data1)


@app.route("/userlogin", methods=['GET', 'POST'])
def userlogin():
    if request.method == 'POST':
        username = request.form['uname']
        password = request.form['password']
        session['uname'] = request.form['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cursor = conn.cursor()
        cursor.execute("SELECT * from regtb where username='" + username + "' and Password='" + password + "'")
        data = cursor.fetchone()
        if data is None:

            flash('Username or Password is wrong')
            return render_template('UserLogin.html')
        else:

            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM regtb where username='" + username + "' and Password='" + password + "'")
            data = cur.fetchall()
            flash("Login successfully")

            return render_template('UserHome.html', data=data)


@app.route("/Search")
def Search():
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb ")
    data = cur.fetchall()

    return render_template('Search.html', data=data)


@app.route("/csearch", methods=['GET', 'POST'])
def csearch():
    if request.method == 'POST':
        city = request.form['city']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM protb where  city ='" + city + "'")
        data = cur.fetchall()

        return render_template('Search.html', data=data)


@app.route("/UserHome")
def UserHome():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  regtb where username='" + uname + "'  ")
    data = cur.fetchall()

    return render_template('UserHome.html', data=data)


@app.route("/Add")
def Add():
    id = request.args.get('id')
    session['pid'] = id
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM protb  where id='" + id + "' ")
    data = cur.fetchall()
    return render_template('AddCart.html', data=data)


@app.route("/addcart", methods=['GET', 'POST'])
def addcart():
    if request.method == 'POST':
        from datetime import datetime

        # dates in string format
        str_d1 = request.form['sdate']
        str_d2 = request.form['edate']

        # convert string to date object
        d1 = datetime.strptime(str_d1, "%Y-%m-%d")
        d2 = datetime.strptime(str_d2, "%Y-%m-%d")

        delta = d2 - d1
        print(f'Difference is {delta.days} days')

        import datetime
        date = datetime.datetime.now().strftime('%Y-%m-%d')
        pid = session['pid']
        uname = session['uname']

        file = request.files['file']
        file.save("static/upload/" + file.filename)

        file1 = request.files['file1']
        file1.save("static/upload/" + file1.filename)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cursor = conn.cursor()
        cursor.execute("SELECT  *  FROM protb  where  id='" + pid + "'")
        data = cursor.fetchone()

        if data:
            VehicleNo = data[1]
            price = data[8]

            Image = data[10]
            dname = data[11]

        else:
            return 'No Record Found!'

        tamount = float(price) * float(delta.days)

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute(
            "SELECT *  FROM  booktb where VehicleNo='"+ VehicleNo +"' and  '" + str_d1 + "' between   SDate  and  Edate  ")
        data2 = cur.fetchone()
        if data2:
            flash('Already Book this  Date')

            id = session['pid']
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM protb  where id='" + id + "' ")
            data = cur.fetchall()
            return render_template('AddCart.html', data=data)
        else:
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
            cursor = conn.cursor()
            cursor.execute("SELECT  *  FROM ownertb  where  username='" + dname + "'")
            data1 = cursor.fetchone()

            if data1:

                mob = data1[3]
                sendmsg(mob,"Car Booked");


            else:
                return 'No Record Found!'




            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO  booktb VALUES ('','" + uname + "','" + VehicleNo + "','" + str(
                    tamount) + "','" + date + "','" + Image
                + "','" + str_d1 + "','" + str_d2 + "','" + file.filename + "','" + file1.filename + "','" + dname + "','waiting')")
            conn.commit()
            conn.close()
            flash('Booking  Successfully')
            conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
            cur = conn.cursor()
            cur.execute("SELECT * FROM  booktb  where username='" + uname + "' ")
            data = cur.fetchall()
            return render_template('UserBook.html', data=data)




def sendmsg(targetno,message):
    import requests
    requests.post("http://smsserver9.creativepoint.in/api.php?username=fantasy&password=596692&to=" + targetno + "&from=FSSMSS&message=Dear user  your msg is " + message + " Sent By FSMSG FSSMSS&PEID=1501563800000030506&templateid=1507162882948811640")



@app.route("/Verification")
def Verification():
    id = request.args.get('id')
    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM protb where  id ='" + id + "'")
    data2 = cursor.fetchone()
    if data2:
        aadhar = data2[9]
        return send_file('static/upload/' + aadhar, as_attachment=True)


@app.route("/BookInfo")
def BookInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status !='waiting'")
    data1 = cur.fetchall()

    return render_template('UserBook.html', data=data, data1=data1)

@app.route("/PayAmount")
def PayAmount():
    id = request.args.get('id')
    session['bid'] = id
    st = request.args.get('st')
    print(st)
    if st =="Accept":
        return render_template('Payment.html')
    elif st =="Reject":
        flash("Reject")
        uname = session['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status='waiting'")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status !='waiting'")
        data1 = cur.fetchall()

        return render_template('UserBook.html', data=data, data1=data1)
    elif st == "paid":
        flash("Already Pay Amount")
        uname = session['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status='waiting'")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status !='waiting'")
        data1 = cur.fetchall()

        return render_template('UserBook.html', data=data, data1=data1)


@app.route("/pay", methods=['GET', 'POST'])
def pay():
    if request.method == 'POST':
        id = session['bid']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cursor = conn.cursor()
        cursor.execute(
            "update   booktb set status='paid' where id='" + id + "'")
        conn.commit()
        conn.close()

        uname = session['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status='waiting'")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status !='waiting'")
        data1 = cur.fetchall()

        return render_template('UserBook.html', data=data, data1=data1)


@app.route("/Agreement")
def Agreement():
    id = request.args.get('id')
    session['bid'] = id
    st = request.args.get('st')
    print(st)
    if st =="Accept":
        flash("Waiting For  Payment")
        return render_template('Payment.html')
    elif st =="Reject":
        flash("Reject")
        uname = session['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status='waiting'")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status !='waiting'")
        data1 = cur.fetchall()

        return render_template('UserBook.html', data=data, data1=data1)
    elif st == "paid":
        from datetime import datetime
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where id='" + id + "'")
        data2 = cur.fetchone()
        if data2:
            oname = data2[10]
            uname =  data2[1]
            vno = data2[2]
            sdate =  data2[6]
            edate   =  data2[7]

            str_d1 = str(sdate)
            str_d2 = str(edate)

            # convert string to date object
            d1 = datetime.strptime(str_d1, "%Y-%m-%d")
            d2 = datetime.strptime(str_d2, "%Y-%m-%d")

            delta = d2 - d1
            print(f'Difference is {delta.days} days')
            date = delta.days

        return render_template('Agreement.html', oname=oname,uname=uname,vno=vno,date= date)




@app.route("/Query")
def Query():
    id = request.args.get('id')
    session['bid'] = id
    st = request.args.get('st')
    print(st)
    if st =="Accept":
        flash("Waiting For  Payment")
        return render_template('Payment.html')
    elif st =="Reject":
        flash("Reject")
        uname = session['uname']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status='waiting'")
        data = cur.fetchall()

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where username='" + uname + "' and Status !='waiting'")
        data1 = cur.fetchall()

        return render_template('UserBook.html', data=data, data1=data1)
    elif st == "paid":
        from datetime import datetime
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cur = conn.cursor()
        cur.execute("SELECT * FROM  booktb where id='" + id + "'")
        data2 = cur.fetchone()
        if data2:
            session['oname'] = data2[10]
            session['uname'] =  data2[1]
        return render_template('Query.html')







@app.route("/newquery", methods=['GET', 'POST'])
def newquery():
    if request.method == 'POST':
        query = request.form['query']
        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO Querytb VALUES ('','"+ session['uname'] +"','" + session['oname'] + "','" + query + "','','waiting')")
        conn.commit()
        conn.close()
        flash('Query Enter successfully')
        return render_template('Query.html')
@app.route("/Answer")
def Answer():
    session['qid'] = request.args.get('id')
    return render_template('Answer.html')




@app.route("/answ", methods=['GET', 'POST'])
def answ():
    if request.method == 'POST':
        query = request.form['query']
        id = session['qid']

        conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
        cursor = conn.cursor()
        cursor.execute(
            "update   Querytb set Answer='"+ query  +"',status='Answer' where id='" + id + "'")
        conn.commit()
        conn.close()
        flash('Query Answer Info Update successfully')
        return render_template('Answer.html')

@app.route("/UQueryInfo")
def UQueryInfo():
    uname = session['uname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Querytb where username='" + uname + "' ")
    data = cur.fetchall()



    return render_template('UQueryInfo.html', data=data)



@app.route("/DQueryInfo")
def DQueryInfo():
    uname = session['dname']

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Querytb where ownername='" + uname + "' and Status='waiting'")
    data = cur.fetchall()

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cur = conn.cursor()
    cur.execute("SELECT * FROM  Querytb where ownername='" + uname + "' and Status!='waiting'")
    data1 = cur.fetchall()



    return render_template('DQueryInfo.html', data=data,data1=data1)



@app.route("/ViewLocation")
def ViewLocation():
    id = request.args.get('id')

    conn = mysql.connector.connect(user='root', password='', host='localhost', database='2carrentaldb')
    cursor = conn.cursor()
    cursor.execute("SELECT  *  FROM protb  where  id='" + id + "'")
    data1 = cursor.fetchone()

    if data1:
        lat = data1[13]
        lon = data1[14]

    else:
        return 'No Record Found!'

    return render_template('map.html', lat=lat,lon=lon)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
