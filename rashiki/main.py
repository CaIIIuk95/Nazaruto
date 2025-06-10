import re
import dateparser



text = "7 (903) 402-14-88 Николь Попова \
А еще напишу в єтом тексте что русню ебал 89038765467,затем без 7 напишу номер 9037876562 \
Позвоните мне на +7 (912) 345-67-89 или на 8 913 456 78 90. \
Ещё вариант: 89123456789 или 7-915-123-45-67 вот такі русячіє прімєри, ще є 14 і 22 циферки,\
шоб глянуть чи не сработає на якусь дічь маленьку а далі текст з різними датами.\
Мы начали разработку проекта ещё 12.05.2023, но из-за задержек в поставках его реализация сдвинулась.\
В документации указано, что конечный срок сдачи — 2023-10-01, однако на встрече 3 октября 2023 года было решено продлить контракт.\
Следующая проверка запланирована на 15/11/23, а общее собрание пройдёт 01 Декабря 2023.\
Финальный отчёт нужно будет подготовить к 5 янв 24, а презентация состоится 25.12.2023 в 10:00.\
Помимо этого, в календаре стоит напоминание на Wednesday, 20 December 2023."

numbers_pattern = r'(?:\d[\s\-\(\)]*){10,11}'
date_pattern = re.compile(r"""
    \b\d{1,2}\.\d{1,2}\.\d{2,4}\b   |
    \b\d{4}\.\d{1,2}\.\d{1,2}\b     |
    \b\d{1,2}-\d{1,2}-\d{2,4}\b     |    
    \b\d{4}-\d{1,2}-\d{1,2}\b       |
    \b\d{1,2}/\d{1,2}/\d{2,4}\b     |
    \b\d{4}/\d{1,2}/\d{1,2}\b       | 
    \b\d{1,2}\s+[а-яА-Яa-zA-Z]+\s+\d{2,4}\b""", re.VERBOSE)
    

number_items = re.findall(numbers_pattern, text)
date_items = re.findall(date_pattern,text)
#print(date_items)

def number_taker(items):
    if items:
        result = []
        for item in items:
            try:
                formatted = re.sub(r'\D', '', item)
                formatted = re.sub(r'^8','7', formatted)
                formatted = re.sub(r'^9',r'7\g<0>', formatted)
                result.append(formatted)
                spaces = 20 - len(item)
                print(f"{item}{' ' * spaces}➝ {formatted}")
            except:
                print(f'Fail to convert number: {item}')
        #print(result)
        

def date_format(items):
    if items:
        result = []
        for item in items:
            try:
                dt = dateparser.parse(item)
                formatted = dt.strftime('%d-%m-%Y')
                result.append(formatted)
                spaces = 20 - len(item)
                print(f"{item}{' ' * spaces}➝ {formatted}")
            except:
                print(f'Fail to convert date: {item}')
        #print(result)


def def_open_file(file, number): #"DEF.csv"
    with open(file, "r", encoding = "utf-8") as f:
        for line in f:
            if line[:3] == number[1:4]:
                parts = line.split(';')
                if parts[1] <= number[4:11] <= parts[2]:
                    print(f"{number} | {parts[4]} | {parts[6]} | {get_utc(number)}")
                    


def get_utc(number):
    with open("rashiki/UTC.csv", "r", encoding = "utf-8") as f:
        for line in f:
            if line[:3] == number[1:4]:
                parts = line.split(',')
                if parts[0] == number[1:4]:
                    return parts[1]

                                 

#number_taker(number_items)
#date_format(date_items)
def_open_file("rashiki/DEF.csv", "79043709001")