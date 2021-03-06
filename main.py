from kivy.uix.button import Button
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.image import Image
from kivy.uix.button import ButtonBehavior
from kivy.uix.behaviors import CoverBehavior
from kivy.graphics import Color
import random
from kivmob import KivMob
from kivy.uix.screenmanager import ScreenManager, Screen

class CoverImage(CoverBehavior, Image):
    def __init__(self, **kwargs):
        super(CoverImage, self).__init__(**kwargs)
        texture = self._coreimage.texture
        self.reference_size = texture.size
        self.texture = texture
class winImg(ButtonBehavior,Image): 
    def __init__(self,i, **kwargs):
        super(winImg,self).__init__(**kwargs)
        
class CovAbt(ButtonBehavior,Label): 
    def __init__(self, **kwargs):
        super(CovAbt,self).__init__(**kwargs)
        file=open('About.txt', 'r')
        abt=file.read()
        file.close()
        self.text=abt


class game(ButtonBehavior,Screen):     
    def __init__(self,pnum,i, **kwargs):
        super(game,self).__init__(**kwargs)
        self.pnum=pnum
        self.name='game'+str(i)
        self.bl=BoxLayout()
        diff=open('difficulty.txt', 'r')
        present=diff.read()
        diff.close()
        self.font=30
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
        self.cgrid.add_widget(Image(source="0c.gif"))

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
        self.pgrid.add_widget(Image(source="2cy.png"))
        self.pgrid.add_widget(Image(source="3.gif"))
        self.pgrid.add_widget(Image(source="4.gif"))
        self.pgrid.add_widget(Image(source="5.gif"))


    def press(self, constant):
        constant=constant
        reason=open('constant.txt', 'r')
        remove=reason.read()
        reason.close()

        reason=open('constant.txt', 'w')
        reason.write(str(abs(constant-self.pnum)))
        reason.close()
        remember=list(range(6))
        
        try :
            remember.remove(int(remove))
            self.fnum=remember[random.randint(0,4)]
        except ValueError :
            self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.pfin)
        self.pfin=Image(source=str(constant)+".gif")
        self.bl.add_widget(self.pfin, index=2)        
        #self.fnum=random.randint(0,5)
        self.bl.remove_widget(self.cfin)
        self.cfin=Image(source=str(self.fnum)+'c.gif')
        self.bl.add_widget(self.cfin, index=4)

        self.bl.remove_widget(self.add)
        self.add=Label(text="\n \n"+str(constant+self.fnum)+"\n \n",font_size=self.font)
        self.bl.add_widget(self.add, index=3)
        if constant+self.fnum== self.pnum :
            self.popup = Popup(title="                                             YOU WIN",auto_dismiss=True ,content=winImg(self.i, source='you_win.jpeg',on_press=self.gopickNum), opacity=0.5)
            #self.popup = Popup(title="YOU WIN", content=Button(text='New GAME',on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
            self.popup.open()

        elif constant+self.fnum== self.cnum:
            self.popup = Popup(title="CPU WINS", content=winImg(self.i, source='again.jpg',on_press=self.gopickNum), opacity=0.5)
            self.popup.open()

    def on_press(self):
        print(self.last_touch.spos)
        touch=self.last_touch.spos
        if 0.86< touch[0] <1 and 0< touch[1] <0.15 :
            self.press(5)
        elif  0.7< touch[0] <0.78 and 0< touch[1] <0.15 :
            self.press(4)
        elif  0.54< touch[0] <0.62 and 0< touch[1] <0.15 :
            self.press(3)
        elif  0.37< touch[0] <0.45 and 0< touch[1] <0.15 :
            self.press(2)
        elif  0.21< touch[0] <0.28 and 0< touch[1] <0.15 :
            self.press(1)
        elif  0< touch[0] <0.12 and 0< touch[1] <0.15 :
            self.press(0)
        
    def gopickNum(self,instance):
        count=open('count.txt', 'r')
        j=count.read()
        count.close()
        i=1+int(j)
        #print(i)
        count=open('count.txt', 'w')
        count.write(str(i))
        count.close()        
        count=open('count.txt', 'r')
        j=count.read()
        count.close()
        self.parent.parent.parent.add_widget(manager(int(j)))
        self.parent.clear_widgets()
        self.clear_widgets()
        self.bl.clear_widgets()
        self.popup.dismiss()

class tourn(ButtonBehavior,Screen):     
    def __init__(self,pnum,i, **kwargs):
        super(tourn,self).__init__(**kwargs)
        self.qual1=False
        self.qual2=False
        self.qual3=False
        self.qualp=False
        self.qual1_2=False
        self.qual2_2=False
        self.qual3_2=False
        self.qualp_2=False
        self.round1=True
        self.round2=False
        self.round3=False
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
        self.popup = Popup(title="    Round One",auto_dismiss=False,content=Button(text='Start', on_press=self.remove), opacity=0.5, size_hint=(None, None), size=(200, 200))
        self.popup.open()        

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
        self.p0=Image(source='0.gif')
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
        self.pgrid.add_widget(self.p5)
    def remove(self, instance):
        self.popup.dismiss()
    def ply(self, constant):
        constant=constant
        if self.round1==True and self.qual1==False and self.qual2==False and self.qual3==False and self.qualp==False :
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            self.fnum1=random.randint(0,5)
            self.fnum2=random.randint(0,5)
            self.fnum3=random.randint(0,5)
            self.sum.text=str(self.fnum1 +self.fnum2+self.fnum3+constant)
            
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Image(source=str(self.fnum2)+'.gif')
            self.c23grid.add_widget(self.cfin2, index=-1)

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Image(source=str(self.fnum3)+'.gif')
            self.c23grid.add_widget(self.cfin3, index=-3)

            self.bl.remove_widget(self.cfin1)
            self.cfin1=Image(source=str(self.fnum1)+'.gif')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.round1=False
                self.round2=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False,content=Button(text='Next Round', on_press=self.gornd2), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
            elif int(self.sum.text)== self.cnum1 :
                self.popup = Popup(title="CPU1 Qualify", content=Label(text='Continue', opacity=0.5),  size_hint=(None, None), size=(200, 200))   
                self.popup.open()
                self.qual1=True
            elif int(self.sum.text)== self.cnum2 :
                self.popup = Popup(title="CPU2 Qualify", content=Label(text='Continue'), size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual2=True
            elif int(self.sum.text)== self.cnum3 :
                self.popup = Popup(title="CPU3 Qualify", content=Label(text='Continue'), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual3=True
        elif self.round1==True and  self.qual1==True and self.qual2==False and self.qual3==False and self.qualp==False :
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            #self.fnum1=random.randint(0,5)
            self.fnum2=random.randint(0,5)
            self.fnum3=random.randint(0,5)
            self.sum.text=str(self.fnum2+self.fnum3+constant)
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Image(source=str(self.fnum2)+'.gif')
            self.c23grid.add_widget(self.cfin2, index=-1)

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Image(source=str(self.fnum3)+'.gif')
            self.c23grid.add_widget(self.cfin3, index=-3)

            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Qualified')
            self.bl.add_widget(self.cfin1, index=4)
        
            if int(self.sum.text)== self.pnum :
                self.round1=False
                self.round2=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round', on_press=self.gornd2), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True

            elif int(self.sum.text)== self.cnum2 :
                self.popup = Popup(title="CPU2 Qualify", content=Label(text='Continue'), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual2=True
            elif int(self.sum.text)== self.cnum3 :
                self.popup = Popup(title="CPU3 Qualify", content=Label(text='Continue', on_press=self.gornd2), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual3=True
        elif self.round1==True and  self.qual1==False and self.qual2==True and self.qual3==False and self.qualp==False :
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)
            self.fnum1=random.randint(0,5)
            self.fnum3=random.randint(0,5)
            self.sum.text=str(self.fnum1+self.fnum3+constant)
            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Image(source=str(self.fnum3)+'.gif')
            self.c23grid.add_widget(self.cfin3, index=-3)

            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Qualified')
            self.c23grid.add_widget(self.cfin2, index=-1)

            self.bl.remove_widget(self.cfin1)
            self.cfin1=Image(source=str(self.fnum1)+'.gif')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.round1=False
                self.round2=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round', on_press=self.gornd2), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
            elif int(self.sum.text)== self.cnum1 :
                self.popup = Popup(title="CPU1 Qualify", content=Label(text='Continue'),  size_hint=(None, None), size=(200, 200))               
                self.popup.open()
                self.qual1=True
            elif int(self.sum.text)== self.cnum3 :
                self.popup = Popup(title="CPU3 Qualify", content=Label(text='Continue'), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual3=True
        elif self.round1==True and  self.qual1==False and self.qual2==False and self.qual3==True and self.qualp==False :
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)
            self.fnum1=random.randint(0,5)
            self.fnum2=random.randint(0,5)
            self.sum.text=str(self.fnum1 +self.fnum2+constant)         
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Image(source=str(self.fnum2)+'.gif')
            self.c23grid.add_widget(self.cfin2, index=-1)
            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Qualified')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Image(source=str(self.fnum1)+'.gif')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.round1=False
                self.round2=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round', on_press=self.gornd2), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
            elif int(self.sum.text)== self.cnum1 :
                self.popup = Popup(title="CPU1 Qualify", content=Label(text='Continue'),  size_hint=(None, None), size=(200, 200))                
                self.popup.open()
                self.qual1=True
            elif int(self.sum.text)== self.cnum2 :
                self.popup = Popup(title="CPU2 Qualify", content=Label(text='Continue'), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual2=True
        elif self.round1==True and  self.qual1==True and self.qual2==True and self.qual3==False and self.qualp==False :
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)
            self.fnum3=random.randint(0,5)
            self.sum.text=str(self.fnum3+constant)          
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Qualified')
            self.c23grid.add_widget(self.cfin2, index=-1)
            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Image(source=str(self.fnum3)+'.gif')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Qualified')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.round1=False
                self.round2=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round', on_press=self.gornd2), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
            elif int(self.sum.text)== self.cnum3 :
                self.popup = Popup(title="You Are Out",content=Button(text='Play Again', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.c23grid.remove_widget(self.cfin3)
                self.cfin3=Label(text='Qualified')
                self.c23grid.add_widget(self.cfin3, index=-3)
                self.popup.open()
                self.qual3=True
        
        elif self.round1==True and self.qual1==True and self.qual2==False and self.qual3==True and self.qualp==False :
            
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)
            
            self.fnum2=random.randint(0,5)
            self.sum.text=str(self.fnum2+constant)
            
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Image(source=str(self.fnum2)+'.gif')
            self.c23grid.add_widget(self.cfin2, index=-1)
            

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Qualified')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Qualified')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.round1=False
                self.round2=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round', on_press=self.gornd2), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
                
            elif int(self.sum.text)== self.cnum2 :
                self.popup = Popup(title="You Are Out", auto_dismiss=False,content=Button(text='Play Again', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual2=True

        elif self.round1==True and self.qual1==False and self.qual2==True and self.qual3==True and self.qualp==False :
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            self.fnum1=random.randint(0,5)
            self.sum.text=str(self.fnum1 +constant)
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Qualified')
            self.c23grid.add_widget(self.cfin2, index=-1)
            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Qualified')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Image(source=str(self.fnum1)+'.gif')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round', on_press=self.gornd2), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
                self.round1=False
                self.round2=True
            elif int(self.sum.text)== self.cnum1 :
                self.popup = Popup(title="CPU1 Qualify",auto_dismiss=False, content=Button(text='You Are Out',on_press=self.gopickNum, opacity=0.5),  size_hint=(None, None), size=(200, 200))                
                self.popup.open()
                self.qual1=True
        
        #Round Two
        #Player 1 did not qualify phase one
        elif self.round2==True and  self.qual1==False and self.qual2==True and self.qual3==True and self.qualp==True and self.qual2_2==False and self.qual3_2==False :
            print('Player 1 did not qualify phase one')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            #self.fnum1=random.randint(0,5)
            self.fnum2=random.randint(0,5)
            self.fnum3=random.randint(0,5)
            self.sum.text=str(self.fnum2+self.fnum3+constant)
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Image(source=str(self.fnum2)+'.gif')
            self.c23grid.add_widget(self.cfin2, index=-1)

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Image(source=str(self.fnum3)+'.gif')
            self.c23grid.add_widget(self.cfin3, index=-3)

            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Out')
            self.bl.add_widget(self.cfin1, index=4)
        
            if int(self.sum.text)== self.pnum :
                self.round2=False
                self.round3=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round\n(3)', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                #self.bl.remove_widget(self.pfin)
                #self.pfin=Label(text="Qualified")
                #self.bl.add_widget(self.pfin, index=2)
                self.popup.open()
                self.qualp_2=True

            elif int(self.sum.text)== self.cnum2 :
                self.popup = Popup(title="CPU2 Qualify", content=Label(text='Continue'), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual2_2=True
            elif int(self.sum.text)== self.cnum3 :
                self.popup = Popup(title="CPU3 Qualify", content=Label(text='Continue'), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual3_2=True
        #Player2 did not qualify phase one
        elif self.round2==True and  self.qual1==True and self.qual2==False and self.qual3==True and self.qualp==True and self.qual1_2==False and self.qual3_2==False  :
            #print('Player2 did not qualify phase one')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            self.fnum1=random.randint(0,5)
            #self.fnum2=random.randint(0,5)
            self.fnum3=random.randint(0,5)
            self.sum.text=str(self.fnum1+self.fnum3+constant)

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Image(source=str(self.fnum3)+'.gif')
            self.c23grid.add_widget(self.cfin3, index=-3)

            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Out')
            self.c23grid.add_widget(self.cfin2, index=-1)

            self.bl.remove_widget(self.cfin1)
            self.cfin1=Image(source=str(self.fnum1)+'.gif')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.round2=False
                self.round3=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round\n(3)', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                #self.bl.remove_widget(self.pfin)
                #self.pfin=Label(text="Qualified")
                #self.bl.add_widget(self.pfin, index=2)
                self.popup.open()
                self.qualp_2=True
            elif int(self.sum.text)== self.cnum1 :
                self.popup = Popup(title="CPU1 Qualify", content=Label(text='Continue'),  size_hint=(None, None), size=(200, 200))               
                self.popup.open()
                self.qual1_2=True

            elif int(self.sum.text)== self.cnum3 :
                self.popup = Popup(title="CPU3 Qualify", content=Label(text='Continue'), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual3_2=True
        #Player3 did not qualify phase one
        elif self.round2==True and  self.qual1==True and self.qual2==True and self.qual3==False and self.qualp==True and self.qual2_2==False and self.qual1_2==False  :
            #print('Player3 did not qualify phase one')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)
            self.fnum1=random.randint(0,5)
            self.fnum2=random.randint(0,5)
            self.sum.text=str(self.fnum1 +self.fnum2+constant)
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Image(source=str(self.fnum2)+'.gif')
            self.c23grid.add_widget(self.cfin2, index=-1)
            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Out')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Image(source=str(self.fnum1)+'.gif')
            self.bl.add_widget(self.cfin1, index=4)
        
            if int(self.sum.text)== self.pnum :
                self.round2=False
                self.round3=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp_2=True
            elif int(self.sum.text)== self.cnum1 :
                self.popup = Popup(title="CPU1 Qualify", content=Label(text='Continue'),  size_hint=(None, None), size=(200, 200))                
                self.popup.open()
                self.qual1_2=True
            elif int(self.sum.text)== self.cnum2 :
                self.popup = Popup(title="CPU2 Qualify", content=Label(text='Continue'), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual2_2=True


        #Player1 did not qualify for round one Player2 Quaalify for round 3
        elif self.round2==True and  self.qual1==False and self.qual2_2==True and self.qual3_2==False and self.qualp_2==False :  
            print('Player1 did not qualify for round one Player2 Quaalify for round 3')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            self.fnum3=random.randint(0,5)
            self.sum.text=str(self.fnum3+constant)
            
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Qualified')
            self.c23grid.add_widget(self.cfin2, index=-1)

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Image(source=str(self.fnum3)+'.gif')
            self.c23grid.add_widget(self.cfin3, index=-3)

            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Out')
            self.bl.add_widget(self.cfin1, index=4)
        
            if int(self.sum.text)== self.pnum :
                self.round2=False
                self.round3=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round\n(3)', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp_2=True
            elif int(self.sum.text)== self.cnum3 :
                self.popup = Popup(title="You Are Out",auto_dismiss=False,content=Button(text='Play Again', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.c23grid.remove_widget(self.cfin3)
                self.cfin3=Label(text='Qualified')
                self.c23grid.add_widget(self.cfin3, index=-3)
                self.popup.open()
                self.qual3_2=True
        #Player1 did not qualify for round one But player3 qualify for round 3
        elif self.round2==True and  self.qual1==False and self.qual2_2==False and self.qual3_2==True and self.qualp_2==False :              
            print('Player1 did not qualify for round one But player3 qualify for round 3')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)
            
            self.fnum2=random.randint(0,5)
            self.sum.text=str(self.fnum2+constant)
            
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Image(source=str(self.fnum2)+'.gif')
            self.c23grid.add_widget(self.cfin2, index=-1)
            

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Qualified')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Out')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.round1=False
                self.round2=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round\n3', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp_2=True
                
            elif int(self.sum.text)== self.cnum2 :
                self.popup = Popup(title="You Are Out", auto_dismiss=False,content=Button(text='Play Again', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual2_2=True
        #Player2 did not qualify for round one Player1 Quaalify for round 3
        elif self.round2==True and self.qual1_2==True and self.qual2==False and self.qual3_2==False and self.qualp_2==False :  
            print('Player2 did not qualify for round one Player1 Quaalify for round 3')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            self.fnum3=random.randint(0,5)
            self.sum.text=str(self.fnum3+constant)
            
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Out')
            self.c23grid.add_widget(self.cfin2, index=-1)

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Image(source=str(self.fnum3)+'.gif')
            self.c23grid.add_widget(self.cfin3, index=-3)

            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Qualified\round 3')
            self.bl.add_widget(self.cfin1, index=4)
        
            if int(self.sum.text)== self.pnum :
                self.round2=False
                self.round3=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp_2=True
            elif int(self.sum.text)== self.cnum3 :
                self.popup = Popup(title="You Are Out",auto_dismiss=False,content=Button(text='Play Again', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.c23grid.remove_widget(self.cfin3)
                self.cfin3=Label(text='Qualified')
                self.c23grid.add_widget(self.cfin3, index=-3)
                self.popup.open()
                self.qual3_2=True
        #Player2 did not qualify for round one Player3 Quaalify for round 3
        elif self.round2==True and self.qual1_2==False and self.qual2==False and self.qual3_2==True and self.qualp_2==False :  
            print('Player2 did not qualify for round one Player3 Quaalify for round 3')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            self.fnum1=random.randint(0,5)
            self.sum.text=str(self.fnum1 +constant)
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Out')
            self.c23grid.add_widget(self.cfin2, index=-1)
            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Qualified\nround 3')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Image(source=str(self.fnum1)+'.gif')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round\n3', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
                self.round2=False
                self.round3=True
            elif int(self.sum.text)== self.cnum1 :
                self.popup = Popup(title="CPU1 Qualify", auto_dismiss=False,content=Button(text='You Are Out',on_press=self.gopickNum, opacity=0.5),  size_hint=(None, None), size=(200, 200))                
                self.popup.open()
                self.qual1=True
        #Player3 did not qualify for round one Player1 Quaalify for round 3
        elif self.round2==True and self.qual1_2==True and self.qual2_2==False and self.qual3==False and self.qualp_2==False :  
            print('Player3 did not qualify for round one Player1 Quaalify for round 3')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)
            
            self.fnum2=random.randint(0,5)
            self.sum.text=str(self.fnum2+constant)
            
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Image(source=str(self.fnum2)+'.gif')
            self.c23grid.add_widget(self.cfin2, index=-1)
            

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Out')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Qualified\round 3')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.round2=False
                self.round3=True
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round\3', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
                
            elif int(self.sum.text)== self.cnum2 :
                self.popup = Popup(title="You Are Out", auto_dismiss=False,content=Button(text='Play Again', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual2=True
        #Player3 did not qualify for round one Player2 Quaalify for round 3
        elif self.round2==True and self.qual2_2==True and self.qual1_2==False and self.qual3==False and self.qualp_2==False :  
            print('Player3 did not qualify for round one Player2 Quaalify for round 3')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            self.fnum1=random.randint(0,5)
            self.sum.text=str(self.fnum1 +constant)
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Qualified\round 3')
            self.c23grid.add_widget(self.cfin2, index=-1)
            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Out')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Image(source=str(self.fnum1)+'.gif')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.popup = Popup(title="Player Qualify",auto_dismiss=False ,content=Button(text='Next Round', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
                self.round2=False
                self.round3=True
            elif int(self.sum.text)== self.cnum1 :
                self.popup = Popup(title="CPU1 Qualify", content=Button(text='You Are Out',on_press=self.gopickNum, opacity=0.5),  size_hint=(None, None), size=(200, 200))                
                self.popup.open()
                self.qual1=True
        #Round 3
        #CPU1 Got final
        elif self.round3==True and self.qual1_2==True and self.qual2_2==False and self.qual3_2==False :
            print('CPU1 Got final')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            self.fnum1=random.randint(0,5)
            self.sum.text=str(self.fnum1 +constant)
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Out')
            self.c23grid.add_widget(self.cfin2, index=-1)
            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Out')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Image(source=str(self.fnum1)+'.gif')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.popup = Popup(title="You Win The Tournament",auto_dismiss=False ,content=Button(text='New Game', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
                self.round2=False
                self.round3=True
            elif int(self.sum.text)== self.cnum1 :
                self.popup = Popup(title="You Loose", content=Button(text='New Game',on_press=self.gopickNum, opacity=0.5),  size_hint=(None, None), size=(200, 200))                
                self.popup.open()
                self.qual1=True
        #CPU2 got final
        elif self.round3==True and self.qual1_2==False and self.qual2_2==True and self.qual3_2==False :
            print('CPU2 got final')
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)
            
            self.fnum2=random.randint(0,5)
            self.sum.text=str(self.fnum2+constant)
            
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Image(source=str(self.fnum2)+'.gif')
            self.c23grid.add_widget(self.cfin2, index=-1)
            

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Label(text='Out')
            self.c23grid.add_widget(self.cfin3, index=-3)
            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Out')
            self.bl.add_widget(self.cfin1, index=4)
            if int(self.sum.text)== self.pnum :
                self.round2=False
                self.round3=True
                self.popup = Popup(title="You Win The Tournament",auto_dismiss=False ,content=Button(text='New Game', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp=True
                
            elif int(self.sum.text)== self.cnum2 :
                self.popup = Popup(title="You Loose", auto_dismiss=False,content=Button(text='Play Again', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qual2=True

        elif self.round3==True and self.qual1_2==False and self.qual2_2==False and self.qual3_2==True :
            self.bl.remove_widget(self.pfin)
            self.pfin=Image(source=str(constant)+".gif")
            self.bl.add_widget(self.pfin, index=2)

            self.fnum3=random.randint(0,5)
            self.sum.text=str(self.fnum3+constant)
            
            self.c23grid.remove_widget(self.cfin2)
            self.cfin2=Label(text='Out')
            self.c23grid.add_widget(self.cfin2, index=-1)

            self.c23grid.remove_widget(self.cfin3)
            self.cfin3=Image(source=str(self.fnum3)+'.gif')
            self.c23grid.add_widget(self.cfin3, index=-3)

            self.bl.remove_widget(self.cfin1)
            self.cfin1=Label(text='Out')
            self.bl.add_widget(self.cfin1, index=4)
        
            if int(self.sum.text)== self.pnum :
                self.round2=False
                self.round3=True
                self.popup = Popup(title="You Win The Tournament",auto_dismiss=False ,content=Button(text='Next Round\n(3)', on_press=self.gornd3), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.popup.open()
                self.qualp_2=True
            elif int(self.sum.text)== self.cnum3 :
                self.popup = Popup(title="You Loose",auto_dismiss=False,content=Button(text='Play Again', on_press=self.gopickNum), opacity=0.5, size_hint=(None, None), size=(200, 200))
                self.c23grid.remove_widget(self.cfin3)
                self.cfin3=Label(text='Winner')
                self.c23grid.add_widget(self.cfin3, index=-3)
                self.popup.open()
                self.qual3_2=True
    def gornd2(self, instance):
        print('gornd2 worked')
        if self.round1==False and self.qual1==False and self.qual2==False and self.qual3==False and self.qualp==True :
            print('gornd2 if')
            rndfirst=random.randint(1,3)
            pk=list([1,2,3])
            pk.remove(rndfirst)
            rndsecond=pk[random.randint(0,1)]
            print(rndfirst,'   ', rndsecond)
            qual=list([rndfirst, rndsecond])
            if 1 in qual :
                if 2 in qual :
                    self.qual1 =True
                    self.qual2=True
                elif 3 in qual:
                    self.qual1=True
                    self.qual3 = True
            elif 2 in qual :
                if 3 in qual:
                    self.qual2 =True
                    self.qual3 = True
        elif self.round1==False and self.qual1==True and self.qual2==False and self.qual3==False and self.qualp==True :
            print('gornd2 elif1')
            rndfirst=random.randint(1,2)
            if rndfirst==1 :
                self.qual2= True
            elif rndfirst==2  :
                self.qual3=True
        elif self.round1==False and self.qual1==False and self.qual2==True and self.qual3==False and self.qualp==True :
            print('gornd2 elif2')
            rndfirst=random.randint(1,2)
            if rndfirst==1 :
                self.qual1= True
            elif rndfirst==2  :
                self.qual3=True
        elif self.round1==False and self.qual1==False and self.qual2==False and self.qual3==True and self.qualp==True :
            print('gornd2 elif3')
            rndfirst=random.randint(1,2)
            if rndfirst==1 :
                self.qual2= True
            elif rndfirst==2  :
                self.qual1=True
        else :
            pass
        self.popup.dismiss()
        print(self.qual1,' ', self.qual2,' ', self.qual3)
    def gornd3(self, instance):
        print('gornd3 worked')
        if self.round2==False and self.qual1==False and self.qual2_2==False and self.qual3_2==False :
            rndfirst=random.randint(1,2)
            print('gornd3 if')
            if rndfirst==1 :
                self.qual2_2= True
            elif rndfirst==2  :
                self.qual3_2=True
        elif self.round2==False and self.qual2==False and self.qual1_2==False and self.qual3_2==False :
            print('gornd3 elif1')
            rndfirst=random.randint(1,2)
            if rndfirst==1 :
                self.qual1_2= True
            elif rndfirst==2  :
                self.qual3_2=True
        elif self.round2==False and self.qual3==False and self.qual2_2==False and self.qual1_2==False :
            print('gornd3 elif2')
            rndfirst=random.randint(1,2)
            if rndfirst==1 :
                self.qual2_2= True
            elif rndfirst==2  :
                self.qual1_2=True
        self.popup.dismiss()
        print(self.qual1_2,' ',self.qual2_2,' ', self.qual3_2 )

    def on_press(self):
        touch=self.last_touch.spos
        print(touch)
        if 0.86< touch[0] <1 and 0< touch[1] <0.15 :
            self.ply(5)
        elif  0.7< touch[0] <0.78 and 0< touch[1] <0.15 :
            self.ply(4)
        elif  0.54< touch[0] <0.62 and 0< touch[1] <0.15 :
            self.ply(3)
        elif  0.37< touch[0] <0.45 and 0< touch[1] <0.15 :
            self.ply(2)
        elif  0.21< touch[0] <0.28 and 0< touch[1] <0.15 :
            self.ply(1)
        elif  0< touch[0] <0.12 and 0< touch[1] <0.15 :
            self.ply(0)

        if 0.48< touch[0] <0.51 and 0.55< touch[1] <0.61 :
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
            #print(j)
            self.parent.parent.parent.add_widget(manager(int(j)))
            try :
                self.parent.parent.clear_widgets()
            except:
                pass
            self.parent.clear_widgets()
            self.clear_widgets()
            self.pgrid.clear_widgets()
            self.bl.clear_widgets()
        

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
        self.pgrid.clear_widgets()
        self.popup.dismiss()
    def round21(self):
        pass

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


class pickNum(ButtonBehavior,Screen):
    def __init__(self,i, **kwargs):
        super(pickNum, self).__init__(**kwargs)
        self.add_widget(CoverImage(source="picknum.jpg"))
        self.i=i
        self.name='pickNum'+str(i)
    def pikk(self,number):
        number=number
        self.parent.add_widget(pickto(i=self.i, pnum=number))
        self.manager.current='pickto'+str(self.i)
        self.clear_widgets()
    def on_press(self):
        print(self.last_touch.spos)
        if 0.035<self.last_touch.spos[0]<0.125 and 0.36<self.last_touch.spos[1]<0.47 :
            self.pikk(1)
        elif 0.26<self.last_touch.spos[0]<0.35 and 0.36<self.last_touch.spos[1]<0.47 :
            self.pikk(8)
        elif 0.46<self.last_touch.spos[0]<0.55 and 0.36<self.last_touch.spos[1]<0.47 :
            self.pikk(5)
        elif 0.69<self.last_touch.spos[0]<0.78 and 0.36<self.last_touch.spos[1]<0.47 :
            self.pikk(10)
        elif 0.85<self.last_touch.spos[0]<1 and 0.36<self.last_touch.spos[1]<0.47 :
            self.pikk(3)
        elif 0.035<self.last_touch.spos[0]<0.125 and 0.17<self.last_touch.spos[1]<0.27 :
            self.pikk(4)
        elif 0.26<self.last_touch.spos[0]<0.35 and 0.17<self.last_touch.spos[1]<0.27 :
            self.pikk(2)
        elif 0.46<self.last_touch.spos[0]<0.55 and 0.17<self.last_touch.spos[1]<0.27 :
            self.pikk(7)
        elif 0.69<self.last_touch.spos[0]<0.78 and 0.17<self.last_touch.spos[1]<0.27 :
            self.pikk(9)
        elif 0.85<self.last_touch.spos[0]<1 and 0.17<self.last_touch.spos[1]<0.27 :
            self.pikk(6)

    
class welcome(Screen):
    def __init__(self, i, **kwargs):
        super(welcome, self).__init__(**kwargs)
        self.name='welcome'+str(i)
        self.ads = KivMob('ca-app-pub-7708734421318076~2678563608')
        self.ads.add_test_device("DC7FB264B3E07750BCCFC5EAA779E24E")
        self.ads.new_banner('ca-app-pub-7708734421318076/7320424307', top_pos=True)
        self.ads.request_banner()
        self.ads.show_banner()
        self.i=i
        self.add_widget(CoverImage(source="cover.jpeg"))
        self.gd=FloatLayout()
        self.add_widget(self.gd)
        self.gd.add_widget(Button(text="Play", on_press=self.gopickNum, opacity=0.6, pos_hint={'x':0.45,'y':0.55},size_hint=(0.1,0.1)))
        self.gd.add_widget(Button(text="Difficulty", on_press=self.difficulty, opacity=0.6, pos_hint={'x':0.45,'y':0.35},size_hint=(0.1,0.1)))
        self.gd.add_widget(Button(text="About", on_press=self.abt, opacity=0.6, pos_hint={'x':0.45,'y':0.15},size_hint=(0.1,0.1)))
    def gopickNum(self,instance):
        self.parent.add_widget(pickNum(self.i))
        self.manager.current='pickNum'+str(self.i)
        self.clear_widgets()
    #def _update_rect(self, instance, value):
        #self.rect.pos = instance.pos
        #self.img.size = instance.size

    def abt(self,instance):
        self.parent.add_widget(about())
        self.manager.current='about'
    def difficulty(self,instance):
        self.parent.add_widget(difficulty())
        self.manager.current='difficulty'

class about(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name='about'
        self.gd=GridLayout(cols=1)
        self.add_widget(self.gd)
        self.lbl=CovAbt()
        self.gd.add_widget(self.lbl)
        file=open('count.txt', 'r')
        self.i=int(file.read())
        file.close()
    def on_touch_down(self,touch):
        self.manager.current='welcome'+str(self.i)
class difficulty(ButtonBehavior,Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.name='difficulty'
        self.gd=GridLayout(cols=1)
        self.add_widget(self.gd)
        file=open('difficulty.txt', 'r')
        difficulty=file.read()
        file.close()

        self.gd.add_widget(Button(text="Easy", on_press=self.easy, opacity=1, pos_hint={'x':0.5,'y':0.5},size_hint=(0.01,0.1)))
        self.gd.add_widget(Button(text="Medium", on_press=self.medium, opacity=1, pos_hint={'x':0.5,'y':0.3},size_hint=(0.01,0.1)))
        self.gd.add_widget(Button(text="Hard", on_press=self.hard, opacity=1, pos_hint={'x':0.5,'y':0.1},size_hint=(0.01,0.1)))
    

        self.lbl=Label(text='Current Difficulty : '+difficulty+'\n\nExit')
        self.gd.add_widget(self.lbl)
        file=open('count.txt', 'r')
        self.i=int(file.read())
        file.close()
    def easy(self,touch):
        diff=open('difficulty.txt', 'w')
        diff.write('Easy')
        diff.close()        
        diff=open('difficulty.txt', 'r')
        present=diff.read()
        diff.close()
        self.lbl.text='Current Difficulty : '+present+'\n\nExit'
    def medium(self, instance):
        diff=open('difficulty.txt', 'w')
        diff.write('Medium')
        diff.close()        
        diff=open('difficulty.txt', 'r')
        present=diff.read()
        diff.close()
        self.lbl.text='Current Difficulty : '+present+'\n\nExit'
    def hard(self,instance):
        diff=open('difficulty.txt', 'w')
        diff.write('Hard')
        diff.close()        
        diff=open('difficulty.txt', 'r')
        present=diff.read()
        diff.close()
        self.lbl.text='Current Difficulty : '+present+'\n\nExit'
    def on_press(self):
        touch=self.last_touch.spos
        #print(touch)
        if 0.3<touch[0]<0.45 and 0.3<touch[1]<0.4:
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
        self.icon='icon.png'
  
        return root
        
if __name__ =="__main__":
    Kivy().run()
