import os 
from pathlib import Path 

ROOT = str(Path(__file__).parent.absolute())
path2EnvFile = str(Path(os.path.join(ROOT, '../..', '.env')).resolve())

def loadEnvFile(path:str=path2EnvFile) -> dict:
    '''
        Load the project Env keys 

        Parameter 
        ---------
            path : str | OPTIONAL, Absoloute path to the .env file.  

        Return 
        -------
            dict 
                Dictionary with the project Env Keys. example {'openWeather': 'API_KEY', ....}

        NOTE
        -----
            The text inside of the .env file must following the following structure/syntax 
                nameOfTheKey=KEYVALUE     
            No white spaces must exist between the  nameOfTheKey and the KEYVALUE  only the character '='
    '''
    if not os.path.exists(path):
        raise ValueError(f'The .env file does not exist!. {path}')
    list2dict = []
    with open(path, 'r') as objFile: 
        lines = objFile.readlines()
        if len(lines)<=0:
            raise ValueError(f'The .env file is empty. {path}')
        for line in lines:
            if len(line)==0:
                continue
            keyValue = line.find('=')
            if not keyValue:
                raise ValueError('The defined syntax for the key values are not correct')
            keyValue = [line[:keyValue], line[keyValue+1:].replace('\n', '') if '\n' in line[keyValue+1:] else line[keyValue+1:]]
            if len(keyValue) != 2:
                raise ValueError(f'Unexpected values while reading env file. The structure must be keyName=KeyValue and received {keyValue}')
            list2dict.append(keyValue)
    return {cList[0]:cList[1] for cList in list2dict}