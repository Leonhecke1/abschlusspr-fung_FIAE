# SQL Training
Wenn ihr Probleme mit der Installation habt meldet euch. Ich kann sonst auch eine VM aufsetzen auf die ihr euch mit SSH verbindet.
## Prerequisite*

SQLITE3
```bash
sudo apt install sqlite3
```
Python3.11  
nicht sicher ob niedrigere Versionen gehen. Falls etwas nicht klappt einfach melden. 

Python Venv
```bash
sudo apt install python3-venv
```
Pip
```bash
sudo apt install python3-pip
```
###### * befehle sind für Debian/Ubuntu 
---

1. Python Venv erstellen
```bash
python3 -m venv venv
```

2. aktivieren
```bash
. ./venv/bin/activate
# oder
source ./venv/bin/activate
```

3. SQL Alchemy installieren
```bash
pip install sqlalchemy
# Optional: confirm installation:
pip freeze
```

4. Optional: Datensätze erweitern.  
**Falls ihr Datensätze ergänzt, schickt sie mir ruhig, dann füge ich sie für alle auf dem main branch hinzu**  
Ich hatte keine Lust mehr mir Datensätze auszudenken ^^ 
Im Directory `src/data/` gibt es 3 `*_data.py` files. Da sind Listen zu finden die ihr entsprechend ergänzen könnt. 

5. create DB
```bash
python src/create_database.py 
```
Hier gibt es jede Menge Output wie die DB erstellt wird. 
Da könnt ihr gerne mit rein lesen.

6. Wenn benötigt (zB falls man neue Daten in die Datenbank laden will):
```bash
python src/delete_database.py 
```

7. Auf DB connecten
```bash
sqlite3 test.db 
```

8. Optional: Tabellen Header aktivieren
```
.headers on
```
