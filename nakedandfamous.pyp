#image input = 480x270
#cropped image (without black border) = 480x192

count = 0
def setup():
        size(1280, 720, P3D)
        background(255)
        sphereDetail(3)
        lights()
        
def draw():
        #centres the drawing
	rotateX(0.12)
	translate(width/3 , (height-192)/2, -100) 
	
        background(255)
        
        frame = imageUpdate() #read in the frame to be used
        
        pointMap(frame) 
        
        screenshot() #saves an image of the current canvas

#Draws the output/3d spheres based on the frame given
def pointMap(frame):
        frame.loadPixels() #load the pixels of the frame
        
        for x in range(0, frame.width, 4):
                for y in range(39, frame.height-39, 4): #altered slightly to get rid of the black top and bottom
                        
                        pixelColour = frame.get(x, y) #get pixel colour
                        fill(pixelColour, 50) #change the fill and stroke to the pixel colour
                        stroke(pixelColour)
                        
                        pushMatrix()
                        #move sphere according to x and y coordindates and the brightness of the colour
                        translate(x, y, 2*(int(brightness(pixelColour)))) #move sphere according to x and y coordindates
                        sphere(3)
                        popMatrix()

#Loads and returns the next frame to be drawn
#Note: When it's been through all of the photos in the source folder
#      it causes an error as it tries to load a file Y 0000 which doesn't exist
#      This is done on purpose to prevent it getting caught in a infinite loop
#      and it also made it easy to tell when it was done processing all of the files
def imageUpdate():
        fileName = 'Input frames/Y ' #Location and beginning of the file name
        fileNumber = str(frameCount%7356) #Frame number        
        fileNumber= fileNumber.zfill(4) #Padding the digits to 4 digits
        #print fileNumber
        fileName = fileName + fileNumber + '.jpg'
        return loadImage(fileName)

#Saves an image of each frame to the folder Output frames
#If that directory doesn't exist it's created.
def screenshot():
    global count
    filename="Output frames\screen "+ str(count) +".png"
    save(filename)
    count+=1
