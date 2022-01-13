import datetime

import pyodbc
from flask import Flask, render_template, flash, request, session, redirect, url_for, get_flashed_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
conn = pyodbc.connect('''Driver={SQL Server};
                      Server=localhost\sqlexpress;
                      Database=RESTAURANT_MANAGEMENT_SYSTEM;
                      Trusted_Connection=yes;''')

cursor = conn.cursor()


#####################################################################################

# Customer page #
def customer_query():
    query = "SELECT c.customerID AS 'ID', c.firstName AS 'Name', c.lastName AS 'Surname', c.customerAddress AS 'Address' FROM Customer c"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/customer', methods=('GET', 'POST'))
def customer():
    records, columns = customer_query()
    if request.method == 'POST':
        if request.form['button'] == 'add':
            customer_id = records[-1][0] + 1
            first_name = request.form['firstName']
            last_name = request.form['lastName']
            address = request.form['address']
            if first_name == '' or last_name == '' or address == '':
                session.pop('_flashes', None)
                flash("First Name, Last Name and Address can not be empty!!")
                return redirect(url_for('customer'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC new_customer @customerID ={customer_id}, @firstName={first_name}, @lastName={last_name}, @customerAddress={address} '
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('customer'))
        else:
            customer_id = request.form['ID']
            if customer_id == '':
                session.pop('_flashes', None)
                flash("ID can not be empty!!")
                return redirect(url_for('customer'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC delete_customer @customerID ={customer_id}'
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('customer'))

    return render_template("customer.html", data=records, column_data=columns)


#####################################################################################

# Customer Phone Number Page #
def customer_phone_number_query():
    query = "SELECT Customer.customerID AS 'ID', firstName AS 'Name', lastName AS 'Surname', phoneNumber AS 'Phone' FROM Customer_Phone_Num, Customer WHERE Customer.customerID = Customer_Phone_Num.customerID"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/customerphonenum', methods=('GET', 'POST'))
def customer_phone_num():
    records, columns = customer_phone_number_query()
    if request.method == 'POST':
        customer_id = request.form['ID']
        customer_phone_number = request.form['phoneNumber']
        if customer_id == '' or customer_phone_number == '':
            session.pop('_flashes', None)
            flash("empty!!")
            return redirect(url_for('customer_phone_num'))
        else:
            session.pop('_flashes', None)
            procedure = f'EXEC new_customer_phone_num @customerID ={customer_id}, @phoneNumber={customer_phone_number}'
            cursor.execute(procedure)
            cursor.commit()
            flash('Successful!!')
            return redirect(url_for('customer_phone_num'))

    return render_template("customerphone.html", data=records, column_data=columns)


#####################################################################################

# Supplier Phone Number Page #

def supplier_phone_number_query():
    query = "SELECT s.supplierID AS 'ID', s.supplierName AS 'Supplier Name', sp.phoneNumber AS 'Phone' FROM SupplierPhoneNum sp, Supplier s WHERE s.supplierID = sp.supplierID"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/supplierphonenum', methods=['GET', 'POST'])
def supplier_phone_num():
    records, columns = supplier_phone_number_query()
    if request.method == 'POST':
        if request.form['button'] == 'add':
            supplier_id = request.form['ID']
            supplier_phone = request.form['phone']
            if supplier_id == '' or supplier_phone == '':
                session.pop('_flashes', None)
                flash("ID and phone number can not be empty!!")
                return redirect(url_for('supplier_phone_num'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC new_supplier_phone_num @supplierID ={supplier_id}, @phoneNumber={supplier_phone}'
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('supplier_phone_num'))

    return render_template("supplierphonenum.html", data=records, column_data=columns)


#####################################################################################

# Supplier Page #

def supplier_query():
    query = "SELECT s.supplierID AS 'ID', s.supplierName AS 'Supplier Name', s.supplierAddress AS 'Address' FROM Supplier s"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/supplier', methods=('GET', 'POST'))
def supplier():
    records, columns = supplier_query()
    if request.method == 'POST':
        if request.form['button'] == 'add':
            supplier_id = records[-1][0] + 1
            supplier_name = request.form['name']
            supplier_address = request.form['address']
            if supplier_name == '' or supplier_address == '':
                session.pop('_flashes', None)
                flash("Name and Address can not be empty!!")
                return redirect(url_for('supplier'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC new_supplier @supplierID ={supplier_id}, @supplierName={supplier_name}, @supplierAddress={supplier_address} '
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('supplier'))
        else:
            supplier_id = request.form['ID']
            if supplier_id == '':
                session.pop('_flashes', None)
                flash("ID can not be empty!!")
                return redirect(url_for('supplier'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC delete_supplier @supplierID ={supplier_id}'
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('supplier'))

    return render_template("supplier.html", data=records, column_data=columns)


#####################################################################################

# Item Page #

def item_query():
    query = "SELECT i.itemID as ID, c.categoryName as 'Category', i.itemName as 'Name', i.itemDescription as 'Description',i.itemPrice as 'Price' FROM Item i, Category c WHERE i.categoryID=c.categoryID"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/item', methods=('GET', 'POST'))
def item():
    records, columns = item_query()
    if request.method == 'POST':
        if request.form['button'] == 'add':
            item_id = request.form['itemID']
            item_price = request.form['price']
            if item_id == '' or item_price == '':
                session.pop('_flashes', None)
                flash("ID and Price can not be empty!!")
                return redirect(url_for('item'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC update_item_price @itemID ={item_id}, @new_item_price ={item_price}'
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('item'))

    return render_template("item.html", data=records, column_data=columns)


#####################################################################################

# Item Order Page #

def item_order_query():
    query = "SELECT i.itemID as ID, i.itemName as 'Item Name', i2.orderID 'OrderID', i.itemPrice as 'Price' FROM Item i, ItemOrder i2 WHERE i.itemID = i2.itemID"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/itemorder', methods=('GET', 'POST'))
def item_order():
    records, columns = item_order_query()
    if request.method == 'POST':
        if request.form['button'] == 'add':
            item_id = request.form["itemID"]
            order_id = request.form["orderID"]
            if item_id == '' or order_id == '':
                session.pop('_flashes', None)
                flash("Item ID and Order ID can not be empty!!")
                return redirect(url_for('item_order'))
            else:
                query = "SELECT * FROM FoodOrder"
                cursor.execute(query)
                records = cursor.fetchall()
                if int(order_id) > records[-1][0] or int(order_id) < 0:
                    session.pop('_flashes', None)
                    flash('Order not found!!')
                    return redirect(url_for('item_order'))
                else:
                    session.pop('_flashes', None)
                    procedure = f'EXEC new_order @itemID={item_id}, @orderID={order_id}'
                    cursor.execute(procedure)
                    cursor.commit()
                    flash('Successful!!')
                    return redirect(url_for('item_order'))

    return render_template("itemorder.html", data=records, column_data=columns)


#####################################################################################

# Recipe Page #

def recipe_query():
    query = "SELECT r.recipeID AS 'ID', r.recipeName AS 'Name', r.instruction AS 'Instruction' FROM Recipe r"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/recipe')
def recipe():
    records, columns = recipe_query()
    return render_template("recipe.html", data=records, column_data=columns)


#####################################################################################

# Employee Page #
def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def employee_query():
    query = "SELECT e.employeeID AS 'ID', e.positionID AS 'PositionID', e.firstName AS 'Name', e.lastName AS 'Surname', e.birthDate AS 'Birthdate', e.age AS 'Age', e.EmployeeAddr AS 'Address', e.salary AS 'Salary' FROM Employee e"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/employee', methods=('GET', 'POST'))
def employee():
    records, columns = employee_query()
    if request.method == 'POST':
        if request.form['button'] == 'add':
            employee_id = records[-1][0] + 1
            position_id = request.form['positionID']
            first_name = request.form['firstName']
            last_name = request.form['lastName']
            birthdate = request.form['birthDate']
            address = request.form['address']
            salary = request.form['salary']
            born = datetime.datetime.strptime(birthdate, '%d-%m-%Y')
            age = calculate_age(born)
            if position_id == '' or first_name == '' or last_name == '' or birthdate == '' or address == '' or salary == '':
                session.pop('_flashes', None)
                flash("Position ID, First Name, Last Name, Birthdate, Address and Salary can not be empty!!")
                return redirect(url_for('employee'))
            elif int(salary) < 2825:
                session.pop('_flashes', None)
                flash("Salary can not be lower than minimum wage!!")
                return redirect(url_for('employee'))
            elif age < 18:
                session.pop('_flashes', None)
                flash("Age can not be lower than 18!!")
                return redirect(url_for('employee'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC new_employee @employeeID ={employee_id}, @positionID={position_id}, @firstName={first_name}' \
                            f', @lastName={last_name}, @birthDate=\'{birthdate}\', @EmployeeAddr={address},' \
                            f' @salary={salary} '
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('employee'))
        else:
            employee_id = request.form['employeeID']
            if employee_id == '':
                session.pop('_flashes', None)
                flash("ID can not be empty!!")
                return redirect(url_for('employee'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC delete_employee @employeeID ={employee_id}'
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('employee'))

    return render_template("employee.html", data=records, column_data=columns)


#####################################################################################

# Booking Page #

def booking_query():
    query = "SELECT b.bookingID AS 'ID', b.bookingDate AS 'Date', b.personAmount AS 'Number of People', b.tableID AS 'Table ID'  FROM Booking b"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/booking', methods=('GET', 'POST'))
def booking():
    records, columns = booking_query()
    if request.method == 'POST':
        if request.form['button'] == 'add':
            booking_id = records[-1][0] + 1
            person_amount = request.form['personAmount']
            table_id = request.form['tableID']
            if person_amount == '' or table_id == '':
                session.pop('_flashes', None)
                flash("Person Amount and Table ID can not be empty!!")
                return redirect(url_for('booking'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC new_booking @bookingID ={booking_id}, @personAmount={person_amount}, @tableID={table_id}'
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('booking'))
        else:
            booking_id = request.form['ID']
            if booking_id == '':
                session.pop('_flashes', None)
                flash("ID can not be empty!!")
                return redirect(url_for('booking'))
            else:
                query = "SELECT * FROM RestaurantTable"
                cursor.execute(query)
                records = cursor.fetchall()
                if int(booking_id) > records[-1][0] or int(booking_id) < 0:
                    session.pop('_flashes', None)
                    flash('Table not found!!')
                    return redirect(url_for('booking'))
                else:
                    session.pop('_flashes', None)
                    procedure = f'EXEC delete_booking @bookingID ={booking_id}'
                    cursor.execute(procedure)
                    cursor.commit()
                    flash('Successful!!')
                    return redirect(url_for('booking'))

    return render_template("booking.html", data=records, column_data=columns)


#####################################################################################

# Food Transaction Page #

def food_transaction_query():
    query = "SELECT f.transactionID AS 'ID', f.orderID AS 'Order ID', f.customerFName AS 'Name', f.customerLName AS 'Surname', f.deliveryStatus AS 'Status', f.deliveryDate AS 'Delivery Date' FROM FoodTransaction f"
    cursor.execute(query)
    records = cursor.fetchall()
    columns = [column[0] for column in cursor.description]
    return records, columns


@app.route('/foodtransaction', methods=['GET', 'POST'])
def food_transaction():
    print(get_flashed_messages())
    records, columns = food_transaction_query()
    if request.method == 'POST':
        if request.form['button'] == 'add':
            query = "SELECT * FROM FoodOrder"
            cursor.execute(query)
            temp_records = cursor.fetchall()
            transaction_id = records[-1][0] + 1
            order_id = request.form['orderID']
            first_name = request.form['customerName']
            last_name = request.form['customerLastName']

            if order_id == '' or first_name == '' or last_name == '':
                session.pop('_flashes', None)
                flash("Order ID, First Name and Last Name can not be empty!!")
                return redirect(url_for('food_transaction'))

            elif int(order_id) > temp_records[-1][0] or int(order_id) < 0:
                session.pop('_flashes', None)
                flash('Order not found!!')
                return redirect(url_for('food_transaction'))

            else:
                session.pop('_flashes', None)
                procedure = f'EXEC new_delivery @transactionID ={transaction_id}, @orderID={order_id}, @customerFname={first_name}, @customerLName={last_name}'
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('food_transaction'))

        elif request.form['button'] == 'updateOnTheWay':
            transaction_id = request.form['transactionID']
            if transaction_id == '':
                session.pop('_flashes', None)
                flash("ID can not be empty!!")
                return redirect(url_for('food_transaction'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC delivery_ontheway @transactionID ={transaction_id}'
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('food_transaction'))

        elif request.form['button'] == 'updateDelivered':
            transaction_id = request.form['transactionID']
            if transaction_id == '':
                session.pop('_flashes', None)
                flash("ID can not be empty!!")
                return redirect(url_for('food_transaction'))
            else:
                session.pop('_flashes', None)
                procedure = f'EXEC delivered @transactionID ={transaction_id}'
                cursor.execute(procedure)
                cursor.commit()
                flash('Successful!!')
                return redirect(url_for('food_transaction'))

        else:
            session.pop('_flashes', None)
            procedure = f'EXEC delete_delivered_orders'
            cursor.execute(procedure)
            cursor.commit()
            flash('Successful!!')
            return redirect(url_for('food_transaction'))

    return render_template("foodtransaction.html", data=records, column_data=columns)


#####################################################################################


@app.route('/')
def index():  # put application's code here
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
