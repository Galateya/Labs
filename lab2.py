#!/usr/bin/python
# -*- encoding: UTF-8 -*-

import random
list0 = list('!"#$%&\'()*')
list1 = list('0123456789')
list2 = list('qwertyuiopasdfghjklzxcvbnm')
ID = input('Введите свой идентификатор: ')
IDl=list(ID)
count = 0
password=''
while count < 8:
	if count < len(IDl)%5 :
		password += random.choice(list0)
	else:
		password += random.choice(list2)
	count += 1
print('Идентификатор пользователя: ', ID)
print('Сгенерированный пароль    : ', password+(random.choice(list1)), '\n')
