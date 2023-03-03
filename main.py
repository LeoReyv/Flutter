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


from get_data import  get_collection,registro_producto,get_precios


collection_name = get_collection()
collection_registro = get_precios()
class Compra(UserControl):
    def __init__(self, task_new_compra):
        super().__init__()
        self.task_new_compra = task_new_compra

    def build(self):
        self.display_compra=TextField(label="producto -",label_style=TextStyle(size=20,color=colors.BLACK) ,border=flet.InputBorder.UNDERLINE, disabled=True,expand=True, value=self.task_new_compra,text_size=32,text_style=TextStyle(color=colors.BLACK,size=25))

class Task(UserControl):
    def __init__(self, task_producto,task_cantidad, task_precio):
        super().__init__()
        self.task_producto  = task_producto
        self.task_cantidad  = task_cantidad
        self.precio    = task_precio
        
     

    def build(self):
        self.display_task=TextField(label="producto -",label_style=TextStyle(size=20,color=colors.BLACK) ,border=flet.InputBorder.UNDERLINE, disabled=True,expand=True, value=self.task_producto,text_size=32,text_style=TextStyle(color=colors.BLACK,size=25))
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
                        Text(self.task_cantidad,color="black",size=28),
                        IconButton(
                        visible = False,
                        icon=icons.ARROW_RIGHT
                        ),
                        IconButton(
                        icon = icons.ATTACH_MONEY
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
        self.new_compra=TextField(
            hint_text="que desea llevar?",
            )
        self.compras=Column()
        self.total_articulos= Text("0")
        return Column(
            controls=[
                Row([Text(value="Lista de articulos",style="headlineMedium")],alignment="center"),
                Row([self.new_compra,FloatingActionButton(icon=icons.ADD,)]
                ),
                Column(spacing=20,
                controls=[
                    self.compras,
                   Container(
                    padding=flet.padding.symmetric(vertical=50),content=( Row(vertical_alignment=CrossAxisAlignment.END,
                    
                        controls=[self.total_articulos]))),
                   
                ])
            ]
        )

    def agregar_click(self, e):
        if self.new_compra.value:
            # precio=collection_registro.find({"registro":self.new_task.value})
            # if precio!= False:
            #     for n in precio:
            #         for m in n:
            #             if m["nombre"]==self.new_compra.value:
            #                 valor=m["precio"]
            #                 self.compras.controls.append()
            print("encontraso")



class Registro(UserControl):
      
    

    def build(self):
        self.total=0
        
        self.nombre_task= TextField(hint_text="Nomre del producto",expand=True)
        self.precio_task= TextField(hint_text="Precio del producto", expand=True)
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
        if self.nombre_task.value and self.precio_task.value:
           respuesta =registro_producto(self.nombre_task.value,float(self.precio_task.value))
        if respuesta==True:
            print("incercion exitosa")
                
                   
                    
        

class TodoApp(UserControl):
    
   
    
    

    def build(self):
        self.total=0
        self.new_task = TextField(
            hint_text="busqueda",
            on_submit=self.button_clicked,
            expand = True)
        self.tasks = Column()
        self.task_total=Text(f"Total = {self.total}",size=32)
        self.filter=Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="lista de compras"),Tab(text="Lista de clientes"),Tab(text="Lista de proveedores"),Tab(text="Productos")],
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
                            spacing=25,
                            controls=[
                                self.filter,
                                self.tasks,
                                 
                                ]

                        ),Row(
                            
                            vertical_alignment="center",
                            alignment=MainAxisAlignment.END ,
                            
                            controls=[Container(content=self.task_total,
                            padding=flet.padding.symmetric(horizontal=20)),
                                
                                
                                
                                
                                
                             ],
                                ),
                                
                        ]

            
                )
                
                
                   
                    
        
   
        
        


            
    def button_clicked(self, e):
        dic_sec =[]
        self.total=0
        self.tasks.controls.clear()
        self.update()
        if self.new_task.value:
            cliente=collection_name.find({"cliente":self.new_task.value})
            
            for n in cliente:
                data=n['lista']

            print(data)
            for n in data:
                dic_sec.append(n['producto'])

            for i in range(len(data)):
                self.total=self.total + float(dic_sec[i]["precio"])*int(dic_sec[i]["cant"])
                task=Task(dic_sec[i]["nombre"],dic_sec[i]["cant"],dic_sec[i]["precio"])
                
                
                self.tasks.controls.append(task)
            
            self.update()

    def tabs_changed(self, e):
        if self.filter.selected_index==1:
            self.tasks.visible=False
        elif self.filter.selected_index==0:
            self.tasks.visible=True
        self.update()

    
    def update(self):
        
        self.task_total.value= f"Total = {self.total}"
        super().update()


class Con(UserControl):
    def build(self):

        
        
        self.c1 = Container(
            

            
            content= TodoApp(),
            
            border_radius=20,
            margin=10,
            padding=flet.padding.symmetric(horizontal=10,vertical=50),
            alignment= flet.alignment.center,
            bgcolor=colors.AMBER,
            
           
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
            content=OutlinedButton("Outlined Button in Container"),
            visible=False,
            bgcolor=colors.WHITE,
            padding=5,
        )

        return Column(  expand=True,          
                
                    alignment=MainAxisAlignment.SPACE_AROUND,
                    controls=[
                            self.c1,  
                            self.c2, 
                            Row( alignment="spaceAround",
                                
                                vertical_alignment="center",
                                controls=[  
                                        ElevatedButton(text="Inicio",on_click=self.button_clicked),
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
        self.update()

    def button_clicked(self,e):
        self.c1.visible=True
        self.c2.visible=False
        self.update()
    
    
  
def main(page: Page):
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.window_max_height=800
    page.window_max_width=1200
    page.window_min_height=600
    page.window_min_width=800    
    page.update()
   
    # create application instance
    app=Con()
   # app2= Otra()
        # def router_change(route):
    
   
    
    page.add(app)

    
    
flet.app(target=main)

#flet.app(target=main, view=flet.WEB_BROWSER)