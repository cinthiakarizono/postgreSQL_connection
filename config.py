from configparser import ConfigParser

def config(filename = 'database.ini', section = 'postresql'):
    parser = ConfigParser()
    parser.read(filename)
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
            
    else:
        raise Exception (f'section {0} not found in the {1} file')
    return db

