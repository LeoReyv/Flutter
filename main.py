import flet 

from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    Page,
    Ref,
    row,
    Container,
    Card,
    InputBorder,
    ElevatedButton,
    NavigationRail,
    NavigationBar,
    MainAxisAlignment,
    CrossAxisAlignment,
    NavigationRailLabelType,
    TextStyle,
    NavigationRailDestination,
    Row,
    Icon,
    Tab,
    Tabs,
    VerticalDivider,
    Text,
    TextField,
    UserControl,
    colors,
    icons,
    BoxShape,
)


from get_data import  get_database


dbase=get_database()

class Compras(UserControl):
    def __init__(self, producto, precio:float, agregar_producto):
        super().__init__()
        self.task_producto  = producto
        
        self.agregar_producto= agregar_producto
        self.precio    = precio
        self.task_cantidad=1
        #self.agregar_producto(self,self.precio)
        
        
        
    def build(self):
        #self.total=self.precio
        
        self.display_task=TextField(label="producto -",
        label_style=TextStyle(size=20,color="black") ,
        border=flet.InputBorder.UNDERLINE, disabled=True,
         value=self.task_producto,text_size=32,
        text_style=TextStyle(color="black",size=25))
        self.total_view=0
        self.task_cantidad_view=Text(f"{self.task_cantidad}")
        
        
        
        self.task_precio = Text(f"{self.precio}",size=32)
        
       
        self.task_total_compra=Text(f"{self.total_view}")

        self.display_items=Row(controls=[ IconButton(
                        visible =True,
                        icon = icons.ARROW_LEFT,
                        
                        on_click=self.quitar_producto2,
                        ),
                        self.task_cantidad_view,
                        IconButton(
                        visible = True,
                        icon=icons.ARROW_RIGHT,
                        on_click=self.agregar_producto2 
                        
                        
                        ),
                        IconButton(
                        icon = icons.ATTACH_MONEY,disabled=True
                        ),self.task_precio ])


        self.display_view= Row(expand=True,
            
            controls=[
                 self.display_task,
            ]
                 
            
        )
        return(Column (expand=True,controls=[Row(controls=[self.display_view,self.display_items]),
                            ],
                            ))
    

    def agregar_producto2(self,e):
        self.total_view+=float(self.task_precio.value)
        
        self.task_cantidad=self.task_cantidad+1
        print("agregar2")
        print(self.total_view)
        #print(self.task_precio.value)
        self.update()



    def quitar_producto2(self, e):
        self.total_view-=float(self.task_precio.value)
        
        self.task_cantidad=self.task_cantidad-1
        print("quitar2")
        print(self.total_view)
        
        
        self.update()
    
    def update(self):
        
           
        
        
        self.task_cantidad_view.value=f"{self.task_cantidad}"
        self.task_total_compra.value=f"{self.total_view}"
        super().update()
    

class NoTasK(UserControl):
    def __init__(self, error):
        super().__init__()
        self.task_error = error

    def build(self):
        

        self.display_view=Row(controls=[TextField(value=self.task_error,
        expand=True, 
         border=flet.InputBorder.UNDERLINE, disabled=True,
         text_style=TextStyle(color="black",size=25)
         )])
        return(self.display_view)
class Task(UserControl):
    def __init__(self, task_producto,task_cantidad, task_precio):
        super().__init__()
        self.task_producto  = task_producto
        self.task_cantidad  = task_cantidad
        self.precio    = task_precio
        
     

    def build(self):
        self.display_task=TextField(label="producto -",
        label_style=TextStyle(size=20,color="black") ,
        border=flet.InputBorder.UNDERLINE, disabled=True,
        expand=True, value=self.task_producto,text_size=32,
        text_style=TextStyle(color="black",size=25))

        self.precio = Text(self.precio,size=32)
        self.display_view= Row(
            
            controls=[
                 self.display_task,
                 Row(
            
                    spacing=10,
                    controls=[
                        IconButton(
                            visible =False,
                            icon = icons.ARROW_LEFT
                        ),
                        TextField(
                            self.task_cantidad,color="black",size=25,width=50,
                            ),
                        IconButton(
                            visible = False,
                            icon=icons.ARROW_RIGHT,
                            icon_color="black",
                            icon_size=30,
                        ),
                        IconButton(
                            icon = icons.ATTACH_MONEY,
                            icon_color="black",
                            icon_size=30,
                        ),
                        
                        self.precio
                        ,

                    ],
                 )
            ]
        )

        return(self.display_view)


class Compra(UserControl):
    
    
    

    def build(self):
        self.precio=0.0
        self.new_precio=0.0
        self.task_cantidad=1
        self.total=0
        self.total_view=0
        self.new_compra = TextField(
            hint_text="producto",
            on_submit=self.agregar_click,
            expand = True)
        self.compras = Column()
        self.task_total_compra=Text(f"{self.total_view}")
        
        
        
        return Column(
            expand=True,
                   
                    controls=[
                
                        Row(
                            controls=[
                            self.new_compra,
                            FloatingActionButton(icon=icons.ADD, on_click=self.agregar_click),
                           
                            ],

                        ),
                    
                        Column(
                            spacing=25,
                            controls=[
                                
                                self.compras,
                                 
                                ]

                        ),Row(controls=[self.task_total_compra])
                       
                                
                        ]

            
                )

    
    
    def get_precios(self,producto):
        
        dbname=dbase
        test=dbname["registros"]
        dic=test.find({"nombre":producto})
        for b in dic:
            if b["nombre"]== producto:
                print("encontrado")
                prec=b["precio"]

        self.total_view+=float(prec)
        print(prec)    
        return(float(prec))
        #precio=db
        
       

  

    def agregar_click(self, e):
    
        if self.new_compra.value:
            self.new_precio=self.get_precios(self.new_compra.value)
           
           
            
            task=Compras(self.new_compra.value,self.new_precio,self.agregar_producto)

        self.compras.controls.append(task)
        #total_precio=self.total_view+self.new_precio
        self.update()

   
            
            


    def total_view(self, e):
        
        
        #self.total=total_compras
        
        #print(self.total_view)
        #print(total)
        print("agregar_producto")
        print(self.total_view)
        #self.update()
        self.update()
        
       

    def update(self):
        
        

        
        #self.task_total
        print("agregar_update")
        print(self.total_view)
        
        
       
        
        super().update()

class Registro(UserControl):
      
    

    def build(self):
        self.total=0
        
        self.nombre_task= TextField(hint_text="Nomre del producto",hint_style=TextStyle(color="black"),label_style=TextStyle(color="black"),color="black",expand=True)
        self.precio_task= TextField(hint_text="Precio del producto",hint_style=TextStyle(color="black"),color="black", expand=True)
        self.buton_task= ElevatedButton(text="Registrar",on_click=self.registro_click)
        self.tasks = Column()
        
        
        
        return Row(
            expand=True,
                            vertical_alignment=MainAxisAlignment.SPACE_BETWEEN,
                    controls=[

                            Column(
                                expand=True,
                                spacing=20,
                                horizontal_alignment="center",
                                controls=[
                                    Row(
                                        controls=[self.nombre_task,]                           
                                        ),
                                    Row(
                                        controls=[self.precio_task,]
                                    ),                       
                                ]
                        ) ,VerticalDivider(),
                            Column(
                                controls=[
                                    
                                   
                                        Row(controls=[self.buton_task])
                                        
                                    
                                ]
                            ),
                        
                      
                    ]
                    
        )
               
            
    def registro_click(self, e):
        # if self.nombre_task.value and self.precio_task.value:
        #    #respuesta =registro_producto(self.nombre_task.value,float(self.precio_task.value))
        # if respuesta==True:
        print("incercion exitosa")
                
                   
                    
        

class TodoApp(UserControl):
    
   
    
    

    def build(self):
        self.total=0
        self.new_task = TextField(
            hint_text="busqueda",hint_style=TextStyle(color="black"),
            on_submit=self.button_clicked,
            color="black",
            expand = True)
        self.tasks = Column()
        self.task_total_lista=Text(size=32,color="black")
        self.filter=Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab( tab_content=Text("lista de compras",color="black")),
                  Tab( tab_content=Text("lista de compras",color="black")),
                  Tab( tab_content=Text("lista de compras",color="black")),
                  Tab( tab_content=Text("lista de compras",color="black"))],
            )
        
        
        return Column(
            expand=True,
                   
                    controls=[
                
                        Row(
                            controls=[
                            self.new_task,
                            ElevatedButton(text="Submit", on_click=self.button_clicked),
                           
                            ],

                        ),
                    
                        Column(
                                alignment="center",
                            spacing=25,
                            controls=[
                                self.filter,
                                self.tasks,
                                 
                                ]

                        ),Row(
                            
                            vertical_alignment="center",
                            alignment=MainAxisAlignment.END ,
                            
                            controls=[Container(content=self.task_total_lista,
                            padding=flet.padding.symmetric(horizontal=20)),
                                
                                
                                
                                
                                
                             ],
                                ),
                                
                        ]

            
                )
                
                
                   
                    
        
   
            
        
    def get_collection(self):
        try:
            dbname=dbase
            if dbname is None:
                dbname = get_database() 
            
            
            return(dbname["productos"] )
        except Exception as e:
            return(False)



            
    def button_clicked(self, e):
        dic_sec =[]
        self.total=0
        self.tasks.controls.clear()
        self.update()
        
        try:
            collection_name = dbase["productos"]
            cliente=collection_name.find({"cliente":self.new_task.value})
            print(cliente[0]["cliente"])
            if  cliente[0]["cliente"]==self.new_task.value:
                print("cliente  existe:")
            else:
                print("no existe")
                collection_name=get_database()
                cliente=collection_name["productos"]
                

            
            for n in cliente:
                data=n['lista']

            print(data)
            for n in data:
                dic_sec.append(n['producto'])

            for i in range(len(data)):
                self.total=self.total + float(dic_sec[i]["precio"])*int(dic_sec[i]["cant"])
                task=Task(dic_sec[i]["nombre"],dic_sec[i]["cant"],dic_sec[i]["precio"])
                
                
                self.tasks.controls.append(task)
        except Exception as ex:
            error="Cliente no existe pruebe nuevamente"
            task=NoTasK(error)
            self.tasks.controls.append(task)
        finally:
            self.update()

    def tabs_changed(self, e):
        if self.filter.selected_index==1:
            self.tasks.visible=False
        elif self.filter.selected_index==0:
            self.tasks.visible=True
        self.update()

    
    def update(self):
       
       #self.task_total.value= f"Total = {self.total}"
        super().update()


class Con(UserControl):
    def build(self):

      
        
        self.c1 = Container(
            

            
            content= TodoApp(),
            
            border_radius=20,
            margin=10,
            padding=flet.padding.symmetric(horizontal=10,vertical=50),
            alignment= flet.alignment.center,
            bgcolor=flet.colors.BLUE_ACCENT_100
            
           
        )

        self.c2 =Container(
            content=Registro(),
            visible=False,
             border_radius=20,
            margin=10,
            padding=flet.padding.symmetric(horizontal=10,vertical=50),
            
            bgcolor=flet.colors.LIGHT_BLUE_100,
            
        )

        self.c3 = Container(
            content=Compra(),
            visible=False,
             border_radius=20,
            margin=10,
            padding=flet.padding.symmetric(horizontal=10,vertical=50),
            
            bgcolor=flet.colors.BROWN_500,
        )

        return Column(  expand=True,          
                
                    alignment=MainAxisAlignment.SPACE_AROUND,
                    controls=[
                            self.c1,  
                            self.c2, 
                            self.c3,
                            Row( alignment="spaceAround",
                                
                                vertical_alignment="center",
                                controls=[  
                                        ElevatedButton(text="Inicio",on_click=self.button_clicked3),
                                        ElevatedButton(text="Buscar",on_click=self.button_clicked),
                                        ElevatedButton(text="Agregar",on_click=self.button_clicked2),
                                        ElevatedButton(text="Historial",on_click=self.button_clicked)
                                ]
                            ),
                        ]
                    )


    def button_clicked2(self,e):
        self.c1.visible=False
        self.c2.visible=True
        self.c3.visible=False
        self.update()

    def button_clicked(self,e):
        self.c1.visible=True
        self.c2.visible=False
        self.c3.visible=False
        self.update()
    
    def button_clicked3(self,e):
        self.c1.visible=False
        self.c2.visible=False
        self.c3.visible=True
        self.update()
  
def main(page: Page):
    page.expand=True
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.window_max_height=800
    page.window_max_width=1200
    page.window_min_height=600
    page.window_min_width=800    
    
    page.window_bgcolor=flet.colors.BLUE_GREY_400
    page.update()
   
    # create application instance
    app=Con()
   # app2= Otra()
        # def router_change(route):
    
   
   
    page.add(app)

    
    
flet.app(target=main)

#flet.app(target=main, view=flet.WEB_BROWSER)