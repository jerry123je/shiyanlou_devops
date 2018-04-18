#!/usr/bin/env python3
import sys
import os 
import csv
from multiprocessing import Process, Queue
import getopt
import configparser
from datetime import datetime

class Args():
	def __init__(self):
		self.optlist, self.args = getopt.getopt(sys.argv[1:],"C:c:d:o:")
		self._analysis()
	
	def __repr__(self):
		return(','.join(self.arg_dic.keys()))

	def _usage(self):
		print("File not exists!")
		exit(1)

	def _analysis(self):
		self.arg_dic = {}
		for _opt,_arg in self.optlist:
			if (_opt != '-o' and _opt != '-C' and not os.path.exists(_arg)) or _arg is None:
				self._usage()
			else:
				self.arg_dic[_opt] = _arg
				
	@property
	def cityname(self):
		if '-C' not in self.arg_dic.keys():
			self.arg_dic['-C'] = 'DEFAULT'
		else:
			self.arg_dic['-C'] = self.arg_dic['-C'].upper()
		return self.arg_dic['-C']

	@property		
	def configfile(self):
		return self.arg_dic['-c']
	
	@property
	def datafile(self):
		return self.arg_dic['-d']

	@property
	def outputfile(self):
		return self.arg_dic['-o']


class Config():
	def __init__(self,configfile,cityname):
		self.config = self._read_config(configfile,cityname)

	def _usage(self):
		print("Wrong config!")
		exit(1)

	def _read_config(self,configfile,cityname):
		config = configparser.ConfigParser()
		config.read(configfile)
		if cityname in config.sections():
			return config[cityname]
		else:
			_usage()
		#config = {}
		#_f = open(configfile,'r')
		#for line in _f.readlines():
		#	config_keys, config_values = line.split('=')
		#	try:
		#		config_keys = config_keys.strip()
		#		config_values = float(config_values.strip())
		#	except ValueError:
		#		self._usage()
		#	config[config_keys] = config_values
		#return config	
	 	 	
	def get_config(self,conf_key):
		if conf_key not in self.config.keys():
			print('Key not exists!')
		else:
			return float(self.config.get(conf_key))		

	def __repr__(self):
		return ','.join(self.config.keys())

class UserData():
	#def __init__(self,datafile):
		#self.userdata = self._read_users_data(datafile)

	def _usage(self):
		print("Wrong data!")
		exit(1)

	def read_users_data(self,datafile):
		userdata = []
		_f = open(datafile,'r')
		for line in _f.readlines():
			try:
				user, salary = line.split(',')
				user = user.strip()
				salary = float(salary.strip())
			except IndexError or ValueError:
				self._usage()
			userdata.append((user,salary))
		queue1.put(userdata)
	
class IncomeTaxCalculator():
	def __init__(self,outputfile,conf):
		self.opf = outputfile
		self.conf = conf
		self.userdata = queue1.get()

	def calc_for_all_userdata(self):
		result = []
		for user, salary in self.userdata:
			salary_before = salary
			if salary_before < self.conf.get_config('JiShuL'):
				tax_count = self.conf.get_config('JiShuL')
			elif salary_before > self.conf.get_config('JiShuH'):
				tax_count = self.conf.get_config('JiShuH')	
			else:
				tax_count = salary_before
			shebao = self.conf.get_config('YangLao') + self.conf.get_config('YiLiao') + self.conf.get_config('ShiYe') + self.conf.get_config('GongShang') + self.conf.get_config('ShengYu') + self.conf.get_config('GongJiJin')	
			fee = float(tax_count * shebao)
			tax_to_count = float(salary_before - fee - 3500)
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
			count_date = datetime.strftime(datetime.now(),'%Y-%m-%d %H:%M:%S')
			salary_after = "{:.2f}".format(float(salary_before - fee - tax))
			tax = "{:.2f}".format(tax)
			fee = "{:.2f}".format(fee)
			user_info = [user,salary_before,fee,tax,salary_after,count_date]
			result.append(user_info)
		queue2.put(result)

		
	def export(self,  default='csv'):
		#result = self.calc_for_all_userdata()
		result = queue2.get()
		with open(self.opf,'w') as f:
			writer = csv.writer(f)
			writer.writerows(result)

if __name__ == '__main__':
	arg = Args()
	conf = Config(arg.configfile,arg.cityname)
	queue1 = Queue()
	queue2 = Queue()
	userdata = UserData()
	Process(target=userdata.read_users_data(arg.datafile)).start()
	income=IncomeTaxCalculator(arg.outputfile,conf)
	Process(target=income.calc_for_all_userdata()).start()
	Process(target=income.export()).start()


