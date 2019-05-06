
#############################################
#import random 
#r1 = random.randint(1,360) 
#print(r1/100) 
#f = open("a.txt", "a")
#loadamberparams \"bor.dat\"
# addAtomTypes { { "B1" "B" "sp2" } }
# addAtomTypes { { "oh" "O" "sp2" } }
# addAtomTypes { { "os" "O" "sp2" } }

#@<TRIPOS>ATOM
#      1 H1          -0.1660     2.5890    -0.2030 ho          1 MOL       0.425234
#      2 O1          -0.6950     1.8160    -0.3360 oh          1 MOL      -0.740851
#      3 B1          -0.0040     0.6800    -0.0410 B           1 MOL       0.916675
#      4 O2           1.2760     0.7930     0.3900 os          1 MOL      -0.584834
#      5 C1           2.0810    -0.3200     0.7070 c3          1 MOL       0.351772
#      6 C2           2.8020    -0.8460    -0.5220 c3          1 MOL      -0.254733
#      7 H2           3.3950    -0.0620    -0.9800 hc          1 MOL       0.065923
#      8 H3           2.0930    -1.2150    -1.2550 hc          1 MOL       0.065923
#      9 H4           3.4660    -1.6630    -0.2510 hc          1 MOL       0.065923
#     10 H5           1.4780    -1.0990     1.1550 h1          1 MOL      -0.005252
#     11 H6           2.7960     0.0200     1.4450 h1          1 MOL      -0.005252
#     12 O3          -0.5850    -0.5340    -0.1770 os          1 MOL      -0.584834
#     13 C3          -1.9220    -0.7000    -0.5940 c3          1 MOL       0.351772
#     14 C4          -2.8780    -0.6420     0.5840 c3          1 MOL      -0.254733
#     15 H7          -3.8950    -0.8350     0.2550 hc          1 MOL       0.065923
#     16 H8          -2.8530     0.3360     1.0520 hc          1 MOL       0.065923
#     17 H9          -2.6110    -1.3870     1.3260 hc          1 MOL       0.065923
#     18 H10         -2.1780     0.0530    -1.3290 h1          1 MOL      -0.005252
#     19 H11         -1.9740    -1.6700    -1.0740 h1          1 MOL      -0.005252
################################################
#tleap              
#a=loadmol2 bor.mol2
#source leaprc.gaff
#loadamberparams "bor.frcmod"
#addAtomTypes { { "bo" "B" "sp2" } }
#addAtomTypes { { "oh" "O" "sp2" } }
#addAtomTypes { { "os" "O" "sp2" } }
#impose a {1}, { {"B" "O2" "C1" "H2" 91 } }
#savepdb a a_2.pdb
#saveamberparm a a_a_1.prmtop "amber_inps/A_struc_a_1.mdcrd"
#quit
###################################################################
#for x in xrange(1,10):
#	import random 
#	print(x)
#	r1 = random.randint(1,360) 
#	f = open("leapin.txt", "a")
#	f.write("""tleap              
#a=loadmol2 file.mol2
#source leaprc.gaff
#loadamberparams \"bor.frcmod\"
#addAtomTypes { { \"B\" \"B1\" \"sp2\" } }
#addAtomTypes { { \"oh\" \"O\" \"sp2\" } }
#addAtomTypes { { \"os\" \"O\" \"sp2\" } }
#impose a {1}, { {\"B1\" \"O2\" \"C1\" \"H2\" %d } }
#savepdb a a_%d.pdb
#saveamberparm a a_a_%d.prmtop \"amber_inps/A_struc_a_%d.mdcrd\"
#quit
#	""" %(r1,x,x,x)  )
#	pass
#
#
#f.close()
####################################################################


for x in xrange(1,10):
	import random 
	print(x)
	r1 = random.randint(1,360) 
	f = open("leapin.txt", "a")
	f.write("""
impose a {1}, { {\"O3\" \"C\" \"O1\" \"H1\" %d } }
savepdb a a_%d.pdb
	""" %(r1,x)  )
	pass


f.close()


