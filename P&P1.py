# Algorithmen und Datenstrukturen
# Hausaufgabe 1 - Matrixmultiplikation
# Abgabedatum: 21.5.2017
#
# Gruppennummer: 55
# Gruppenmitglieder:
# - Eike Pubantz
# - Max Wiedenhöft
# - Jan Heuer

# Diese Funktion können Sie verwenden, um Matrizen auszugeben.
def printMatrix(m):
    for line in m:
        print('|', end='')
        i = 0
        for value in line:
            if (i > 0):
                print(' ', end='')
            print(value, end='')
            i = i + 1
        print("|")



# Erstellt neue Matirx gefüllt mit Nullen
def newMatrix(m ,n): # m: Zeilenanzahl, n: Spaltenanzahl
    new = []
    for i in range(0,m): # Schleife über Zeilen
        new.append([]) # Hinzufügen einer neuen Zeile
        for j in range(0,n): # Schleife über Spalten
            new[i].append(0) # Füllen der Zeilen mit Nullen
    return new



# Matrixaddition
def matadd(a, b):
    result = newMatrix(len(a),len(a[0])) # Ergebnismatrix gleicher Größe wie a bzw. b
    for i in range(len(a)): # Schleife über Zeilen
        for j in range(len(a[0])): # Schleife über Spalten
            result[i][j] = a[i][j] + b[i][j] # Wert der Ergenbnismatrix wird Addition der Werte von a und b an der jeweiligen Stelle
    return result



# Implementieren Sie ab hier Ihre Lösungen:
def matMultDef(a, b):
    print('Parameter a:')
    printMatrix(a)
    print('Parameter b:')
    printMatrix(b)

    result = newMatrix(len(a),len(b[0])) # Ergebnismatrix mit Zeilenanzahl = a, Spaltenanzahl = b

    if len(a[0]) != len(b): # Prüft ob a*b definiert ist (Spaltenanzahl a = Zeilenanzahl b)
        print("Die Berechnung ist nicht definiert, da die Spaltenanzahl der ersten Matrix nicht mit der Zeilenanzanhl der zweiten Matrix übereinstimmt!")
        return result

    for i in range(0,len(result)): # Schleife über Zeilen der Ergebnismatrix
        for j in range(0,len(result[0])): # Schleife über Spalten der Ergebnismatrix
            for k in range(0,len(b)): # Schleife über Spalten von a bzw. Zeilen von b
                result[i][j] = result[i][j] + a[i][k]*b[k][j] # Aufsummieren der Produkte
    return result



def matMultDC(a, b):
    print('Parameter a:')
    printMatrix(a)
    print('Parameter b:')
    printMatrix(b)

    result = newMatrix(len(a),len(b[0])) # Ergebnismatrix mit Zeilenanzahl = a, Spaltenanzahl = b

    if len(a[0]) != len(b): # Prüft ob a*b definiert ist (Spaltenanzahl von a muss gleich Zeilenanzahl von b sein)
        print("Die Berechnung ist nicht definiert, da die Spaltenanzahl der ersten Matrix nicht mit der Zeilenanzanhl der zweiten Matrix übereinstimmt!")
        return result

    n = len(a) # Zeilenanzahl a
    m = len(a[0]) # Spaltenanzahl a bzw. Zeilenanzahl b
    o = len(b[0]) # Spaltenanzahl b

    if ((len(a[0]) == 1) or (len(a) == 1) or (len(b) == 1) or (len(b[0]) == 1)): # Basisfall (eventuell noch weiter zurückführen?)
        return(matMultDef(a,b))

    else:
        c = newMatrix(int(n/2),int(o/2)) # c = Matrix mit halber Zeilen- und Spaltenanzahl im Vergleich zur Ergebnismatrix
        # Zur Speicherung des Zwischenergebnisse genutzt

        ''' r11 = linkes oberes Viertel der Ergebnismatrix
            r12 = rechtes oberes Viertel der Ergebnismatrix
            r21 = linkes unteres Viertel der Ergebnismatrix
            r22 = rechtes unteres Viertel der Ergebnismatrix
            Die Bezeichnungen a11,...,b11,... analog dazu

            Der Ausdruck [a[i][0:int(m/2)] for i in range(0,int(n/2))] gibt das obere linke Viertel von a zurück,
            dabei laüft i über die Zeilen (von 0 bis zur Hälfte der Zeilen), durch die Slice-Operation wird der
            halbe Inhalt jeder Zeile genommen (von Index 0 bis zum Index Hälfte der Spalten)
            [a[i][(int(m/2)):m] for i in range(int(n/2),n)] gibt die unteren Zeilen zurück (da i von der Hälfte
            der Zeilen bis zum Ende läuft) und von jeder Zeile die hintere Hälfte des Inhalts (durch Slicing
            vom Index Hälfte der Spalten bis zum Ende)

            Im Folgenden wird jeweils ein Viertel der Ergebnismatrix berechnet, dazu werden zwei Matrizenprodukte
            der jeweiligen Viertel von a und b gebildet und die beiden Teilergebnismatrizen dann addiert,
            das Ergebnis wird in c zwischengespeichert
            Die jeweilig folgende for-Schleife überträgt dann die Einträge aus c an die passenden Stellen der
            Ergebnismatrix
            Beispielsweise füllt die folgende for-Schleife das obere linke Viertel der Ergenismatrix:
            for i in range(0,int(n/2)):
                result[i][0:int(o/2)] = c[i]
            i läuft über die Zeilen der Ergebnismatrix (von Index 0 bis zur Hälfte), durch die Slice Operation wird
            dann die Hälfte der jeweiligen Zeilen beschrieben (von Index 0 bis zur Hälfte der Zeile), die Matrix c
            muss dabei nur Zeile für Zeile durchgegangen werden
            '''

        # 1. Berechnung r11 = a11*b11 + a12*b21
        c = matadd(matMultDC([a[i][0:int(m/2)] for i in range(0,int(n/2))],[b[i][0:int(o/2)] for i in range(0,int(m/2))]),matMultDC([a[i][(int(m/2)):m] for i in range(0,int(n/2))],[b[i][0:int(o/2)] for i in range(int(m/2),m)]))
        for i in range(0,int(n/2)):
            result[i][0:int(o/2)] = c[i]
        printMatrix(result)

        # 2. Berechnung r12 = a11*b12 + a12*b22
        c = matadd(matMultDC([a[i][0:int(m/2)] for i in range(0,int(n/2))],[b[i][int(o/2):o] for i in range(0,int(m/2))]),matMultDC([a[i][(int(m/2)):m] for i in range(0,int(n/2))],[b[i][int(o/2):o] for i in range(int(m/2),m)]))
        for i in range(0,int(n/2)):
            result[i][int(o/2):o] = c[i]
        printMatrix(result)

        # 3. Berechnung r21 = a21*b11 + a22*b21
        c = matadd(matMultDC([a[i][0:int(m/2)] for i in range(int(n/2),n)],[b[i][0:int(o/2)] for i in range(0,int(m/2))]),matMultDC([a[i][(int(m/2)):m] for i in range(int(n/2),n)],[b[i][0:int(o/2)] for i in range(int(m/2),m)]))
        for i in range(int(n/2),n):
            result[i][0:int(o/2)] = c[i-int(n/2)]
        printMatrix(result)

        # 4. Berechnung r22 = a21*b12 + a22*b22
        c = matadd(matMultDC([a[i][0:int(m/2)] for i in range(int(n/2),n)],[b[i][int(o/2):o] for i in range(0,int(m/2))]),matMultDC([a[i][(int(m/2)):m] for i in range(int(n/2),n)],[b[i][int(o/2):o] for i in range(int(m/2),m)]))
        for i in range(int(n/2),n):
            result[i][int(o/2):o] = c[i-int(n/2)]
        printMatrix(result)

    return result



# Testfälle:
#2x3 * 3x2
'''a=[[3,2,1],[1,0,2]]
b=[[1,2],[0,1],[4,0]]'''

#4x4 * 4x4
'''a=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
b=[[1,5,9,13],[2,6,10,14],[3,7,11,15],[4,8,12,16]]'''

#2x2 * 2x2
'''a=[[1,2],[3,4]]
b=[[1,3],[2,4]]'''

#2x3 * 3x4
'''a=[[1,2,3],[4,5,6]]
b=[[1,4,7,10],[2,5,8,11],[3,6,9,12]]'''

#4x3 * 3x4
'''a=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
b=[[1,4,7,10],[2,5,8,11],[3,6,9,12]]'''

result = matMultDC(a,b)

print('Das Endergebnis ist:')
printMatrix(result)
