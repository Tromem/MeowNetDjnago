import json
import os
from random import randint


    

print('Введите название файла без формата')
get_fyle_name = input()
city = ['Владивосток',"Хабаровск"]
def make_city(get_fyle_name,city_names):
    with open(f'{get_fyle_name}.json','w',encoding="UTF-8") as fyle:
        sity_cout= 1 
        sity_to_model = []
        for city in city_names:
            make_dict_city = {
            'model':'crm.city',
            'pk':sity_cout,
            'fields':{
                'city_name':city,
                
            }
        }
            print(make_dict_city)
            sity_cout = sity_cout + 1
            sity_to_model.append(make_dict_city)

        json.dump(sity_to_model,fyle,indent=4, ensure_ascii=False)

def make_homes(name):
    with open(f'{name}.json','r',encoding='UTF-8') as f:
        fyle_json = json.load(f)
        dict_conv_homes = []
        cout_homes = 1
        cout_adres = 1
        for key,values in fyle_json.items():
            for homes,inf in values.items():
                ports = inf.get('Количество доступных подключений')
                tech = None
                if ports > 0: tech = True 
                else: tech = False
                make_dict_homes = {
                'model':'crm.Home',
                'pk':cout_homes,
                'fields':{       
                       
                    'number_home':homes,                   
                    'ports':ports,
                    'tech_opportunity':inf.get('Тип подключения'),
                    'adres_name':cout_adres
                    
                }
            }
            
                cout_homes = cout_homes+1
                dict_conv_homes.append(make_dict_homes) 
             
            cout_adres = cout_adres + 1
    return dict_conv_homes

    
def make_adres(name):
    with open(f'{name}.json','r',encoding='UTF-8') as f:
        fyle_json = json.load(f)
        dict_conv_adres = []
        cout_adres = 1
        for key,values in fyle_json.items():
            make_dict_adres = {
            'model':'crm.adres',
            'pk':cout_adres,
            'fields':{
                'from_city':1,
                'index':'123456',
                'name_adres':key,
                
            }
        }
            cout_adres = cout_adres + 1
            dict_conv_adres.append(make_dict_adres)
    return dict_conv_adres

adres = make_adres(get_fyle_name)
home = make_homes(get_fyle_name)
make_city('city',city)

with open(f'{get_fyle_name}_new_adres.json','w',encoding="UTF-8") as fyle:
        json.dump(adres,fyle,indent=4, ensure_ascii=False)
with open(f'{get_fyle_name}_new_homes.json','w',encoding="UTF-8") as fyle:
        json.dump(home,fyle,indent=4,ensure_ascii=False)
       
       
    
   
        
       
        
        
