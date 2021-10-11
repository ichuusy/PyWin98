import pygame,time,os
from pygame.draw import rect
from pygame.locals import *
from datetime import datetime
from pygame import mixer

mixer.init()
pygame.init()
mixer.music.set_volume(1)
if __name__ == "__main__":
    print("Welcome to the Win98 Simulator.\nDiscord : https://discord.gg/BzJRTe2gap\nProject Author : ichuusy#5823\nIf any idea for this project, come to discord server and write your idea.\nProject 0.1 Beta, Project every day updating by ichuusy.")
else:
    os.run = False
    print("Error : Win98Sim don't working on another code.")

class OSCMD():
    def __init__(self):
        self.run = True
        self.file = __file__[0:len(__file__)-len(os.path.basename(__file__))]
        self.screen = pygame.display.set_mode((1800,1000))
        self.Objects()
        pygame.display.set_icon(self.start)
        pygame.display.set_caption("Windows98")
        self.secret = []
        self.rects = [50,80,35,35]
        self.cube = pygame.Rect(50,50,50,50)
        self.user = [20,20,30,50]
        self.mouse = pygame.Rect(self.user)
        self.Settings()
        for i in range(0,8):
            self.secret.append(pygame.Rect(self.rects))
            self.rects[1] += 90
        
    def Objects(self):
        self.internet = pygame.image.load(self.file+"Images/internet.png")
        self.winamp = pygame.image.load(self.file+"Images/winamp.jpg")
        self.start = pygame.image.load(self.file+"Images/win95.png")
        self.sound = pygame.image.load(self.file+"Images/sound.png")
        self.recycle = pygame.image.load(self.file+"Images/recyclebin.png")
        self.computer = pygame.image.load(self.file+"Images/computer.png")
        self.notepad = pygame.image.load(self.file+"Images/notepad.png")
        self.msdos = pygame.image.load(self.file+"Images/ms-dos.png")
        self.explorer = pygame.image.load(self.file+"Images/internetexplorer.png")
        self.player = pygame.image.load(self.file+"Images/player.png")
        self.msn = pygame.image.load(self.file+"Images/msn.png")
        self.musicplayer = pygame.image.load(self.file+"Images/winamplogo.png")
        self.lol = pygame.image.load(self.file+"Images/lol.png")
        self.javascript = pygame.image.load(self.file+"Images/javascript.png")
        self.internet = pygame.transform.scale(self.internet,(1200,850))
        self.winamp = pygame.transform.scale(self.winamp,(500,800))
        self.start = pygame.transform.scale(self.start,(25,25))
        self.sound = pygame.transform.scale(self.sound,(20,20))
        self.recycle = pygame.transform.scale(self.recycle,(80,50))
        self.computer = pygame.transform.scale(self.computer,(50,50))
        self.notepad = pygame.transform.scale(self.notepad,(90,50))
        self.msdos = pygame.transform.scale(self.msdos,(50,50))
        self.explorer = pygame.transform.scale(self.explorer,(50,60))
        self.player = pygame.transform.scale(self.player,(50,50))
        self.msn = pygame.transform.scale(self.msn,(55,55))
        self.musicplayer = pygame.transform.scale(self.musicplayer,(55,55))
        self.lol = pygame.transform.scale(self.lol,(70,70))
        self.javascript = pygame.transform.scale(self.javascript,(70,70))
        self.wallerr = 0
        try:
            self.wallpaper = pygame.image.load(self.file+"Images/wallpaper.jpg")
            self.wallpaper = pygame.transform.scale(self.wallpaper,(1800,1000))
        except:
            self.wallerr = 1
    def Settings(self):
        self.ultrafont = pygame.font.SysFont("Arial",50)
        self.bigfont = pygame.font.SysFont("Arial",24)
        self.font = pygame.font.SysFont("Arial",17)
        self.status,self.unicode,self.easteregg,self.window = "","","",""
        self.enter,self.err,self.timer,self.err,self.check  = 0,0,0,0,0
        self.process = None

    def ClickCheck(self,rect):
        for num,rects in enumerate(rect):
            if rects.colliderect(self.user):
                if event.type == MOUSEBUTTONUP and event.button == 1:
                    if num == 0:
                        self.process = 0
                    elif num == 1:
                        self.process = 1
                    elif num == 2:
                        self.process = 2
                    elif num == 3:
                        self.process = 3
                    elif num == 4:
                        self.process = 4
                    elif num == 5:
                        self.process = 5
                    elif num == 6:
                        self.process = 6
                    elif num == 7:
                        self.process = 7
                    self.status = "opening"
                    time.sleep(0.1)

    def Desktop(self):
        self.screen.blit(self.recycle,(self.secret[1].x-16,self.secret[1].y-30))
        self.screen.blit(self.computer,(self.secret[0].x,self.secret[0].y-30)) 
        self.screen.blit(self.notepad,(self.secret[2].x-23,self.secret[2].y-30))
        self.screen.blit(self.msdos,(self.secret[3].x,self.secret[3].y-30))
        self.screen.blit(self.explorer,(self.secret[4].x,self.secret[4].y-30))
        self.screen.blit(self.player,(self.secret[5].x,self.secret[5].y-30))
        self.screen.blit(self.musicplayer,(self.secret[6].x,self.secret[6].y-30))
        self.screen.blit(self.msn,(self.secret[7].x,self.secret[7].y-30))
        pygame.draw.rect(self.screen,("LightGray"),(0,960,1800,40))
        start = self.font.render(f"Start",True,(0,0,0))
        recycletext = self.font.render(f"Recycle Bin",True,(0,0,0))
        computertext = self.font.render(f"My Computer",True,(0,0,0))
        notepadtext = self.font.render(f"Notepad",True,(0,0,0))
        msdostext = self.font.render(f"MS-DOS",True,(0,0,0))
        explorertext = self.font.render(f"Internet Explorer",True,(0,0,0))
        videoplayertext = self.font.render(f"Media Player Classic",True,(0,0,0))
        musicplayertext = self.font.render(f"Winamp",True,(0,0,0))
        msntext = self.font.render(f"MSN",True,(0,0,0))
        pygame.draw.rect(self.screen,("gray"),(10,965,70,30))
        self.screen.blit(start,(40,970))
        self.screen.blit(computertext,(35,105))
        self.screen.blit(recycletext,(40,195))
        self.screen.blit(notepadtext,(45,285))
        self.screen.blit(msdostext,(45,375))
        self.screen.blit(explorertext,(25,470))
        self.screen.blit(videoplayertext,(15,560))
        self.screen.blit(musicplayertext,(50,650))
        self.screen.blit(msntext,(60,740))
        self.screen.blit(self.start,(13,968))
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        pygame.draw.rect(self.screen,("gray"),(1700,965,90,30))
        self.screen.blit(self.sound,(1705,970))
        time = self.font.render(f"{current_time}",True,(0,0,0))
        self.screen.blit(time,(1735,970))
    
        
        
    def EasterEgg(self,syntax):
        if "usage" == syntax[:5] or "usage" == syntax[126:131]:
            self.easteregg = "usage"
        if "pykatone" == syntax[:8] or "pykatone" == syntax[126:131]:
            self.easteregg = "pykatone"

    def Process(self,num):
        if num == 0 or num == 1 or num == 2 or num == 3 or num == 4 or num == 5 or num == 6 or num == 7:
            if self.status == "opening":
                self.timer += 1
                self.unicode = ""
                self.err = 0
                self.easteregg = ""
                self.enter = 0
                if self.timer <= 100:
                    self.status = "opened"
                    self.timer = 0
                    return pygame.draw.rect(self.screen,("black"),(300,80,1200,850))
            else:
                self.timer = 0
            self.timer += 1
            if self.window == "Rick Astley - Never Gonna Give You Up - Winamp":
                pygame.draw.rect(self.screen,(0,0,0),(600,50,500,30))
                pygame.draw.rect(self.screen,("red"),(1070,50,30,30))
                pygame.draw.rect(self.screen,("gray"),(1030,50,30,30))
                pygame.draw.rect(self.screen,("gray"),(990,50,30,30))
                cross = self.font.render(f"X",True,(255,255,255))
                minimalize = self.font.render(f"_",True,(255,255,255))
                fullscreen = self.font.render(f"[ ]",True,(255,255,255))
                win = self.font.render(f"{self.window}",True,(255,255,255))
                self.screen.blit(win,(610,55))
                self.screen.blit(cross,(1080,55))
                self.screen.blit(minimalize,(1000,50))
                self.screen.blit(fullscreen,(1040,53))
            else:
                pygame.draw.rect(self.screen,(0,0,0),(300,50,1200,30))
                pygame.draw.rect(self.screen,("red"),(1470,50,30,30))
                pygame.draw.rect(self.screen,("gray"),(1430,50,30,30))
                pygame.draw.rect(self.screen,("gray"),(1390,50,30,30))
                cross = self.font.render(f"X",True,(255,255,255))
                minimalize = self.font.render(f"_",True,(255,255,255))
                fullscreen = self.font.render(f"[ ]",True,(255,255,255))
                win = self.font.render(f"{os.window}",True,(255,255,255))
                self.screen.blit(win,(310,55))
                self.screen.blit(cross,(1480,55))
                self.screen.blit(minimalize,(1400,50))
                self.screen.blit(fullscreen,(1440,53))
            if num == 0:
                pygame.draw.rect(self.screen,("white"),(300,80,1200,850))
                soon = self.ultrafont.render("Coming Soon...",True,("gray"))
                self.screen.blit(soon,(740,425))
            elif num == 1:
                pygame.draw.rect(self.screen,("white"),(300,80,1200,850))
                self.screen.blit(self.lol,(345,110))
                self.screen.blit(self.javascript,(500,110))
                lol = self.font.render(f"League of Legends",True,(0,0,0))
                javascript = self.font.render(f"Javascript",True,(0,0,0))
                self.screen.blit(lol,(320,190))
                self.screen.blit(javascript,(502,190))
            elif num == 2:
                pygame.draw.rect(self.screen,("white"),(300,80,1200,850))
                word = self.font.render(f"{self.unicode[:145]}",True,(0,0,0))
                word1 = self.font.render(f"{self.unicode[145:290]}",True,(0,0,0))
                word2 = self.font.render(f"{self.unicode[290:435]}",True,(0,0,0))
                self.screen.blit(word,(310,90))
                self.screen.blit(word1,(310,110))
                self.screen.blit(word2,(310,130))
            elif num == 3:
                pygame.draw.rect(self.screen,("black"),(300,80,1200,850))
                pykatone_dos_1 = self.font.render(f"Microsoft(R) Windows 98",True,(255,255,255))
                pykatone_dos_2 = self.font.render(f"       (C)Copyright Microsoft Corp 1981-1999.",True,(255,255,255))
                pykatone_dos_3 = self.font.render(f"C:\>{self.unicode[:125]}",True,(255,255,255))
                if len(self.easteregg) != 0:
                    if self.easteregg == "usage":     
                        usage = "Windows98 System Usage : Ram : %60, CPU : %100 , GPU : %0 , Ethernet : %100"
                    elif self.easteregg == "pykatone":
                        usage = "Pykatone Discord : https://discord.gg/fsVutVh3sJ"
                    if self.easteregg == "usage" and self.enter == 1:
                        sum = 275 - len(self.unicode)
                        for add in range(0,sum+1):
                            self.unicode += " "
                        pykatone_dos_4 = self.font.render(usage,True,(255,255,255))
                    elif self.easteregg == "pykatone" and self.enter == 1:
                        sum = 275 - len(self.unicode)
                        for add in range(0,sum+1):
                            self.unicode += " "
                        pykatone_dos_4 = self.font.render(usage,True,(255,255,255))
                    else:
                        pykatone_dos_4 = self.font.render(f"C:\>{self.unicode[125:276]}",True,(255,255,255))
                    if self.easteregg == "usage" and self.enter == 2:
                        sum = 400 - len(self.unicode)
                        for add in range(0,sum+1):
                            self.unicode += " "
                        pykatone_dos_5 = self.font.render(usage,True,(255,255,255))
                    elif self.easteregg == "pykatone" and self.enter == 2:
                        sum = 400 - len(self.unicode)
                        for add in range(0,sum+1):
                            self.unicode += " "
                        pykatone_dos_5 = self.font.render(usage,True,(255,255,255))
                    else:
                        pykatone_dos_5 = self.font.render(f"C:\>{self.unicode[276:]}",True,(255,255,255))
                else:
                    pykatone_dos_4 = self.font.render(f"C:\>{self.unicode[125:276]}",True,(255,255,255))
                    pykatone_dos_5 = self.font.render(f"C:\>{self.unicode[276:]}",True,(255,255,255))
                error = os.font.render(f"Windows98 System Error : Ram usage very high.",True,("red"))
                self.screen.blit(pykatone_dos_1,(310,90))
                self.screen.blit(pykatone_dos_2,(310,110))
                self.screen.blit(pykatone_dos_3,(310,150))
                if len(self.unicode) > 125:
                    self.screen.blit(pykatone_dos_4,(310,170))
                if len(self.unicode) > 276:
                    self.screen.blit(pykatone_dos_5,(310,190))
                if len(self.unicode) >= 400:
                    self.screen.blit(error,(310,220))
                    self.err = 1
            elif num == 4:
                self.screen.blit(self.internet,(300,80))
            elif num == 5:
                pygame.draw.rect(self.screen,("white"),(300,80,1200,850))
                soon = self.ultrafont.render("Coming Soon...",True,("gray"))
                self.screen.blit(soon,(740,425))
            elif num == 6:
                self.screen.blit(self.winamp,(600,80))
                if self.check == 0:
                    self.check = 1
                    mixer.music.load(f"{self.file}Music/music.mp3")
                    mixer.music.play()
                elif not mixer.music.get_busy():
                    mixer.music.load(f"{self.file}Music/music.mp3")
                    mixer.music.play()
                    self.check = 0
            elif num == 7:
                pygame.draw.rect(self.screen,("white"),(300,80,1200,850))
                soon = os.ultrafont.render("Coming Soon...",True,("gray"))
                self.screen.blit(soon,(740,425))
            else:
                pygame.draw.rect(os.screen,(255,255,255),(300,80,1200,850))
            if num != 6:
                mixer.music.stop()
                self.check = 0
            if num == 0:
                self.window = "My Computer"
            elif num == 1:
                self.window = "Recycle Bin"
            elif num == 2:
                self.window = "Untitled - Notepad"
            elif num == 3:
                self.window = "MS-DOS"
            elif num == 4:
                self.window = "Microsoft Internet Explorer"
            elif num == 5:
                self.window = "Media Player Classic"
            elif num == 6:
                self.window = "Rick Astley - Never Gonna Give You Up - Winamp"
            elif num == 7:
                self.window = "Windows Live Messenger"
os = OSCMD()

while os.run:
    for event in pygame.event.get():
        if event.type == QUIT:
            os.run = False
        if event.type == pygame.KEYDOWN:
            if os.window == "MS-DOS" or os.window == "Untitled - Notepad":
                if os.err == 0:
                    if event.key == pygame.K_BACKSPACE:
                        os.unicode = os.unicode[:-1]
                    elif event.key == pygame.K_RETURN:
                        continue
                    else:      
                        os.unicode += event.unicode
        if event.type == pygame.KEYUP:
            if os.window == "MS-DOS" or os.window == "Untitled - Notepad":
                if os.err == 0:
                    if event.key == pygame.K_RETURN:
                        if os.enter == 0:
                            if os.window == "Untitled - Notepad":
                                sum = 145 - len(os.unicode)
                            else:
                                sum = 125 - len(os.unicode)
                            for add in range(0,sum+1):
                                os.unicode += " "
                        elif os.enter == 1:
                            if os.window == "Untitled - Notepad":
                                sum = 290 - len(os.unicode)
                            else:
                                sum = 276 - len(os.unicode)
                            for add in range(0,sum+1):
                                os.unicode += " "
                        elif os.enter == 2:
                            if os.window == "Untitled - Notepad":
                                sum = 435 - len(os.unicode)
                            else:
                                sum = 400 - len(os.unicode)
                            for add in range(0,sum+1):
                                os.unicode += " "
                        os.enter += 1
                        if os.window == "MS-DOS":
                            os.EasterEgg(os.unicode)
    if os.wallerr == 1:
        os.screen.fill((120,40,60))
    else:
        os.screen.blit(os.wallpaper,(0,0))
    mouse = pygame.mouse.get_pos()
    os.user[0] = mouse[0]-5
    os.user[1] = mouse[1]
    os.ClickCheck(os.secret)
    os.Process(os.process)
    os.Desktop()
    pygame.draw.rect(os.screen,(0,0,0),(os.user[0]+10,os.user[1]+10,5,5))
    pygame.display.flip()
