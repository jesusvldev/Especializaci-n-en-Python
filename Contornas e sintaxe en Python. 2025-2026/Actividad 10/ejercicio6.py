""" 6.- Pídelle ao usuario o seu peso (en kg) e estatura (en metros) e móstralle unha mensaxe indicando cal é o 
seu Índice de Masa Corporal (IMC). A fórmula para calculalo é a seguinte: IMC = Peso (kg) / [Estatura (m)]² """

peso = float(input('Introduce tu peso: '))
estatura = float(input('Introduce tu estatura: '))

imc = peso / estatura**2

print(f'Tu Índice de Masa Corporal (IMC) es {imc:.2f}.')
