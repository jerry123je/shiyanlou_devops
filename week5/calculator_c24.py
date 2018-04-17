#!/usr/bin/env python3
import sys

user_lst = sys.argv[1:]
if user_lst is None:
	print('Parameter Error')
	exit(1)
user_dic = {}

for user_info in user_lst:
	try:
		user, salary = user_info.split(':')
		user_dic[user] = [int(salary),]
	except ValueError:
		print('Parameter Error,haha')
		exit(1)

for user in user_dic.keys():
	salary = user_dic[user][0]
	fee = salary * 0.08 + salary * 0.02 + salary * 0.005 + salary * 0.06
	tax_to_count = salary - fee - 3500 
	if tax_to_count > 80000:
		tax = tax_to_count * 0.45 - 13505
	elif tax_to_count > 55000:
		tax = tax_to_count * 0.35 - 5505
	elif tax_to_count > 35000:
		tax = tax_to_count * 0.30 - 2755
	elif tax_to_count > 9000:
		tax = tax_to_count * 0.25 - 1005
	elif tax_to_count > 4500:
		tax = tax_to_count * 0.20 - 555
	elif tax_to_count > 1500:
		tax = tax_to_count * 0.10 - 105
	elif tax_to_count > 0:
		tax = tax_to_count * 0.03
	else:
		tax = 0

	actual_salary = float(salary - fee - tax)
	user_dic[user].append(float(actual_salary))
	print('{0}:{1:.2f}'.format(user,actual_salary))


	
