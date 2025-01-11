import flet as ft
import numpy as np

class Bac3(ft.Container):
    def __init__(self):
        super().__init__()    
                                             
        self.a =ft.TextField(label="Nhập a",hint_text="a")        
        self.b=ft.TextField(label="Nhập b",hint_text="b")        
        self.c=ft.TextField(label="Nhập c",hint_text="c")
        self.d=ft.TextField(label="Nhập d",hint_text="d")  
        self.result=ft.Text("", color="#000000", italic=True, weight="bold")
        self.result2=ft.Text("", color="#f24b0c", weight="bold")        
        self.content = ft.Column(
            controls=[    
                ft.Container(
                    padding=ft.padding.only(top=10),
                    content=ft.ResponsiveRow(
                        controls=[                                                                       
                            ft.Column(col={"xs":12}, controls=[ ft.Text("Pt: Ax³ + Bx² + Cx + D = 0", size=21, weight="bold")])                                                                                                                                              
                        ]                                        
                    )                     
                ),  
              
                ft.Container(                           
                    content=ft.Column(
                        controls=[ 
                            ft.Row(controls=[ft.Text("", size=0)]),                             
                            ft.ResponsiveRow(controls=[                              
                                ft.Column(col={"xs": 12}, controls=[self.a]),   
                            ]),                        
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.b]),   
                            ]),                           
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.c]),   
                            ]),                            
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.d]),   
                            ]),                                                                                                                      
                            ft.Row(controls=[ft.Text("", size=0)]),  
                            ft.Row(
                                controls=[                           
                                    ft.ElevatedButton(" Kết quả ", bgcolor="blue50", color="blue", on_click=self.calc),
                                    ft.ElevatedButton(" Làm lại ", bgcolor="blue50", color="blue", on_click=self.de)                                     
                                ], alignment="spaceEvenly"
                            ),                                     
                            ft.Row(controls=[ft.Text("", size=0)]), 
                            ft.Container(
                                padding=ft.padding.only(left=5, right=5),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":12},controls=[self.result])                                                                                    
                                    ]                                        
                                )                                    
                            ),
                            ft.Container(
                                padding=ft.padding.only(left=5, right=5),
                                content=ft.ResponsiveRow(
                                    controls=[
                                        ft.Column(col={"xs":12},controls=[self.result2])                                                                                    
                                    ]                                        
                                )                                    
                            ),
                            ft.Row(controls=[ft.Text("", size=0)]), 
                            ft.Row(controls=[ft.Text("", size=0)]),                                                                                                                                                                                          
                        ], scroll=ft.ScrollMode.AUTO, height=410                                                                                         
                    )                                                           
                )                      
            ]
        )   

    def de (self,e):       
        self.a.value = ""
        self.b.value = ""
        self.c.value = ""  
        self.d.value = ""       
        self.result.value = ""            
        self.result2.value = ""       
        self.update()        
             
    def calc(self,e):        
        self.result.size=18
        self.result2.size=20
        choice_a= float(self.a.value)
        choice_b= float(self.b.value)
        choice_c= float(self.c.value)  
        choice_d= float(self.d.value)         
        if (choice_a != 0): 
            roots = np.roots([choice_a, choice_b, choice_c, choice_d])
            self.result.value = str("Phương trình: \n {0}x³ + {1}x² + {2}x + {3} = 0".format(choice_a,choice_b,choice_c,choice_d) + " \n có các nghiệm: ")
            self.result2.value = str(roots)             
        else:
            self.result.value = str ("Không phải phương trình Bậc 3.")        
        self.update()     
        