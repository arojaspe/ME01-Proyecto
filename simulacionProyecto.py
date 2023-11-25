import random

qulityTeamA = random.randint(0, 3)
qulityTeamB = random.randint(0, 3)
qulityTeamC = random.randint(0, 3)

print("Calidad del equipo A: ", qulityTeamA)
print("Calidad del equipo B: ", qulityTeamB)
print("Calidad del equipo C: ", qulityTeamC)

classification = {}

classification['Equipo A'] = 0
classification['Equipo B'] = 0
classification['Equipo C'] = 0


def probOfResult(qualityTeam1, qualityTeam2):
    probVictory = 0
    probDraw = 0
    probDefeat = 0

    differenceOfQuality = qualityTeam1 - qualityTeam2
    
    if differenceOfQuality > 1:        
        probVictory = 0.8
        probDraw = 0.1
    if differenceOfQuality == 1:        
        probVictory = 0.6
        probDraw = 0.1
    elif differenceOfQuality < 1:        
        probVictory = 0.2
        if differenceOfQuality == 0:            
            probVictory = 0.5
            probDraw = 0.3
        if differenceOfQuality < 0:            
            probDraw = 0.2
        if differenceOfQuality == -1:
            probVictory = 0.4
 
    probDefeat = 1 - probVictory - probDraw

    probVictory = round(probVictory, 2)
    probDraw = round(probDraw, 2)
    probDefeat = round(probDefeat, 2)

    return probVictory, probDraw, probDefeat
 
def matchEvent(probVictory, probDraw, probDefeat):
    max_prob = max(probVictory, probDraw, probDefeat)
    # Si alguna de las probabilidades es igual
    if max_prob == probVictory:
        print('Victoria de local')
        pointsTeam1 = 3
        pointsTeam2 = 0 

    elif max_prob == probDraw:
        print('Empate')
        pointsTeam1 = 1
        pointsTeam2 = 1
    
    else:
        print('Victoria de visitante')
        pointsTeam1 = 0
        pointsTeam2 = 3

    return pointsTeam1, pointsTeam2

def updateClassification(pointsTeam1, pointsTeam2, team1, team2):
    classification[team1] += pointsTeam1
    classification[team2] += pointsTeam2

#def bayesianNetwork():
#def inferenceAlgorithm():


def simulate():
    # Match 1: A vs B
    probVictory1, probDraw1, probDefeat1 = probOfResult(qulityTeamA, qulityTeamB)
    print('\n---------------------------------------------------')
    print('Fecha 1 ----- A vs B')
    print('\nDiferencia de calidad: ', qulityTeamA - qulityTeamB)
    print('Probabilidades de resultado: ')
    print(probVictory1, probDraw1, probDefeat1)
    print('\nResultado final: ')
    pointsTeam1, pointsTeam2 = matchEvent(probVictory1, probDraw1, probDefeat1)
    updateClassification(pointsTeam1, pointsTeam2, 'Equipo A', 'Equipo B')
    print("\nClasificación después de la fecha 1:\n", classification)


    # Match 2: A vs C
    probVictory2, probDraw2, probDefeat2 = probOfResult(qulityTeamA, qulityTeamC)
    print('\n---------------------------------------------------')
    print('Fecha 2 ----- A vs C')
    print('\nDiferencia de calidad: ', qulityTeamA - qulityTeamC)
    print('Probabilidades de resultado: ')
    print(probVictory2, probDraw2, probDefeat2)
    print('\nResultado final: ')
    pointsTeam1, pointsTeam2 = matchEvent(probVictory2, probDraw2, probDefeat2)
    updateClassification(pointsTeam1, pointsTeam2, 'Equipo A', 'Equipo C')
    print("\nClasificación después de la fecha 2:\n", classification)


    # Match 3: C vs B
    probVictory3, probDraw3, probDefeat3 = probOfResult(qulityTeamC, qulityTeamB)
    print('\n---------------------------------------------------')
    print('Fecha 3 ----- C vs B')
    print('\nDiferencia de calidad: ', qulityTeamC - qulityTeamB)
    print('Probabilidades de resultado: ')  
    print(probVictory3, probDraw3, probDefeat3)
    print('\nResultado final: ')
    pointsTeam1, pointsTeam2 = matchEvent(probVictory3, probDraw3, probDefeat3)
    updateClassification(pointsTeam1, pointsTeam2, 'Equipo C', 'Equipo B')


    print("\nClasificación final: \n", classification)

simulate()