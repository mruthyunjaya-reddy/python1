
from random import *
import sys
class customer:
	# well come to bank customedrs
	Bankname="*************************** STATE BANK OF INDIA ***********************"
	print(Bankname)
	def __init__(self,name,balance=0.0):
		self.name=name
		self.balance=0.0
	def deposite(self,amount):
		print()
		print("@---------------- amount depodite to your bank ------------------@")
		print()
		self.balance=self.balance+amount
		print("after deposite amount in your account:",self.balance)
		print()

	def withdraw(self,amount):
		print()
		print("@---------------- withdraw amount from your account -------------@")

		print()
		if amount <= self.balance:
			self.balance=self.balance-amount
			print("withdraw amount is:",amount)
			#print()
			#print("after withdraw amount in your account:",self.balance)
		else:
			print("insufficiant balance in your account")
			sys.exit(0)

	def BalanceEnquiry(self):#,amount
		#if amount <= self.balance:
			#self.balance=self.balance - amount
		print("amount in your account:",self.balance)

print("@@@@@@@@@@@@@@@@@@@@@@@@ WELL COME TO BANK CUSTOMERS @@@@@@@@@@@@@@@@@@@@")
print()
name=input("enter customer name:")
print()
a=customer(name)
while True:
	print("D-Deposite\nW-Withdraw\nB-Balance Enquiry\nE-Exit")
	print()
	option=input("enter your option:").lower()
	print()
	if option=='d':
		Ac=int(input("enter your A/C Number:"))
		if Ac==9876543210:
			print()
			D=int(input("enter amount:"))
			a.deposite(D)
		else:
			print("please enter valid Account Number")
			print()

	elif option=='w':
		while True:
			p=int(input("enter password:"))
			if p==9052:
				print()
				W=int(input("enter withdraw amount:"))
				print()
				if not(W>=100):
					print("minimum withdraw is Rs.100")
					print()
				else:
					break
			else:
				print("please enter valid password")
				print()
		a.withdraw(W)

	elif option=='b':
		a.BalanceEnquiry()

	elif option=='e':
		print("Exit from your account:")
		print("Thank you for visit and again")
		sys.exit()
	else:
		print("invalid option\n please enter valid option:")
	

'''s=["wellcome","takecare"]
s1=["friends","sir"]

data1=[i+" "+j for i,j in  zip(s,s1)]
print("output is:",str(data1))
# print(data1)
# data1="wellcome"+" "+"friends","takecare"+" "+

l=[1,2,3,4,5,6,7]
l1=[10,20,30,40,50,60]
l2=[100,200,300,400,500,600]
for i,j,k in zip(l,l1,l2[::-1]):
	print(i,j,k)
	# print(j)'''

	

	
