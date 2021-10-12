def esta(x, lista):
        for i in lista: 
                if i ==x:
                        return True
                                 
def selectionSort(aList):
    for i in range(len(aList)):
        least = i
        for k in range(i+1, len(aList)):
            if aList[k] > aList[least]:
                least = k
                 
        swap(aList, least, i)
         
def swap(A, x, y):
    temp = A[x]
    A[x] = A[y]
    A[y] = temp



cadena ='''RIJ AZKKZHC PIKCE XT ACKCUXJHX SZX, E NZ PEJXKE, PXGIK XFDKXNEQE RIPI RIPQEHCK ET OENRCNPI AXNAX ZJ RKCHXKCI AX CJAXDXJAXJRCE 
AX RTENX, E ACOXKXJRCE AXT RITEQIKERCIJCNPI OKXJHXDIDZTCNHE AX TE ACKXRRCIJ EJEKSZCNHE.
AZKKZHC OZX ZJ OERHIK AX DKCPXK IKAXJ XJ XT DEDXT AX TE RTENX IQKXKE XJ REHETZJVE XJ GZTCI AX 1936. DXKI AZKKZHC, RIPI IRZKKX RIJ 
TEN DXKNIJETCAEAXN XJ TE MCNHIKCE, JI REVI AXT RCXTI. DXKNIJCOCREQE TE HKEACRCIJ KXvITZRCIJEKCE AX TE RTENX IQKXKE. NZ XJIKPX 
DIDZTEKCAEA XJHKX TE RTENX HKEQEGEAIKE, KXOTXGEAE XJ XT XJHCXKKI PZTHCHZACJEKCI XJ QEKRXTIJE XT 22 AX JIvCXPQKX AX 1936, 
PZXNHKE XNE CAXJHCOCRERCIJ. NZ PZXKHX OZX NCJ AZAE ZJ UITDX IQGXHCvI ET DKIRXNI KXvITZRCIJEKCI XJ PEKRME. NCJ AZKKZHC SZXAI PEN 
TCQKX XT REPCJI DEKE SZX XT XNHETCJCNPI, RIJ TE RIPDTCRCAEA AXT UIQCXKJI AXT OKXJHX DIDZTEK V AX TE ACKXRRCIJ EJEKSZCNHE, 
HXKPCJEKE XJ PEVI AX 1937 TE HEKXE AX TCSZCAEK TE KXvITZRCIJ, AXNPIKETCLEJAI E TE RTENX IQKXKE V OERCTCHEJAI RIJ XTTI XT DINHXKCIK 
HKCZJOI OKEJSZCNHE.'''
max=0
letra=' '
lista=[]
listanueva=[]
for i in cadena:
	
	cont=0
	j=i
	for j in cadena:
	
		if i==j and (j!=' ' and  j!='.' and  j!=',' and j!='·' and j!='\n'):
				cont=cont+1
	
	if not  esta(cont, listanueva):
		
		listanueva.append(cont)
	if max<cont:
		max=cont
		letra=i
selectionSort(listanueva)
for t in  listanueva:
	
	for o in cadena :
		conta=0
		g=o
		for g in cadena:
			if o==g and (g!=' ' and  g!='.' and  g!=',' and g!='·' and g!='d'and g!='\n'):
                                conta=conta+1
		if t == conta and not esta(o,lista):
			lista.append(o)


print (lista)
print (listanueva)


for w in cadena:
	if w==letra:
		cadena=cadena.replace(w,"e")
	if w==lista[1]:
		cadena=cadena.replace(w,"a")
	if w=="A":
		cadena=cadena.replace(w,"d")
	if w=="T":
		cadena=cadena.replace(w,"l")
	if w=="J":
		cadena=cadena.replace(w,"n")
	if w=="I":
		cadena=cadena.replace(w,"o")
	if w=="D":
		cadena=cadena.replace(w,"p")
	if w=="C":
		cadena=cadena.replace(w,"i")
	if w=="P":
		cadena=cadena.replace(w,"m")
	if w=="Q":
                cadena=cadena.replace(w,"b")
	if w=="K":
                cadena=cadena.replace(w,"r")
	if w=="R":
                cadena=cadena.replace(w,"c")
	if w=="U":
                cadena=cadena.replace(w,"g")
	if w=="Z":
                cadena=cadena.replace(w,"u")
	if w=="N":
                cadena=cadena.replace(w,"s")
	if w=="O":
                cadena=cadena.replace(w,"f")
	if w=="H":
                cadena=cadena.replace(w,"t")
	if w=="S":
                cadena=cadena.replace(w,"q")
	if w=="V":
                cadena=cadena.replace(w,"y")
	if w=="F":
                cadena=cadena.replace(w,"x")
	if w=="G":
                cadena=cadena.replace(w,"j")
	if w=="M":
                cadena=cadena.replace(w,"h")
	if w=="L":
                cadena=cadena.replace(w,"z")
print (cadena)



