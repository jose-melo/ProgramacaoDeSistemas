orig = 'dumper.txt'

arq = open(orig, 'r')
TS = {}

TabInst = {
	'JP':'0',
	'JZ':'1',
	'JN':'2',
	'LV':'3',
	'+':'4',
	'-':'5',
	'*':'6',
	'/':'7',
	'LD':'8',
	'MM':'9',
	'SC':'A',
	'RS':'B',
	'HM':'C',
	'GD':'D',
	'PD':'E',
	'OS':'F'
}


locationCounter = 0x0000

for linha in arq:
	
	if linha[0] == ';': continue
	if linha[0] == '#': continue	
	
	linha = linha.split(' ')
	print(linha)

	rotulo = linha[0]
	op = linha[1]
	operando = linha[2]

	if rotulo != '':
		if rotulo not in TS:
			TS[rotulo] = locationCounter
	
	if op == '@':
		locationCounter = int(operando[1:-1], 16)
		continue 
	locationCounter += 2

arq.close()
arq = open(orig, 'r')
saida = open('saida.txt', 'w')

locationCounter = 0x0000
for linha in arq:
	
	if linha[0] == ';':
		for i in linha:
			saida.write(i)
		saida.write('\n')
		continue
	if linha[0] == '#': continue	

	linha = linha.split(' ')

	rotulo = linha[0]
	op = linha[1]
	operando = linha[2]

	if operando[0] == '/':
		operando = operando[1:-1]
	else:
		operando = operando[:-1]


	if op == '@':
		locationCounter = int(operando, 16)
		continue 
	
	if op == 'K':
		saida.write(format(locationCounter, '#06x').upper()[2:] + ' ' + operando+'; Constante '+rotulo+'\n')
		locationCounter += 2
		continue

	opp = operando
	if operando in TS:
		operando = int(TS[operando])

	print("Operando = ", operando)

	saida.write(format(locationCounter, '#06x').upper()[2:] + ' ' +TabInst[linha[1]] + format(operando, '#05x').upper()[2:]+'; '+linha[1]+' '+opp+'\n')
	locationCounter += 2



print(TS)
saida.close()
arq.close()












