from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.uix.button import ButtonBehavior
from kivy.graphics import Color, Rectangle
from kivy.event import EventDispatcher
import random
from kivy.uix.screenmanager import ScreenManager, Screen

cdi={"0":Image(source="img0.jpg"),
"1":Image(source="1c.gif"),
"2":Image(source="2c.gif"), 
"3":Image(source="3c.gif"), 
"4":Image(source="4c.gif"), 
"5":Image(source="5c.gif")}
cover= Image(source="cover.jpg")

pdi={"0":Image(source="img0.jpg"),
"1":Image(source="1.gif"),
"2":Image(source="2.gif"), 
"3":Image(source="3.gif"), 
"4":Image(source="4.gif"), 
"5":Image(source="5.gif")}


class game(Screen):  
    
    def __init__(self,pnum,i, **kwargs):
        super().__init__(**kwargs)
        self.name='game'+str(i)
        self.bl=BoxLayout()
        self.cnum=random.randint(0,10)
        self.bl.orientation="vertical"
        self.add_widget(self.bl)
        self.pnum=pnum
        self.popup=None
        self.cgrid=BoxLayout()
        self.cgrid.orientation="horizontal"
        self.bl.add_widget(self.cgrid)
        self.i=i
        self.cgrid.add_widget(Image(source="5c.gif"))
        self.cgrid.add_widget(Image(source="4c.gif"))
        self.cgrid.add_widget(Image(source="3c.gif"))
        self.cgrid.add_widget(Image(source="2c.gif"))
        self.cgrid.add_widget(Image(source="1c.gif"))
        self.cgrid.add_widget(Image(source="img0.jpg"))

        #DISPLAY COMPUTER CHOOSEN NUMBER
        self.clbl= Label(text=str(self.cnum), color=(1,1,1,1), )
        self.bl.add_widget(self.clbl)
        
        #display computer finger on table
        self.cfin=Label()
        self.bl.add_widget(self.cfin)

        #show the sum of computer finger and player finger
        self.add=Label(text="\n \n"+"  "+"\n \n")
        self.bl.add_widget(self.add)

        #display player finger on table
        self.pfin=Label()
        self.bl.add_widget(self.pfin)

        #DISPLAY player CHOOSEN NUMBER
        self.plbl= Label(text=str(self.pnum), color=(1,1,1,1), )
        #self.plbl= Label(text=str(9), color=(0,0,0,1), )
        self.bl.add_widget(self.plbl)

        #player finger grid
        self.pgrid=BoxLayout()
        self.pgrid.padding=(1,0.5,0.5,0.5)
        self.pgrid.spacing=100
        self.pgrid.orientation="horizontal"
        self.bl.add_widget(self.pgrid)
        
        self.p0=Button(size_hint=(0.85,1)) 
        self.p0.background_down="0.gif"
        self.p0.background_normal="0.gif"
        self.p0.background_disabled="0.gif"
        self.p0.on_press=self.press0
        self.pgrid.add_widget(self.p0)

        self.p1=Button(size_hint=(0.8,1)) 
        self.p1.background_down="1.gif"
        self.p1.background_normal="1.gif"
        self.p1.background_disabled="1.gif"
        self.p1.on_press=self.press1
        self.pgrid.add_widget(self.p1)
        
        self.p2=Button(size_hint=(0.8,1)) 
        self.p2.background_down="2.gif"
        self.p2.background_normal="2.gif"
        self.p2.background_disabled="2.gif"
        self.p2.on_press=self.press2
        self.pgrid.add_widget(self.p2)

        self.p3=Button(size_hint=(0.8,1)) 
        self.p3.background_down="3.gif"
        self.p3.background_normal="3.gif"
        self.p3.background_disabled="3.gif"
        self.p3.on_press=self.press3
        self.pgrid.add_widget(self.p3)

        self.p4=Button(size_hint=(0.8,1)) 
        self.p4.background_down="4.gif"
        self.p4.background_normal="4.gif"
        self.p4.background_disabled="4.gif"
        self.p4.on_press=self.press4
        self.pgrid.add_widget(self.p4)

        self.p5=Button(size_hint=(0.8,1)) 
        self.p5.background_down="5.gif"
        self.p5.background_normal="5.gif"
        self.p5.background_disabled="5.gif"
        self.p5.on_press=self.press5
        self.pgrid.add_widget(self.p5)
        with self.canvas.before:
            Color(1,0,1,0)
            Rectangle()
    def press0(self, *args):
        
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(0)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 0+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='NEW GAME', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 0+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

    def press1(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(1)]
        self.bl.add_widget(self.pfin, index=2)
        
        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(1+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 1+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif 1+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
     
    def press2(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(2)]
        self.bl.add_widget(self.pfin, index=2)

        
        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(2+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 2+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif 2+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

    def press3(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(3)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(3+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 3+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif 3+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
    def press4(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(4)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(4+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 4+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 4+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
    def press5(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(5)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(5+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 5+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 5+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

    def gopickNum(self,instance):
        count=open('count.txt', 'r')
        j=count.read()
        count.close()
        i=1+int(j)
        print(i)
        count=open('count.txt', 'w')
        count.write(str(i))
        count.close()        
        count=open('count.txt', 'r')
        j=count.read()
        count.close()
        print(j)
        self.parent.parent.parent.add_widget(manager(int(j)))
        try :
            self.parent.parent.clear_widgets()
        except:
            pass
        self.parent.clear_widgets()
        self.clear_widgets()
        self.bl.clear_widgets()
        self.popup.dismiss()

class pickto(Screen):
    def __init__(self, pnum, i, **kwargs):
        super(pickto, self).__init__(**kwargs)
        self.gl=GridLayout(cols=1)
        self.name='pickto'+str(i)
        self.i=i
        self.pnum=pnum
        self.add_widget(self.gl)
        self.gl.add_widget(Button(text='Player vs CPU', on_press=self.single))
        self.gl.add_widget(Button(text='Tournament', on_press=self.tourn))
    def single(self, instance):
        self.parent.add_widget(game(i=self.i, pnum=self.pnum))
        self.manager.current='game'+str(self.i)
        self.clear_widgets()
    def tourn(self, instance):
        pass
        '''
        self.parent.add_widget(pickto(i=self.i, pnum=self.pnum))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
        '''
class contest(Screen):      
    def __init__(self,pnum,i, **kwargs):
        super().__init__(**kwargs)
        self.name='game'+str(i)
        self.bl=BoxLayout()
        self.cnum=random.randint(0,10)
        self.bl.orientation="vertical"
        self.add_widget(self.bl)
        self.pnum=pnum
        self.popup=None
        self.cgrid=BoxLayout()
        self.cgrid.orientation="horizontal"
        self.bl.add_widget(self.cgrid)
        self.i=i
        self.cgrid.add_widget(Image(source="5c.gif"))
        self.cgrid.add_widget(Image(source="4c.gif"))
        self.cgrid.add_widget(Image(source="3c.gif"))
        self.cgrid.add_widget(Image(source="2c.gif"))
        self.cgrid.add_widget(Image(source="1c.gif"))
        self.cgrid.add_widget(Image(source="img0.jpg"))

        #DISPLAY COMPUTER CHOOSEN NUMBER
        self.clbl= Label(text=str(self.cnum), color=(1,1,1,1), )
        self.bl.add_widget(self.clbl)
        
        #display computer finger on table
        self.cfin=Label()
        self.bl.add_widget(self.cfin)

        #show the sum of computer finger and player finger
        self.add=Label(text="\n \n"+"  "+"\n \n")
        self.bl.add_widget(self.add)

        #display player finger on table
        self.pfin=Label()
        self.bl.add_widget(self.pfin)

        #DISPLAY player CHOOSEN NUMBER
        self.plbl= Label(text=str(self.pnum), color=(1,1,1,1), )
        #self.plbl= Label(text=str(9), color=(0,0,0,1), )
        self.bl.add_widget(self.plbl)

        #player finger grid
        self.pgrid=BoxLayout()
        self.pgrid.padding=(1,0.5,0.5,0.5)
        self.pgrid.spacing=100
        self.pgrid.orientation="horizontal"
        self.bl.add_widget(self.pgrid)
        
        self.p0=Button(size_hint=(0.85,1)) 
        self.p0.background_down="0.gif"
        self.p0.background_normal="0.gif"
        self.p0.background_disabled="0.gif"
        self.p0.on_press=self.press0
        self.pgrid.add_widget(self.p0)

        self.p1=Button(size_hint=(0.8,1)) 
        self.p1.background_down="1.gif"
        self.p1.background_normal="1.gif"
        self.p1.background_disabled="1.gif"
        self.p1.on_press=self.press1
        self.pgrid.add_widget(self.p1)
        
        self.p2=Button(size_hint=(0.8,1)) 
        self.p2.background_down="2.gif"
        self.p2.background_normal="2.gif"
        self.p2.background_disabled="2.gif"
        self.p2.on_press=self.press2
        self.pgrid.add_widget(self.p2)

        self.p3=Button(size_hint=(0.8,1)) 
        self.p3.background_down="3.gif"
        self.p3.background_normal="3.gif"
        self.p3.background_disabled="3.gif"
        self.p3.on_press=self.press3
        self.pgrid.add_widget(self.p3)

        self.p4=Button(size_hint=(0.8,1)) 
        self.p4.background_down="4.gif"
        self.p4.background_normal="4.gif"
        self.p4.background_disabled="4.gif"
        self.p4.on_press=self.press4
        self.pgrid.add_widget(self.p4)

        self.p5=Button(size_hint=(0.8,1)) 
        self.p5.background_down="5.gif"
        self.p5.background_normal="5.gif"
        self.p5.background_disabled="5.gif"
        self.p5.on_press=self.press5
        self.pgrid.add_widget(self.p5)
        with self.canvas.before:
            Color(1,0,1,0)
            Rectangle()
    def press0(self, *args):
        
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(0)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 0+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='NEW GAME', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 0+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

    def press1(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(1)]
        self.bl.add_widget(self.pfin, index=2)
        
        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(1+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 1+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif 1+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
     
    def press2(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(2)]
        self.bl.add_widget(self.pfin, index=2)

        
        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(2+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 2+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif 2+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

    def press3(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(3)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(3+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 3+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif 3+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
    def press4(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(4)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(4+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 4+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 4+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
    def press5(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(5)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(5+self.fnum)+"\n \n")
        self.bl.add_widget(self.add, index=3)
        if 5+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 5+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

    def gopickNum(self,instance):
        count=open('count.txt', 'r')
        j=count.read()
        count.close()
        i=1+int(j)
        print(i)
        count=open('count.txt', 'w')
        count.write(str(i))
        count.close()        
        count=open('count.txt', 'r')
        j=count.read()
        count.close()
        print(j)
        self.parent.parent.parent.add_widget(manager(int(j)))
        try :
            self.parent.parent.clear_widgets()
        except:
            pass
        self.parent.clear_widgets()
        self.clear_widgets()
        self.bl.clear_widgets()
        self.popup.dismiss()
           



class pickNum(Screen):
    plnum=NumericProperty(12)
    def __init__(self,i, **kwargs):
        super(pickNum, self).__init__(**kwargs)
        self.mbox= BoxLayout(orientation='vertical')
        self.add_widget(self.mbox)
        self.mbox.add_widget(Label(text='Pick Your Number'))
        self.mgrid=GridLayout()
        self.mgrid.cols=3
        self.i=i
        self.btn10=Button(text='10',on_press=self.gotofirst10)
        self.mgrid.add_widget(self.btn10)
        self.btn9=Button(text='9',on_press=self.gotofirst9)
        self.mgrid.add_widget(self.btn9)
        self.btn8=Button(text='8',on_press=self.gotofirst8)
        self.mgrid.add_widget(self.btn8)
        self.btn7=Button(text='7',on_press=self.gotofirst7)
        self.mgrid.add_widget(self.btn7)
        self.btn6=Button(text='6',on_press=self.gotofirst6)
        self.mgrid.add_widget(self.btn6)
        self.btn5=Button(text='5',on_press=self.gotofirst5)
        self.mgrid.add_widget(self.btn5)
        self.btn4=Button(text='4',on_press=self.gotofirst4)
        self.mgrid.add_widget(self.btn4)
        self.btn3=Button(text='3',on_press=self.gotofirst3)
        self.mgrid.add_widget(self.btn3)
        self.btn2=Button(text='2',on_press=self.gotofirst2)
        self.mgrid.add_widget(self.btn2)
        self.btn1=Button(text='1',on_press=self.gotofirst1)
        self.mgrid.add_widget(self.btn1)
        self.mbox.add_widget(self.mgrid)
        self.btn0=Button(text='0',on_press=self.gotofirst0)
        self.mgrid.add_widget(self.btn0)
        self.btnn=Button(text='')
        self.mgrid.add_widget(self.btnn)
        self.name='pickNum'+str(i)

    def gotofirst10(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=10))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst9(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=9))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst8(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=8))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst7(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=7))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst6(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=6))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst5(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=5))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst4(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=4))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst3(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=3))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst2(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=2))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst1(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=1))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def gotofirst0(self,instance):
        self.parent.add_widget(pickto(i=self.i, pnum=0))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def on_plnum(self, instance, plnum):
        print(plnum)
        return plnum
class welcome(Screen):
    def __init__(self, i, **kwargs):
        super().__init__(**kwargs)
        self.name='welcome'+str(i)
        self.i=i
        self.add_widget(cover)
        self.gd=FloatLayout()
        self.add_widget(self.gd)
        self.gd.add_widget(Button(text="Play", on_press=self.gopickNum, opacity=0.6, pos_hint={'x':0.5,'y':0.3},size_hint=(0.1,0.1)))
        self.gd.add_widget(Button(text="About", on_press=self.abt, opacity=0.6, pos_hint={'x':0.5,'y':0.1},size_hint=(0.1,0.1)))
    def gopickNum(self,instance):
        self.parent.add_widget(pickNum(self.i))
        self.manager.current='pickNum'+str(self.i)
        self.clear_widgets()

    def abt(self,instance):
        self.parent.add_widget(about())
        self.manager.current='about'

class about(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name='about'
        self.gd=GridLayout(cols=1)
        self.add_widget(self.gd)
        file=open('About.txt', 'r')
        abt=file.read()
        file.close()
        self.gd.add_widget(Label(text=abt))
        file=open('count.txt', 'r')
        self.i=int(file.read())
        file.close()
    def on_touch_down(self,touch):
        #self.parent.add_widget(welcome(self.i))
        self.manager.current='welcome'+str(self.i)  

class manager(ScreenManager):
    def __init__(self, i,**kwargs):
        super(manager, self).__init__(**kwargs)
        self.i=i
        #self.name='win'
        #self.i=i
        self.add_widget(welcome(self.i))

class Kivy(App):
    def build(self):
        count=open('count.txt', 'w')
        count.write(str(0))
        count.close()
        count=open('count.txt', 'r')
        self.i=count.read()
        count.close()
        r=GridLayout(cols=1)
        r.add_widget(manager(int(self.i)))
        self.root = root=r
        self.icon='icon.jpg'
  
        return root
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ =="__main__":
    Kivy().run()
