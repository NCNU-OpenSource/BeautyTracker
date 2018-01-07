# String Formatting
fmt0 = "{0:0.1%}"
fmt5 = "{0:5.1%}"
a = 0.015
s0 = fmt0.format(a)
s5 = fmt5.format(a)
print( len(s0), len(s5) )
