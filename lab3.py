#!usr/bin/python
# -*- encoding: UTF-8 -*-

# Программа универсальна для любого варианта

import optparse

parser = optparse.OptionParser(usage = "Пример регистрации пользователя: \n\n lab3.py -r Vasya<идентификатор> -f file1<имя файла> read<операция над файлом>\n -f file2 write ... -f fileN none. \n\n При вызове программы без дополнительных опций будет проведена идентификацияп пользователя и допуск работы с файлами",version = "DiscModel 0.69")

parser.add_option("-r",help="Регистрация нового пользователя. Следует вводить только имя пользователя, оно будет использовано как идентификатор")
parser.add_option('-f',action='append',nargs=2,help='Файлы, которые вы хотите учесть с параметрами прав. Пример: -f file1 read -f file2 write ... -f fileN None')

(options,args) = parser.parse_args()

Sample = options.__dict__

# В функцию SaveUser в name передается значение опции register (-r) (Sample.get('register')),
# а в rights передается значени опции files (-f) (Sample.get('files'))

def SaveUser(name, rights):
	right_u = ''
	for k in rights:
		for k1 in k:
			right_u += str(' ' + k1 + ' ')
	user_r = (str(name) + right_u)
	f = open('{0}'.format(name),'w')
	f.write(user_r)
	f.close()

# В функцию OpenUser в name передается то же значение, что и в функцию SaveUser

def OpenUser (name):
	f = open('{0}'.format(name))
	UserRight = f.readlines()[0]
	print('\n',UserRight, '\n')
	f.close()

# В функцию RightChecker в name передается то же значение, что и в функцию SaveUser

def RightChecker (name):
	count = 0
	while count != 1:
		f = open('{0}'.format(name))
		UserRight = f.readlines()[0]
		oname = input('Какую операцию вы хотите провести: ')
		if oname != 'exit':
			fname = input('Введите имя файла: ')	
		start = UserRight.find(fname) + len(fname) + 2
		end =   len(oname) + start 

		file_r = UserRight[start:end]

		if oname == file_r and oname != 'exit':
			print('Вы обладаете правом на эту операцию \n')
		elif oname != 'exit':
			print('Вы не обладаете правом на эту операцию \n')
		elif oname == 'exit':
			count += 1

# Вызов функции SaveUser проводится только, если программа была запущена с доп. опциями

if Sample.get('register') is not None and Sample.get('files') is not None:
	SaveUser(Sample.get('register'),Sample.get('files'))
# Вызов остальных функций проводится только, если программа была запущена без доп. опций
if Sample.get('register') is None and Sample.get('files') is None:
	count = 0
	while count != 1:
		try:
			UserName = input ('Введите свой идентификатор: ')
			OpenUser(UserName)
			RightChecker(UserName)
			count += 1
		except IOError:
			print('Такого пользователя не существует')
