import os
from shutil import move
import argparse
from organize_file import organize_file

# istanzio ArgumentParser
parser = argparse.ArgumentParser()
# aggiungo argomento per CLI
parser.add_argument('filename', type=str, default='', help='filename')
# recupero argomento inserito
filename = parser.parse_args().filename

dir_name = 'files'   # valore default per directory corrente

# se (e finchè) la directory 'files' non esiste nel path corrente
while(not os.path.isdir(dir_name)):
    # chiedo all'utente di inserire il path alla directory corretta
    dir_name = input('"{}" directory not found. which directory would you use instead? (enter directory path) '.format(dir_name))

# definisco dizionario che mappi i tipi di file alle estensioni
types_dict = {'audio': ['.mp3','.wav','.mpeg'], 'images':['.jpg','.png','.jpeg'], 'docs':['.txt','.odt']}

# apro file recap in scrittura (appending)
recap = open(dir_name+'/'+'recap.csv', 'a')
# apro file recap in sola lettura (per verificare unicità record)
recap_readonly = open(dir_name+'/'+'recap.csv', 'r')

# verifico che filename iserito esista
if(os.path.isfile(dir_name+'/'+filename)):
    # eseguo funzione filename inserito
    organize_file(filename, types_dict, recap, recap_readonly, dir_name)
else:
    print('ERROR: {} does not exist!'.format(filename))
# chiudo i file
recap.close()
recap_readonly.close()
