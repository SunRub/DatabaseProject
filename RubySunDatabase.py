#Tianyue Ruby Sun
#Lists and Files Assignment
#December 2019

#Imports
from pygame import * #Imports pygame
import os #Imports os
os.environ['SDL_VIDEO_WINDOW_POS']="%d, %d" %(10,10) #Opens in same location

init() #Initializes pygame

#A What is happening to decide what happens
whatIsHappening=0 #This is a very important variable for the while True loop

#Sets colours
BACKGROUND=(135,206,235) #Background colour

#Box colours (they are the same colour but are separated for hovering purposes for different options)
BOXCOLOUR=(200,200,240) #Box colours for options
BOXCOLOUR1=(200,200,240) #Box colours for options
BOXCOLOUR2a=(200,200,240) #Box colours for options
BOXCOLOUR2b=(200,200,240) #Box colours for options
BOXCOLOUR3=(200,200,240) #Box colours for options
BOXCOLOUR4=(200,200,240) #Box colours for options
BOXCOLOUR5=(200,200,240) #Box colours for options
BOXCOLOUR6=(200,200,240) #Box colours for options

BOXCOLOURLIGHT=(215,215,254) #Lighter version of the colour of boxes for when the mouse hovers over it
BOXBORDERCOLOUR=(40,40,48) #Box border colour

EXITSIGNCOLOUR=(255,30,30) #Exit sign colour
EXITSIGNCOLOURLIGHT=(255,100,100) #Lighter version of exit sign colour

BACKSIGNCOLOUR=(255,30,30) #Back sign colour
BACKSIGNCOLOURLIGHT=(255,255,0) #A yellow colour for when the mouse hovers on a red colour

ACTIVECOLOUR=(255,255,0) #Colour for when a box is active
INACTIVECOLOUR=(51,51,255) #Colour for when the box is inactive

CHOICEBOX=(200,200,200) #Choice box colour
OKAY=(0,255,0) #Okay button colour
BLACK=(0,0,0) #Black

info=display.Info()
width=1000 #Sets the width
height=700 #Sets the height

SIZE=(width,height) #Sets SIZE to be the width,height (1000,700)
screen=display.set_mode(SIZE) #Sets screen to be the display with SIZE dimensions

#Setting Fonts
fontTNR100=font.SysFont("Times New Roman",100) #Times New Roman, Size 100
fontTNR30=font.SysFont("Times New Roman",30) #Times New Roman, Size 30
fontTNR25=font.SysFont("Times New Roman",25) #Times New Roman, Size 25
fontTNR20=font.SysFont("Times New Roman",20) #Times New Roman, Size 20
fontTNR10=font.SysFont("Times New Roman",10) #Times New Roman, Size 10

#Empty lists
idL=[] #Empty list for IDs
namesL=[] #Empty list for names
yearsL=[] #Empty list for years
genderL=[] #Empty list for genders
heightL=[] #Empty list for heights
weightL=[] #Empty list for weights
abilitiesL=[] #Empty list for abilities

#Setting Rectangles for collisions (on home screen)
optionExit=Rect(900,20,70,40) #Exit rectangle

optionPrintAllD=Rect(95,175,180,90) #The print all button
optionFindByID=Rect(375,175,250,40) #The find by ID button
optionNamesAndID=Rect(375,225,250,40) #The names and ID button
optionEditDetails=Rect(695,175,180,90) #The edit details button
optionAddHero=Rect(255,310,210,90) #The add hero button
optionDeleteHero=Rect(560,335,210,90) #The delete hero button
optionMeaningfulReports=Rect(385,465,250,90) #The meaningful reports button

#Buttons for back to home, choice, OK, and done
optionBackToHome=Rect(25,15,70,40) #Back to home screen button
optionChoiceBox=Rect(600,300,250,80) #Choice box (for searching ID)
optionOKChoice=Rect(770,430,80,40) #The OK button

#For fields in editing and adding a hero
optionIDEdit=Rect(150,190,350,40) #The ID field (cannot be edited but shows ID)
optionNameEdit=Rect(150,240,350,40) #Name field
optionYearEdit=Rect(150,290,350,40) #Year field
optionGenderEdit=Rect(150,340,350,40) #Gender field
optionHeightEdit=Rect(150,390,350,40) #Height field
optionWeightEdit=Rect(150,440,350,40) #Weight field
optionAbilitiesEdit=Rect(150,490,350,40) #Abilities field
optionSaveEdit=Rect(150,550,100,40) #Saving everything
optionCancelEdit=Rect(400,550,100,40) #Cancelling edits

#Page forwards, page backwards (back, next) buttons for new pages in the print all
optionBackChoice=Rect(35,600,70,40) #Back button
optionNextChoice=Rect(135,600,70,40) #Next button

#Mouse positions
mouse=[0,0] #Mouse coordinates
mx=0 #x coordinate for mouse
my=0 #y coordinate for mouse

superheroFile=open("RubySunData.dat", "r") #Opens the data file called RubySunData.dat

line=0 #Counter for each new line starting at 0

while True: #A while True loop
    text=superheroFile.readline() #Reads each line and saves it as text
    text=text.rstrip("\n") #Strips the new line
    if text=="End#~#": #If the text is "End#~#"
        break #Breaks out of loop
    if line%8==0: #Modular 8 for each feature (IDs)
        idL+=[int(text)] #Adds to list for the feature
    if line%8==1: #Modular 8 for each feature (name)
        namesL+=[text] #Adds to list for the feature
    if line%8==2: #Modular 8 for each feature (years)
        yearsL+=[int(text)] #Adds to list for the feature
    if line%8==3: #Modular 8 for each feature (genders)
        genderL+=[text] #Adds to list for the feature
    if line%8==4: #Modular 8 for each feature (heights)
        heightL+=[int(text)] #Adds to list for the feature
    if line%8==5: #Modular 8 for each feature (weights)
        weightL+=[int(text)] #Adds to list for the feature
    if line%8==6: #Modular 8 for each feature (abilities)
        abilitiesL+=[text] #Adds to list for the feature
    line+=1 #Adds 1 to line    
superheroFile.close() #Closes the file

def homeScreen(): #Homescreen function
    spiderman=image.load("Spider Man Webs.png") #Spiderman photo loaded
    
    draw.rect(screen,BACKGROUND,(0,0,1000,700)) #The blue background
    
    #Print all details box
    draw.rect(screen,BOXCOLOUR1,(95,175,180,90)) #Box colour 1 (Print all details)
    draw.rect(screen,BOXBORDERCOLOUR,(95,175,180,90),3) #Border around the box
    screen.blit(fontTNR30.render("Print all details",1,(BLACK)), Rect(98,200,180,90)) #Text in the box
    
    draw.rect(screen,BOXCOLOUR2a,(375,175,250,40)) #Box colour 2a (Find by ID)
    draw.rect(screen,BOXBORDERCOLOUR,(375,175,250,40),3) #Border around the box
    screen.blit(fontTNR30.render("Find by ID",1,(BLACK)), Rect(433,178,250,90)) #Text in the box
    
    draw.rect(screen,BOXCOLOUR2b,(375,225,250,40)) #Box colour 2b (Print names and ID)
    draw.rect(screen,BOXBORDERCOLOUR,(375,225,250,40),3) #Border around the box 
    screen.blit(fontTNR30.render("Print names and ID",1,(BLACK)), Rect(385,225,250,90)) #Text in the box 
    
    draw.rect(screen,BOXCOLOUR3,(695,175,180,90)) #Box colour 3 (Print names and ID)
    draw.rect(screen,BOXBORDERCOLOUR,(695,175,180,90),3) #Border around the box
    screen.blit(fontTNR30.render("Edit details",1,(BLACK)), Rect(715,200,180,90)) #Text in the box
    
    draw.rect(screen,BOXCOLOUR4,(255,310,210,90)) #Box colour 4 (Add new hero)
    draw.rect(screen,BOXBORDERCOLOUR,(255,310,210,90),3) #Border around the box
    screen.blit(fontTNR30.render("Add new hero",1,(BLACK)), Rect(275,335,210,90))  #Text in the box
    
    draw.rect(screen,BOXCOLOUR5,(535,310,210,90)) #Box colour 5 (Delete a hero)
    draw.rect(screen,BOXBORDERCOLOUR,(535,310,210,90),3) #Border around the box
    screen.blit(fontTNR30.render("Delete a hero",1,(BLACK)), Rect(560,335,210,90)) #Text in the box
    
    draw.rect(screen,BOXCOLOUR6,(375,440,250,90)) #Box colour 6 (Delete a hero)
    draw.rect(screen,BOXBORDERCOLOUR,(375,440,250,90),3) #Border around the box
    screen.blit(fontTNR30.render("Meaningful reports",1,(BLACK)), Rect(385,465,250,90)) #Text in the box 
    
    draw.rect(screen,EXITSIGNCOLOUR,(900,20,70,40)) #Exit sign at top right
    draw.rect(screen,BLACK,(900,20,70,40),2) #Border around the exit
    screen.blit(fontTNR25.render("EXIT",1,(BLACK)), Rect(908,25,70,40)) #Text "EXIT" in the box
    
    screen.blit(fontTNR100.render("Superheroes",1,(BLACK)), Rect(250,10,480,60)) #Superhero title at the top
    
    spiderman=transform.scale(spiderman,(160,160)) #Scales size of the spiderman photo
    sm=Rect(100,0,spiderman.get_width(), spiderman.get_height()) #Spiderman photo
    screen.blit(spiderman,sm) #Shows photo
    display.flip() #Displays everything
    

def printAll(): #Printing all details
    draw.rect(screen,BACKGROUND,(0,0,1000,700)) #Draws the background fullscreen
    screen.blit(fontTNR100.render(("All heroes and details"),1,(BLACK)),Rect(100,10,600,100)) #Title, all heroes and details
    line=0 #Starts line counter at 0
    screen.blit(fontTNR10.render(("(cm)         (lbs)"),1,(BLACK)),Rect(377,110,600,100)) #The cm and lbs units for indicating
    screen.blit(fontTNR25.render(("ID  Name                     Year  Gender  H    W  Abilities"),1,(BLACK)),Rect(10,115,600,100)) #Headers
    superheroFile=open("RubySunData.dat", "r") #Opens the data file called RubySunData.dat
    x=0 #For print all, x starts at 0
    EXITSIGNCOLOUR=(255,30,30) #Exit sign colour
    EXITSIGNCOLOURLIGHT=(255,100,100) #Lighter   
    draw.rect(screen,EXITSIGNCOLOUR,(25,15,70,40)) #Exit sign at top right
    draw.rect(screen,BLACK,(25,15,70,40),2) #Border around it
    screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40)) #Text on it 
    
    page=len(idL) // 10 #Gets number of pages based on number of objects in list idL (10/page)
    currentpage=0 #Sets current page to be 0
    done=False #Boolean done at false
    BACKSIGNCOLOUR=EXITSIGNCOLOUR #Back sign colour is equal to the colour of the exit sign
    BUTTONCOLOUR=CHOICEBOX #Button colour (back, next) is the same colour as 
    BUTTONCOLOURLIGHT=(225,225,225) #Lighter version of the button colour (light grey)
    
    while done==False: #While the program is not done
        for evnt in event.get(): #For events          
            if evnt.type==MOUSEMOTION: #If the event is moving the mouse
                if optionBackChoice.collidepoint(evnt.pos): #If it collides with the back button
                    BUTTONCOLOUR=BUTTONCOLOURLIGHT #Makes it light                                       
                elif optionNextChoice.collidepoint(evnt.pos): #If it collides with the next choice button
                    BUTTONCOLOUR=BUTTONCOLOURLIGHT #Makes both buttons light
                else:
                    BUTTONCOLOUR=CHOICEBOX #Back to the same colour
                if optionBackToHome.collidepoint(evnt.pos): #If it collides with back to home
                    BACKSIGNCOLOUR=BACKSIGNCOLOURLIGHT #Changes the colour
                else:
                    BACKSIGNCOLOUR=(255,30,30) #Back to its original
            if evnt.type==MOUSEBUTTONDOWN: #If the user clicks (mouse button is down)
                if optionBackChoice.collidepoint(evnt.pos) and currentpage>0: #Pages for back (previous page)
                    currentpage-=1 #Back one page
                if optionNextChoice.collidepoint(evnt.pos) and currentpage<page: #Pages for next (next page)
                    currentpage+=1 #Next page
                if optionBackToHome.collidepoint(evnt.pos)==True: #Back to home
                    return #Return
                
        draw.rect(screen,BACKSIGNCOLOUR,(25,15,70,40)) #Exit sign at top right
        draw.rect(screen,BLACK,(25,15,70,40),2) #Border around it
        screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40))  #Text in the button
        line=1 #Line begins at 1
        y=150 #y value (below headers)
        x=5 #x value starting at 5
        draw.rect(screen,BACKGROUND,(x,y,1050,600)) #Draws rectangle to cover up 
        if page>=1: #If the page is 1 or more (all pages)
            draw.rect(screen,BUTTONCOLOUR,(35,600,70,40)) #Back button
            screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(40,605,70,40)) #Text
            draw.rect(screen,BUTTONCOLOUR,(135,600,70,40)) #Next button
            screen.blit(fontTNR25.render("Next",1,(BLACK)), Rect(140,605,70,40)) #Text      
        for numberRecord in range(currentpage*10, min(currentpage*10+10,len(idL))): #10 for each page
            y=line*35+130 #y value increments
            x=5 #x is 5 for IDs
            screen.blit(fontTNR20.render(("%5i" %idL[numberRecord]),1,(BLACK)), Rect(x,y,15,15)) #Prints ID
            x=50 #x is 50 for names
            screen.blit(fontTNR20.render(("%s" %namesL[numberRecord]),1,(BLACK)), Rect(x,y,200,15)) #Prints name
            x=250 #x is 250 for years
            screen.blit(fontTNR20.render(("%5i" %yearsL[numberRecord]),1,(BLACK)), Rect(x,y,100,15)) #Prints year 
            x=330 #x 330 for genders
            screen.blit(fontTNR20.render(("%3s" %genderL[numberRecord]),1,(BLACK)), Rect(x,y,60,15)) #Prints gender
            x=400 #x is 400 for heights
            screen.blit(fontTNR20.render(("%7i" %heightL[numberRecord]),1,(BLACK)), Rect(x,y,100,15)) #Prints height
            x=500 #x is 500 for weights
            screen.blit(fontTNR20.render(("%7i" %weightL[numberRecord]),1,(BLACK)), Rect(x,y,100,15)) #Prints weight  
            x=600 #x is 600 for abilities
            screen.blit(fontTNR10.render(("%s"%abilitiesL[numberRecord]),1,(BLACK)), Rect(x,y,60,15)) #Prints abilities
            line+=1 #Adds 1 to line counter
        display.flip() #Displays everything    
    
def printIDandName(): #Function for printing ID and name (mostly same as function above, but this is only for ID and name (possibly the more important features))
    draw.rect(screen,BACKGROUND,(0,0,1000,700)) #Full screen background rectangle
    screen.blit(fontTNR100.render(("All IDs and Names"),1,(BLACK)),Rect(100,10,600,100)) #Title, all IDs and names  
    line=0 #Starts line counter at 0
    screen.blit(fontTNR25.render(("ID  Name"),1,(BLACK)),Rect(310,115,600,100)) #Headings, ID and name
    superheroFile=open("RubySunData.dat", "r") #Opens the data file called RubySunData.dat
    x=300 #Starting x value at 300
    y=80 #Starting y value at 80
    while True:
        text=superheroFile.readline() #Reads each line and saves it as text    
        text=text.rstrip("\n") #Strips the new line    
        if text=="End#~#": #If the text is "End#~#"
            break #Breaks out of loop   
        y=25*(int(line/8))+140   
        if line%8==0: #Modular 8 for each feature (ID)
            x=300 #If ID is to be printed, x=300
            screen.blit(fontTNR20.render(("%5i" %int(text)),1,(BLACK)), Rect(x,y,15,15)) #Prints the ID
        if line%8==1: #Modular 8 for each feature (name)
            x=350 #If name is to be printed, x=350
            screen.blit(fontTNR20.render((text),1,(BLACK)), Rect(x,y,200,15)) #Prints the name
        line+=1 #Adds 1 to line counter
    display.flip() #Displays
    superheroFile.close() #Closes the data 
    
def theHeroIWant(): #Function for the desired hero
    draw.rect(screen,BACKGROUND,(0,0,1000,700)) #Draws the background fullscreen
    screen.blit(fontTNR100.render(("Choose Your Hero"),1,(BLACK)),Rect(100,10,600,100)) #Prints "Choose Your Hero" as a title
    line=0 #Starts line counter at 0
    screen.blit(fontTNR25.render(("ID  Name"),1,(BLACK)),Rect(50,115,600,100)) #Headings for ID and name
    superheroFile=open("RubySunData.dat", "r") #Opens the data file called RubySunData.dat
    x=40 #Starting x value at 40
    y=80 #Starting y value at 80
    EXITSIGNCOLOUR=(255,30,30) #Exit sign colour
    EXITSIGNCOLOURLIGHT=(255,100,100) #Lighter version of the exit sign colour   
    draw.rect(screen,EXITSIGNCOLOUR,(25,15,70,40)) #Back sign (colour same as exit sign)
    draw.rect(screen,BLACK,(25,15,70,40),2) #Black border around it
    screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40)) #Puts text in the box "Back"
    screen.blit(fontTNR20.render("Enter your choice: ",1,(BLACK)), Rect(600,270,250,50)) #Prompts user to enter choice
    draw.rect(screen,CHOICEBOX,(600,300,250,80)) #Choice box
    draw.rect(screen,BLACK,(600,300,250,80),4) #Black border around it
    draw.rect(screen,OKAY,(770,430,80,40)) #Okay button (for proceeding)
    draw.rect(screen,BLACK,(770,430,80,40),3) #Black border around it
    screen.blit(fontTNR25.render("OK",1,(BLACK)), Rect(785,435,80,40)) #Prints the "OK" in the Okay button  
    while True: #Start of while True loop
        text=superheroFile.readline() #Reads each line and saves it as text
        text=text.rstrip("\n") #Strips the new line    
        if text=="End#~#": #If the text is "End#~#"
            break #Breaks out of loop   
        y=25*(int(line/8))+140 #y value is proportionate
        if line%8==0: #Modular 8 for each feature
            x=40 #Sets x=40
            screen.blit(fontTNR20.render(("%5i" %int(text)),1,(BLACK)), Rect(x,y,15,15)) #ID
        if line%8==1: #Modular 8 for each feature
            x=90 #Sets y=90
            screen.blit(fontTNR20.render((text),1,(BLACK)), Rect(x,y,200,15)) #Name
        line+=1 #Adds 1 to line counter
    display.flip() #Displays
    superheroFile.close() #Closes the file
    
def findByID(): #Function for finding by ID
    draw.rect(screen,BACKGROUND,(0,0,1000,700)) #The blue background
    screen.blit(fontTNR30.render(("Enter ID to search:"),1,(BLACK)),Rect(600,200,250,50)) #Prompts user to enter ID to search
    draw.rect(screen,EXITSIGNCOLOUR,(25,15,70,40)) #Exit sign at top right
    draw.rect(screen,BLACK,(25,15,70,40),2) #Black border around it
    screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40)) #Text "Back" inside
    draw.rect(screen,CHOICEBOX,(600,300,250,80)) #Choice box
    draw.rect(screen,BLACK,(600,300,250,80),4) #Black border around it
    draw.rect(screen,BLACK,(25,15,70,40),2) #Black border around the exit sign
    draw.rect(screen,OKAY,(770,430,80,40)) #Okay button
    draw.rect(screen,BLACK,(770,430,80,40),3) #Black border around it   
    screen.blit(fontTNR25.render("OK",1,(BLACK)), Rect(785,435,80,40)) #Ok in the box
    heroinfo="" #Hero info is blank (for now)
    active=False #Sets active to be False
    text="" #Text is empty
    heroID="" #Hero ID is empty
    intHeroID=-1 #Sets intHeroID=-1
    message="Enter ID to Search" #Prompts user to enter ID to search
    index=-1 #Sets index=-1
    heroinfo1="" #Empty hero info (name)
    heroinfo2="" #Empty hero info (year)
    heroinfo3="" #Empty hero info (gender)
    heroinfo4="" #Empty hero info (height)
    heroinfo5="" #Empty hero info (weight)
    heroinfo6="" #Empty hero info (abilities)
    BACKSIGNCOLOUR=(255,30,30) #Sets colour of the back sign
    OKCOLOUR=(OKAY) #Sets OK colour to be OKAY
    while True: #Start of a while True loop
        finished=False #Sets finished to be False
        for evnt in event.get(): #For events
            if evnt.type==MOUSEMOTION: #If the event is mouse motion (mouse moving)
                if optionBackToHome.collidepoint(evnt.pos): #If the mouse collides with back to home
                    BACKSIGNCOLOUR=BACKSIGNCOLOURLIGHT #Changes the colour
                else: #Else
                    BACKSIGNCOLOUR=(255,30,30) #Makes the back sign the original colour
                if optionOKChoice.collidepoint(evnt.pos): #If the mouse collides with the OK button
                    OKCOLOUR=BACKSIGNCOLOURLIGHT #Changes colour
                else: #Else
                    OKCOLOUR=(OKAY) #OK colour is OKAY
            if evnt.type==MOUSEBUTTONDOWN: #If the mouse is clicked 
                if optionBackToHome.collidepoint(evnt.pos): #If the mouse is clicked on back to home
                    heroID="" #Clears heroID
                    text="" #Clears text
                    intHeroID=-1 #Makes intHeroID -1
                    message="" #Empties message
                    finished=True #Finished becomes True
                    break #Breaks out of loop
                if optionChoiceBox.collidepoint(evnt.pos): #If the mouse is clicked on choice box
                    active=not active #Active becomes not active which is True
                else: #Else
                    active=False #Active is False
                if optionOKChoice.collidepoint(evnt.pos): #If the mouse is clicked on OK
                    if not heroID.isdigit(): #If the hero ID is not an integer
                        message="The ID must be an integer" #Prints the message telling the user so
                        heroID="" #Empties hero ID
                        text=""                                      
                    else: #ID is an integer
                        message="" #Empties message
                        intHeroID=int(heroID) #Sets intHeroID to be the integer of hero ID
                        index=0 #Index starts at 0
                        for idItem in idL: #For ID items in the list idL
                            if idItem==intHeroID: #If it is found in the list
                                break #Breaks out of loop
                            index+=1 #Adds 1 to index if not broken out
                        if index==len(idL): #If the index is the length of the list of IDs (meaning that it has reached the end and there has been nothing found)
                            message="ID does not exist" #Tells user the ID does not exist
                        else: #If ID is found
                            draw.rect(screen,BACKGROUND,(550,200,450,80)) #Draws a background to cover up parts of the screen
                            message="Found the hero!" #Gives message that hero was found
                            text="" #Text is emptied
                            heroinfo1="Name:         "+namesL[index] #Name of hero
                            heroinfo2="Year:         "+str(yearsL[index]) #Year of hero
                            heroinfo3="Gender:       "+genderL[index] #Gender of hero
                            heroinfo4="Height (cm):  "+str(heightL[index]) #Height of hero
                            heroinfo5="Weight (lbs): "+str(weightL[index]) #Weight of hero
                            heroinfo6="Abilities:    "+abilitiesL[index] #Abilities of hero
            if evnt.type==KEYDOWN: #If event is key down
                if active: #If active is true
                    if evnt.key==K_RETURN: #If the user presses return (enter)
                        text="" #Text is emptied
                    elif evnt.key==K_BACKSPACE: #Else, if the key is a backspace
                        text=text[:-1] #Erases the last character of the text
                        heroID=text #Sets heroID to be the text again
                    else: #Else
                        if len(text)<3: #If the length of the text is acceptable
                            text+=evnt.unicode #Adds the unicode of what is entered into text (unicode links key events to what they represent)
                            heroID=text #Updates heroID to equal to text            
        draw.rect(screen,OKCOLOUR,(770,600,80,40)) #Draws ok button
        draw.rect(screen,BLACK,(770,600,80,40),3) #Black border around it  
        screen.blit(fontTNR25.render("OK",1,(BLACK)), Rect(785,605,80,40)) #Puts "OK" in the box                     
        draw.rect(screen,BACKSIGNCOLOUR,(25,15,70,40)) #Back sign at top left
        draw.rect(screen,BLACK,(25,15,70,40),2) #Black border around it
        screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40)) #Puts "back" in the box
        colour=colourACTIVE if active else colourINACTIVE #If the box is active (user is entering stuff), sets the colour to be colourACTIVE, else it is inactive and colour is colourINACTIVE
        draw.rect(screen,BACKGROUND,(600,300,250,80)) #Draws a background coloured box to cover up
        textSurface=fontTNR20.render(text,True,colour) #Prints the text
        screen.blit(textSurface, (inputBox.x+5,inputBox.y+5)) #Puts textSurface where input box is
        draw.rect(screen,colour,inputBox,2) #Draws rectangle in colour (active or inactive based on what is happening)
        draw.rect(screen,BACKGROUND,(610,500,250,80)) #Background-coloured rectangle
        screen.blit(fontTNR20.render(message,1,(BLACK)), Rect(610,500,250,80)) #Puts message on screen
        draw.rect(screen,BACKGROUND,(100,100,450,450)) #Background-coloured rectangle   
        screen.blit(fontTNR20.render(heroinfo1,1,(BLACK)), Rect(60,100,250,130)) #Prints heroinfo1 (name)
        screen.blit(fontTNR20.render(heroinfo2,1,(BLACK)), Rect(60,130,250,160)) #Prints heroinfo2 (year)
        screen.blit(fontTNR20.render(heroinfo3,1,(BLACK)), Rect(60,160,250,190)) #Prints heroinfo3 (gender)
        screen.blit(fontTNR20.render(heroinfo4,1,(BLACK)), Rect(60,190,250,220)) #Prints heroinfo4 (height)
        screen.blit(fontTNR20.render(heroinfo5,1,(BLACK)), Rect(60,220,250,250)) #Prints heroinfo5 (weight)
        screen.blit(fontTNR20.render(heroinfo6,1,(BLACK)), Rect(60,250,250,280)) #Prints heroinfo6 (abilities)
        display.flip() #Displays
        time.Clock().tick(10) #Waits for a little bit
        if finished: #If it is finished
            break #Breaks out of loop
        
def heroFeatures(): #Hero features
    low_year="" #Lowerbound for year is empty
    up_year="" #Upperbound for year is empty
    gender="" #Gender is empty
    low_height="" #Lowerbound for height is empty
    up_height="" #Upperbound for height is empty
    low_weight="" #Lowerbound for weight is empty
    up_weight="" #Upperbound for weight is empty
    editing_lyear=False #Editing is false
    editing_uyear=False #Editing is false
    editing_gender=False #Editing is false
    editing_lheight=False #Editing is false
    editing_uheight=False #Editing is false
    editing_lweight=False #Editing is false
    editing_uweight=False  #Editing is false
    editing_ok=False #Editing is false
    optionLyearDone=Rect(750,300,80,40) #Rectangle for lowerbound of year
    optionUyearDone=Rect(880,300,80,40) #Rectangle for upperbound of year
    optionGenderDone=Rect(750,350,210,40) #Rectangle for gender
    optionLheightDone=Rect(750,400,80,40) #Rectangle for lowerbound of height
    optionUheightDone=Rect(880,400,80,40) #Rectangle for upperbound of height
    optionLweightDone=Rect(750,450,80,40) #Rectangle for lowerbound of weight
    optionUweightDone=Rect(880,450,80,40) #Rectangle for upperbound of weight
    optionOkButtonDone=Rect(750,550,80,40) #Rectangle for the OK button
    templist=[] #A temporary list
    valid=False #Valid is False
    finished=False #Finished is False
    colour=ACTIVECOLOUR #Colour is active
    colour1=INACTIVECOLOUR #Colour 1 is inactive
    colour2=INACTIVECOLOUR #Colour 2 is inactive
    message="Enter search conditions." #Prompts user to enter search conditions      
    while finished==False: #While not finished
        for evnt in event.get(): #Events
            if evnt.type==MOUSEMOTION: #If the event is mousemotion
                mouse=[] #Mouse
                mx,my=evnt.pos #Event posiition         
                mouse.append(mx) #Adds mx
                mouse.append(my) #Adds my
                if optionBackToHome.collidepoint(mx,my)==True: #If mouse collides with back to home
                    colour2=(255,255,0) #Changes colour
                else: #Else
                    colour2=(255,30,30) #Colour is the original exit colour
                if optionOkButtonDone.collidepoint(mx,my)==True: #If mouse collides with the done button
                    colour1=ACTIVECOLOUR #Makes colour1 active
                else: #Else
                    colour1=INACTIVECOLOUR #It is inactive
            if evnt.type==MOUSEBUTTONDOWN: #Mouse is clicked
                if optionBackToHome.collidepoint(mx,my): #If mouse collides with back to home
                    whatIsHappening="homeScreen" #Changes what is happening back to home screen
                    finished=True #Finished is true so breaks out of loop
                    return #Returns
                if optionLyearDone.collidepoint(mx,my): #If mouse collides with lowerbound for year
                    editing_lyear=not editing_lyear #Editing becomes True (not, in this case, makes False into True)
                else: #Else
                    editing_lyear=False #Editing is false like before
                if optionUyearDone.collidepoint(mx,my): #If mouse collides with upperbound for year
                    editing_uyear=not editing_uyear #Editing becomes True (not, in this case, makes False into True)
                else: #Else
                    editing_uyear=False #Editing is false like before
                    
                if optionGenderDone.collidepoint(mx,my): #If mouse collides with gender box
                    editing_gender=not editing_gender #Editing becomes True (not, in this case, makes False into True)
                else: #Else
                    editing_gender=False #Editing is false like before   
                    
                if optionLheightDone.collidepoint(mx,my): #If mouse collides with lowerbound for height
                    editing_lheight=not editing_lheight #Editing becomes True (not, in this case, makes False into True)
                else: #Else
                    editing_lheight=False #Editing is false like before              
                if optionUheightDone.collidepoint(mx,my): #If mouse collides with upperbound for height
                    editing_uheight=not editing_uheight #Editing becomes True (not, in this case, makes False into True)
                else: #Else
                    editing_uheight=False #Editing is false like before
                    
                if optionLweightDone.collidepoint(mx,my): #If mouse collides with lowerbound for weight
                    editing_lweight=not editing_lweight #Editing becomes True (not, in this case, makes False into True)
                else: #Else
                    editing_lweight=False #Editing is false like before          
                if optionUweightDone.collidepoint(mx,my): #If mouse collides with upperbound for weight
                    editing_uweight=not editing_uweight #Editing becomes True (not, in this case, makes False into True)
                else: #Else
                    editing_uweight=False #Editing is false like before

                if optionOkButtonDone.collidepoint(mx,my): #If it collides with the ok button
                    valid=True #Valid becomes true
                #Year
                    if low_year=="": #If nothing is entered into the lowerbound
                        lyear=0 #There is no lowerbound, so it is 0
                    elif low_year.isdigit()==True: #Else, if entered is a digit
                        lyear=int(low_year) #Makes it into an integer
                    else: #Else
                        valid=False #Valid becomes False
                    if up_year=="": #If nothing is entered into the upperbound
                        uyear=99999 #Upperbound is a very large integer
                    elif up_year.isdigit()==True: #Else, if entered is a digit
                        uyear=int(up_year) #Makes it into an integer
                    else: #Else
                        valid=False #Valid becomes False
                #Height
                    if low_height=="": #If nothing is entered into the lowerbound
                        lheight=0 #There is no lowerbound, so it is 0
                    elif low_height.isdigit()==True: #Else, if entered is a digit
                        lheight=int(low_height) #Makes it into an integer
                    else: #Else
                        valid=False #Valid becomes False   
                    if up_height=="": #If nothing is entered into the upperbound
                        uheight=9999 #Upperbound is a very large integer 
                    elif up_height.isdigit()==True: #Else, if entered is a digit
                        uheight=int(up_height) #Makes it into an integer
                    else: #Else
                        valid=False #Valid becomes false
                #Weight
                    if low_weight=="": #If nothing is entered into the lowerbound
                        lweight=0 #There is no lowerbound, so it is 0
                    elif low_weight.isdigit()==True: #Else, if entered is a digit
                        lweight=int(low_weight) #Makes it into an integer
                    else: #Else
                        valid=False #Valid becomes false
                    if up_weight=="": #If nothing is entered into the upperbound
                        uweight=9999 #Upperbound is a very large integer 
                    elif up_weight.isdigit()==True: #Else, if entered is a digit
                        uweight=int(up_weight) #Makes it into an integer
                    else: #Else
                        valid=False #Valid becomes false
                #Valid would become false in above cases because the input is not an integer
                        
                    if valid==True: #If valid is True
                        templist.clear() #Clears the temporary list
                        for record in range(len(idL)): #For record in range of the length of the list
                            if lyear<=yearsL[record] and uyear>=yearsL[record]: #If years boundaries are satisfied
                                if lheight<=heightL[record] and uheight>=heightL[record]: #If height boundaries are satisfied
                                    if lweight<=weightL[record] and uweight>=weightL[record]: #If weight boundaries are satisfied
                                        if gender=="" or gender==genderL[record]: #If gender is satisfied
                                            templist+=[record] #Add the record
                        message="Found "+str(len(templist))+" heros" #Prints the number of heroes in the temporary list (how many heroes satisfy given conditions)
                    else: #Else (valid=False)
                        message="Input is Invalid!" #Tell user that input is invalid
                        
            if evnt.type==KEYDOWN: #If key is down
                if active: #If active
                    if evnt.key==K_RETURN: #If enter is pressed
                        text="" #Clears text
                    elif evnt.key==K_BACKSPACE: #Else, if backspace is pressed
                        text=text[:-1] #Erases last character
                        heroID=text #Sets heroID to be the text
                    else: #Else
                        if len(text)<30: #While the text is not too long
                            text+=evnt.unicode #Adds the unicode of the key to text
                            heroID=text #Sets heroID to be the text
                if editing_lyear: #If editing lowerbound of year is True
                    if evnt.key==K_BACKSPACE: #If backspace
                        low_year=low_year[:-1] #Erases last character
                    else: #Else
                        if len(low_year)<5: #If the length is less than 5
                            low_year+=evnt.unicode #Adds unicode to lowerbound of year
                if editing_uyear: #If editing upperbound of year is True
                    if evnt.key==K_BACKSPACE: #If backspace
                        up_year=up_year[:-1] #Erases last character
                    else: #Else
                        if len(up_year)<5: #If the length is less than 5
                            up_year+=evnt.unicode #Adds unicode to lowerbound of year
                if editing_gender: #If editing gender is True
                    if evnt.key==K_BACKSPACE: #If backspace
                        gender=gender[:-1] #Erases last character
                    else: #Else
                        if len(gender)<6: #If the length is less than 6
                            gender+=evnt.unicode #Adds unicode to gender  
                if editing_lheight: #If editing lowerbound of height is True
                    if evnt.key==K_BACKSPACE: #If backspace
                        low_height=low_height[:-1] #Erases last character
                    else: #Else
                        if len(low_height)<5: #If the length is less than 5
                            low_height+=evnt.unicode #Adds unicode to lowerbound of height   
                if editing_uheight: #If editing upperbound of height is True
                    if evnt.key==K_BACKSPACE: #If backspace
                        up_height=up_height[:-1] #Erases last character
                    else: #Else
                        if len(up_height)<5: #If the length is less than 5
                            up_height+=evnt.unicode #Adds unicode to upperbound of height  
                            
                if editing_lweight: #If editing lowerbound of weight is True
                    if evnt.key==K_BACKSPACE: #If backspace
                        low_weight=low_weight[:-1] #Erases last character
                    else:
                        if len(low_weight)<5:
                            low_weight+=evnt.unicode #Adds unicode to lowerbound of weight   
                if editing_uweight: #If editing uuperbound of weight is True
                    if evnt.key==K_BACKSPACE: #If backspace
                        up_weight=up_weight[:-1] #Erases last character
                    else:
                        if len(up_weight)<5:
                            up_weight+=evnt.unicode #Adds unicode to upperbound of weight
    
        draw.rect(screen,BACKGROUND,(0,0,1000,700)) #The blue background
        screen.blit(fontTNR100.render(("Meaningful Reports"),1,(BLACK)),Rect(100,10,600,100)) #Meaningful reports title
        screen.blit(fontTNR30.render(("Choose Features"),1,(BLACK)),Rect(700,200,250,50)) #Choose features header
        draw.rect(screen,colour2,(25,15,70,40)) #Back sign at top left
        draw.rect(screen,colour2,(25,15,70,40),2) #Border
        screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40)) #Back sign
        draw.rect(screen,BLACK,(25,15,70,40),2) #Black border around it
        
        draw.rect(screen,colour1,(750,550,80,40)) #OK box
        draw.rect(screen,BLACK,(750,550,80,40),2) #Black border  
        screen.blit(fontTNR25.render("OK",1,(BLACK)), Rect(765,555,80,40)) #OK text inside box
         
        screen.blit(fontTNR30.render("Year: ",1,(BLACK)), Rect(650,300,100,40)) #Year
        colour=ACTIVECOLOUR if editing_lyear else INACTIVECOLOUR #Active colour if user is editing, else inactive colour
        draw.rect(screen, CHOICEBOX,(750,300,80,40)) #Year lowerbound         
        draw.rect(screen, colour,(750,300,80,40), 3) #Border coloured active/inactive
        screen.blit(fontTNR30.render(low_year, True, INACTIVECOLOUR), (750,300,80,40)) #Shows lowerbound

        colour=ACTIVECOLOUR if editing_uyear else INACTIVECOLOUR #Active colour if user is editing, else inactive colour
        draw.rect(screen, CHOICEBOX,(880,300,80,40)) #Year upperbound
        draw.rect(screen, colour,(880,300,80,40), 3) #Border coloured active/inactive
        screen.blit(fontTNR30.render(up_year, True, INACTIVECOLOUR), (880,300,80,40)) #Shows upperbound 

        screen.blit(fontTNR30.render("Gender: ",1,(BLACK)), Rect(650,350,210,40)) #Gender
        colour=ACTIVECOLOUR if editing_gender else INACTIVECOLOUR #Active colour if user is editing, else inactive colour
        draw.rect(screen, CHOICEBOX,(750,350,210,40)) #Gender box
        draw.rect(screen, colour,(750,350,210,40), 3) #Border coloured active/inactive
        screen.blit(fontTNR30.render(gender, True, INACTIVECOLOUR), (750,350,210,40)) #Shows gender

        screen.blit(fontTNR30.render("Height: ",1,(BLACK)), Rect(650,400,100,40)) #Height    
        colour=ACTIVECOLOUR if editing_lheight else INACTIVECOLOUR #Active colour if user is editing, else inactive colour
        draw.rect(screen, CHOICEBOX,(750,400,80,40)) #Height lowerbound
        draw.rect(screen, colour,(750,400,80,40), 3) #Border coloured active/inactive
        screen.blit(fontTNR30.render(low_height, True, INACTIVECOLOUR), (750,400,80,40)) #Shows lowerbound
        
        colour=ACTIVECOLOUR if editing_uheight else INACTIVECOLOUR #Active colour if user is editing, else inactive colour
        draw.rect(screen, CHOICEBOX,(880,400,80,40)) #Height upperbound
        draw.rect(screen, colour,(880,400,80,40), 3) #Border coloured active/inactive    
        screen.blit(fontTNR30.render(up_height, True, INACTIVECOLOUR), (880,400,80,40)) #Shows upperbound
        
        screen.blit(fontTNR30.render("Weight: ",1,(BLACK)), Rect(650,450,100,40)) #Weight      
        colour=ACTIVECOLOUR if editing_lweight else INACTIVECOLOUR #Active colour if user is editing, else inactive colour
        draw.rect(screen, CHOICEBOX,(750,450,80,40)) #Weight lowerbound
        draw.rect(screen, colour,(750,450,80,40), 3) #Border coloured active/inactive
        screen.blit(fontTNR30.render(low_weight, True, INACTIVECOLOUR), (750,450,80,40)) #Shows lowerbound
        
        colour=ACTIVECOLOUR if editing_uweight else INACTIVECOLOUR #Active colour if user is editing, else inactive colour
        draw.rect(screen, CHOICEBOX,(880,450,80,40)) #Weight upperbound
        draw.rect(screen, colour,(880,450,80,40), 3) #Border coloured active/inactive
        screen.blit(fontTNR30.render(up_weight, True, INACTIVECOLOUR), (880,450,80,40)) #Shows upperbound
        
        if len(templist)>0: #If the temporary list has more than one hero
            line=0 #Line counter starting at 0
            screen.blit(fontTNR20.render(("(cm)              (lbs)"),1,(BLACK)),Rect(400,150,600,100)) #Units of measurement
            screen.blit(fontTNR25.render(("ID  Name                       Year     Gender   H              W "),1,(BLACK)),Rect(15,175,600,100)) #Feature headers
        
            for numberRecord in templist: #For each record in the temporary list
                y=line*35+210 #y value calculation and assignment
                x=5 #x value
                screen.blit(fontTNR20.render(("%5i" %idL[numberRecord]),1,(colour)), Rect(x,y,15,15)) #ID
                x=50 #x value
                screen.blit(fontTNR20.render(("%s" %namesL[numberRecord]),1,(colour)), Rect(x,y,200,15)) #Name
                x=250 #x value
                screen.blit(fontTNR20.render(("%5i" %yearsL[numberRecord]),1,(colour)), Rect(x,y,100,15)) #Year
                x=330 #x value
                screen.blit(fontTNR20.render(("%3s" %genderL[numberRecord]),1,(colour)), Rect(x,y,60,15)) #Gender
                x=400 #x value
                screen.blit(fontTNR20.render(("%7i" %heightL[numberRecord]),1,(colour)), Rect(x,y,100,15)) #Height
                x=500 #x value
                screen.blit(fontTNR20.render(("%7i" %weightL[numberRecord]),1,(colour)), Rect(x,y,100,15)) #Weight
                line+=1 #Adds 1 to line counter

        screen.blit(fontTNR25.render(message,1,(102,0,0)), Rect(700,620,250,80)) #Shows message 
        display.flip() #Displays             
        time.Clock().tick(10) #Waits a bit
  
#Global variables 
active=False #Active is false
inputBox=Rect(600,300,250,80) #input box rectangle
colourINACTIVE=(200,200,255) #Sets inactive colour (Blue)
colourACTIVE=(0,0,255) #Active colour
colour=colourINACTIVE #Starts colour as inactive
text="" #Empty text
heroID="" #Empty heroID
message="Enter ID and Click OK to Edit" #Message
intHeroID=-1 #integer heroID
index=-1 #index
whatIsHappening="homeScreen" #What is happening (starts at homescreen)
tempID="" #Empty temporary ID
tempName="" #Empty temporary name
tempYear="" #Emptry temporary year
tempGender="" #Empty temporary gender
tempHeight="" #Empty temporary height
tempWeight="" #Empty temporary weight
tempAbilities="" #Empty temporary abilities
editingName=False #Editing name is false
editingYear=False #Editing year is false
editingGender=False #Editing gender is false
editingHeight=False #Editing height is false
editingWeight=False #Editing weight is false
editingAbilities=False #Editing abilities is false

running=True #Running is True
while running==True: #While running is true
    if whatIsHappening=="homeScreen": #If homescreen
        homeScreen() #Homescreen function
        for evnt in event.get(): #For events
            if evnt.type==MOUSEMOTION: #If mouse is moved
                mouse=[] #Mouse
                mx,my=evnt.pos #Event position is mx and my
                mouse.append(mx) #Add mx to mouse
                mouse.append(my) #Add my to mouse
                if optionExit.collidepoint(mx,my)==True: #If collides with exit
                    EXITSIGNCOLOUR=(255,255,30) #Changes colour of box
                elif optionPrintAllD.collidepoint(mx,my)==True: #If collides with print all
                    BOXCOLOUR1=BOXCOLOURLIGHT #Changes colour of box
                elif optionFindByID.collidepoint(mx,my)==True: #If collides with find by ID
                    BOXCOLOUR2a=BOXCOLOURLIGHT #Changes colour of box
                elif optionNamesAndID.collidepoint(mx,my)==True: #If collides with names and ID
                    BOXCOLOUR2b=BOXCOLOURLIGHT #Changes colour of box
                elif optionEditDetails.collidepoint(mx,my)==True: #If collides with edit details
                    BOXCOLOUR3=BOXCOLOURLIGHT #Changes colour of box
                elif optionAddHero.collidepoint(mx,my)==True: #If collides with add hero
                    BOXCOLOUR4=BOXCOLOURLIGHT #Changes colour of box
                elif optionDeleteHero.collidepoint(mx,my)==True: #If collides with delete hero
                    BOXCOLOUR5=BOXCOLOURLIGHT #Changes colour of box
                elif optionMeaningfulReports.collidepoint(mx,my)==True: #If collides with meaningful reports
                    BOXCOLOUR6=BOXCOLOURLIGHT #Changes colour of box
                else: #Else, everything is back to the original colour
                    EXITSIGNCOLOUR=(255,30,30) #Exit
                    BOXCOLOUR1=BOXCOLOUR #Box colour original
                    BOXCOLOUR2a=BOXCOLOUR #Box colour original
                    BOXCOLOUR2b=BOXCOLOUR #Box colour original
                    BOXCOLOUR3=BOXCOLOUR #Box colour original
                    BOXCOLOUR4=BOXCOLOUR #Box colour original
                    BOXCOLOUR5=BOXCOLOUR #Box colour original
                    BOXCOLOUR6=BOXCOLOUR #Box colour original
            if evnt.type==MOUSEBUTTONDOWN: #If the mouse is clicked
                if optionExit.collidepoint(mx,my)==True: #If colliding with exit
                    running=False #Not running anymore/breaks out
                elif optionPrintAllD.collidepoint(mx,my)==True: #If colliding with print all
                    whatIsHappening="printAll" #Sets what is happening to be print all
                elif optionNamesAndID.collidepoint(mx,my)==True: #If colliding with names and ID
                    whatIsHappening="printIDandName" #Sets what is happening to be print ID and name
                elif optionEditDetails.collidepoint(mx,my)==True: #If colliding with edit details
                    whatIsHappening="theHeroIWant Edit" #Sets what is happening to be edit
                elif optionFindByID.collidepoint(mx,my)==True: #If colliding with find by ID
                    whatIsHappening="findByID" #Sets what is happening to be find by ID
                elif optionDeleteHero.collidepoint(mx,my)==True: #If colliding with delete hero
                    whatIsHappening="theHeroIWant Delete" #Sets what is happening to be delete
                elif optionAddHero.collidepoint(mx,my)==True: #If colliding with add hero
                    whatIsHappening="theHeroIWant Add" #Sets what is happening to be add
                elif optionMeaningfulReports.collidepoint(mx,my): #If colliding with meaningful reports
                    whatIsHappening="MeaningfulReports" #Sets what is happening to be meaningful reports
    if whatIsHappening=="printAll": #If what is happening = printAll
        printAll() #printAll function
        whatIsHappening="homeScreen" #Return to home screen
    if whatIsHappening=="printIDandName": #If what is happening = printIDandName
        printIDandName() #printIDandName function
        BACKSIGNCOLOUR=(255,30,30) #Sets back sign colour
        done=False #Done is false
        while not done: #While not done (while True)
            for evnt in event.get(): #For events
                if evnt.type==MOUSEMOTION: #If event is mousemotion
                    mouse=[] #Mouse
                    mx,my=evnt.pos #mx,my for event position
                    mouse.append(mx) #Adds mx to mouse
                    mouse.append(my) #Adds my to mouse
                    if optionBackToHome.collidepoint(mx,my)==True: #If colliding with back to home
                        BACKSIGNCOLOUR=BACKSIGNCOLOURLIGHT #Turns box lighter
                    else: #Else
                        BACKSIGNCOLOUR=(255,30,30) #Box is original colour
                if evnt.type==MOUSEBUTTONDOWN: #If clicking
                    if optionBackToHome.collidepoint(mx,my)==True: #If mouse collides with back to home
                        whatIsHappening="homeScreen" #whatIsHappening becomes home screen
                        done=True #Done becomes True, breaks out of loop
            draw.rect(screen,BACKSIGNCOLOUR,(25,15,70,40)) #Back sign at top left
            draw.rect(screen,BLACK,(25,15,70,40),2) #Black border around it
            screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40)) #Text inside
            display.flip() #Displays
    if whatIsHappening=="theHeroIWant Edit": #If what is happening = theHeroIWant Edit 
        theHeroIWant() #theHeroIWant function
        screen.blit(fontTNR30.render(("Edit"),1,(BLACK)),Rect(600,200,250,50)) #Prints edit
        for evnt in event.get(): #For events
            if evnt.type==MOUSEMOTION: #If event is mousemotion
                mouse=[] #Mouse
                mx,my=evnt.pos #mx,my for event position
                mouse.append(mx) #Adds mx to mouse
                mouse.append(my) #Adds my to mouse
                if optionBackToHome.collidepoint(mx,my)==True: #If colliding with back to home
                    BACKSIGNCOLOUR=(255,255,0) #Backsign colour changes
                else: #Else
                    BACKSIGNCOLOUR=(255,30,30) #Backsign colour is original
            if evnt.type==MOUSEBUTTONDOWN: #If clicks
                if optionBackToHome.collidepoint(mx,my): #If collides with back to home
                    whatIsHappening="homeScreen" #Returns to home screen
                    #Clears global variables:
                    heroID=""
                    text=""
                    intHeroID=-1
                    active=False
                    message="" 
                    running=True
                    tempID=""
                    tempName=""
                    tempYear=""
                    tempGender=""
                    tempHeight=""
                    tempWeight=""
                    tempAbilities=""
                    editingName=False
                    editingYear=False
                    editingGender=False
                    editingHeight=False
                    editingWeight=False
                    editingAbilities=False                    
                if optionChoiceBox.collidepoint(mx,my): #If colliding with choice box
                    active=not active #Active is reversed
                else: #Else
                    active=False #Active is false
                if optionOKChoice.collidepoint(mx,my): #If colliding with OK box
                    if heroID.isdigit()==False: #If heroID is not a digit
                        message="The ID must be an integer" #Tells user it must be an integer
                        heroID="" #Clears heroID
                        text="" #Clears text                        
                    else: #ID is an integer
                        message="" #Message is empty
                        intHeroID=int(heroID) #Integer version of heroID
                        if idL.count(intHeroID)<1: #If not found
                            message="The ID does not exist." #Tells user ID does not exist
                            intHeroID=-1 #intHeroID=-1
                        else: #Else
                            message="Edit Superhero with ID " + heroID #Changes message
                            index=idL.index(intHeroID) #Sets index
                            #Sets temporary variables to be index of the lists
                            tempName=namesL[index]
                            tempYear=str(yearsL[index])
                            tempGender=genderL[index]
                            tempHeight=str(heightL[index])
                            tempWeight=str(weightL[index])
                            tempAbilities=abilitiesL[index]
                                              
                if optionIDEdit.collidepoint(mx,my): #If mouse collides with ID edit
                    message="ID is not editable" #ID cannot be edited          
                if optionNameEdit.collidepoint(mx,my): #If colliding is True
                    editingName=not editingName #Changes to True
                else: #Else
                    editingName=False #False
                if optionYearEdit.collidepoint(mx,my): #If colliding is True
                    editingYear=not editingYear #Changes to True
                else: #Else
                    editingYear=False #False
                if optionGenderEdit.collidepoint(mx,my): #If colliding is True
                    editingGender=not editingGender #Changes to True
                else: #Else
                    editingGender=False #False
                if optionHeightEdit.collidepoint(mx,my): #If colliding is True
                    editingHeight=not editingHeight #Changes to True
                else: #Else
                    editingHeight=False #False
                if optionWeightEdit.collidepoint(mx,my): #If colliding is True
                    editingWeight=not editingWeight #Changes to True
                else: #Else
                    editingWeight=False #False
                if optionAbilitiesEdit.collidepoint(mx,my): #If colliding is True
                    editingAbilities=not editingAbilities #Changes to True
                else: #Else
                    editingAbilities=False #False
                if optionSaveEdit.collidepoint(mx,my) and intHeroID!=-1: #If all is good when pressing save edit
                    valid=True #Valid becomes true
                    index=idL.index(intHeroID) #Sets index
                    if tempYear.isdigit()==False: #If not an integer
                        message="Year must be an integer" #Tells user must be an integer
                        valid=False #Valid becomes False
                    if tempHeight.isdigit()==False: #If not an integer
                        message="Height must be an integer" #Tells user must be an integer
                        valid=False #Valid becomes False                    
                    if tempWeight.isdigit()==False: #If not an integer
                        message="Weight must be an integer" #Tells user must be an integer
                        valid=False #Valid becomes False                        
                    if valid: #If valid is true
                        message="Superhero info updated" #Information is updated
                        #Sets originals to be the temporary variables used before:
                        namesL[index]=tempName
                        yearsL[index]=int(tempYear)
                        genderL[index]=tempGender
                        heightL[index]=int(tempHeight)
                        weightL[index]=int(tempWeight)
                        abilitiesL[index]=tempAbilities                    
                        superheroFile=open("RubySunData.dat", "w") #Opens the data file called RubySunData.dat            
                        counter=0 #Counter starting at 0
                        while counter<len(idL): #While counter is less than the length of the ID list
                            superheroFile.write(str(idL[int(counter)])+"\n") #Writes ID
                            superheroFile.write(namesL[counter]+"\n") #Writes name
                            superheroFile.write(str(yearsL[int(counter)])+"\n") #Writes year
                            superheroFile.write(genderL[counter]+"\n") #Writes gender
                            superheroFile.write(str(heightL[int(counter)])+"\n") #Writes height
                            superheroFile.write(str(weightL[int(counter)])+"\n") #Writes weight
                            superheroFile.write(str(abilitiesL[counter])+"\n") #Writes abilities
                            superheroFile.write("\n") #Writes new line
                            counter+=1 #Adds 1 to counter
                        superheroFile.write("End#~#") #Writes end message
                        superheroFile.close() #Closes data file               
                if optionCancelEdit.collidepoint(mx,my): #If user chooses close
                    intHeroID=-1 #intHeroID=-1
                    theHeroIWant() #theHeroIWant function              
                    
            if evnt.type==KEYDOWN: #If event is keydown
                if active: #If active
                    if evnt.key==K_RETURN: #If key is return
                        text="" #Clears text
                    elif evnt.key==K_BACKSPACE: #If key is backspace
                        text=text[:-1] #Gets rid of last character
                        heroID=text #Sets heroID to be text
                    else: #Else
                        if len(text)<3: #If length is not too long
                            text+=evnt.unicode #Adds unicode of key to text
                            heroID=text #Sets heroID to be text
                if editingName: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempName=tempName[:-1] #Erases last character
                    else: #Else
                        if len(tempName)<18: #If length is not too long
                            tempName+=evnt.unicode #Adds unicode of key to temporary variable
                if editingYear: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempYear=tempYear[:-1] #Erases last character
                    else: #Else
                        if len(tempYear)<4: #If length is not too long
                            tempYear+=evnt.unicode #Adds unicode of key to temporary variable
                if editingGender: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempGender=tempGender[:-1] #Erases last character
                    else: #Else
                        if len(tempGender)<6: #If length is not too long
                            tempGender+=evnt.unicode #Adds unicode of key to temporary variable
                if editingHeight: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempHeight=tempHeight[:-1] #Erases last character
                    else: #Else
                        if len(tempHeight)<6: #If length is not too long
                            tempHeight+=evnt.unicode #Adds unicode of key to temporary variable
                if editingWeight: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempWeight=tempWeight[:-1] #Erases last character
                    else: #Else
                        if len(tempWeight)<6: #If length is not too long
                            tempWeight+=evnt.unicode #Adds unicode of key to temporary variable
                if editingAbilities: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempAbilities=tempAbilities[:-1] #Erases last character
                    else: #Else
                        if len(tempAbilities)<40: #If length is not too long
                            tempAbilities+=evnt.unicode #Adds unicode of key to temporary variable
                                            
        draw.rect(screen,BACKSIGNCOLOUR,(25,15,70,40)) #Back sign at top left
        draw.rect(screen,BLACK,(25,15,70,40),2) #Black border around it
        screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40)) #Text in the box                
        colour=colourACTIVE if active else colourINACTIVE #Colour active/inactive
        draw.rect(screen,CHOICEBOX,(600,300,250,80)) #Choice box
        draw.rect(screen,BLACK,(600,300,250,80),4) #Black border around it
        screen.blit(fontTNR20.render(text, True, colour), (inputBox.x+5, inputBox.y+5)) #Input box
        draw.rect(screen,colour,inputBox,2) #Border around it
        screen.blit(fontTNR20.render(message,1,(BLACK)), Rect(610,500,250,80)) #Message 
        if intHeroID!=-1: #If intHeroID is not = to -1  
            draw.rect(screen,BACKGROUND,(0,110,500,590)) #Draws bacground coloured box
            #Prints details:
            screen.blit(fontTNR20.render("ID : ",1,(BLACK)), Rect(50,200,250,130))  
            screen.blit(fontTNR20.render("Name : ",1,(BLACK)), Rect(50,250,250,160)) 
            screen.blit(fontTNR20.render("Year : ",1,(BLACK)), Rect(50,300,250,190)) 
            screen.blit(fontTNR20.render("Gender : ",1,(BLACK)), Rect(50,350,250,220)) 
            screen.blit(fontTNR20.render("Height : ",1,(BLACK)), Rect(50,400,250,250)) 
            screen.blit(fontTNR20.render("Weight : ",1,(BLACK)), Rect(50,450,250,280))  
            screen.blit(fontTNR20.render("Abilities : ",1,(BLACK)), Rect(50,500,250,280))    
            colour=colourINACTIVE #Colour becomes inactive
            draw.rect(screen, CHOICEBOX,(150,190,350,40)) #Draws choicebox
            draw.rect(screen, colour,(150,190,350,40), 2) #Border around it
            #Printing features: ID, name, year, gender, height, weight, abilities
            screen.blit(fontTNR30.render(str(intHeroID), True, colour), (150,190,350,40))
            colour=colourACTIVE if editingName else colourINACTIVE 
            draw.rect(screen, CHOICEBOX,(150,240,350,40)) 
            draw.rect(screen, colour,(150,240,350,40), 2)
            screen.blit(fontTNR30.render(tempName, True, colour), (150,240,350,40))
            colour=colourACTIVE if editingYear else colourINACTIVE
            draw.rect(screen, CHOICEBOX,(150,290,350,40)) 
            draw.rect(screen, colour,(150,290,350,40), 2)   
            screen.blit(fontTNR30.render(tempYear, True, colour), (150,290,350,40))
            colour=colourACTIVE if editingGender else colourINACTIVE  
            draw.rect(screen, CHOICEBOX,(150,340,350,40))    
            draw.rect(screen, colour,(150,340,350,40), 2)      
            screen.blit(fontTNR30.render(tempGender, True, colour), (150,340,350,40))
            colour=colourACTIVE if editingHeight else colourINACTIVE 
            draw.rect(screen, CHOICEBOX,(150,390,350,40)) 
            draw.rect(screen, colour,(150,390,350,40), 2)     
            screen.blit(fontTNR30.render(tempHeight, True, colour), (150,390,350,40))
            colour=colourACTIVE if editingWeight else colourINACTIVE  
            draw.rect(screen, CHOICEBOX,(150,440,350,40)) 
            draw.rect(screen, colour,(150,440,350,40), 2)   
            screen.blit(fontTNR30.render(tempWeight, True, colour), (150,440,350,40))
            colour=colourACTIVE if editingAbilities else colourINACTIVE  
            draw.rect(screen, CHOICEBOX,(150,490,350,40))    
            draw.rect(screen, colour,(150,490,350,40), 2)  
            screen.blit(fontTNR30.render(tempAbilities, True, colour), (150,490,350,40))
            
            draw.rect(screen,CHOICEBOX,(150,550,100,40)) #Rectangle
            draw.rect(screen,CHOICEBOX,(400,550,100,40)) #Rectangle
            screen.blit(fontTNR20.render("Save It",1,(colourACTIVE)), Rect(165,560,100,40)) #Save details
            screen.blit(fontTNR20.render("Cancel",1,(colourACTIVE)), Rect(425,560,100,40)) #Edit details                      
        
        display.flip() #Displays              
        time.Clock().tick(10) #Waits a little bit
        
    if whatIsHappening=="theHeroIWant Add": #If whatIsHappening is theHeroIWant Add
        draw.rect(screen,BACKGROUND,(0,0,1000,700)) #Background
        screen.blit(fontTNR100.render(("Add A New Hero"),1,(BLACK)),Rect(100,10,600,100)) #Add a hero
        screen.blit(fontTNR30.render(("Add"),1,(BLACK)),Rect(600,200,250,50)) #Add
        EXITSIGNCOLOUR=(255,30,30) #Exit sign colour
        EXITSIGNCOLOURLIGHT=(255,100,100) #Exit sign colour lighter  
        draw.rect(screen,EXITSIGNCOLOUR,(25,15,70,40)) #Back sign at top left
        draw.rect(screen,BLACK,(25,15,70,40),2) #Black border around it
        screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40)) #Text for Back
        screen.blit(fontTNR20.render("Enter your choice: ",1,(BLACK)), Rect(600,270,250,50)) #Enter choice
        draw.rect(screen,CHOICEBOX,(600,300,250,80)) #Choice box
        draw.rect(screen,BLACK,(600,300,250,80),4) #Black border around it
        draw.rect(screen,OKAY,(770,430,80,40)) #Okay box
        draw.rect(screen,BLACK,(770,430,80,40),3) #Black border around it
        screen.blit(fontTNR25.render("OK",1,(BLACK)), Rect(785,435,80,40)) #OK text in the box    
        for evnt in event.get(): #For events
            if evnt.type==MOUSEMOTION: #If event is mousemotion
                mouse=[] #Mouse
                mx,my=evnt.pos #mx,my for event position
                mouse.append(mx) #Adds mx to mouse
                mouse.append(my) #Adds my to mouse
                if optionBackToHome.collidepoint(mx,my)==True: #If colliding with back to home
                    BACKSIGNCOLOUR=BACKSIGNCOLOURLIGHT #Turns box lighter
                else: #Else
                    BACKSIGNCOLOUR=(255,30,30) #Box is original colour
            if evnt.type==MOUSEBUTTONDOWN: #If user clicks
                if optionBackToHome.collidepoint(mx,my): #If collides with back to home button
                    whatIsHappening="homeScreen" #Returns to home screen
                    #Clears global variables:
                    heroID=""
                    text=""
                    intHeroID=-1
                    active=False
                    message="" 
                    running=True
                    tempID=""
                    tempName=""
                    tempYear=""
                    tempGender=""
                    tempHeight=""
                    tempWeight=""
                    tempAbilities=""
                    editingName=False
                    editingYear=False
                    editingGender=False
                    editingHeight=False
                    editingWeight=False
                    editingAbilities=False                        
                if optionChoiceBox.collidepoint(mx,my): #If colliding with choice box
                    active=not active #Active is reversed
                else: #Else
                    active=False #Active is false
                if optionOKChoice.collidepoint(mx,my): #If colliding with OK box
                    if heroID.isdigit()==False: #If heroID is not an integer
                        message="The ID must be an integer" #Tells user it must be an integer
                        heroID="" #Clears heroID
                        text="" #Clears text                                  
                    else: #ID is an integer
                        message="" #Empties message
                        intHeroID=int(heroID) #intHeroID to be the integer
                        if idL.count(intHeroID)>=1: #If counted the ID
                            message="The ID already exists." #Tell user it already exists
                            intHeroID=-1 #intHeroID=-1
                        else: #Else
                            message="Add a new hero with ID " + heroID #Proceed with adding
                            #index=idL.index(intHeroID)
                            tempName=""#namesL[index]
                            tempYear=""#str(yearsL[index])
                            tempGender=""#genderL[index]
                            tempHeight=""#str(heightL[index])
                            tempWeight=""#str(weightL[index])
                            tempAbilities=""#abilitiesL[index]
                                              
                if optionIDEdit.collidepoint(mx,my): #If mouse collides with ID edit
                    message="ID is not editable" #ID cannot be edited          
                if optionNameEdit.collidepoint(mx,my): #If colliding is True
                    editingName=not editingName #Changes to True
                else: #Else
                    editingName=False #False
                if optionYearEdit.collidepoint(mx,my): #If colliding is True
                    editingYear=not editingYear #Changes to True
                else: #Else
                    editingYear=False #False
                if optionGenderEdit.collidepoint(mx,my): #If colliding is True
                    editingGender=not editingGender #Changes to True
                else: #Else
                    editingGender=False #False
                if optionHeightEdit.collidepoint(mx,my): #If colliding is True
                    editingHeight=not editingHeight #Changes to True
                else: #Else
                    editingHeight=False #False
                if optionWeightEdit.collidepoint(mx,my): #If colliding is True
                    editingWeight=not editingWeight #Changes to True
                else: #Else
                    editingWeight=False #False
                if optionAbilitiesEdit.collidepoint(mx,my): #If colliding is True
                    editingAbilities=not editingAbilities #Changes to True
                else: #Else
                    editingAbilities=False #Editing abilities is false
                if optionSaveEdit.collidepoint(mx,my) and intHeroID!=-1: #If good to proceed
                    valid=True #Valid = True
                    #index=idL.index(intHeroID)
                    if tempYear.isdigit()==False: #If not an integer
                        message="Year must be an integer" #Tells user must be an integer
                        valid=False #Valid becomes False
                    if tempHeight.isdigit()==False: #If not an integer
                        message="Height must be an integer" #Tells user must be an integer
                        valid=False #Valid becomes False                    
                    if tempWeight.isdigit()==False: #If not an integer
                        message="Weight must be an integer" #Tells user must be an integer
                        valid=False #Valid becomes False                        
                    if valid: #If valid is true
                        message="Superhero info updated" #Information is updated
                        idL.append(intHeroID)
                        namesL.append(tempName) #[index]=tempName
                        yearsL.append(int(tempYear)) #[index]=int(tempYear)
                        genderL.append(tempGender) #[index]=tempGender
                        heightL.append(int(tempHeight)) #[index]=int(tempHeight)
                        weightL.append(int(tempWeight)) #[index]=int(tempWeight)
                        abilitiesL.append(tempAbilities) #[index]=tempAbilities                    
                        superheroFile=open("RubySunData.dat", "w") #Opens the data file called RubySunData.dat            
                        counter=0 #Counter starting at 0
                        #Writing information to file
                        while counter<len(idL): #While counter is less than the length of ID list
                            superheroFile.write(str(idL[int(counter)])+"\n") #ID
                            superheroFile.write(namesL[counter]+"\n") #Name
                            superheroFile.write(str(yearsL[int(counter)])+"\n") #Years
                            superheroFile.write(genderL[counter]+"\n") #Gender
                            superheroFile.write(str(heightL[int(counter)])+"\n") #Height
                            superheroFile.write(str(weightL[int(counter)])+"\n") #Weight
                            superheroFile.write(str(abilitiesL[counter])+"\n") #Abilities
                            superheroFile.write("\n") #Writes new line
                            counter+=1 #Adds 1 to counter
                        superheroFile.write("End#~#") #Writes end message
                        superheroFile.close()               
                if optionCancelEdit.collidepoint(mx,my): #If user chooses close
                    intHeroID=-1 #intHeroID=-1
                    theHeroIWant() #theHeroIWant function              
                    
            if evnt.type==KEYDOWN: #If event is keydown
                if active: #If active
                    if evnt.key==K_RETURN: #If key is return
                        text="" #Clears text
                    elif evnt.key==K_BACKSPACE: #If key is backspace
                        text=text[:-1] #Gets rid of last character
                        heroID=text #Sets heroID to be text
                    else: #Else
                        if len(text)<3: #If length is not too long
                            text+=evnt.unicode #Adds unicode of key to text
                            heroID=text #Sets heroID to be text
                if editingName: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempName=tempName[:-1] #Erases last character
                    else: #Else
                        if len(tempName)<18: #If length is not too long
                            tempName+=evnt.unicode #Adds unicode of key to temporary variable
                if editingYear: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempYear=tempYear[:-1] #Erases last character
                    else: #Else
                        if len(tempYear)<4: #If length is not too long
                            tempYear+=evnt.unicode #Adds unicode of key to temporary variable
                if editingGender: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempGender=tempGender[:-1] #Erases last character
                    else: #Else
                        if len(tempGender)<6: #If length is not too long
                            tempGender+=evnt.unicode #Adds unicode of key to temporary variable
                if editingHeight: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempHeight=tempHeight[:-1] #Erases last character
                    else: #Else
                        if len(tempHeight)<6: #If length is not too long
                            tempHeight+=evnt.unicode #Adds unicode of key to temporary variable
                if editingWeight: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempWeight=tempWeight[:-1] #Erases last character
                    else: #Else
                        if len(tempWeight)<6: #If length is not too long
                            tempWeight+=evnt.unicode #Adds unicode of key to temporary variable
                if editingAbilities: #If editing
                    if evnt.key==K_BACKSPACE: #If backspace
                        tempAbilities=tempAbilities[:-1] #Erases last character
                    else: #Else
                        if len(tempAbilities)<40: #If length is not too long
                            tempAbilities+=evnt.unicode #Adds unicode of key to temporary variable
        draw.rect(screen,BACKSIGNCOLOUR,(25,15,70,40)) #Back sign at top left
        draw.rect(screen,BLACK,(25,15,70,40),2)
        screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40))                             
        colour=colourACTIVE if active else colourINACTIVE
        draw.rect(screen,CHOICEBOX,(600,300,250,80))
        draw.rect(screen,BLACK,(600,300,250,80),4)
        screen.blit(fontTNR20.render(text, True, colour), (inputBox.x+5, inputBox.y+5))
        draw.rect(screen, colour, inputBox, 2)
        screen.blit(fontTNR20.render(message,1,(BLACK)), Rect(610,500,250,80))    
        if intHeroID!=-1: #If intHeroID is not = to -1  
            draw.rect(screen,BACKGROUND,(0,110,500,590)) #Draws bacground coloured box
            #Prints details:
            screen.blit(fontTNR20.render("ID : ",1,(BLACK)), Rect(50,200,250,130))  
            screen.blit(fontTNR20.render("Name : ",1,(BLACK)), Rect(50,250,250,160)) 
            screen.blit(fontTNR20.render("Year : ",1,(BLACK)), Rect(50,300,250,190)) 
            screen.blit(fontTNR20.render("Gender : ",1,(BLACK)), Rect(50,350,250,220)) 
            screen.blit(fontTNR20.render("Height : ",1,(BLACK)), Rect(50,400,250,250)) 
            screen.blit(fontTNR20.render("Weight : ",1,(BLACK)), Rect(50,450,250,280))  
            screen.blit(fontTNR20.render("Abilities : ",1,(BLACK)), Rect(50,500,250,280))    
            colour=colourINACTIVE #Colour becomes inactive
            draw.rect(screen, CHOICEBOX,(150,190,350,40))            
            draw.rect(screen, colour,(150,190,350,40), 2)   
            screen.blit(fontTNR30.render(str(intHeroID), True, colour), (150,190,350,40))
            colour=colourACTIVE if editingName else colourINACTIVE 
            draw.rect(screen, CHOICEBOX,(150,240,350,40)) 
            draw.rect(screen, colour,(150,240,350,40), 2)
            screen.blit(fontTNR30.render(tempName, True, colour), (150,240,350,40))
            colour=colourACTIVE if editingYear else colourINACTIVE
            draw.rect(screen, CHOICEBOX,(150,290,350,40)) 
            draw.rect(screen, colour,(150,290,350,40), 2)   
            screen.blit(fontTNR30.render(tempYear, True, colour), (150,290,350,40))
            colour=colourACTIVE if editingGender else colourINACTIVE  
            draw.rect(screen, CHOICEBOX,(150,340,350,40))    
            draw.rect(screen, colour,(150,340,350,40), 2)      
            screen.blit(fontTNR30.render(tempGender, True, colour), (150,340,350,40))
            colour=colourACTIVE if editingHeight else colourINACTIVE 
            draw.rect(screen, CHOICEBOX,(150,390,350,40)) 
            draw.rect(screen, colour,(150,390,350,40), 2)     
            screen.blit(fontTNR30.render(tempHeight, True, colour), (150,390,350,40))
            colour=colourACTIVE if editingWeight else colourINACTIVE  
            draw.rect(screen, CHOICEBOX,(150,440,350,40)) 
            draw.rect(screen, colour,(150,440,350,40), 2)   
            screen.blit(fontTNR30.render(tempWeight, True, colour), (150,440,350,40))
            colour=colourACTIVE if editingAbilities else colourINACTIVE  
            draw.rect(screen, CHOICEBOX,(150,490,350,40))    
            draw.rect(screen, colour,(150,490,350,40), 2)  
            screen.blit(fontTNR30.render(tempAbilities, True, colour), (150,490,350,40))
            
            draw.rect(screen,CHOICEBOX,(150,550,100,40)) #Rectangle 
            draw.rect(screen,CHOICEBOX,(400,550,100,40)) #Rectangle 
            screen.blit(fontTNR20.render("Save It",1,(colourACTIVE)), Rect(165,560,100,40)) #Save
            screen.blit(fontTNR20.render("Cancel",1,(colourACTIVE)), Rect(425,560,100,40)) #Cancel                         
        
        display.flip() #Displays               
        time.Clock().tick(10) #Waits a bit

    if whatIsHappening=="theHeroIWant Delete": #if whatIsHappening = theHeroIWant Delete
        goodToProceed=False #goodToProceed starts as False
        theHeroIWant() #theHeroIWant function
        screen.blit(fontTNR30.render(("Delete"),1,(BLACK)),Rect(600,200,250,50)) #Delete
        for evnt in event.get(): #For events
            if evnt.type==MOUSEMOTION: #If event is mousemotion
                mouse=[] #Mouse
                mx,my=evnt.pos #mx,my for event position
                mouse.append(mx) #Adds mx to mouse
                mouse.append(my) #Adds my to mouse
                if optionBackToHome.collidepoint(mx,my)==True: #If colliding with back to home
                    BACKSIGNCOLOUR=BACKSIGNCOLOURLIGHT #Turns box lighter
                else: #Else
                    BACKSIGNCOLOUR=(255,30,30) #Box is original colour
            if evnt.type==MOUSEBUTTONDOWN: #Mousebuttondown
                if optionBackToHome.collidepoint(mx,my): #If collides with back to home
                    whatIsHappening="homeScreen" #Changes what is happening
                    #Clears variables
                    heroID=""
                    text=""
                    intHeroID=-1
                    message="Enter ID and Click OK to Edit" #Message
                if optionChoiceBox.collidepoint(mx,my): #If clicked on choice box
                    active=not active #Active becomes True
                else: #Else
                    active=False #Active becomes False
                if optionOKChoice.collidepoint(mx,my): #If collides with OK
                    if heroID.isdigit()==False: #If it is an integer
                        message="The ID must be an integer" #Tells user
                        #Clears variables
                        heroID=""
                        text=""                                      
                    else: #ID is an integer
                        message="" #Empties message
                        intHeroID=int(heroID) #intHeroID is the integer of heroID
                        if idL.count(intHeroID)<1: #If not found
                            message="The ID does not exist." #Tells user it does not exist
                        else: #Else
                            message="Ok" #Message is ok
                            goodToProceed=True #Sets good to proceed to be True
                            
            if evnt.type==KEYDOWN: #If keydown
                if active: #If active
                    if evnt.key==K_RETURN: #If return
                        text="" #Clears text
                    elif evnt.key==K_BACKSPACE: #If backspace
                        text=text[:-1] #Removes last character
                        heroID=text #Sets heroID to be text
                    else:
                        if len(text)<3: #If length is not too long
                            text+=evnt.unicode #Adds unicode of key to text
                            heroID=text #Sets heroID to be text             
        draw.rect(screen,BACKSIGNCOLOUR,(25,15,70,40)) #Back sign at top left
        draw.rect(screen,BLACK,(25,15,70,40),2) #Black border around it
        screen.blit(fontTNR25.render("Back",1,(BLACK)), Rect(35,20,70,40)) #Back text in box  
        colour=colourACTIVE if active else colourINACTIVE #Colour active/inactive
        draw.rect(screen,CHOICEBOX,(600,300,250,80)) #Choicebox
        draw.rect(screen,BLACK,(600,300,250,80),4) #Black border around it
        textSurface=fontTNR20.render(text, True, colour) #textSurface
        screen.blit(textSurface, (inputBox.x+5, inputBox.y+5)) #Input box
        draw.rect(screen, colour, inputBox, 2) #Input Box
        screen.blit(fontTNR20.render(message,1,(BLACK)), Rect(610,500,250,80)) #Message    
        display.flip() #Displays
        time.Clock().tick(10) #Waits a bit
        if goodToProceed==True: #If good to proceed
            place=idL.index(int(heroID)) #Finds place
            #Deletes
            del idL[place]
            del namesL[place]
            del yearsL[place]
            del genderL[place]
            del heightL[place]
            del weightL[place]
            del abilitiesL[place]
            superheroFile=open("RubySunData.dat", "w") #Opens the data file called RubySunData.dat            
            counter=0 #Starts counter at 0
            while counter<len(idL): #While counter is less than the length of ID list
                superheroFile.write(str(idL[int(counter)])+"\n") #ID
                superheroFile.write(namesL[counter]+"\n") #Name
                superheroFile.write(str(yearsL[int(counter)])+"\n") #Years
                superheroFile.write(genderL[counter]+"\n") #Gender
                superheroFile.write(str(heightL[int(counter)])+"\n") #Height
                superheroFile.write(str(weightL[int(counter)])+"\n") #Weight
                superheroFile.write(str(abilitiesL[counter])+"\n") #Abilities
                superheroFile.write("\n") #Writes new line
                counter+=1 #Adds 1 to counter
            superheroFile.write("End#~#") #Writes end message
            superheroFile.close() #Closes file
            whatIsHappening=="homeScreen" #Sets what is happening to be home screen
    if whatIsHappening=="findByID": #If whatIsHappening = findByID
        findByID() #findByID function
        whatIsHappening="homeScreen" #Sets what is happening to be home screen
    if whatIsHappening=="MeaningfulReports": #If whatIsHappening = MeaningfulReports
        heroFeatures() #heroFeatures function
        whatIsHappening="homeScreen" #Sets what is happening to be home screen