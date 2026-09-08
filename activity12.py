#import getpass
from getpass import getpass

username = 'andoy'
password = 'tulong andoy'

u = input("Enter Username ---> ")
p = input("Enter Password ---> ")
#p = getpass.getpass("Enter Password ---> ")

if username == u and password == p :
       print("ACCESS GRANTED")
else: 
       print("ACCESS DENIED")