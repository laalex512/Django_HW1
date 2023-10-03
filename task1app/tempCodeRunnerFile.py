pathfile, mode='r', encoding='utf-8') as f:
        text = f.read()
        last_visit = text[text.rfind(visit_page):] # срез начиная с последнего вхождения слов main, about...
        last_visit = last_visit[:last_visit.find('\n')]
        return i