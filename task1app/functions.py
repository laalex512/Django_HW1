

def import_count(pathfile: str):
    with open(pathfile, mode='r', encoding='utf-8') as f:
        text = f.read()
        if text:
            return int(text.split()[-1])
        return 0
    

        
        