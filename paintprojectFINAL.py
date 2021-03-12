
#PAINT PROGRAM
from pygame import *
from random import *
from math import *
from tkinter import *
root=Tk()
root.withdraw()
size=width,height=1200,830
screen=display.set_mode(size)
RED=(255,0,0)   
GREEN=(0,255,0)
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

#defining all rects
canvas=Rect(380,110,770,520)
undoRect=Rect(1090,645,60,60)
redoRect=Rect(1090,715,60,60)
saveRect=Rect(1015,645,60,60)
loadRect=Rect(1015,715,60,60)
colourPreview=Rect(45,50,70,220)
colourWheel=Rect(140,50,220,220)
pencilRect=Rect(45,295,70,70) 
eraserRect=Rect(140,295,70,70) 
brushRect=Rect(235,295,70,70)
sprayRect=Rect(45,390,70,70)
highlighterRect=Rect(140,390,70,70)
lineRect=Rect(235,390,70,70)
rectRect=Rect(45,485,70,70)
ellipseRect=Rect(140,485,70,70)
triangleRect=Rect(235,485,70,70)
fillRect=Rect(325,295,30,120)
unfillRect=Rect(325,435,30,120)
krabsRect=Rect(45,580,100,100)
spongeRect=Rect(150,580,100,100)
sandyRect=Rect(255,580,100,100)
plankRect=Rect(45,685,100,100)
squidRect=Rect(150,685,100,100)
patRect=Rect(255,685,100,100)
krustBGRect=Rect(380,640,174,100)
houseBGRect=Rect(564,640,133,100)
skyBGRect=Rect(707,640,150,100)
pauseRect=Rect(867,715,62,60)
playRect=Rect(942,715,62,60)

#load all images
wheelPic=image.load("images/Colourwheel.png")
pencilPic=image.load("images/Pencil.png")
eraserPic=image.load("images/eraser.png")
brushPic=image.load("images/paintbrush.png")
sprayPic=image.load("images/spray.png")
highlighterPic=image.load("images/highlighter.png")
backgroundPic=image.load("images/backgroundsponge.png")
krabsPic=image.load("images/krabs.png")
spongePic=image.load("images/spongebobpoint.png")
sandyPic=image.load("images/sandycheeks.png")
plankPic=image.load("images/plankton.png")
squidPic=image.load("images/squidward.png")
patPic=image.load("images/patrick.png")
undoPic=image.load("images/undo.png")
redoPic=image.load("images/redo.png")
savePic=image.load("images/save.png")
loadPic=image.load("images/load.png")
playPic=image.load("images/play.png")
pausePic=image.load("images/pause.png")
krustBGPic=image.load("images/krusty.png")
houseBGPic=image.load("images/backgrounds.png")
skyBGPic=image.load("images/sky.png")
krustBGBig=image.load("images/krustycrop.png")
houseBGBig=image.load("images/backgroundscrop.png")
skyBGBig=image.load("images/skycrop.png")

#resize pictures
wheelPic1=transform.scale(wheelPic,(220,220)) #resizes each image to fit wanted spot
pencilPic1=transform.scale(pencilPic,(60,60))
eraserPic1=transform.scale(eraserPic,(60,60))
brushPic1=transform.scale(brushPic,(60,60))
sprayPic1=transform.scale(sprayPic,(60,60))
highlighterPic1=transform.scale(highlighterPic,(60,60))
krabsPic1=transform.scale(krabsPic,(84,90))
spongePic1=transform.scale(spongePic,(90,80))
sandyPic1=transform.scale(sandyPic,(64,90))
plankPic1=transform.scale(plankPic,(67,90))
squidPic1=transform.scale(squidPic,(42,90))
patPic1=transform.scale(patPic,(65,90))
krabsPic2=transform.scale(krabsPic,(137,145))
spongePic2=transform.scale(spongePic,(140,124))
sandyPic2=transform.scale(sandyPic,(103,145))
plankPic2=transform.scale(plankPic,(96,130))
squidPic2=transform.scale(squidPic,(70,150))
patPic2=transform.scale(patPic,(108,150))
undoPic1=transform.scale(undoPic,(50,50))
redoPic1=transform.scale(redoPic,(50,50))
savePic1=transform.scale(savePic,(50,50))
loadPic1=transform.scale(loadPic,(50,50))
krustBGPic1=transform.scale(krustBGPic,(174,100))
houseBGPic1=transform.scale(houseBGPic,(133,100))
skyBGPic1=transform.scale(skyBGPic,(150,100))

#blit all main images
screen.blit(backgroundPic,(0,0)) #blits main images first
screen.blit(wheelPic1,(140,50))

#drawing canvas
draw.rect(screen,WHITE,canvas)

#text/title
font.init() #initiates font system
comicFont=font.SysFont("Berlin Sans FB",24)
comicFont2=font.SysFont("Berlin Sans FB",15)
comicFont3=font.SysFont("Berlin Sans FB",48)
txtPic=comicFont.render(("WELCOME TO SPONGEBOB PAINT!"),True,(30,90,100))
draw.rect(screen,(221, 163, 189, 255),(380,50,770,50))
screen.blit(txtPic,(580,62)) #prints specific text on specified area
Title=comicFont3.render(("SPONGEBOB PAINT!"),True,(RED))
screen.blit(Title,(400,750)) #title at bottom 

#lists
tools=[pencilRect,eraserRect,brushRect,sprayRect,highlighterRect,rectRect,ellipseRect,undoRect,redoRect,triangleRect,fillRect,unfillRect,loadRect,saveRect,krabsRect,spongeRect
       ,sandyRect,plankRect,squidRect,patRect,lineRect,krustBGRect,houseBGRect,skyBGRect,pauseRect,playRect]
toolExplain=["PENCIL; allows the user to draw lines that follow the mouse","ERASER; use the mouse to erase work that was done","BRUSH; use the mouse to paint",
             "SPRAY PAINT; use mouse to spray paint","HIGHLIGHTER; use mouse to highlight","RECT TOOL; use the mouse to draw rectangles, both filled and unfilled",
            "ELLIPSE TOOL; use the mouse to draw ovals, both filled and unfilled","UNDO; reverse the action of an earlier action","REDO; reverse your last Undo",
             "POLYGON TOOL; use the mouse to draw polygons","FILLED SHAPES; draw filled shapes","UNFILLED SHAPES; draw unfilled shapes",
             "LOAD; load the canvas from a bitmap file","SAVE; save canvas to a bitmap file","STAMP; press/drag on canvas to apply stamp","STAMP; press/drag on canvas to apply stamp",
             "STAMP; press/drag on canvas to apply stamp","STAMP; press/drag on canvas to apply stamp","STAMP; press/drag on canvas to apply stamp",
             "STAMP; press/drag on canvas to apply stamp","LINE TOOL; use the mouse to draw lines","BACKGROUND; applies selected background",
             "BACKGROUND; applies selected background","BACKGROUND; applies selected background","PAUSE; pause music playback","PLAY; play music"]
#a related list between tools and toolExplain allows me to ensure that whenever a tool is chosen, an adequate explanation is provided
music=["music/regetta.ogg","music/gator.ogg","music/hilo-rag.ogg",
      "music/seaweed.ogg","music/tripping-upstairs.ogg"]
#an ogg file is used as mp3 malfunctioned
#a playlist of songs

#load music
mixer.init() #initiates music mixer
shuffle(music) #shuffles the playlist to change songs
for x in music: #x represents each song in the list
    mixer.music.load(x) #loads all the songs in the playlist 
    mixer.music.play(-1)#plays forever

#variables
col=(BLACK) #represents the colour of all tools in the beginning 
boxColour=BLACK #represents of the colours of the tools that aren't hovered over or clicked
scroll=1 #represents the thickness in the beginning
omx=0 #a value to avoid program from crashing
omy=0
r,g,b,a=0,0,0,10 #represents the transparency
copy=screen.subsurface(canvas).copy() #screenshots only the canvas
undo=[copy] #places the clear screenshot in each list
redo=[copy]
tool="no tool" #represents that there is no tool in the beginning
filled=False #represents the fact that in the beginning the tools are unfilled until changed
adjustH=0 #beginning value for the pictures that will be edited to fit
adjustW=0
krustBG=False #tells eraser what kind of background will be used
skyBG=False
houseBG=False
Red=False #represents that tools arent red in the beginning
mb=0 #start values
mx,my=0,0

running=True
while running:
    for evt in event.get():
        if evt.type==QUIT:
            running=False
        mb=mouse.get_pressed()
        mx,my=mouse.get_pos()
                
        if evt.type==MOUSEBUTTONDOWN:
            sx,sy=mouse.get_pos() #gets old positions when pressed
            screenCap=screen.copy() #screenshots
            if evt.button==4: #changes thickness when scroll is used
                scroll=scroll+1  #up makes it go higher          
            if evt.button==5:
                scroll-=1 #down make it go lower
                                          
        if scroll<1: #sets a limit to the scroll
            scroll=1
        if scroll>50:
            scroll=50
                
        if evt.type==MOUSEBUTTONUP:
            if canvas.collidepoint(mx,my):
                capture=screen.subsurface(canvas).copy() #screenshots canvas whenever you let go of the mouse clicker
                undo.append(capture) #add the screenshot to end of the undo list
                
        if undoRect.collidepoint(mx,my) and mb[0]==1: #if undo is clicked on
            try: 
                redo.append(undo[-1]) #the screenshot goes to the redo list
                undo.pop() #the screenshot is removed from the undo file
                screen.blit(undo[-1],(380,110)) #blits screenshot

            except:
                pass #prevents program from crashing due to some errors
            
        if redoRect.collidepoint(mx,my) and mb[0]==1: # if redo is clicked on
            try:
                undo.append(redo[-1]) #screenshot that was originally in undo is sent back
                redo.pop() #screenshot is removed from undo
                screen.blit(redo[-1],(380,110)) #screenshot is blitted

            except:
                pass #avoids crashing
                      
    #drawing all rects
    for x in tools: #loop draws every rectangle in tools list
        draw.rect(screen,WHITE,x)
    draw.rect(screen,col,colourPreview) #colour preview rect is drawn seperately 
    draw.rect(screen,BLACK,(333,303,13,103))
    draw.rect(screen,BLACK,(333,443,13,103),1)
    draw.rect(screen,BLACK,(55,495,50,50),3)
    draw.rect(screen,(255, 230, 230),(867,645,135,60))
    draw.rect(screen,(255, 230, 230),(867,645,135,60))

    #drawing extra shapes
    draw.ellipse(screen,BLACK,(150,495,50,50),3) #shapes to preview tools
    draw.polygon(screen,BLACK,[(245,545) ,(295,545),(270,495)],3)
    draw.line(screen,BLACK,(245,400),(295,450),3)  
    
    #text
    txtSize=comicFont.render((("SIZE")),True,(30,90,100)) #these texts require to be in the loops due to the fact that they are constantly changing
    screen.blit(txtSize,(893,649)) #blits text
    SizePic=comicFont.render(str(scroll),True,(30,90,100))
    screen.blit(SizePic,(950,649))
    txtCol=comicFont2.render((("COLOUR")),True,(col))
    screen.blit(txtCol,(903,672))
    ColPic=comicFont2.render(str(col),True,(col))
    screen.blit(ColPic,(880,683))    
 
    #blit all images
    screen.blit(pencilPic1,(50,300)) #every image is blitted to a specific position
    screen.blit(eraserPic1,(145,300))
    screen.blit(brushPic1,(240,300))
    screen.blit(sprayPic1,(48,395))
    screen.blit(highlighterPic1,(144,394))
    screen.blit(savePic1,(1020,650))
    screen.blit(loadPic1,(1020,720))
    screen.blit(undoPic1,(1095,650))
    screen.blit(redoPic1,(1095,720))
    screen.blit(krabsPic1,(50,585))
    screen.blit(spongePic1,(152,590))
    screen.blit(sandyPic1,(265,585))
    screen.blit(plankPic1 ,(53,687))
    screen.blit(squidPic1,(170,688))
    screen.blit(patPic1,(270,689))
    screen.blit(krustBGPic1,(380,640))
    screen.blit(houseBGPic1,(564,640))
    screen.blit(skyBGPic1,(707,640))
    screen.blit(playPic,(945,715))
    screen.blit(pausePic,(870,715))
                            
    #highlighting the box
    for x in tools: #goes through every tool in the list to check
        draw.rect(screen,boxColour,x,3) #first draw a black outline
        if x.collidepoint(mx,my) and mb[0]==0: #checks if the mouse is hovering over a tool
            draw.rect(screen,RED,x,3) # if it is then the tool turns red while the mouse is still there
        if x.collidepoint(mx,my) and mb[0]==1: #checks if the mouse has clicked
            pos=tools.index(x)# finds the position of the tool in the list
            Red=True #makes red true 
        if Red==True:
            draw.rect(screen,RED,tools[pos],3) #changes the colour of the outline
            
    #explaining the tools
    if mb[0]==1:        
        for x in tools: #goes through list of tools
          if x.collidepoint(mx,my) and mb[0]==1: 
            ind=tools.index(x)#finds the position of the tools clicked on
            txtPic=comicFont.render((toolExplain[ind]),True,RED) #displays the instructions through a related list
            draw.rect(screen,WHITE,(380,50,770,50)) #draws a rectangle to clear previous instructions
            screen.blit(txtPic,(390,60)) #blits text

    #selecting the tools
    if mb[0]==1:  #checks which tool is selected       
        if pencilRect.collidepoint(mx,my):
            tool="pencil"        
        elif eraserRect.collidepoint(mx,my):
            tool="eraser"
        elif brushRect.collidepoint(mx,my):
            tool="brush"
        elif sprayRect.collidepoint(mx,my):
            tool="spray"
        elif highlighterRect.collidepoint(mx,my):
            tool="highlighter"
        elif rectRect.collidepoint(mx,my):
            tool="rect"
        elif ellipseRect.collidepoint(mx,my):
            tool="ellipse"
        elif triangleRect.collidepoint(mx,my):
            tool="triangle"
        elif fillRect.collidepoint(mx,my):
            filled=True
        elif unfillRect.collidepoint(mx,my):
            filled=False
        elif lineRect.collidepoint(mx,my):
            tool="line"
        elif saveRect.collidepoint(mx,my):
            tool="save"
        elif loadRect.collidepoint(mx,my):
            tool="load"
        elif krabsRect.collidepoint(mx,my):
            tool="krab"
        elif spongeRect.collidepoint(mx,my):
            tool="sponge"
        elif sandyRect.collidepoint(mx,my):
            tool="sandy"
        elif plankRect.collidepoint(mx,my):
            tool="plank"
        elif squidRect.collidepoint(mx,my):
            tool="squid"
        elif patRect.collidepoint(mx,my):
            tool="pat"
        elif krustBGRect.collidepoint(mx,my):
            tool="krustBG"
        elif houseBGRect.collidepoint(mx,my):
            tool="houseBG"
        elif skyBGRect.collidepoint(mx,my):
            tool="skyBG"
        elif pauseRect.collidepoint(mx,my):
            tool="pause"
        elif playRect.collidepoint(mx,my):
            tool="play"
        elif undoRect.collidepoint(mx,my):
            tool="undo"
        elif redoRect.collidepoint(mx,my):
            tool="redo"    

    #using the tools
    if mb[0]==1:
        if canvas.collidepoint(mx,my):
            screen.set_clip(canvas)#only the canvas can be updated
            
            if tool=="pencil":
                if scroll>5: #sets the thickness limit to 5
                    scroll=5
                draw.line(screen,col,(omx,omy),(mx,my),scroll) #draws a line between the current mouse position and the previous one
            
            if tool=="eraser":
                try:
                    if krustBG==True: #checks the background
                    
                        sample=krustBGBig.subsurface(mx-380-scroll//2,my-110-scroll//2,scroll,scroll)# creates an eraser that doesnt erase the background
                        #this is done by creating small parts of the original picture and ensuring that the thickness of the mouse
                        #doesnt interfere with the position of the erase marks and so the thickness is divided by two 
                        screen.blit(sample,(mx-scroll//2,my-scroll//2)) #blits subsurface to area pressed on

                    elif skyBG==True:
                    
                        sample=skyBGBig.subsurface(mx-380-scroll//2,my-110-scroll//2,scroll,scroll)
                        screen.blit(sample,(mx-scroll//2,my-scroll//2))
                    elif houseBG==True:
                    
                        sample=houseBGBig.subsurface(mx-380-scroll//2,my-110-scroll//2,scroll,scroll)
                        screen.blit(sample,(mx-scroll//2,my-scroll//2))
                    else:#eraser for a normal white background
                        dx=mx-omx #horizontal distance=run
                        dy=my-omy #vertical distance=rise
                        dist=int(sqrt(dx**2+dy**2))#finds distance between old mouse position and new mouse position
                        for i in range (1,dist+1,1): #draws a circle each pixel to cover full area
                            dotX=int(omx+i*dx/dist) #finds position of each dot
                            dotY=int(omy+i*dy/dist)
                            draw.circle(screen,WHITE,(dotX,dotY),scroll) #draws each dot through the loop
                except:
                    pass
                
            if tool=="brush":
                dx=mx-omx #horizontal distance=run
                dy=my-omy #vertical distance=rise
                dist=int(sqrt(dx**2+dy**2))#finds distance between old mouse position and new mouse position
                for i in range (1,dist+1,1):#draws a circle each pixel to cover full area
                    dotX=int(omx+i*dx/dist)#finds position of each dot
                    dotY=int(omy+i*dy/dist)
                    draw.circle(screen,col,(dotX,dotY),scroll) #draws each dot through the loop              

            if tool=="spray":
                for x in range (10): #loop keeps on filling the area pressed
                    randX=randint(mx-scroll,mx+scroll) #provides an x coordinate for the random dots that appear
                    randY=randint(my-scroll,my+scroll) #provides a y coordinate for the random dots that appear
                    dx=abs(sqrt((randX-mx)**2+(randY-my)**2)) #checks for the distance of each dot
                    if dx<scroll: #ensures that the dots drawn are within the radius 
                        draw.line(screen,col,(randX,randY),(randX,randY),1) #draws the dot if all standards are met

            if tool=="highlighter":
                marker=Surface((scroll*2,scroll*2),SRCALPHA) #create a surface for the transparent highlighter with an area of your thickness
                draw.circle(marker,(r,g,b,10),(scroll,scroll),scroll) #draw with the highlighter on top of the surface created
                dx=mx-omx #horizontal distance=run
                dy=my-omy #vertical distance=rise
                dist=int(sqrt(dx**2+dy**2)) # find the distance 
                for i in range (1,dist+1,1): #cover the area drawn over
                    dotX=int(omx+i*dx/dist) #find position of each dot
                    dotY=int(omy+i*dy/dist)
                
                    screen.blit(marker,(dotX,dotY))#blit the surface created
                                        
            if filled==False:
                if tool=="rect":
                    if scroll%2==0: #works only with odd thicknesses due to division
                        scroll=scroll-1 #changes even thicknesses to odd
                    screen.blit(screenCap,(0,0)) #screenshot to avoid seeing unwanted shapes
                    h=my-sy #measures total height
                    w=mx-sx #measures total width

                    draw.line(screen,col,(sx,sy-scroll//2),(sx,my+scroll//2),scroll) #adding/subtracting half the scroll makes up for the missing edges 
                    draw.line(screen,col,(mx,sy-scroll//2),(mx,my+scroll//2),scroll) #doing it for each side makes all the edges even
                    draw.line(screen,col,(sx-scroll//2,sy),(mx+scroll//2,sy),scroll)
                    draw.line(screen,col,(sx-scroll//2,my),(mx+scroll//2,my),scroll)
                    if h<0 and w<0: #if the rectangle has negative dimensions, this normalizes the edges
                        draw.line(screen,col,(sx,sy+scroll//2),(sx,my-scroll//2),scroll) #by switching operations, you ensure that the excess areas are in the right sides
                        draw.line(screen,col,(mx,sy+scroll//2),(mx,my-scroll//2),scroll)
                        draw.line(screen,col,(sx+scroll//2,sy),(mx-scroll//2,sy),scroll)
                        draw.line(screen,col,(sx+scroll//2,my),(mx-scroll//2,my),scroll) 

                if tool=="ellipse":
                    ellipse2Rect=Rect(sx,sy,(mx-sx),(my-sy))#creates a rect that has all the dimensions wanted by the user as an ellipse is similar to a rect
                    screen.blit(screenCap,(0,0)) #ensures there are no infinite copies of it as you move the mouse
                    ellipse2Rect.normalize() #makes the dimension proper so it can get drawn
                    try:
                        for x in range(4):
                            draw.ellipse(screen,col,ellipse2Rect,scroll)#draws more than one in an attempt to cover holes

                    except:
                        pass
                    
                if tool=="triangle":
                    screen.blit(screenCap,(0,0))
                    draw.polygon(screen,col,[(sx,sy),(mx,sy),((mx+sx)//2,my)],scroll) # finds the three points based on the mouse positions
                    
            if filled==True: #makes all the shapes filled
                if tool=="triangle":
                    screen.blit(screenCap,(0,0))#ensures there are no infinite copies of it as you move the mouse
                    draw.polygon(screen,col,[(sx,sy),(mx,sy),((mx+sx)//2,my)])# finds the three points based on the mouse positions
                if tool=="ellipse":
                    ellipse2Rect=Rect(sx,sy,(mx-sx),(my-sy))
                    screen.blit(screenCap,(0,0))
                    ellipse2Rect.normalize()
                    try:
                        for x in range(10):
                            draw.ellipse(screen,col,ellipse2Rect)
                    except:
                        pass
                if tool=="rect": #filled rects have perfect corners so only the mouse positions are used
                    rect2Rect=Rect(sx,sy,(mx-sx),(my-sy))
                    screen.blit(screenCap,(0,0))
                    rect2Rect.normalize()
                    draw.rect(screen,col,rect2Rect)
            if tool=="line":
                screen.blit(screenCap,(0,0))
                draw.line(screen,col,(sx,sy),(mx,my),scroll)                        
            if tool=="krab":
                screen.blit(screenCap,(0,0))
                screen.blit(krabsPic2,(mx-50,my-100))
            if tool=="sponge":
                screen.blit(screenCap,(0,0))
                screen.blit(spongePic2,(mx-50,my-150))
            if tool=="sandy":
                screen.blit(screenCap,(0,0))
                screen.blit(sandyPic2,(mx-50,my-100))
            if tool=="plank":
                screen.blit(screenCap,(0,0))
                screen.blit(plankPic2,(mx-50,my-100))
            if tool=="squid":
                screen.blit(screenCap,(0,0))
                screen.blit(squidPic2,(mx-50,my-100))
            if tool=="pat":
                screen.blit(screenCap,(0,0))
                screen.blit(patPic2,(mx-50,my-100))
        if tool=="pause":
            mixer.music.pause()
        if tool=="play":
            mixer.music.unpause()
          
        if tool=="save":
            try:
                fname=filedialog.asksaveasfilename(defaultextension=".png")
                image.save(screen.subsurface(canvasRect),fname)
            except:
                pass

        if tool=="load":
          try:
            fname=filedialog.askopenfilename()
            loadingPic=image.load(fname)
            w=loadingPic.get_width()
            h=loadingPic.get_height()
            print(h,w)
            if w>770 and h>520:
              if w>h:
                adjustW=int(w*(670/w))
                adjustH=int(h*(670/w))
                 
              elif h>w:
                adjustW=int(w*(420/h))
                adjustH=int(h*(420/h))
              else:
                adjustW=int(w*(670/w))
                adjustH=int(h*(670/w))
   
            elif w>=770 and h<=520:
              adjustW=int(w*(670/w))
              adjustH=int(h*(670/w))
                
            elif h>=520 and w<=770:
              adjustW=int(w*(420/h))
              adjustH=int(h*(420/h))

            else:
              screen.blit(loadingPic,(380,110))

            loadingPic1=transform.scale(loadingPic,(adjustW,adjustH))
            screen.blit(loadingPic1,(380,110))
            print(adjustW,adjustH)
          except:
            pass
        
        if tool=="krustBG":
            krustBG=True #changes eraser to match each background
            skyBG=False
            houseBG=False
            screen.blit(krustBGBig,(canvas)) #blits image only on canvas
        if tool=="skyBG":
            skyBG=True
            krustBG=False
            houseBG=False
            screen.blit(skyBGBig,(canvas))
        if tool=="houseBG":
            skyBG=False
            krustBG=False
            houseBG=True
            screen.blit(houseBGBig,(canvas))  

        screen.set_clip(None) #everyhting can now change

    #changing the colour
    if colourWheel.collidepoint(mx,my): #chech whether the mouse is on the colour wheel
        if mb[0]==1:        
            col=screen.get_at((mx,my)) #gets colour of current mouse position
            r,g,b,a=screen.get_at((mx,my)) #introduces transparency
       
          

    omx=mx
    omy=my




    display.flip() 

quit()
