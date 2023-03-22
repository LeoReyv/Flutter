import flet 
from datetime import datetime
import time , threading
from vista import VistaProducto
from flet import (
    Checkbox,
    Column,
    ButtonStyle,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    Page,
    Ref,
    Stack,
    TextAlign,
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


lista =[]
dbase=get_database()

class ListaProductos(Stack):
    def __init__(self,producto,precio):
        self.producto=producto
        self.precio=precio


class Clock(Text):
    def __init__(self):
        super().__init__()
        
        self.size=24
        self.color="black"
        self.visible=True
        
        self.value=None


    def did_mount(self):
        self.running=True
        self.th=threading.Thread(target=self.update_timer, args=(),daemon=True)
        self.th.start() 

    def will_unmount(self):
        self.running=True
    
    
    def update_timer(self):
        while self.running:
            clock_var=datetime.now()
            
            self.value= clock_var.strftime("%Y-%m-%d %H:%M:%S" )
            
            self.update()
            time.sleep(1)
    
class MostrarView(Stack):
    def __init__(self, mostrar):
        super().__init__()
        self.controls = []
        self.mostrar=mostrar
        

    def crear_stack(self):
        self.stack=[]
        self.stack=VistaProducto()
        
class VistaProducto(Container):
    def __init__(self, mostrar ):
        super().__init__()
        self.pile=[]
        self.mostrar=mostrar
        self.width=50
        self.height=110
        self.border=10
        self.border_radius = self.border_radius.all(6)
        self.bgcolor="green"
  
   
      



class Compras(UserControl):
    def __init__(self, producto, new_precio, task_cantidad,quitar_producto, agregar_producto):
        super().__init__()
        self.task_producto  = producto
        self.task_cantidad=task_cantidad
        
        self.task_precio    = new_precio
        #task_total=self.task_precio
        self.quitar_producto=quitar_producto
        
        self.agregar_producto=agregar_producto
        self.agregar_producto(self.task_precio)

        
       
   

    def build(self):
        self.task_total=self.task_precio
        #self.task_precio(self)
        self.display_task=TextField(label="producto -",
        label_style=TextStyle(size=20,color="black") ,value=self.task_producto,
        border=flet.InputBorder.UNDERLINE, disabled=True,
         text_size=32,
        text_style=TextStyle(color="black",size=25))
        
        self.task_cantidad_view=Text(f"{self.task_cantidad}",size=28,color="black")
        
        self.task_precio_view = Text(f"{self.task_precio}",size=32,color="black")
        
        
        

        self.display_items=Row(controls=[ IconButton(
                        visible =False,
                        icon = icons.ARROW_LEFT,
                        tooltip="arrow-quitar",
                        
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
                        ),self.task_precio_view ])


        self.display_view= Row(expand=True,
            
            controls=[
                 self.display_task,
            ]
                 
            
        )

        # return Row(expand=True,controls=[self.display_task,
        #                                 IconButton(
        #                                         visible =False,
        #                                         icon = icons.ARROW_LEFT,
        #                                         on_click=self.quitar_producto2,),
        #                                 self.task_cantidad_view,
        #                                 IconButton(
        #                                         visible = True,
        #                                         icon=icons.ARROW_RIGHT,
        #                                         on_click=self.agregar_producto2),
        #                                 IconButton(
        #                                         icon = icons.ATTACH_MONEY,disabled=True),
        #                                 self.task_precio_view

                                        
        #                                 ])
        return Row(expand=True,controls=[self.display_view,self.display_items])
    
    def agregar_producto2(self,e):
        
        self.task_total+=float(self.task_precio)
        self.task_cantidad=self.task_cantidad+1
        #self.task_cantidad_view.value=f"{self.cantidad}"
        self.agregar_producto(self.task_precio_view.value)
        print("agregar2")
        self.display_items.controls[IconButton.tooltip=="arro-quitar"].visible=True
        print(self.task_total)
        #self.task_cantidad(self)
        self.update()

    def total_total(self):
       

        return(self.task_total)
    def quitar_producto2(self, e):
        if self.task_cantidad>2:
            self.display_items.controls[IconButton.tooltip=="arro-quitar"].visible=True
            self.quitar_producto(self.task_precio_view.value)
            self.task_cantidad=self.task_cantidad-1
            #self.task_total-=float(self.task_precio)
            print("quitar2")
            
        #self.task_cantidad(self)
        elif self.task_cantidad==2:
            self.display_items.controls[IconButton.tooltip=="arro-quitar"].visible=False
            self.quitar_producto(self.task_precio_view.value)
            self.task_cantidad=self.task_cantidad-1
            #self.task_total-=float(self.task_precio)
        
        self.update()
    
    def update(self):
        
        #Compra.task_mostrar(self,total)
        self.task_cantidad_view.value=f"{self.task_cantidad}"
        self.display_task.value=f"{self.task_producto}"
        
        #self.task_total_compra.value=f"{self.total_view}"
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
    def __init__(self, task_producto,task_cantidad, task_precio,precio,cantidad):
        super().__init__()
        self.task_producto  = task_producto
        self.task_cantidad  = task_cantidad
        self.precio    = task_precio
        
     

    def build(self):

        self.display_task=TextField(
            label="producto -",
            label_style=TextStyle(size=20,color="black") ,
            border=flet.InputBorder.UNDERLINE, disabled=True,
            expand=True, 
            tooltip="sopa",
            value=self.task_producto,text_size=32,
            text_style=TextStyle(color="black",size=25))
        self.display_time_view=Text()

        self.precio = Text(
            self.precio,size=32)
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
        lista_total=0
        self.task_total=0
        self.new_precio=0.0
        self.task_cantidad=1
        self.task_precio=0.0
        self.total_view=0
        self.new_compra = TextField(
            hint_text="producto",
            on_submit=self.agregar_click,
            tooltip="sopa",
            expand = True,text_style=TextStyle(color="black",size=25))
        self.compras = Column()
        self.compras2= Stack()
        self.task_total_compra=TextField(value=f"Total={self.total_view}",
                                         text_style=TextStyle(size=32,color="black",),
                                         border=flet.InputBorder.UNDERLINE, disabled=True,
                                         
                                         
                                         text_align=TextAlign.END)
        
        self.clock_time_view=Clock()
        
        return Container(content=( Column(
            expand=True,
                   
                    controls=[
                        Container(width=200,content=(self.clock_time_view)),
                        
                        Row(
                            controls=[
                            self.new_compra,
                            FloatingActionButton(icon=icons.ADD, on_click=self.agregar_click),
                           
                            ],

                        ),
                    
                        
                                
                                Container(padding=flet.padding.symmetric(horizontal=40),
                                                  
                                                  content=(self.compras))
                                 
                                

                        ,Row(vertical_alignment=CrossAxisAlignment.END
                              ,
                              controls=[Container(expand=True,padding=flet.padding.symmetric(horizontal=40),
                                                  
                                                  content=(self.task_total_compra))])
                       
                                
                        ]

            
                )))

   
    
    def get_precios(self,producto):
        
        dbname=dbase
        test=dbname["registros"]
        dic=test.find({"nombre":producto})
        for b in dic:
            if b["nombre"]== producto:
                print("encontrado, precio")
                prec=b["precio"]

        #self.total_view+=float(prec)
        print(prec)    
        return(float(prec))
        #precio=db
        
       

  

    def agregar_click(self, e):
        count=0
        if self.new_compra.value:
            
            self.new_precio=self.get_precios(self.new_compra.value)
           
           
            
            tasks=Compras(self.new_compra.value,self.new_precio,self.task_cantidad,self.quitar_producto,self.agregar_producto)
            
           
              
            self.compras.controls.append(tasks)
            lista.append(self.new_compra.value)
          
            #total_precio=self.total_view+self.new_precio
            self.new_compra.value=""
            self.new_compra.focus()
            


           



            self.update()

        
           
               
           
    def quitar_producto(self,task_precio):
        self.task_precio=task_precio
        self.task_total= self.task_total-(float(self.task_precio))
        print("agregar")
        self.update()

    def agregar_producto(self,task_precio):
        self.task_precio=task_precio
        self.task_total= self.task_total+(float(self.task_precio))
        print("agregar")
        self.update()
            
    def task_mostrar(self,total):
        self.task_total=total
        self.update()
    # def task_cantidad(self, task):
              
        # self.task_cantidad
        # print("Compra task_cantidad")
        # print(self.task_cantidad)
        

    # def task_precio(self,task):
        
        
    #     self.update()
        
       

    def update(self):
        
        
        #self.task_total=Compras.total_total(self)
        
        
        self.total_view=self.task_total
       
       
        self.task_total_compra.value=f"Total = {self.total_view}"
        super().update()

class Registro(UserControl):
      
    

    def build(self):
        self.total=0
        
        self.titulo=TextField(value="Registro",text_size=38, expand=True, border=flet.InputBorder.UNDERLINE,)
        self.nombre_task= TextField(label="Nomre del producto",label_style=TextStyle(size=20,color="black") ,color="black",text_size=32,expand=True)
        self.precio_task= TextField(label="Precio del producto",label_style=TextStyle(size=20,color="black") ,color="black",text_size=32, expand=True)
        self.buton_task= ElevatedButton(width=200,height=70,content=Text(value="Registrar",size=30),on_click=self.registro_click)
        self.tasks = Column()
        self.clock_time_view=Clock()
        self.filter=Tabs(
            width=600,
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab( tab_content=Text("producto",color="black")),
                  Tab( tab_content=Text("clientes",color="black")),
                  Tab( tab_content=Text("proveedores",color="black")),
                  ],
            )
        
        return Column(expand=True,controls=[
            
                    Container(width=200,content=(self.clock_time_view)),
                    Row(
                        controls=[
                    Column(controls=[
                                Row(controls=[self.nombre_task,]),Row(controls=[self.precio_task,])],
                                expand=True,
                                spacing=20,
                                horizontal_alignment="center",
                           
                                ),
                    VerticalDivider(color="white",width=200,visible=True),
                    Column(width=200,controls=[
                                         Row(controls=[self.buton_task])]),],
                                                vertical_alignment=MainAxisAlignment.SPACE_BETWEEN,
                            ),
                  
                                ]
                    )
               
    
    def tabs_changed(self, e):
      
        self.update()


    def registro_click(self, e):
        # if self.nombre_task.value and self.precio_task.value:
        #    #respuesta =registro_producto(self.nombre_task.value,float(self.precio_task.value))
        # if respuesta==True:
        print("incercion exitosa")
                
                   
                    
        

class TodoApp(UserControl):
    
   
    
    

    def build(self):
        self.total=0
        self.titulo=TextField(value="Busqueda",text_size=38, expand=True,  border=flet.InputBorder.NONE,color="black",
                              text_align=TextAlign.CENTER)
        self.new_task = TextField(
            hint_text="busqueda",hint_style=TextStyle(color="black"),
            on_submit=self.button_clicked,
            color="black",
            expand = True)
        self.tasks = Column(width=800)
        self.task_total_lista=Text(size=32,color="black")
        self.filter=Tabs(
            expand=True,
             
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab( tab_content=Text("producto",color="black")),
                  Tab( tab_content=Text("clientes",color="black")),
                  Tab( tab_content=Text("proveedores",color="black")),
                  ],
            )
        self.clock_time_view=Clock()
        
        return Column(
            expand=True,
                   
                    controls=[ Container(bgcolor="white",content=(self.titulo)),
                        Container(width=200,content=(self.clock_time_view)),
                
                        Row(spacing=50,
                            controls=[
                            self.new_task,
                            ElevatedButton(content=(Text(value="Sumit",size=26)),on_click=self.button_clicked,width=150,height=70),
                           
                            ],

                        ),
                    
                       Container(bgcolor="green",content=( Column(
                              
                              expand=True,alignment=MainAxisAlignment.SPACE_BETWEEN,
                            horizontal_alignment=CrossAxisAlignment.CENTER,
                            spacing=25,
                            controls=[
                                Container(bgcolor="red", margin=20,content=(self.filter)),
                                Container(bgcolor="blue", content=(self.tasks))
                                 
                                ]

                        ))),Row(
                            visible=False,
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
                
                for n in cliente:
                    data=n['listas']
                    
                for n in data:
                    fecha=n["fecha"]
                    data2=n["producto"]
                    m=n["total"]
                   
                    print(fecha)
                for bm in data2:
              
                    print(bm)
                print(m)
                print("cliente  existe:")
            else:
                print("no existe")
                collection_name=get_database()
                cliente=collection_name["productos"]
                

            
            for n in cliente:
                data=n['listas']
                data2=n["producto"]
      
            # for n in data:
            #     cno=n
            #     for m in cno:
            #         dic_sec.append(m)
            #         print(m)
            # for i in range(len(data)):
            #     self.total=self.total + float(dic_sec[i]["precio"])*int(dic_sec[i]["cant"])
            #     task=Task(dic_sec[i]["nombre"],dic_sec[i]["cant"],dic_sec[i]["precio"])
                
                
                # self.tasks.controls.append(task)
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

class Mostrar(UserControl):
     def build(self):
       
        self.new_mostrar = TextField(hint_text="Mostrar",expand = True,text_style=TextStyle(color="black",size=25))

        self.mostrar = Column()
        
        
        
        self.clock_time_view=Clock()
        
        return  Column(
            expand=True,
                   
                    controls=[
                        Row( controls=[Container(width=200,bgcolor="white",
                            content=(self.clock_time_view))]),
                        Row( controls=[Container(width=200,bgcolor="white",
                            content=( self.new_mostrar))]),
                        Column( 
                               
                               controls=[Container(width=200,bgcolor="white",
                            content=(self.mostrar))]),
                                  
                                  ],
                    )
     
class Con(UserControl):
    def build(self):

      
        
        self.c1 = Container(
            

            
            content= TodoApp(),
            
            border_radius=20,
            margin=3,
            padding=flet.padding.symmetric(horizontal=15,vertical=1),
            alignment= flet.alignment.center,
            bgcolor=flet.colors.BLUE_ACCENT_100
            
           
        )

        self.c2 =Container(
            content=Registro(),
            visible=False,
             border_radius=20,
            margin=10,
            padding=flet.padding.symmetric(horizontal=10,vertical=50),
            alignment= flet.alignment.center,
            bgcolor=flet.colors.LIGHT_BLUE_100,
            
        )

        self.c3 = Container(
            content=Compra(),
            visible=False,
             border_radius=20,
            margin=10,
            padding=flet.padding.symmetric(horizontal=10,vertical=10),
            alignment= flet.alignment.center,
            bgcolor=flet.colors.BROWN_500,
        )

        self.c4 = Container(
            content=Mostrar(),
            visible=False,
             border_radius=20,
            margin=10,
            padding=flet.padding.symmetric(horizontal=10,vertical=50),
            alignment= flet.alignment.center,
            bgcolor=flet.colors.GREEN_100,
        )
        

        return Column(  expand=True,          
                
                    alignment=MainAxisAlignment.SPACE_AROUND,
                    controls=[
                            self.c1,  
                            self.c2, 
                            self.c3,
                            self.c4,
                            Row( alignment="spaceAround",
                                
                                vertical_alignment="center",
                                controls=[  
                                        ElevatedButton(width=160,height=70,content=Text(value="Inicio",size=26),on_click=self.button_clicked3),
                                        ElevatedButton(width=160,height=70,content=Text(value="Buscar",size=26),on_click=self.button_clicked),
                                        ElevatedButton(width=160,height=70,content=Text(value="Agregar",size=26),on_click=self.button_clicked2),
                                        ElevatedButton(width=160,height=70,content=Text(value="Historial",size=26),on_click=self.button_clicked4)
                                ]
                            ),
                        ]
                    )


    def button_clicked2(self,e):
        self.c1.visible=False
        self.c2.visible=True
        self.c3.visible=False
        self.c4.visible=False
        self.update()

    def button_clicked(self,e):
        self.c1.visible=True
        self.c2.visible=False
        self.c3.visible=False
        self.c4.visible=False
        self.update()
    
    def button_clicked3(self,e):
        self.c1.visible=False
        self.c2.visible=False
        self.c3.visible=True
        self.c4.visible=False
        self.update()

    def button_clicked4(self,e):
        self.c1.visible=False
        self.c2.visible=False
        self.c3.visible=False
        self.c4.visible=True
        self.update()
  
  
def main(page: Page):
    page.expand=True
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
    page.window_max_height=800
    page.window_max_width=1200
    page.window_min_height=600
    page.window_min_width=800    
    
    #page.window_bgcolor=flet.colors.BLUE_GREY_400
    page.update()
   
    # create application instance
    app=Con()
   # app2= Otra()
        # def router_change(route):
    
   
   
    page.add(app)

    
    
flet.app(target=main)

#flet.app(target=main, view=flet.WEB_BROWSER)