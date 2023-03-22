import flet 
from flet import (Container)
class VistaProducto(Container):
     def __init__(self, visor_producto ):
         super().__init__()
         self.pile=[]
         self.visor_producto=visor_producto
         self.width=50
         self.height=110
         self.border=10
         self.border_radius = self.border_radius.all(6)