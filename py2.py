####################################################################
import os
os.remove("leapin.txt")
f = open("leapin.txt", "a")
f.write("""
a=loadmol2 file.mol2
loadamberparams bor.dat
check a
""")

for x in range(0,181,30):
	print(x)
	f.write("""
impose a {1}, { {\"C\" \"O3\" \"C3\" \"H11\" %d } }
savepdb a a_%d.pdb
quit
	""" %(x,x)  )
	pass


f.close()


