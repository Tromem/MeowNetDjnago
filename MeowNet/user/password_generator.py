import random
import re
import string 
from string import digits,ascii_letters ,punctuation
def password_generator():
    
    while True:
        password = ''.join([random.choice(ascii_letters +digits + punctuation) for i in range(16)]) 
        if not re.findall(rf'[{punctuation}{digits}]',password):
            password = ''.join([random.choice(ascii_letters +digits + punctuation) for i in range(16)]) 
            return password   
    
        
def login_generator(ru_names):
    translit_dict = {
    'а':'a','б':'b','в':'v','г':'g','д':'d','е':'e','ё':'yo','ж':'zh',
    'з':'z','и':'i','й':'y','к':'k','л':'l','м':'m','н':'n','о':'o',
    'п':'p','р':'r','с':'s','т':'t','у':'u','ф':'f','х':'kh','ц':'ts',
    'ч':'ch','ш':'sh','щ':'shch','ъ':'','ы':'y','ь':'','э':'e','ю':'yu','я':'ya',
    # Заглавные
    'А':'A','Б':'B','В':'V','Г':'G','Д':'D','Е':'E','Ё':'Yo','Ж':'Zh',
    'З':'Z','И':'I','Й':'Y','К':'K','Л':'L','М':'M','Н':'N','О':'O',
    'П':'P','Р':'R','С':'S','Т':'T','У':'U','Ф':'F','Х':'Kh','Ц':'Ts',
    'Ч':'Ch','Ш':'Sh','Щ':'Shch','Ъ':'','Ы':'Y','Ь':'','Э':'E','Ю':'Yu','Я':'Ya'
    } 
    return ''.join(translit_dict.get(c) for c in ru_names.replace(" ", "")) + '_'+''.join([random.choice(digits) for i in range(5)])

