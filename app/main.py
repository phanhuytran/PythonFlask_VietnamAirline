from app import app, login
from flask import render_template, request, url_for, flash
from app.admin import *
from flask_login import login_user
import os
from app.utils import *


@app.route("/login", methods=['POST', 'GET'])
def login_staff():
    message = ""
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password', '')
        password = hashlib.md5(password.encode('utf-8')).hexdigest()

        user = get_account(username=username,password=password)

        if user:
            acc = Account.query.filter(Account.id == user.id).first()
            if user.user_role:
                login_user(user=acc)
            else:
                message = 'Username or password incorrect'
                render_template('login.html', message=message)
        else:
            message = 'Username or password incorrect'
            return render_template('login.html', message=message)
    elif request.method == 'GET':
        return render_template('login.html')

    return redirect(url_for('search_flight_staff'))


@app.route('/staff/search-flight', methods=['POST', 'GET'])
def search_flight_staff():
    airports = get_all_airport()
    schedules = get_all_schedule()

    enumerate_schedules = enumerate(schedules)
    count_result = len(schedules)

    flight = None

    if request.form.get('btn') == "SEARCH":
        if request.method == 'POST':
            departure = request.form.get('from_locate')
            arrival = request.form.get('to_locate')
            date_flight = request.form.get('date_flight')
            if departure == "Flight from..." or departure is None and arrival == 'Flight to...' or departure is None and date_flight is None:
                schedules = get_all_schedule()
            else:
                schedules = search_schedule(arrival_locate=arrival, departure_locate=departure, date=date_flight)
            enumerate_schedules = enumerate(schedules)
            count_result = len(schedules)
            if schedules:
                return render_template("staff/search-flight.html", airports=airports,
                                       enumerate_schedules=enumerate_schedules, count_result=count_result)
            else:
                return render_template("staff/search-flight.html", airports=airports)

    if request.form.get('btn') not in ["RESET", "ORDER TICKET NOW", "SEARCH"]:
        if request.method == "POST":
            id_flight = request.form.get('btn')
            seats = get_seats_by_id_flight(id_flight=id_flight)
            enumerate_seat = enumerate(seats)
            flight = get_flight_by_id(idFlight=id_flight)

            return render_template("staff/search-flight.html", airports=airports,
                                   enumerate_schedules=enumerate_schedules, enumerate_seat=enumerate_seat,
                                   count_result=count_result, seats=seats, flight=flight, scroll="section_ticket")

    if request.form.get('btn') == "ORDER TICKET NOW":
        if request.method == 'POST':
            mess_err = ''
            id_flight = request.form.get('id_flight')

            if not id_flight:
                mess_err = 'Please choose flight in above'
                return render_template("staff/search-flight.html", airports=airports,
                                       enumerate_schedules=enumerate_schedules,
                                       count_result=count_result, scroll='section_ticket', mess_err=mess_err)
            else:
                if not get_flight_by_id(idFlight=id_flight):
                    mess_err='mã chuyến bay ko hợp lệ'
                    return render_template("staff/search-flight.html", airports=airports,
                                           enumerate_schedules=enumerate_schedules,
                                           count_result=count_result, scroll='section_ticket', mess_err=mess_err)

            id_user = current_user.id
            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            phone = request.form.get('phone')
            email = request.form.get('email')
            identity_card = request.form.get('identity_card')
            seat_location = request.form.get('seat')
            id_seat = get_id_seat(id_flight=id_flight,seat_location=seat_location)

            if not get_customer(firstname=first_name, lastname=last_name,identity_card=identity_card):

                if not add_customer(firstname=first_name, lastname=last_name,
                                    identity_card=identity_card, phone=phone, email=email):
                    mess_err = " system error"
                    return render_template("staff/search-flight.html", airports=airports,
                               enumerate_schedules=enumerate_schedules,
                               count_result=count_result,scroll='section_ticket', mess_err=mess_err)

            customer = get_customer(firstname=first_name, lastname=last_name, identity_card=identity_card)
            if update_ticket_for_Staff(id_flight=id_flight,id_customer=customer.id,id_staff=current_user.staff.id,id_seat=id_seat):
                mess_err=  '''Successful booking, please go to Booking Status to see a list of tickets booked'''
                return  render_template("staff/search-flight.html", airports=airports,
                               enumerate_schedules=enumerate_schedules,
                               count_result=count_result,scroll='section_ticket', mess_err=mess_err)
    if current_user.is_authenticated:
        return render_template("staff/search-flight.html", airports=airports,
                               enumerate_schedules=enumerate_schedules,
                               count_result=count_result, flight=flight)
    else:
        return render_template("login.html")


@app.route('/logout')
def logout_usr():
    logout_user()
    return redirect(url_for('search_flight_staff'))


@app.route("/")
def index():
    return redirect(url_for("search_flight"))


@app.route("/staff")
def index_staff():
    if current_user.is_authenticated:
        return redirect(url_for("search_flight_staff"))
    else:
        return redirect(url_for("login_staff"))


@login.user_loader
def load_user(user_id):
    return Account.query.get(user_id)


@app.route("/login-admin", methods=['GET', 'POST'])
def login_admin():
    message = ''
    if request.method == 'POST':
        username = request.form.get("username")
        password = request.form.get("password")
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())
        user = get_account(username=username,password=password)

        if user:
            acc = Account.query.filter(Account.id == user.id).first()
            if user.user_role == UserRole.ADMIN:
                login_user(user=acc)
            else:
                message = 'Username or password incorrect'
                return MyView().render('admin/index.html', message=message)
        else:
            message = 'Username or password incorrect'
            return MyView().render('admin/index.html', message=message)
    return redirect("/admin")


@app.route("/registration", methods=['GET', 'POST'])
def register():
    message = ''
    if request.method == 'POST':
        id_staff = request.form.get('id-staff')
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        avatar = request.files["avatar"]
        avatar_path = 'img/upload/%s' % avatar.filename
        avatar.save(os.path.join(app.config['ROOT_PROJECT_PATH'], 'static/', avatar_path))

        if password != confirm_password:
            message = "Password confirm incorrect"

        elif check_account(key=username):
            message = "Username already exists"

        elif check_staff(id_staff=id_staff) == False:
            message = 'Id staff not already exists'

        elif check_account(key=id_staff):
            message = 'Id staff has been registered by someone else'

        elif add_account(id_staff=id_staff,
                            username=username, password=password):
                    return redirect(url_for("login_staff"))
    return render_template('admin/registration.html', message=message)


@app.route("/search-flight", methods=['POST','GET'])
def search_flight():
    airports = get_all_airport()
    schedules = get_all_schedule()

    enumerate_schedules = enumerate(schedules)
    count_result = len(schedules)

    flight = None

    if request.form.get('btn') == "SEARCH":
        if request.method == 'POST':
            departure = request.form.get('from_locate')
            arrival = request.form.get('to_locate')
            date_flight = request.form.get('date_flight')
            if departure == "Flight from..." or departure is None and arrival == 'Flight to...' or departure is None and date_flight is None:
                schedules = get_all_schedule()
            else:
                schedules = search_schedule(arrival_locate=arrival, departure_locate=departure, date=date_flight)
            enumerate_schedules = enumerate(schedules)
            count_result = len(schedules)
            if schedules:
                return render_template("search-flight.html", airports=airports,
                                       enumerate_schedules=enumerate_schedules, count_result=count_result)
            else:
                return render_template("search-flight.html", airports=airports)

    if request.form.get('btn') not in ["RESET", "ORDER TICKET NOW", "SEARCH"]:
        if request.method == "POST":
            id_flight = request.form.get('btn')
            seats = get_seats_by_id_flight(id_flight=id_flight)
            enumerate_seat = enumerate(seats)
            flight = get_flight_by_id(idFlight=id_flight)

            return render_template("search-flight.html", airports=airports,
                                   enumerate_schedules=enumerate_schedules, enumerate_seat=enumerate_seat,
                                   count_result=count_result, seats=seats, flight=flight, scroll="section_ticket")

    if request.form.get('btn') == "ORDER TICKET NOW":
        if request.method == 'POST':
            mess_err = ''
            id_flight = request.form.get('id_flight')

            if not id_flight:
                mess_err = 'Please choose flight in above'
                return render_template("search-flight.html", airports=airports,
                                       enumerate_schedules=enumerate_schedules,
                                       count_result=count_result, scroll='section_ticket', mess_err=mess_err)
            else:
                if not get_flight_by_id(idFlight=id_flight):
                    mess_err = 'mã chuyến bay ko hợp lệ'
                    return render_template("search-flight.html", airports=airports,
                                           enumerate_schedules=enumerate_schedules,
                                           count_result=count_result, scroll='section_ticket', mess_err=mess_err)

            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            phone = request.form.get('phone')
            email = request.form.get('email')
            identity_card = request.form.get('identity_card')
            seat_location = request.form.get('seat')
            id_seat = get_id_seat(id_flight=id_flight, seat_location=seat_location)

            if not get_customer(firstname=first_name, lastname=last_name, identity_card=identity_card):

                if not add_customer(firstname=first_name, lastname=last_name,
                                    identity_card=identity_card, phone=phone, email=email):
                    mess_err = " system error"
                    return render_template("search-flight.html", airports=airports,
                                           enumerate_schedules=enumerate_schedules,
                                           count_result=count_result, scroll='section_ticket', mess_err=mess_err)

            customer = get_customer(firstname=first_name, lastname=last_name, identity_card=identity_card)
            if update_ticket_for_customer(id_flight=id_flight, id_customer=customer.id,
                             id_seat=id_seat):
                mess_err = '''Successful booking, please go to Booking Status to see a list of tickets booked'''
                return render_template("search-flight.html", airports=airports,
                                       enumerate_schedules=enumerate_schedules,
                                       count_result=count_result, scroll='section_ticket', mess_err=mess_err)

    return render_template("search-flight.html", airports=airports,
                           enumerate_schedules=enumerate_schedules,
                           count_result=count_result, flight=flight)


@app.route("/staff/check-booking-status",methods=['POST', 'GET'])
def check_booking_status_staff():
    if current_user.is_authenticated:
        tickets = get_ticket_by_id_account(current_user.staff.id)
        id_tickets = [t.idTicket for t in tickets]
        list_ticket_info = [get_ticket_by_id_ticket(id) for id in id_tickets]
        zip_ticket_info = zip(tickets, list_ticket_info)
        mess_err = ''
        if request.method == 'POST':
            if request.form.get('confirm'):
                id_ticket = request.form.get('confirm')
                if update_ticket(id_ticket=id_ticket, id_account=current_user.id):
                    mess_err = 'Confirm successfully'
                else:
                    mess_err = 'Confirm unsuccessfully'
                return render_template("staff/check-booking-status.html",
                                       zip_ticket_info=zip_ticket_info, mess_err=mess_err)

            if request.form.get('delete'):
                id_ticket = request.form.get('delete')
                if update_ticket(id_ticket=id_ticket,id_account=current_user.id, confirm=False):
                    mess_err = 'Delete successfully'
                else:
                    mess_err = 'Delete unsuccessfully'
                return render_template("staff/check-booking-status.html",
                                       zip_ticket_info=zip_ticket_info, mess_err=mess_err)

        if request.method == 'GET':
                return render_template("staff/check-booking-status.html", zip_ticket_info=zip_ticket_info)


    else:
        return render_template("error-404.html")


@app.route("/check-booking-status", methods=['POST', 'GET'])
def check_booking_status():
    if request.method == 'POST':
        firstname = request.form.get('first_name')
        lastname = request.form.get('last_name')
        identity_card = request.form.get('identity_card')
        phone = request.form.get('phone')

        id_customer = get_id_cusomer(firstname=firstname, lastname=lastname, identity_card=identity_card, phone=phone)
        list_id_tickets = get_list_id_ticket_by_id_customer(id_customer)

        list_ticket = [get_ticket_by_id_ticket(item) for item in list_id_tickets]



        return render_template('check-booking-status.html', list_ticket=list_ticket)



    return render_template("check-booking-status.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/revenue-month",methods=['POST', 'GET'])
def revenue_month():
    if current_user.is_authenticated and current_user.username == 'nguyentrong':
        if request.method == 'POST':
            month = request.form.get('month')
            year =request.form.get('year')
            tick = report_by_month(month=month, year=year)
            enum_tick =enumerate(tick)
            list_doanh_thu = [t.count_ticket * t.price for t in tick]
            list_id_flight = [str(t.idFlight) for t in tick]
            print(list_id_flight)
            sum = 0
            for i in list_doanh_thu:
                sum += i

            list_rate = [t/sum*100 for t in list_doanh_thu]

            return render_template("revenue-month.html",enum_tick=enum_tick,
                               list_doanh_thu=list_doanh_thu,sum=sum,list_rate=list_rate,list_id_flight=list_id_flight)

        return render_template('revenue-month.html')
    elif current_user.is_authenticated and current_user.username != 'nguyentrong' or not(current_user.is_authenticated):
        return render_template("error-404.html")


@app.route("/revenue-year")
def revenue_year():
    if current_user.is_authenticated and current_user.username == 'nguyentrong':
        return render_template("revenue-year.html")
    elif current_user.is_authenticated and current_user.username != 'nguyentrong' or not(current_user.is_authenticated):
        return render_template("error-404.html")


if __name__ == "__main__":
    app.run(debug=True)