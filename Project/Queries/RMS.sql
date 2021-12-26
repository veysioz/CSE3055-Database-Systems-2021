USE RESTAURANT_MANAGEMENT_SYSTEM
create table Menu(
menuID int primary key not null,
menuType varchar(20)
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Category(
categoryID int primary key not null identity(1,1),
menuID int foreign key references Menu(menuID),
categoryName varchar(20)
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Item(
itemID int primary key not null identity(1,1),
categoryID int foreign key references Category(categoryID) not null,
itemName varchar(30) not null,
itemDescription varchar(50) not null,
itemPrice float not null
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Recipe(
recipeID int primary key not null,
itemID int foreign key references Item(itemID) not null,
recipeName varchar(20) not null,
instruction varchar(250)
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Supplier(
supplierID smallint primary key not null,
supplierName varchar(30) not null,
supplierAddress varchar(120)
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table SupplierPhoneNum(
supplierID smallint foreign key references Supplier(supplierID),
phoneNumber char(15) unique
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Stock(
stockNo smallint primary key not null,
supplierID smallint foreign key references Supplier(supplierID),
stockName varchar(20) not null unique,
stockAmount_kg int not null,
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Customer(
customerID int primary key not null identity(1,1),
firstName varchar(30),
lastName varchar(30),
customerAddress varchar(120)
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Customer_Phone_Num(
customerID int foreign key references Customer(customerID),
phoneNumber char(15) unique
);
create index customer_phone_num_idx on Customer_Phone_Num(phoneNumber)

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Position(
positionID int primary key not null,
positionName varchar(30) unique
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Employee(
employeeID int primary key not null,
positionID int foreign key references Position(positionID),
firstName varchar(20),
lastName varchar(20),
birthDate date,
age smallint,
EmployeeAddr varchar(120) default 'Istanbul',
salary int check(salary>=2825)
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table EmployeePhoneNumber(
employeeID int foreign key references Employee(employeeID) not null,
phoneNumber char(15) unique
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table ServiceType(
serviceTypeID smallint primary key not null,
serviceTypeName varchar(50) not null,
serviceDescription varchar(100) not null
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table EmployeeForServiceType(
employeeID int foreign key references Employee(employeeID),
serviceTypeID smallint foreign key references ServiceType(serviceTypeID)
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Section(
sectionNo smallint primary key not null,
sectionName varchar(20) not null unique
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Booking(
bookingID smallint primary key not null,
bookingDate datetime unique,
personAmount smallint not null
);

alter table Booking add tableID smallint foreign key references RestaurantTable(tableID)

USE RESTAURANT_MANAGEMENT_SYSTEM
create table RestaurantTable(
tableID smallint primary key not null identity(1,1),
sectionNo smallint foreign key references Section(sectionNO),
chairNum smallint
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table FoodOrder(
orderID int primary key not null,
tableID smallint foreign key references RestaurantTable(tableID),
orderDate datetime
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table ItemOrder(
itemID int foreign key references Item(itemID),
orderID int foreign key references FoodOrder(orderID),
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table FoodTransaction(
transactionID int primary key not null,
orderID int foreign key references FoodOrder(orderID),
customerFName varchar(25),
customerLName varchar(25),
deliveryStatus varchar(20),
deliveryDate datetime,
);

USE RESTAURANT_MANAGEMENT_SYSTEM
create table Bill(
billID int primary key not null,
orderID int foreign key references FoodOrder(orderID),
billDate date,
totalAmount int,
);
alter table Bill add paymentID smallint foreign key references PaymentMethod(paymentID)

USE RESTAURANT_MANAGEMENT_SYSTEM
create table PaymentMethod(
paymentID smallint primary key not null,
paymentType varchar(25),
);


