import flet as ft
from pages.bac1 import Bac1
from pages.bac2 import Bac2
from pages.bac3 import Bac3
from pages.bac4 import Bac4
from pages.hept2an import Hept_Haian
from pages.hept3an import Hept_Baan
from pages.maytinh import CalculatorApp

class Welcome(ft.View):
    def __init__(self, page: ft.Page):
        super(Welcome, self).__init__(
            route="/", horizontal_alignment="center", vertical_alignment="center")
        self.page = page
        self.padding = 30
        self.bgcolor = "#FFFFFF"
        self.logo = ft.IconButton("CALCULATE_OUTLINED", icon_size=70)
        self.title_app = ft.Text("MÁY TÍNH ONLINE".upper(), size=25, weight="bold")
        self.subtitle_app = ft.Text("Giải phương trình", size=18)        
        self.next_page_btn = ft.IconButton(
            "arrow_forward",
            width=53,
            height=53,
            icon_color="#ffffff",
            style=ft.ButtonStyle(
                bgcolor={"": "#0247fe"},
                shape={"": ft.RoundedRectangleBorder(radius=8)},
                side={"": ft.BorderSide(2, "white60")},
            ),                      
            on_click=lambda e: self.page.go("/gallery")
        )
        self.controls = [
            self.logo,
            ft.Divider(height=20, color="transparent"),
            self.title_app,
            self.subtitle_app,           
            ft.Divider(height=10, color="transparent"),
            self.next_page_btn,   
        ]   
    
class NavbarCustom(ft.UserControl):
    def __init__(self):
        super().__init__()   

    def HighLight(self,e):
        if e.data == "true":
            e.control.bgcolor= "blue50"           
            e.control.update()          
            e.control.content.controls[1].color = "blue"
            e.control.content.update()
        else:
            e.control.bgcolor= None
            e.control.update()        
            e.control.content.controls[1].color = "black"
            e.control.content.update()    

    def Bac1(self, icon_name:str, text:str):
        return ft.Container(
            height=45, border_radius=10, on_click=lambda e: self.page.go("/bac1"), on_hover= lambda e: self.HighLight(e),
            content= ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=28                                                            
                    ),
                    ft.Text(
                        value=text, size=17
                    )
                ]                
            )
        )   
    
    def Bac2(self, icon_name:str, text:str):
        return ft.Container(
            height=45, border_radius=10, on_click=lambda e: self.page.go("/bac2"), on_hover= lambda e: self.HighLight(e),
            content= ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=28                                          
                    ),
                    ft.Text(
                        value=text, size=17
                    )
                ]                
            )
        ) 
    
    def Bac3(self, icon_name:str, text:str):
        return ft.Container(
            height=45, border_radius=10, on_click=lambda e: self.page.go("/bac3"), on_hover= lambda e: self.HighLight(e),
            content= ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=28                                            
                    ),
                    ft.Text(
                        value=text, size=17
                    )
                ]                
            )
        ) 
    
    def Bac4(self, icon_name:str, text:str):
        return ft.Container(
            height=45, border_radius=10, on_click=lambda e: self.page.go("/bac4"), on_hover= lambda e: self.HighLight(e),
            content= ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=28                                         
                    ),
                    ft.Text(
                        value=text, size=17
                    )
                ]                
            )
        ) 
    
    def Hept2an(self, icon_name:str, text:str):
        return ft.Container(
            height=45, border_radius=10, on_click=lambda e: self.page.go("/hept2an"), on_hover= lambda e: self.HighLight(e),
            content= ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=28                                         
                    ),
                    ft.Text(
                        value=text, size=17
                    )
                ]                
            )
        ) 
    
    def Hept3an(self, icon_name:str, text:str):
        return ft.Container(
            height=45, border_radius=10, on_click=lambda e: self.page.go("/hept3an"), on_hover= lambda e: self.HighLight(e),
            content= ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=28                                            
                    ),
                    ft.Text(
                        value=text, size=17
                    )
                ]                
            )
        ) 
    
    def Maytinh(self, icon_name:str, text:str):
        return ft.Container(
            height=45, border_radius=10, on_click=lambda e: self.page.go("/maytinh"), on_hover= lambda e: self.HighLight(e),
            content= ft.Row(
                controls=[
                    ft.IconButton(
                        icon=icon_name,
                        icon_size=28                                        
                    ),
                    ft.Text(
                        value=text, size=17
                    )
                ]                
            )
        )     

    def build(self):
        return ft.Container(            
            width=350,           
            padding=ft.padding.only(top=10),       
            content= ft.Column(      
                controls=[
                    ft.Row(
                        controls=[
                            ft.Text("MỤC LỤC", size=21, weight="bold")
                        ], alignment="center"
                    ), 
                    ft.Divider(height=5),                    
                    self.Bac1(ft.Icons.MUSIC_NOTE_ROUNDED, "Bậc 1"),
                    self.Bac2(ft.Icons.EVENT_NOTE_ROUNDED, "Bậc 2"),
                    self.Bac3(ft.Icons.BAR_CHART, "Bậc 3"),
                    self.Bac4(ft.Icons.LIBRARY_BOOKS_OUTLINED, "Bậc 4"),
                    self.Hept2an(ft.Icons.NOTE_ALT_ROUNDED, "Hệ pt 2 ẩn"),
                    self.Hept3an(ft.Icons.SHOP_TWO_OUTLINED, "Hệ pt 3 ẩn"),
                    self.Maytinh(ft.Icons.CALCULATE_ROUNDED, "Máy tính"),
                    ft.Divider(height=5),    
                    ft.Row(
                        controls=[                           
                            ft.ElevatedButton("  Trở về  ", bgcolor="blue", color="white", on_click=lambda e: self.page.go("/"))
                        ], alignment="center"
                    )    
                ]
            )        
        )    

class Gallery(ft.View):
    def __init__(self, page:ft.Page):
        super(Gallery,self).__init__(
            route="/gallery"                         
        )            
        self.page = page   
        self.bgcolor = "#FFFFFF"
        self.padding = ft.padding.only(top=70, left=30, right=30, bottom=30)       
        self.controls = [
            ft.Container(
                width=350,          
                padding=10,        
                content= NavbarCustom()
            )                              
        ]       

class HamBac1(ft.View):
    def __init__(self, page:ft.Page):
        super(HamBac1,self).__init__(
            route="/bac1")            
        self.page = page   
        self.bgcolor = "#FFFFFF"
        self.padding = ft.padding.only(top=70, left=30, right=30, bottom=30)       
        self.controls = [
            ft.Container(
                width=350,  
                content= ft.Column(
                    controls=[
                        Bac1(),
                        ft.Divider(height=5),
                        ft.Row(
                            controls=[                           
                                ft.ElevatedButton("  Trở về  ", bgcolor="blue", color="white", on_click=lambda e: self.page.go("/gallery"))
                            ], alignment="center"
                        )                
                    ]               
                )            
            )                              
        ]  

class HamBac2(ft.View):
    def __init__(self, page:ft.Page):
        super(HamBac2,self).__init__(
            route="/bac2")            
        self.page = page   
        self.bgcolor = "#FFFFFF"
        self.padding = ft.padding.only(top=70, left=30, right=30, bottom=30)       
        self.controls = [
            ft.Container(
                width=350,  
                content= ft.Column(
                    controls=[
                        Bac2(),
                        ft.Divider(height=5),
                        ft.Row(
                            controls=[                           
                                ft.ElevatedButton("  Trở về  ", bgcolor="blue", color="white", on_click=lambda e: self.page.go("/gallery"))
                            ], alignment="center"
                        )                
                    ]               
                )            
            )                              
        ]  

class HamBac3(ft.View):
    def __init__(self, page:ft.Page):
        super(HamBac3,self).__init__(
            route="/bac3")            
        self.page = page   
        self.bgcolor = "#FFFFFF"
        self.padding = ft.padding.only(top=70, left=30, right=30, bottom=30)       
        self.controls = [
            ft.Container(
                width=350,  
                content= ft.Column(
                    controls=[
                        Bac3(),
                        ft.Divider(height=5),
                        ft.Row(
                            controls=[                           
                                ft.ElevatedButton("  Trở về  ", bgcolor="blue", color="white", on_click=lambda e: self.page.go("/gallery"))
                            ], alignment="center"
                        )                
                    ]               
                )            
            )                              
        ]  

class HamBac4(ft.View):
    def __init__(self, page:ft.Page):
        super(HamBac4,self).__init__(
            route="/bac4")            
        self.page = page   
        self.bgcolor = "#FFFFFF"
        self.padding = ft.padding.only(top=70, left=30, right=30, bottom=30)       
        self.controls = [
            ft.Container(
                width=350,  
                content= ft.Column(
                    controls=[
                        Bac4(),
                        ft.Divider(height=5),
                        ft.Row(
                            controls=[                           
                                ft.ElevatedButton("  Trở về  ", bgcolor="blue", color="white", on_click=lambda e: self.page.go("/gallery"))
                            ], alignment="center"
                        )                
                    ]               
                )            
            )                              
        ]  

class Hept2an(ft.View):
    def __init__(self, page:ft.Page):
        super(Hept2an,self).__init__(
            route="/hept2an")            
        self.page = page   
        self.bgcolor = "#FFFFFF"
        self.padding = ft.padding.only(top=70, left=30, right=30, bottom=30)       
        self.controls = [
            ft.Container(
                width=350,  
                content= ft.Column(
                    controls=[
                        Hept_Haian(),
                        ft.Divider(height=5),
                        ft.Row(
                            controls=[                           
                                ft.ElevatedButton("  Trở về  ", bgcolor="blue", color="white", on_click=lambda e: self.page.go("/gallery"))
                            ], alignment="center"
                        )                
                    ]               
                )            
            )                              
        ]  

class Hept3an(ft.View):
    def __init__(self, page:ft.Page):
        super(Hept3an,self).__init__(
            route="/hept3an")            
        self.page = page   
        self.bgcolor = "#FFFFFF"
        self.padding = ft.padding.only(top=70, left=30, right=30, bottom=30)       
        self.controls = [
            ft.Container(
                width=350,  
                content= ft.Column(
                    controls=[                        
                        Hept_Baan(),
                        ft.Divider(height=5),
                        ft.Row(
                            controls=[                           
                                ft.ElevatedButton("  Trở về  ", bgcolor="blue", color="white", on_click=lambda e: self.page.go("/gallery"))
                            ], alignment="center"
                        )                
                    ]               
                )            
            )                              
        ]  

class Calculator(ft.View):
    def __init__(self, page:ft.Page):
        super(Calculator,self).__init__(
            route="/maytinh")            
        self.page = page   
        self.bgcolor = "#FFFFFF"
        self.padding = ft.padding.only(top=60, left=30, right=30, bottom=30)       
        self.controls = [
            ft.Container(
                width=350,  
                content= ft.Column(
                    controls=[                        
                        CalculatorApp(),
                        ft.Divider(height=5),
                        ft.Row(
                            controls=[                           
                                ft.ElevatedButton("  Trở về  ", bgcolor="blue", color="white", on_click=lambda e: self.page.go("/gallery"))
                            ], alignment="center"
                        )                
                    ]               
                )            
            )                              
        ]  
   
def main(page: ft.Page):   
    page.title = "Mini Calc App"    
    def router(route):
        page.views.clear()

        if page.route == "/":
            welc = Welcome(page)
            page.views.append(welc)

        if page.route == "/gallery":
            gall = Gallery(page)
            page.views.append(gall)

        if page.route == "/bac1":
            bac1ct = HamBac1(page)
            page.views.append(bac1ct)

        if page.route == "/bac2":
            bac2ct = HamBac2(page)
            page.views.append(bac2ct)

        if page.route == "/bac3":
            bac3ct = HamBac3(page)
            page.views.append(bac3ct)

        if page.route == "/bac4":
            bac4ct = HamBac4(page)
            page.views.append(bac4ct)

        if page.route == "/hept2an":
            he2an = Hept2an(page)
            page.views.append(he2an)

        if page.route == "/hept3an":
            he3an = Hept3an(page)
            page.views.append(he3an)

        if page.route == "/maytinh":
            calc = Calculator(page)
            page.views.append(calc)

        page.update()
    page.on_route_change = router
    page.go("/")    

ft.app(main, assets_dir="assets")
