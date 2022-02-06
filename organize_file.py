import os
from shutil import move

def organize_file(filename, types_dict, recap, recap_readonly, dir_name):

    # se il nome corrente è relativo ad un file
    if(os.path.isfile(dir_name+'/'+filename)):
        if(filename!='recap.csv'):  # (ignoro il file recap.csv)
            # estraggo estensione del file
            name, ext = os.path.splitext(os.path.basename(dir_name+'/'+filename))
            # aggiungo controllo per verificare se un file è stato spostato
            moved = False
            # itero sui tipi di file
            for file_type in types_dict.keys():
                # se l'estensione del file corrente corrisponde ad uno dei formati corrispondenti al tipo corrente
                if(ext in types_dict[file_type]):
                    # verifico che esista directory corrispondente (se non esiste la creo)
                    if(not os.path.isdir(dir_name+'/'+file_type)):
                            # creo la directory
                            os.mkdir(dir_name+'/'+file_type)
                    # stampo info
                    infos = name, file_type, str(os.stat(dir_name+'/'+filename).st_size)
                    print('{} type:{} size:{}B'.format(*infos))
                    # creo il nuovo record da inserire nel file .csv
                    record = ','.join(infos)+'\n'
                    # imposto posizione all'interno del file all'inizio
                    recap_readonly.seek(0)
                    # se il record non è già presente nel file
                    if(record not in recap_readonly):
                        # aggiorno file recap.csv con il nuovo record
                        recap.write(record)
                    # sposto il file nella directory corrispondente
                    move(dir_name+'/'+filename, dir_name+'/'+file_type)
                    moved = True
            # se il file non è stato riconosciuto stampo messaggio di errore
            if(not moved):
                print('WARNING: file {} not moved (format not recognized)'.format(filename))
