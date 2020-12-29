only works with utf-8 encoding! -> maybe use google sheets to download such a file (copy/paste)

settings for csv importer plugin ('csvimport.app.CSVImportConf' -> https://github.com/edcrewe/django-csvimport)
**********************************
-> only 3 columns
-> delete header and define mapping manually (below)

locations.PLZ

column1=name
column2=plz
column3=bfs_nummer(Municipality|bfs_nummer)
