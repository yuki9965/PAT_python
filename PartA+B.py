while True:
	try:
		line = raw_input()
		A, DA, B, DB = line.strip().split()
		Alist, Blist = list(A), list(B)
		Arlt, Brlt = [], []

		for a in Alist:
			if a == DA:
				Arlt.append(DA)
		for b in Blist:
			if b == DB:
				Brlt.append(DB)
		if len(Arlt) == 0:
			Anum = 0
		else:
			Anum = int(''.join(Arlt))
		if len(Brlt) == 0:
			Bnum = 0
		else:
			Bnum = int(''.join(Brlt))
		print Anum + Bnum

	except:
		break
