import flet as ft
from flet import (
    Column,
    Container,
    Page,
    Text,
    UserControl,
    border_radius,
    colors,
    alignment,
    padding,
    CircleAvatar,
    Theme,
    Divider,
    ListTile, Icon, icons, Image,
)
from pandas import DataFrame
from get_data import get_database
dbname = get_database()
collection_name = dbname["productos"] 
documents=collection_name.find()
import webbrowser
import json








def main(page: ft.Page):




    def button_clicked(e):
        
        
        
        
        
        
        
        
        #t.value = f"Textboxes values are:  '{tb1.value}', '{tb2.value}', '{tb3.value}', '{tb4.value}', '{tb5.value}'."
        page.update() 


    dic_con =[]
    dic_sec=[]

    print(collection_name.count_documents({}))
    
        
    
    print("\n\n")


    for n in collection_name.find({"cliente":"luis"}):
        dic_con=n['lista']
    

    print(dic_con)
    page.window_min_height =600
    page.window_min_width = 400    

    page.window_max_height =1000
    page.window_max_width =800
    
    
    
    print(len(dic_con))
    print("\n\n")
   
    # for i in range(len(dic_con)):
    #     for n in dic_con[i]:
    #         dic_sec=n['producto']


    # print(dic_sec)}
    cont=[]
    
    for n in dic_con:
        dic_sec.append(n['producto'])
        
            
    dic_ter=[]
    print(dic_sec)
    print(dic_sec[1]["nombre"])
    # t = ft.Text()
    #tb1 = ft.TextField(label="Standard")
    tb2 = ft.TextField(label="Disabled", disabled=True, value=dic_sec[1]['nombre'])
    # tb3 = ft.TextField(label="Read-only", read_only=True, value="")
    # tb4 = ft.TextField(label="With placeholder", hint_text="Please enter text here")
    # tb5 = ft.TextField(label="With an icon", icon=ft.icons.EMOJI_EMOTIONS)
    b = ft.ElevatedButton(text="Submit", on_click=button_clicked)
    #page.add(tb1, tb2, tb3, tb4, tb5, b, t)
    
    for i in range(len(dic_con)):
        dic_ter.append(ft.TextField(label="producto -"+str(dic_sec[i]['cant']), disabled=True, value=dic_sec[i]['nombre']))


    print(len(dic_ter))
    for ln in range(len(dic_ter)):

        page.add(dic_ter[ln-1])
    print(i)




ft.app(target=main, assets_dir="assets")