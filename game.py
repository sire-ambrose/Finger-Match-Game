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
import random
from kivy.uix.screenmanager import ScreenManager, Screen

cdi={"0":Image(source="img0.jpg"),
"1":Image(source="1c.gif"),
"2":Image(source="2c.gif"), 
"3":Image(source="3c.gif"), 
"4":Image(source="4c.gif"), 
"5":Image(source="5c.gif")}

pdi={"0":Image(source="img0.jpg"),
"1":Image(source="1.gif"),
"2":Image(source="2.gif"), 
"3":Image(source="3.gif"), 
"4":Image(source="4.gif"), 
"5":Image(source="5.gif")}


class game(Screen, ButtonBehavior, Image):     
    def __init__(self,pnum,i, **kwargs):
        super(game,self).__init__(**kwargs)
        self.pnum=pnum
        self.name='game'+str(i)
        self.bl=BoxLayout()
        self.font=40
        choice=list(range(11))
        choice.remove(self.pnum)
        self.cnum=choice[random.randint(0,9)]
        self.bl.orientation="vertical"
        self.add_widget(self.bl)
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
        self.cgrid.add_widget(Image(source="0.gif"))

        #DISPLAY COMPUTER CHOOSEN NUMBER
        self.clbl= Label(text=str(self.cnum), font_size=self.font)
        self.bl.add_widget(self.clbl)
        
        #display computer finger on table
        self.cfin=Label()
        self.bl.add_widget(self.cfin)

        #show the sum of computer finger and player finger
        self.add=Label(text="\n \n"+"  "+"\n \n", font_size=self.font)
        self.bl.add_widget(self.add)

        #display player finger on table
        self.pfin=Label()
        self.bl.add_widget(self.pfin)

        #DISPLAY player CHOOSEN NUMBER
        self.plbl= Label(text=str(self.pnum), font_size=self.font)
        self.bl.add_widget(self.plbl)

        #player finger grid
        self.pgrid=BoxLayout()
        self.pgrid.orientation="horizontal"
        self.bl.add_widget(self.pgrid)
        self.pgrid.add_widget(Image(source="0.gif"))
        self.pgrid.add_widget(Image(source="1.gif"))
        self.pgrid.add_widget(Image(source="2.gif"))
        self.pgrid.add_widget(Image(source="3.gif"))
        self.pgrid.add_widget(Image(source="4.gif"))
        self.pgrid.add_widget(Image(source="5.gif"))
    def press0(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(0)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=cdi[str(self.fnum)]
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(self.fnum)+"\n \n",font_size=self.font)
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
        self.add=Label(text="\n \n"+str(1+self.fnum)+"\n \n",font_size=self.font)
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
        self.add=Label(text="\n \n"+str(2+self.fnum)+"\n \n",font_size=self.font)
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
        self.add=Label(text="\n \n"+str(3+self.fnum)+"\n \n",font_size=self.font)
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
        self.add=Label(text="\n \n"+str(4+self.fnum)+"\n \n",font_size=self.font)
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
        self.add=Label(text="\n \n"+str(5+self.fnum)+"\n \n",font_size=self.font)
        self.bl.add_widget(self.add, index=3)
        if 5+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 5+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

    def on_press(self):
        print(self.last_touch.spos)
        touch=self.last_touch.spos
        if 0.86< touch[0] <1 and 0< touch[1] <0.15 :
            self.press5()
        elif  0.7< touch[0] <0.78 and 0< touch[1] <0.15 :
            self.press4()
        elif  0.54< touch[0] <0.62 and 0< touch[1] <0.15 :
            self.press3()
        elif  0.37< touch[0] <0.45 and 0< touch[1] <0.15 :
            self.press2()
        elif  0.21< touch[0] <0.28 and 0< touch[1] <0.15 :
            self.press1()
        elif  0< touch[0] <0.12 and 0< touch[1] <0.15 :
            self.press0()
        

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

class tourn(Screen, ButtonBehavior, Image):     
    def __init__(self,pnum,i, **kwargs):
        super(tourn,self).__init__(**kwargs)
        self.pnum=pnum
        self.name='tourn'+str(i)
        self.bl=BoxLayout(orientation="vertical")
        self.add_widget(self.bl)
        choice=list(range(11))
        choice.remove(self.pnum)
        self.cnum1=choice[random.randint(0,9)]
        choice.remove(self.cnum1)
        self.cnum2=choice[random.randint(0,8)]
        choice.remove(self.cnum2)
        self.cnum3=choice[random.randint(0,7)]
        
        self.dcnum1=Label(text=str(self.cnum1))
        self.bl.add_widget(self.dcnum1)
        self.cfin1=Label()
        self.bl.add_widget(self.cfin1)
        
        self.popup=None
        self.c23grid=BoxLayout(orientation="horizontal")
        self.bl.add_widget(self.c23grid)
        self.dcnum2=Label(text=str(self.cnum2))
        self.c23grid.add_widget(self.dcnum2)
        self.cfin2=Label(text='Player2 finger')
        self.sum=Label(text='sum')
        self.cfin3=Label(text='Player3 finger')
        self.c23grid.add_widget(self.cfin2, index=-1)
        self.c23grid.add_widget(self.sum, index=-2)
        self.c23grid.add_widget(self.cfin3, index=-3)
        self.dcnum3=Label(text=str(self.cnum3))
        self.c23grid.add_widget(self.dcnum3, index=-4)
        self.i=i

        '''
        #DISPLAY COMPUTER CHOOSEN NUMBER
        self.clbl= Label(text=str(self.cnum), color=(1,1,1,1), )
        self.bl.add_widget(self.clbl)
        
        #display computer finger on table
        self.cfin=Label()
        self.bl.add_widget(self.cfin)

        #show the sum of computer finger and player finger
        self.add=Label(text="\n \n"+"  "+"\n \n")
        self.bl.add_widget(self.add)
        '''

        #display player finger on table
        self.pfin=Label()
        self.bl.add_widget(self.pfin)

        #DISPLAY player CHOOSEN NUMBER
        self.plbl= Label(text=str(self.pnum), color=(1,1,1,1))
        self.bl.add_widget(self.plbl)

        #player finger grid
        self.pgrid=BoxLayout()
        self.pgrid.orientation="horizontal"
        self.bl.add_widget(self.pgrid)
        
        self.p0=Image(source="0.gif")
        self.pgrid.add_widget(self.p0)

        self.p1=Image(source="1.gif")
        self.pgrid.add_widget(self.p1)
        
        self.p2=Image(source="2.gif")
        self.pgrid.add_widget(self.p2)

        self.p3=Image(source="3.gif")
        self.pgrid.add_widget(self.p3)

        self.p4=Image(source="4.gif")
        self.pgrid.add_widget(self.p4)

        self.p5=Image(source="5.gif")
        #self.p5.on_press=self.press5
        self.pgrid.add_widget(self.p5)
    def press0(self, *args):
        
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(0)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum1=random.randint(0,5)
        self.fnum2=random.randint(0,5)
        self.fnum3=random.randint(0,5)
        self.sum.text=str(self.fnum1 +self.fnum2+self.fnum3+0)
        self.c23grid.remove_widget(self.cfin2)
        self.cfin2=Image(source=str(self.fnum2)+'.gif')
        self.c23grid.add_widget(self.cfin2, index=-1)

        self.c23grid.remove_widget(self.cfin3)
        self.cfin3=Image(source=str(self.fnum3)+'.gif')
        self.c23grid.add_widget(self.cfin3, index=-3)
        self.bl.remove_widget(self.cfin1)
        self.cfin1=Image(source=str(self.fnum1)+'.gif')
        self.bl.add_widget(self.cfin1, index=4)
        '''
        if 0+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='NEW GAME', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 0+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        '''
    def press1(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(1)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum1=random.randint(0,5)
        self.fnum2=random.randint(0,5)
        self.fnum3=random.randint(0,5)
        self.sum.text=str(self.fnum1 +self.fnum2+self.fnum3+1)
        self.c23grid.remove_widget(self.cfin2)
        self.cfin2=Image(source=str(self.fnum2)+'.gif')
        self.c23grid.add_widget(self.cfin2, index=-1)

        self.c23grid.remove_widget(self.cfin3)
        self.cfin3=Image(source=str(self.fnum3)+'.gif')
        self.c23grid.add_widget(self.cfin3, index=-3)
        self.bl.remove_widget(self.cfin1)
        self.cfin1=Image(source=str(self.fnum1)+'.gif')
        self.bl.add_widget(self.cfin1, index=4)
        '''
        if 1+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif 1+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        '''
    def press2(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(2)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum1=random.randint(0,5)
        self.fnum2=random.randint(0,5)
        self.fnum3=random.randint(0,5)
        self.sum.text=str(self.fnum1 +self.fnum2+self.fnum3+2)
        self.c23grid.remove_widget(self.cfin2)
        self.cfin2=Image(source=str(self.fnum2)+'.gif')
        self.c23grid.add_widget(self.cfin2, index=-1)

        self.c23grid.remove_widget(self.cfin3)
        self.cfin3=Image(source=str(self.fnum3)+'.gif')
        self.c23grid.add_widget(self.cfin3, index=-3)
        self.bl.remove_widget(self.cfin1)
        self.cfin1=Image(source=str(self.fnum1)+'.gif')
        self.bl.add_widget(self.cfin1, index=4)
        '''
        if 2+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif 2+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        '''
    def press3(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(3)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum1=random.randint(0,5)
        self.fnum2=random.randint(0,5)
        self.fnum3=random.randint(0,5)
        self.sum.text=str(self.fnum1 +self.fnum2+self.fnum3+3)
        self.c23grid.remove_widget(self.cfin2)
        self.cfin2=Image(source=str(self.fnum2)+'.gif')
        self.c23grid.add_widget(self.cfin2, index=-1)

        self.c23grid.remove_widget(self.cfin3)
        self.cfin3=Image(source=str(self.fnum3)+'.gif')
        self.c23grid.add_widget(self.cfin3, index=-3)
        self.bl.remove_widget(self.cfin1)
        self.cfin1=Image(source=str(self.fnum1)+'.gif')
        self.bl.add_widget(self.cfin1, index=4)
        '''
        if 3+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif 3+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        '''
    def press4(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(4)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum1=random.randint(0,5)
        self.fnum2=random.randint(0,5)
        self.fnum3=random.randint(0,5)
        self.sum.text=str(self.fnum1 +self.fnum2+self.fnum3+4)
        self.c23grid.remove_widget(self.cfin2)
        self.cfin2=Image(source=str(self.fnum2)+'.gif')
        self.c23grid.add_widget(self.cfin2, index=-1)

        self.c23grid.remove_widget(self.cfin3)
        self.cfin3=Image(source=str(self.fnum3)+'.gif')
        self.c23grid.add_widget(self.cfin3, index=-3)
        self.bl.remove_widget(self.cfin1)
        self.cfin1=Image(source=str(self.fnum1)+'.gif')
        self.bl.add_widget(self.cfin1, index=4)
        '''
        if 4+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 4+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        '''
    def press5(self, *args):
        self.bl.remove_widget(self.pfin)
        self.pfin=pdi[str(5)]
        self.bl.add_widget(self.pfin, index=2)

        self.fnum1=random.randint(0,5)
        self.fnum2=random.randint(0,5)
        self.fnum3=random.randint(0,5)
        self.sum.text=str(self.fnum1 +self.fnum2+self.fnum3+5)
        self.c23grid.remove_widget(self.cfin2)
        self.cfin2=Image(source=str(self.fnum2)+'.gif')
        self.c23grid.add_widget(self.cfin2, index=-1)

        self.c23grid.remove_widget(self.cfin3)
        self.cfin3=Image(source=str(self.fnum3)+'.gif')
        self.c23grid.add_widget(self.cfin3, index=-3)
        self.bl.remove_widget(self.cfin1)
        self.cfin1=Image(source=str(self.fnum1)+'.gif')
        self.bl.add_widget(self.cfin1, index=4)
        '''
        if 5+self.fnum== self.pnum :
            self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        elif 5+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()
        '''
    def on_press(self):
        print(self.last_touch.spos)
        touch=self.last_touch.spos
        if 0.86< touch[0] <1 and 0< touch[1] <0.15 :
            self.press5()
        elif  0.7< touch[0] <0.78 and 0< touch[1] <0.15 :
            self.press4()
        elif  0.54< touch[0] <0.62 and 0< touch[1] <0.15 :
            self.press3()
        elif  0.37< touch[0] <0.45 and 0< touch[1] <0.15 :
            self.press2()
        elif  0.21< touch[0] <0.28 and 0< touch[1] <0.15 :
            self.press1()
        elif  0< touch[0] <0.12 and 0< touch[1] <0.15 :
            self.press0()
        

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
        self.parent.add_widget(tourn(i=self.i, pnum=self.pnum))
        self.manager.current='tourn'+str(self.i)
        self.clear_widgets()


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
        self.add_widget(Image(source="cover.jpg"))
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
        self.gd.add_widget(Label(text=abt, size_hint=self.size))
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
