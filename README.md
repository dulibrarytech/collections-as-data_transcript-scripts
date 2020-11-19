# collections-as-data_transcript-scripts

A series of scripts used to create transcripts

Specifically we used these scripts to create our ground truth and training datasets to train a model in Transkribus

word_finder - folder for the word helper made by Alice Tarrant at DU.
12dicts - dictionary of words
word_finder.py - python script when you run it and enter in partial words will give you suggestions on word candidates

clean_transcripts.py - cleaning transcript directories
cleanjcrs.py - batch naming digitized files in jcrs collection
convert.py - tiffs to images
countjcrs.py - file count per folder
pdf_rotate.py - rotate pdfs that were scanned with the incorrect orientation
