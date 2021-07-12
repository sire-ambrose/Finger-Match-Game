'''
from kivmob import KivMob, TestIds

from kivy.app import App
from kivy.uix.label import Label
help(TestIds.APP)
class BannerTest(App):
    """ Displays a banner ad at top of the screen.
    """

    def build(self):
        self.ads = KivMob(TestIds.APP)
        self.ads.new_banner(TestIds.BANNER, top_pos=True)
        self.ads.request_banner()
        self.ads.show_banner()
        return Label(text='Banner Ad Demo')
        #APP_ID = ca-app-pub-7708734421318076~2678563608
        #AD_UNIT_ID=ca-app-pub-7708734421318076/7320424307

if __name__ == "__main__":
    BannerTest().run()
'''
