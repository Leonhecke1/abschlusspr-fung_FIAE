# Automatisierte Schnittstellen-Regressionstests WIP

## Dokumentation für Bereich MMS

## Inhaltsverzeichnis
- [Übersicht](#Übersicht)
- [Abhängigkeiten](#Abghängigkeiten)
- [Umgebungsvariablen](#Umgebungsvariablen)
- [Struktur des Skripts](#StrukturSkript)
- [Struktur des HTML-Berichts](#StrukturReport)
- [Struktur der Testfälle](#StrukturTestcase)
- [Fehlererkennung](#Fehlererkennung)
- [Hinweis](#Hinweis)
- [Installation](#Installation)
- [Verwendung](#Verwendung)
- [Fazit](#Fazit)

## [Übersicht](#Übersicht)

Dieses Skript führt automatische Schnittstellen-Regressionstests durch, indem es erwartete lokale Daten mit den tatsächlichen API-Antworten vergleicht, und generiert einen HTML-Bericht, der etwaige Unterschiede hervorhebt. Die Test-Szenarien sind in JSON-Dateien im Verzeichnis "testcases" definiert.

## [Abhängigkeiten](#Abhängigkeiten)

- axios: Ein auf Versprechungen basierender HTTP-Client für das Senden von API-Anfragen über Node.
- path: Ein Modul zur Verarbeitung von Dateipfaden.
- fs: Ein Modul zur Interaktion mit dem Dateisystem.
- Diff: Eine Bibliothek zum Berechnen von Unterschieden zwischen zwei Datensätzen.
- diff2html: Eine Bibliothek zum Rendern und Stylen von Diff-Ausgaben.
- dotenv(optional): Ein Modul zum Laden von Umgebungsvariablen aus einer ".env"-Datei.
- jsonabc: Eine Bibliothek zum Sortieren von JSON-Objekten in einer kanonischen Reihenfolge.
- luxon: Eine Bibliothek zur Arbeit mit Datum und Uhrzeit.

## [Umgebungsvariablen](#Umgebungsvariablen)

  - TOKENURL: Die URL zum Abrufen des API-Zugriffstoken.
  - USERNAME: Der Benutzername für die Authentifizierung.
  - PASSWORD: Das Passwort für die Authentifizierung.

## [Struktur des Skripts](#StrukturSkript)

1. Umgebungseinrichtung:
   - Import der erforderlichen Module und Bibliotheken.
   - Laden von Umgebungvariablen mit "dotenv".
     
2. Lesen der Testfälle:
   - Lesen von JSON-Testfällen aus dem Verzeichnis "testcases".
   - Speichern der Testfall-Daten im Array "apiRequests".
     
3. Funktion für API-Anfragen:
   - Authentifizierung und Abrufen eines Zugriffstokens mit dem bereitgestellten Anmeldeinformationen.
   - Iteration durch jeden Testfall und Durchführung von API-Anfragen.
   - Vergleich der API-Antwort mit dem erwarteten lokalen Daten.
   - Protokollieren von Unterschieden oder erfolgreichen Tests.
     
4. Generierung des HTML-Berichts:
   - Definition einer Funktion zur Generierung eines HTML-Berichts.
   - Verwendung von "diff2html" zur Formatierung und Hervorherbung von Unterschieden in einer "side-to-side"-Ansicht.
   - Verwendung von "luxon" zum einbeziehen der Zeitstempel.
   - Einbeziehung von zusätzlichen Informationen im HTML-Bericht.
     
5. Hauptausführung:
   - Aufruf der Funktion "apiRequest" zur Initiierung der API-Tests.
   - Generierung des HTML-Berichts basierend auf Ergebnissen.

## [Struktur des HTML-Berichts](#StrukturReport)
  - Der HTML-Bericht ernthält einen Zeitstempel und eine Liste der erfolglosen Tests mit Titel, Beschreibung und hervorgehobenen Unterschieden. Die Unterschiede werden in einer "side-to-side"-Ansicht dargestellt.
  - Erfolgreiche Tests sind ebenfalls im Bericht enthalten, mit Titeln und Beschreibungen.

## [Struktur der Testfälle](#StrukturTestcase)
  - "title": der Titel des Testfalls.
  - "description": eine kurze Beschreibung, was in dem Testfall getestet wird.
  - "steps": die einzelnen Schritte wie die Schnittstelle angefragt wird:
     1. "method": Die Art was für einen Request man der Schnittstelle schickt.
     2. "url": Die URL der Schnittstelle
     3. "body": Falls vorhanden, die übergebenen Body inhalte des Requests.
     4. "localDataPath": der Pfad, wo die lokale JSON liegt, um diese gegen die Schnittstelle zu testen.
  - Für gewöhnlich wird für jeden einzelnen Testfall ein neuer Nutzer erstellt und am Ende wieder gelöscht.
    

## [Fehlererkennung](#Fehlererkennung)
  - Alle Fehler während der API-Anfragen oder der Generierung des HTML-Berichts werden in der Konsole präsentiert.

## [Hinweis](#Hinweis)
  - Stellen Sie sicher, dass eine ".env"-Datei mit den erforderlichen Umgebungsvariablen für die Authentifizierung vorhanden ist.

## [Installation](#Installation)
  - Stellen Sie sicher, dass die neuste Version von Node.js auf ihrem System installiert ist.
    Sie können die neuste Version von Node von der offiziellen Seite downloaden und installieren: [Node.js official website](https://nodejs.org/).

### Klonen des Repositories

1. Klonen Sie dieses Repository auf ihr System:

   ```shell
   git clone https://hierLinkFürRepo.git

2. Navigieren Sie in das Projektverzeichnis:

   ```shell
   cd Axios

4. Installieren der Abhängikeiten:

   ```shell
   npm install

## [Verwendung](#Verwendung)
  - Platzieren Sie JSON-Testfälle im Verzeichnis "testcases".
  - Führen Sie das Skript aus:

    ```shell
    node regression.js

  - Der HTML-Testbericht wird in dem Verzeichnis "results" erstellt.

## [Fazit](#Fazit)
Dieses Skript bietet eine flexible und automatisierte Möglichkeit zur Durchführung von API-Tests, Identifizierung von Unterschieden und Generierung eines umfassenden HTML-Berichts zur Analyse. Anpassungen am Skript können vorgenommen werden, um spezifischen Testanforderungen gerecht zu werden.
