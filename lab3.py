#!usr/bin/python
# -*- encoding: UTF-8 -*-

import optparse

parser = optparse.OptionParser(usage = "DiscModel [-r] [-f] arg1 arg2",version = "DiscModel 0.02")

parser.add_option("-r","--register",help="Регистрация нового пользователя. Следует вводить только имя пользователя, оно будет использовано как идентификатор")
parser.add_option('-f','--files',action='append',nargs=2,help='Файлы, которые вы хотите учесть с параметрами прав. Пример: -f file1 read -f file2 write ... -f fileN None')

(options,args) = parser.parse_args()

print (options)
print (args)

Sample = options.__dict__

def SaveUser(name, rights):
	right_u = ''
	for k in rights:
		for k1 in k:
			right_u += str(' ' + k1 + ' ')
	user_r = (str(name) + right_u)
	f = open('{0}'.format(name),'w')
	f.write(user_r)
	f.close()

def OpenUser (name):
	f = open('{0}'.format(name))
	print(f.readlines()[0])
	f.close()
if Sample.get('register') is not None and Sample.get('files') is not None:
	SaveUser(Sample.get('register'),Sample.get('files'))
	OpenUser(Sample.get('register'))
if Sample.get('register') is None and Sample.get('files') is None:
	UserName = input ('Введите свой идентификатор: ')

