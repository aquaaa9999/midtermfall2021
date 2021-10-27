"""
    Alda Boyd
    Code Toolkit: Python for Fall 2020
    Local Weather Visualization 10.20.2021
"""


circleDirection = 1
circle1x = 0
circle1y = 200
yPos = 800


def setup():
    size(800,800)
    background(97,174,232)
    frameRate(60)
    

def draw():
    global table
    
    
    #loading csv data
    
    table = loadTable("history_data2.csv", "header")
    xCoordinate = 100
    #print("%i total rows in table" % (table.getRowCount()))
    for row in table.rows():
        temperature = row.getString("Temperature")
    
        #for num in temperature.split('.'):
            #print(num)
            #rect(mouseX, mouseY, float(num), float(num))
        name = row.getString("Name")
        windDirection = row.getString("Wind Direction")
        windSpeed = row.getString("Wind Speed")
        visibility = row.getString("Visibility")
        #Temperature Circle
        stroke(200)
        fill(227,121,0,float(temperature))
        circle(20, 20, float(temperature)*10)
        
        #adjusting fill color according to temperature

        global circle1x
        global circle1y
        global windSpeed
        global visibility


        # img = loadImage("grass.png")
        #  imageMode(CORNER)
        #  image(img, 0, 0, 400, 400)
    fill(0,200,0)
    rect(0,650,width,200)
    
    
    fill(5,5,float(temperature))
    text(name + " has an temperature of " + str(temperature), width/2, yPos-float(windSpeed))
    text(name + " has an windSpeed of " + str(windSpeed), 0, yPos-float(windSpeed))
    text(name + " has a visbility of " + str(visibility), 200, 790)


    fill(float(windDirection),float(windDirection),float(windDirection),float(visibility))
    
    #cloud opacity determined by visibility

    circle(circle1x, circle1y, float(windDirection))

    circle1x = circle1x + float(windSpeed)
    
    #clouds movement is determined by wind speed
   
    
    if mousePressed and (mouseButton == LEFT):
        background(97,174,232)
    if mousePressed and (mouseButton == RIGHT):
        circle1x = 0
        #the intention was different random weather direction value
        #circle1y = float(windDirection[int(random(4))])
        circle1y = int(random(600))
        
