from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from kivy.uix.button import ButtonBehavior
from kivy.graphics import Color, Rectangle
from kivy.event import EventDispatcher
#help(EventDispatcher)
import random
from kivy.uix.screenmanager import ScreenManager, Screen
'''
 |                  >>> print(wid.property('sticks', quiet=True))
 |                  None
 |                  >>> wid.apply_property(sticks=ObjectProperty(55, max=10))
-- More  --
'''

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

#file=open("plnum.txt", "r")




class win(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        #self.wpnum=plnum
        #self.wi=i
        self.name='win'
        win=open('win.txt', 'r')
        rd=win.read()
        win.close()
        self.gd=BoxLayout(orientation='vertical')
        self.add_widget(self.gd)
        self.gd.add_widget(Label(text=rd))
        self.gd.add_widget(Button(text="New Game", on_press=self.gopickNum))
        self.gd.add_widget(Button(text="View Previous", on_press=self.previous))
    def gopickNum(self,instance):
        	#r.remove_widget(game())
        	#r.add_widget(pickNum())
        	self.manager.current='pickNum'
    def previous(self,instance):
        	r.remove_widget(win())
        	self.manager.current='game'
        	
        
#win=win()

class game(Screen):  
    
    def __init__(self,pnum, **kwargs):
        super().__init__(**kwargs)
        self.name='game'
        self.bl=BoxLayout()
        self.cnum=random.randint(0,10)
        self.bl.orientation="vertical"
        #self.add_widget(cover)
        self.add_widget(self.bl)
        self.pnum=pnum
        #plnum=pnum
        self.cgrid=BoxLayout()
        self.cgrid.orientation="horizontal"
        self.bl.add_widget(self.cgrid)

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
        #self.add_widget(self.pgrid)
    def yyess(self, instance, plnum):
        print('NO OnJHGF')
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
            w=open("win.txt", 'w')
            w.write(' You\n Win ')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
            print('GVDTKVDYYJ<GFKU')
        elif 0+self.fnum== self.cnum:
            w=open('win.txt', 'w')
            w.write('CPU\nWin')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
        
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
            w=open("win.txt", 'w')
            w.write(' You\n Win ')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
        elif 1+self.fnum== self.cnum:
            w=open('win.txt', 'w')
            w.write('CPU\nWin')
            w.close()
            r.add_widget(win())
            self.manager.current='win'


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
            w=open("win.txt", 'w')
            w.write(' You\n Win ')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
        elif 2+self.fnum== self.cnum:
            w=open('win.txt', 'w')
            w.write('CPU\nWin')
            w.close()
            r.add_widget(win())
            self.manager.current='win'

        

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
            w=open("win.txt", 'w')
            w.write(' You\n Win ')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
        elif 3+self.fnum== self.cnum:
            w=open('win.txt', 'w')
            w.write('CPU\nWin')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
        
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
            w=open("win.txt", 'w')
            w.write(' You\n Win ')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
        elif 4+self.fnum== self.cnum:
            w=open('win.txt', 'w')
            w.write('CPU\nWin')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
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
            w=open("win.txt", 'w')
            w.write(' You\n Win ')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
        elif 5+self.fnum== self.cnum:
            w=open('win.txt', 'w')
            w.write('CPU\nWin')
            w.close()
            r.add_widget(win())
            self.manager.current='win'
           

class pickNum(Screen):
    plnum=NumericProperty(12)
    def __init__(self, **kwargs):
        super(pickNum, self).__init__(**kwargs)
        self.mbox= BoxLayout(orientation='vertical')
        self.add_widget(self.mbox)
        self.mbox.add_widget(Label(text='Pick Your Number'))
        self.mgrid=GridLayout()
        self.mgrid.cols=3
        
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
        self.name='pickNum'

    def gotofirst10(self,instance):
        count=open('count.txt', 'r')
        j=count.read()
        count.close()
        i=1+int(j)
        print(i)
        count=open('count.txt', 'w')
        count.write(str(i))
        count.close()
        r.add_widget(game(pnum=10))
        self.manager.current='game'
    def gotofirst9(self,instance):
        count=open('count.txt', 'r')
        j=count.read()
        count.close()
        i=1+int(j)
        print(i)
        count=open('count.txt', 'w')
        count.write(str(i))
        count.close()
        r.add_widget(game(pnum=9))
        self.manager.current='game'
    def gotofirst8(self,instance):
        r.add_widget(game(pnum=8))
        self.manager.current='game'
    def gotofirst7(self,instance):
        r.add_widget(game(pnum=7))
        self.manager.current='game'
    def gotofirst6(self,instance):
        r.add_widget(game(pnum=6))
        self.manager.current='game'
    def gotofirst5(self,instance):
        r.add_widget(game(pnum=5))
        self.manager.current='game'
    def gotofirst4(self,instance):
        r.add_widget(game(pnum=4))
        self.manager.current='game'
    def gotofirst3(self,instance):
        r.add_widget(game(pnum=3))
        self.manager.current='game'
    def gotofirst2(self,instance):
        r.add_widget(game(pnum=2))
        self.manager.current='game'
    def gotofirst1(self,instance):
        r.add_widget(game(pnum=1))
        self.manager.current='game'
    def gotofirst0(self,instance):
        r.add_widget(game(pnum=0))
        self.manager.current='game'
    def on_plnum(self, instance, plnum):
        print(plnum)
        return plnum
#pick=pickNum()
class welcome(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name='welcome'
        print(self.size)
        self.add_widget(cover)
        self.gd=FloatLayout()
        self.add_widget(self.gd)
        #self.gd.add_widget(Label(text=rd))
        self.gd.add_widget(Button(text="Play", on_press=self.gopickNum, opacity=0.5, pos_hint={'x':0.5,'y':0.3},size_hint=(0.1,0.1)))
        #self.gd.add_widget(Button(text="View Previous", on_press=self.previous))
    def gopickNum(self,instance):
        	r.add_widget(pickNum())
        	#r.remove_widget(win())
        	self.manager.current='pickNum'

class manager(ScreenManager):
    def __init__(self, **kwargs):
        super(manager, self).__init__(**kwargs)
        self.add_widget(welcome())
       
r=manager()


class Kivy(App):
    def build(self):
        count=open('count.txt', 'w')
        count.write(str(0))
        count.close()
        self.root = root=r
        root.bind(size=self._update_rect, pos=self._update_rect)

        with root.canvas.before:
            Color(0, 0, 0, 0)
            self.rect = Rectangle(size=root.size, pos=root.pos)
        return root
    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

if __name__ =="__main__":
    Kivy().run()
