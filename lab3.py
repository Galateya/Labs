#!usr/bin/python
# -*- encoding: UTF-8 -*-

import optparse

parser = optparse.OptionParser(usage = "DiscModel [-r] [-f] arg1 arg2",version = "DiscModel 0.01")

parser.add_option("-r","--register",help="Регистрация нового пользователя")
parser.add_option('-f','--files',action='append',nargs=2,help='Файлы, которые вы хотите учесть')

(options,args) = parser.parse_args()

print (options)
print (args)

Sample = options.__dict__

user = {Sample.get('register'):Sample.get('files')}
print(user)

right = user.get(Sample.get('register'))
print(right)
print(right[0][0])
if 'w' in right[0]:
	print('Yes')

def SaveUser(name, rights):
	right_u = ''
	for k in rights:
		right_u +=str(k) 


	user_r = (str(name) + right_u)
	f = open('{0}'.format(name),'w')
	f.write(user_r)
	f.close()

SaveUser(Sample.get('register'),Sample.get('files'))

def OpenUser (name):
	f = open('{0}'.format(name))
	print(f.readlines())

OpenUser(Sample.get('register'))