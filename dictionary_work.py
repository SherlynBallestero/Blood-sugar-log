import json
import datetime

#collection of answers for guia
file_form=['Date','Level','Time','Notes']

def open_dictionary(directory_path):
    '''
    Returns a string == No if the required JSON directory does not exist, 
    if it exists, it returns it
    '''
    
    try:
        with open(directory_path, 'r') as file:
            answer=json.load(file)
            return answer
    except:
        answer={ "day1":{'Como se veria un dia en tu vida ideal?:':'', 'Donde te encuentras y que te hace falta para estar ahi':""}}
        print(answer)
        return 'No'

def save_directory(directory_path, file):
    '''
    This function incorporates the corresponding data for the current day into 
    the daily data collection dictionary. If any data does not exist,
    it creates it with the current day's data.
    '''
    date = str(datetime.datetime.now())
    dictionary=open_dictionary(directory_path)
    if dictionary == 'No':
        # Obtener la fecha actual
        files={date: file}
        # To save json
        with open(directory_path, "w") as archivo:
            json.dump(files, archivo)
    else:
        dictionary[date]=file
         # To save json
        with open(directory_path, "w") as archivo:
            json.dump(dictionary, archivo)
 
 
#proof_place....           
# file={'Como se veria un dia en tu vida ideal?:':'', 'Donde te encuentras y que te hace falta para estar ahi':""}        
# save_directory('./files', file)
        
        