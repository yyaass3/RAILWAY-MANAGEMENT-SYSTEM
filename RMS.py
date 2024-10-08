# Railway Management System


# database connection
import mysql.connector as sql
from random import randint
print('enter the details of your mysql server: ')
x = input('host name:')
y = input('user:')
z = input('password:')
con = sql.connect(host = x, user = y, password = z)
con.autocommit = True
cur = con.cursor()


# database creation
cur.execute('create database IRCTC;')
cur.execute('use IRCTC;')
cur.execute('create table accounts (id int primary key, pass varchar(16), name varchar(100), sex char(1), age varchar(100), dob date, ph_no char(10));')
cur.execute('create table tickets(id int primary key, pnr int, train varchar(25), doj date, tfr varchar(100), tto varchar(100));')


# login menu creation
def login_menu():
  print('welcome to the IRCTC portal')
  print('1.create new account \n'
        '2.login \n'
        '3.exit')
  opt = int(input('enter your choice:'))
  if opt == 1:
    create_acc()
  elif opt == 2:
    login()
  else:
    e = input('exit the portal? (Y/N)')
    if e.upper == 'N':
      login_menu()
    else:
      exit()


# account creation
def create_acc():
  print('enter the detailes to create your account:')
  i = randint(1000, 10000)
  print(f'your generated ID is: {i}')
  p = input('enter your password: ')
  n = input('enter your name: ')
  sex = input('enter your gender(m/f/o): ')
  age = input('enter  your age: ')
  dob = input('enter your date of birth (YYYY-MM-DD): ')
  ph = input('enter your contact number: ')
  cur.execute('insert into accounts values f'({i}, '{p}', '{n}', '{sex.upper}', {age}, '{dob}', '{ph}')';')
  print('now you may log in with your newly created account!')
  login()


# login window
def login():
  global a
  try:
    a = int(input('enter your ID: '))
    b = input('enter your password: ')
    cur.execute(f'select name from account where ID = {a} and pass = '{b}';')
    j = cur.fetchone()
    print(f'welcome back j[0]!')
    main_menu()
  except:
    print('your account was not found')
    print('you can: \n'
          '1.try logging in again \n'
          '2.create new account')
    ch = input('enter your choice: ')
    if ch == '1':
      login()
    elif ch == '2':
      create_acc()
    else:
      print('invalid choice!')
      x1 = input('exit the portal? (Y/N)')
      if x1.upper() == 'N':
        login_menu()
      else:
        exit()


# main menu creation
def main_menu():
  print('what would you like to do today? \n'
        '1.purchase a ticket \n'
        '2.check ticket status \n'
        '3.request a refund \n'
        '4.account settings \n'
        '5.logout \n'
        '6.exit')
  ch1 = int(input('enter your choice: '))
  if ch1 == 1:
    buy_ticket()
  elif ch1 == 2:
    show_ticket()
  elif ch1 == 3:
    cancel_ticket()
  elif ch1 == 4:
    account()
  elif ch1 == 5:
    login_menu()
  else:
    exit()


def back_to_main_menu():
  x3 = input('return to the main menu? (Y/N)')
  if x3.upper() == 'Y':
    print('returning to main menu...')
    main_menu()


#buying ticket
def buy_ticket():
  print('enter details for your journy: ')
  i = a
  pnr = randint(100000, 1000000)
  print(f'your PNR is {pnr}')
  train = input('enter your tarin name: ')
  doj = input('enter the date of your  journy (YYYY-MM-DD): ')
  fr = input('enter the departing station: ')
  to = input('enter the destination station: ')
  cur.execute(f'insert into tickets values({i}, {pnr}, '{train}', '{doj}', '{fr}', '{to}');')
  back_to_main_menu()


# ticket checking
def show_tickets():
  try:
    pnr = int(input('enter your PNR: '))
    cur.execute(f'select * from tickets where pnr = {pnr};')
    j = cur.fetchone()
    if j[0] == a:
      print(f'train {j[2]} \n date of journy {j[3]} \n from {j[4]} \n to {j[5]}')
      back_to_main_menu()
    else:
      print('unauthorized! \n your ID does not match the pnr of ticket.')
      back_to_main_menu()
  except:
    ticket_not_found()


# canceling tickets
def cancel_ticket():
  try:
    pnr = int(input('enter the pnr number of the ticket: '))
    cur.execute(f'select id, pnr, train from tickets where pnr = {pnr};')
    j = cur.fetchone()
    if j[0] == a:
      print(f'pnr: {j[1]} \n train: {j[2]}')
      x4 = input('do you really want to cancel this ticket? (Y/N)')
      if x4.upper == 'Y':
        cur.execute(f'delete * from tickets where pnr = {pnr};')
        print('you will be refunded shortly!')
        back_to_main_menu()
      else:
        back_to_main_menu()
    else:
      print('unauthorized! \n your ID does not match the pnr of ticket.')
      back_to_main_menu()
  except:
    ticket_not_found()


# if ticket is not found
def ticket_not_found():
  print('Ticket not found!')
  print('You can: \n '
        '1.try entering your pnr number again \n'
        '2.purchase a ticket \n'
        '3.return to main menu \n'
        '4.exit')
  ch = int(input('enter your choice: '))
  if ch == 1:
    show_ticket()
  elif ch == 2:
    buy_ticket()
  elif ch == 3:
    print('returning to main menu...')
    main_menu()
  else:
    exit()


# Account settings
def account():
  print('do you want to: \n'
        '1.show account details \n'
        '2.delete account')
  ch = int(input('enter your choice: '))
  if ch == 1:
    cur.execute(f'select * from account where ID = {a};')
    j = cur.fetchone()
    print(f'ID: {j[0]} \n name: {j[2]} \n gender: {j[3]} \n age: {j[4]} \n dob: {j[5]} \n phone number: {j[6]}')
    back_to_main_menu()
  elif ch == 2:
    x6 = input('Do you want to request for refund(s) for your ticket(s) too? (Y/N)')
    if x6.upper() == 'Y':
      cur.execute(f'delete * from ticket where id = {a};')
      print('you will be refunded shortly!')
      cur.execute(f'delete * from account where id = {a};')
      print('account succsessfully deleted!')
      login_menu()
    else:
      back_to_main_menu()


# calling the first function
login_menu()
