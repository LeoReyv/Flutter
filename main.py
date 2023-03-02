import flet 

from flet import (
    Checkbox,
    Column,
    FloatingActionButton,
    IconButton,
    OutlinedButton,
    Page,
    Container,
    Card,
    ElevatedButton,
    NavigationRail,
    NavigationBar,
    MainAxisAlignment,
    CrossAxisAlignment,
    NavigationRailLabelType,
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
)


from get_data import get_cliente, get_collection


collection_name = get_collection()

class Task(UserControl):
    def __init__(self, task_producto,task_cantidad, task_precio):
        super().__init__()
        self.task_producto  = task_producto
        self.task_cantidad  = task_cantidad
        self.precio    = task_precio
        
     

    def build(self):
        self.display_task=TextField(label="producto -", disabled=True, value=self.task_producto)
        self.precio = Text(self.precio)
        self.display_view= Row(
            
            controls=[
                 self.display_task,
                 Row(
                    spacing=0,
                    controls=[
                        IconButton(
                        visible =False,
                        icon = icons.ARROW_LEFT
                        ),
                        Text(self.task_cantidad),
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



class Otra(UserControl):
      
    

    def build(self):
        self.total=0
        self.new_task = TextField(
            hint_text="otra",
            
            expand = True)
        self.tasks = Column()
        self.task_total=Text(f"Total = {self.total}")
        
        
        return Column(
                    width=600,
                    controls=[
                
                        Row(
                            controls=[
                            self.new_task,
                            ElevatedButton(text="Submit", ),
                        
                            ],

                        ),
                    
                        Column(
                            spacing=25,
                            controls=[
                                
                                self.tasks,
                                 Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.task_total,
                                
                             ],
                                ),
                                
                                ]

                        ),
                        ]

            
                )
                
                
                   
                    
        

class TodoApp(UserControl):
    
   
    
    

    def build(self):
        self.total=0
        self.new_task = TextField(
            hint_text="busqueda",
            on_submit=self.button_clicked,
            expand = True)
        self.tasks = Column()
        self.task_total=Text(f"Total = {self.total}")
        self.filter=Tabs(
            selected_index=0,
            on_change=self.tabs_changed,
            tabs=[Tab(text="lista de compras"),Tab(text="Lista de clientes"),Tab(text="Lista de proveedores"),Tab(text="Productos")],
            )
        
        
        return Column(
                    width=600,
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
                                 Row(
                            alignment="spaceBetween",
                            vertical_alignment="center",
                            controls=[
                                self.task_total,
                                
                             ],
                                ),
                                
                                ]

                        ),
                        ]

            
                )
                
                
                   
                    
        
        


            
    def button_clicked(self, e):
        dic_sec =[]
        self.total=0
        self.tasks.controls.clear()
        self.update()
        
        

        #data = get_cliente(self.new_task)
        for n in collection_name.find({"cliente":self.new_task.value}):
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


    
  
def main(page: Page):
    page.horizontal_alignment = "center"
    page.scroll = "adaptive"
   
    
    page.update()
    
    # create application instance
    app = TodoApp()
    app2= Otra()
        # def router_change(route):
        #     page.add()
        
    page.navigation_bar=NavigationBar(destinations=[
                NavigationRailDestination(
                    icon=icons.FAVORITE_BORDER, selected_icon=icons.FAVORITE, label="otra",
                    
                ),
                NavigationRailDestination(
                    icon_content=Icon(icons.BOOKMARK_BORDER),
                    selected_icon_content=Icon(icons.BOOKMARK),
                    label="Second",
                ),
                NavigationRailDestination(
                    icon=icons.SETTINGS_OUTLINED,
                    selected_icon_content=Icon(icons.SETTINGS),
                    
                    label_content=Text("Settings"),
                )
            ],)
    # add application's root control to the page
    
    page.add(app)

    
    
flet.app(target=main)

#flet.app(target=main, view=flet.WEB_BROWSER)