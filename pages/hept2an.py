import flet as ft

class Hept_Haian(ft.Container):
    def __init__(self):
        super().__init__()  
                 
        self.a1 =ft.TextField(label="Nhập a1",hint_text="a1")        
        self.b1=ft.TextField(label="Nhập b1",hint_text="b1")        
        self.c1=ft.TextField(label="Nhập c1",hint_text="c1")
        self.a2 =ft.TextField(label="Nhập a2",hint_text="a2")        
        self.b2=ft.TextField(label="Nhập b2",hint_text="b2")        
        self.c2=ft.TextField(label="Nhập c2",hint_text="c2")             
        self.result=ft.Text("", color="#000000", italic=True, weight="bold")
        self.result2=ft.Text("", color="#f24b0c", weight="bold")        
        self.content = ft.Column(
            controls=[ 
                ft.Container(
                    padding=ft.padding.only(top=10),
                    content=ft.ResponsiveRow(
                        controls=[                                                                       
                            ft.Column(col={"xs":12}, controls=[ ft.Text("GIẢI HỆ PT BẬC NHẤT 2 ẨN", size=20, weight="bold")])                                                                                                                                              
                        ]                                        
                    )                     
                ),  
                ft.Container(                           
                    content=ft.Column(
                        controls=[ 
                            ft.Row(controls=[ft.Text("", size=0)]),                             
                            ft.ResponsiveRow(controls=[                              
                                ft.Column(col={"xs": 12}, controls=[self.a1]),   
                            ]),                        
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.b1]),   
                            ]),                           
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.c1]),   
                            ]),                            
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.a2]),   
                            ]),   
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.b2]),   
                            ]),      
                            ft.ResponsiveRow(controls=[
                                ft.Column(col={"xs": 12}, controls=[self.c2]),   
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
        self.a1.value = ""
        self.b1.value = ""
        self.c1.value = ""  
        self.a2.value = ""
        self.b2.value = ""
        self.c2.value = ""       
        self.result.value = ""            
        self.result2.value = ""       
        self.update()    
                 
    def calc(self,e):        
        self.result.size=18
        self.result2.size=20
        choice_a1= float(self.a1.value)
        choice_b1= float(self.b1.value)
        choice_c1= float(self.c1.value)    
        choice_a2= float(self.a2.value)
        choice_b2= float(self.b2.value)
        choice_c2= float(self.c2.value)  
        DT = (choice_a1 * choice_b2) - (choice_b1 * choice_a2)
        DTx = (choice_c1 * choice_b2) - (choice_b1 * choice_c2) 
        DTy = (choice_a1 * choice_c2) - (choice_a2 * choice_c1)
        if (DT != 0):   
            self.result.value = str("Hệ pt: \n {0}x + {1}y = {2} ; \n {3}x + {4}y = {5} ; ".format(choice_a1,choice_b1,choice_c1,choice_a2,choice_b2,choice_c2) + " \n có 1 nghiệm: ")  
            self.result2.value = str("x= " + str("%.2f" %(DTx/DT)) + " ; " + "y= " + str("%.2f" %(DTy/DT)))
        else:
            if DTx != 0 or DTy != 0:
                self.result.value = str("Hệ pt: {0}x + {1}y = {2} ; {3}x + {4}y = {5} ".format(choice_a1,choice_b1,choice_c1,choice_a2,choice_b2,choice_c2))             
                self.result2.value = str("Hệ pt vô nghiệm")
            else:
                self.result.value = str("Hệ pt: {0}x + {1}y = {2} ; {3}x + {4}y = {5} ".format(choice_a1,choice_b1,choice_c1,choice_a2,choice_b2,choice_c2))            
                self.result2.value = str("Hệ pt vô số nghiệm")           
        self.update()         
