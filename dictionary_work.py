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
        return 'No'

def save_directory(directory_path, file):
    '''
    This function incorporates the corresponding data for the current day into 
    the daily data collection dictionary. If any data does not exist,
    it creates it with the current day's data.
    '''
    #date = str(datetime.datetime.now())
    dictionary=open_dictionary(directory_path)
    if dictionary == 'No':
        index="0"
        # Obtener la fecha actual
        files={index: file}
        # To save json
        with open(directory_path, "w") as archivo:
            json.dump(files, archivo)
    else:
        index=len(dictionary)
        dictionary[str(index)]=file
         # To save json
        with open(directory_path, "w") as archivo:
            json.dump(dictionary, archivo)
 
 
def delete_row(directory_path, index):
    '''
    This function deletes the row that is passed as an argument.
    '''
    dictionary=open_dictionary(directory_path)
    dictionary.pop(index)
    with open(directory_path, "w") as archivo:
        json.dump(dictionary, archivo)
        
        