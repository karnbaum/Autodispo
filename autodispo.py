# -*- coding: iso-8859-1 -*-
#Projekt: "MSH-Autodispo"
#Kunde: Cullmann-Germany GmbH
#Sachbearbeiter: Julian Schleicher, Rainer Karnbaum
#Beginn: 
#Versionsstand 1.0

#History List:
# Datum Thema
# Ziel10 Fehler-Handlung
# Ziel9 Zusammenbau
# Ziel8 Datenbankabfrage (V3) auf Artikelnummer, ean, lagerbestand, vkp nach hpl
# Ziel7Verknüpfung mit verteilten Daten in Access-Tabelle
# Ziel6 XY-Tabelle \ Feld \ Matrizenverarbeitung (Feld füllen, Spalten \ Zeilen auswählen, verändern z.B. durch Druckausgabe)
# Ziel5 CSV-Datei Lesen und Schreiben
# Ziel4 Executable - > Automatik-Betrieb
# Ziel3 neue autodispo-datei mittels FTP und Privatekey hochladen

# 20181119 Test2
# 20181119 Integration in Github
# 20180902 Ziel2 last_autodispo_datei auf Datum und Uhrzeit von heute umsetzen
# 20180902 Ziel1 Finde die zuletzt mit autodispo auf Rendserv2 hochgeladene autodispo-Datei und weise sie der Variablen last_autodispo_datei zu
# 20180902 Arbeitsdateinamen lesen und auf neues Datum umsetzen
# 20180830 Zusammenbau neuer Autodispo-Dateiname mit aktuellem Datum und Uhrzeit
        # 20180829 Gelesenen Dateinamen in 3 Teile Splitten 
# 20180418 Datenbank-Abfrage über drei Tabellen und Join ok

#Fehlercodes
#000 xxx
#001 yyy

# Bibliotheken
import time
import os
import re
import urllib
import logging
import smtplib
import csv
import sys #für Ordnername 
import shutil
import datetime
import pysftp


# Deklarationen

def logschreiben(eineoperation):
    with open('auto-dispo-log.txt', 'a') as f:
        f.write(eineoperation)
        f.close()
        
        return

# Variablen-Vorbelegungen

# Logstart
timestr = time.strftime("%Y-%m-%d_%H-%M")
timestr_log = time.strftime("%Y-%m-%d %H:%M")
logschreiben('\nAutodispo gestartet um: ' + timestr_log + ';\n')

# Datum heute
heute = time.strftime("%Y-%m-%d")
print heute
logschreiben('Datum heute: ' + heute + ';\n')

# Datum gestern

from datetime import datetime, timedelta
now = datetime.strptime(heute, "%Y-%m-%d")
gestern = now - timedelta (days=1)
gestern = gestern.strftime ("%Y-%m-%d")
print gestern
logschreiben('Datum gestern: ' + gestern + ';\n')
                                                                              #gestern = time.strftime('%Y-%m-%d')
                                                                              #Finde die zuletzt mit autodispo auf Rendserv2 hochgeladene autodispo-Datei

                                                                              #dateiname_alt="DE_MS_742060_2018-08-10_11-00.csv"
                                                                              #path = "L:\\Python27\\work\\Auto-Dispo"
# path = "W:\\Entwicklung\\work\\autodispo"                                   Cullmann Netzwerk-Laufwerk
path = "C:\Users\SchleicherJ\Documents\GitHub\Autodispo"                                   # Github Local


                                                                              #count=0
                                                                              #for fname in os.listdir(path):
                                                                              #count=count+1
                                                                              #print(fname,"count=",count)
    
                                                                              #if fname.endswith('.pdf'):




count=0
for fname in os.listdir(path):
    print(fname,"count=",count)

#---Ziel1 Finde die zuletzt mit autodispo auf Rendserv2 hochgeladene autodispo-Datei und weise sie der Variablen last_autodispo_datei zu---------------

    if fname.endswith('.csv'):
        print fname
    
#---Ende Ziel 1--------------------------------------------------------------------------------------------------------------------------------------

#---Ziel2 last_autodispo_datei auf Datum und Uhrzeit von heute umsetzen------------------------------------------------------------------------------
        
        fname_datum = fname.split("DE_MS_742060_")                                                                                                          #Split wird erstellt, trennt ab " | "
                                                                              #dateiname_neu = portal_rueckantwort.splitlines('|', 1 )
        print fname_datum
        print fname_datum[0]                                                                                                                                  #Erster Split-Part wird angezeigt
        print fname_datum[1]                                                                                                                                  #Erster Split-Part wird angezeigt
        fname_teil2und3 = fname_datum[1].split("_")
        
        #Kundennummer DExx
        dateiname_teil1 = 'DE_MS_742060_'
        #Datum
        dateiname_teil2 = fname_teil2und3[0]
        #Uhrzeit und Dateityp
        dateiname_teil3 = fname_teil2und3[1]
        
        Teil1=dateiname_teil1
        print Teil1
        Teil2=dateiname_teil2
        print Teil2
        Teil3="_"+dateiname_teil3
        print Teil3

        print "heute:"
        print heute
        #print "gestern:"
        #print gestern
        fname_heute = Teil1 + heute + Teil3 
        print fname_heute
        
        path2= path.split("\\")
        print path2
        path1= path2[0] + "\\" + path2[1] + "\\" + path2[2] + "\\" + path2[3]  
        print("Suchordner path1")
        print path1
        if not os.path.exists(path1 + "/" + fname_heute):
            path3= path1 + "\\" + "Test"
            print fname
            print fname_heute
            shutil.copy(fname, fname_heute)
            print Teil2 
            print heute
            path_archiv= path1 + "\\" + "Archiv"
            print path_archiv
            print fname_heute
            os.rename(path1 + "/" + fname, path1 + "/Upload-Bereit/Archiv/" + fname)
            os.rename(path1 + "/" + fname_heute, path1 + "/Upload-Bereit/" + fname_heute)
        
        
        if os.path.exists(path1 + "/" + fname_heute):
            print fname
            print fname_heute
            #shutil.copy(fname, fname_heute)
            path_archiv= path1 + "\\" + "Archiv"
            print path_archiv
            print fname_heute
            #os.rename(path1 + "/" + fname, path1 + "/Upload-Bereit/Archiv/" + fname)
            os.rename(path1 + "/" + fname_heute, path1 + "/Upload-Bereit/" + fname_heute)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#        path2 = path1.split("/")                                                                                                                         #Pfad wird gesplittet
#       print path2                                                                                                                                      #Aufruf neuer Splits
#        path_a = path2[0] + "\\" + "\\" + path2[1] + "\\" + "\\" + path2[2] + "\\" + "\\" + path2[3] + "\\" + "\\" + path2[4] + "\\" + "\\" + path2[5]   #Splits werden neu geordnet
#        print ("Speicherort")
#        print path_a                                                                                                                                     #umgestellter Aufrufpfad
       
#        path3 = path_a                                                                                                                                   #Split wird in Variable verwandelt
#        ziela = "\\" + "\\" + ziele[1] + "\\" + "\\" + ziele[2] + "//" + ziele[3]                                                                        #Ausgabepfad wird neu geordnet
#        print ziela
        
#        zielb = ziela                                                                                                                                    #Split wird in Variable umgewandelt
#        zielort = path3 + zielb                                                                                                                          #Zielort wird aus 2 Variablen zusammengefügt
#        print ("zielort =")
#        print zielort                                                                                                                                    #Zielort wird aufgerufen
        
#        path_1=zielort
#        print path_1
        
#        portal_endname = portal[1]                                                                                                                       #Variable wird für Split erstellt
#        print portal_endname
#        path2 = "zielort"
        
        #zielort =
         
        
        
        
#        print portal_endname                                                                                                                            #zeigt End-Name an
#        os.rename(path + "/" + fname, ziela + "/" + portal_endname)                                                                                    #verschiebt Datei in anderen Ordner und nennt sie um
#        os.rename(path + "/" + fname, path + "/" + portal_endname) # umbennen
#        print (path + "/" + portal_endname)

#        os.rename(path + "/" + portal_endname, zielort + "/" + portal_endname) #verschieben
#        print (zielort + "/" + portal_endname)
        
#        print(fname, portal_endname)                                                                                                                    #zeigt Namensänderungen an
        
        


# 3. Datei am Zielort ablegen



                





#Auf was wird die Datei umbenannt
# 1. Aktuelles Datum
#Aktuelles Datum vom System holen
#timestr = time.strftime("%Y-%m-%d_%H-%M")
#aktuelles_datumstr = time.strftime("%Y-%m-%d_%H-%M")
#timestr = time.strftime("%Y-%m-%d_%H-%M")
#timestr_log = time.strftime("%Y-%m-%d %H:%M")
#print timestr
#print timestr_log
#print aktuelles_datumstr

#os.rename(path + "/00" + "/" + ScanName, path + "/00/Fehler/" + ScanName + "_Portal_findet_Zielordner_nicht_" + Dateiname_Neu) #verschiebt Datei in anderen Ordner und nennt sie um
#os.rename(path + "/00" + "/" + ScanName, pfad_gesamt.decode('utf-8') + "/" + Dateiname_Neu.decode('utf-8')) #verschiebt Datei in anderen Ordner und nennt sie um  
#------------------------------------------------------------------------------



#def logschreiben(eineoperation):
#    with open('auto-dispo-log.txt', 'a') as f:
#        f.write(eineoperation)
#        f.close()
        
#        return
#------------------------------------------------------------------------------

#with open('DE_MS_742060_'+timestr+'.csv', 'wb') as csvfile:
#    filewriter = csv.writer(csvfile, delimiter=';')
#    filewriter.writerow(['EAN','EK','sofortLieferbar'"\n"]) 
#    filewriter.writerow([123.645,'2345.67','2,23',"\n"])
#    eineoperation="auto-dispo started running: "+timestr_log+";""\n\n"
#    logschreiben(eineoperation)


    




