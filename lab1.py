passenter = str(input ('Введите пароль: '))

#Списки алфавитов

alf1 = ['q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
alf2 = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M']
alf3 = ['1','2','3','4','5','6','7','8','9','0']
alf4 = ['!','@','#','$','%','^','&','*','(',')','_','-','+',':',';','"','?','<','>']


#функция, считающая суммарный алфавит
def passlook(password):
	pl = 0
	pl1 = 0
	pl2 = 0
	pl3 = 0
	pl4 = 0
	step = 0
	while step < len(password):
		if password[step] in alf1 and pl1 == 0:
			pl1+=len(alf1)
		elif password[step]in alf2 and pl2 == 0:
			pl2+=len(alf2)
		elif password[step] in alf3 and pl3 == 0:
			pl3+=len(alf3)
		elif password[step] in alf4 and pl4 == 0:
			pl4+=len(alf4)
		print (pl)
		pl = pl1 + pl2 + pl3 + pl4
		step+=1
	return pl

#функция, расчитывающая силу пароля	
def passmeter (passlen):
	#A =  мощность алфавита
	#L =  длина пароля
	V = 100  #скорость перебора паролей злоумышленником
	T = 12 #время действия пароля
	P = 10**-4 #вероятность подбора пароля злоумышленником
	Sn = (V*T)//P  # нижняя граница стойкости
	Ar = passlook(passenter)
	print(Ar)
	L = len (passenter)
	A = Sn**(1/L)
	print(Sn, A)
	ar = passlen + 4
	print(ar)
passmeter(passlook)
