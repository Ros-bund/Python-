f = input()
name = input()
ot = input()
if ('Г' in f) and ('Т' in name) and ('А' in ot):
    print(f[0], name[0], ot[0], sep='\n')
else:
    print(f, name, ot, sep='\n')