from pymongo import MongoClient
import datetime
import pygame 

# initialize the pygame library and prepare it for use
pygame.init() 

# set window size to 400x300 pixels
window = pygame.display.set_mode((400, 300))   
# set the window name
pygame.display.set_caption('My Alert')   

# create a font Arial with size 30 for text display
font = pygame.font.SysFont("Arial", 30)
# create a clock to control frame rate
clock = pygame.time.Clock()

# Your URI copied from the MongoDB Atlas website
# Replace <password> with the password you created for your database user
uri = 'mongodb+srv://adrianlamyc:aVdgzKgHl8dQqHt7@cluster0.zhbxr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0'
client = MongoClient(uri)
db = client.database
collection = db.sensors   

# The code block inside while True loop repeats continuously until 
# you press Ctrl+C in the terminal
while True:
    # process any pending events to ensure the application remains responsive
    pygame.event.pump()
# Get the last record from the collection (sorted by "date")
    lastRecord = collection.find().sort("date", -1).limit(1)[0]  

    print("Temperature: {0:.1f} °C".format(lastRecord['temp']))

    print("Humidity: {0:.1f} %".format(lastRecord['humi']))

    # fill the window with white color by RGB code (255, 255, 255)
    if lastRecord['temp'] > 28:
       window.fill((255, 0, 0))  # red background
    else:
       window.fill((255, 255, 255)) # white background

    # create a text surface with black color, RGB code (0, 0, 0)
    tempText = font.render("Temperature: {0:.1f}°C".format(lastRecord['temp']), True, (0, 0, 0))    

    # draw the tempText surface at the position (10, 10)
    window.blit(tempText, (10, 10))

    # Exercise: Displaying humidity value in the window
    # Fill out the ... below

    # create a text surface with black color, RGB code (0, 0, 0)
    humiText = font.render("Humidity: {0:.1f}%".format(lastRecord['humi']), True, (0, 0, 0)) 

    # draw the humiText surface at the position (10, 40)
    window.blit(humiText, (10, 40))

    # update the display window
    pygame.display.update()      
    # set the frame rate to 1 frame per second
    clock.tick(1) 
  
