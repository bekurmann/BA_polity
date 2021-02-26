deutsche spracherkennung batch in folder:

parallel --tag -j 2 ocrmypdf -l deu '{}' 'output/{}' ::: *.pdf

after ocr: generate txt files

for file in *.pdf; do pdftotext -raw "$file" "$file.txt"; done

after txt: generate one .csv file


