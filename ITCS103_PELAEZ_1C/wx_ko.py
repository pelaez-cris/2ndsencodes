import wx

class MyApp(wx.App):
    def OnInit(self):
        """WIDGETS"""
        frame = wx.Frame(None,title = "hello world", size=(2025 , 1075))
        panel = wx.Panel(frame)
        text = wx.StaticText(panel, label= "Welcome to wxPY!!", pos=(1000 , 500))
        frame.Show()
        return True
    
app = MyApp()
app.MainLoop()