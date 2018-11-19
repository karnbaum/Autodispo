import sys, os

# Zugriffsversuch
try:
    d = open("DE_MS_742060_2018-08-10_11-00.csv","r")
except:
    print "Dateizugriff nicht erfolgreich"
    sys.exit(0)

# Erste Zeile ausgeben

# Gezieltes Lesen
for i in range(1,4):
    # Datum Lesen, beginnt auf Position 1 - 29 =29
    d.seek(65+(134*i))
    datum = (d.read(30))
#    datum = int(d.read(4))

    # filename Lesen, beginnt ab Pos. 69 - 83 =14
    d.seek(65+(134*i) + 69)
#    ep = float(d.read(28))
    filename = d.read(15)

    # Ausgabe
    print "IT:", i, "Datum", datum, ", filename", filename

# Schliessen der Datei
d.close()
