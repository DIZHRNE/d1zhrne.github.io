from flask import Flask
from datetime import datetime
from datetime import datetime as dt
import time
import webbrowser
app = Flask(__name__)

@app.route('/')
def homepage():


    def day():
        while True:
            if dt.now().day == 22:
                print("now.day = 22")
        
            else:
                time.sleep(10)
            
        
            return True
            
        
    def hour():
        while True:
            if dt.now().hour == 2:
                print("now.hour = 2")
        
            else:
                time.sleep(10)
        
            return True
            
            
    def minute():
        while True:
            if dt.now().minute == 54: 
                print("now.minute = 54")   
            
        
            else:
                time.sleep(10)
    
            return True
    
    def second():
        while True:
            if dt.now().second == 30:
                print("now.second() = 30")
        
            else:
                time.sleep(10)
            
        return True
        
    
    def allTrue():
        while True:
            if day() == True and minute() == True and second() == True:
                print("Success!")
        
            return True
            
    day() 
    hour()
    minute()
    second()           
    allTrue()

    def playMusic():
        if allTrue() == True:
            webbrowser.open('https://s0.vocaroo.com/media/download_temp/Vocaroo_s0HThOXEH3gI.mp3')
            

    playMusic()
    
    return playmusic

    <h1>Hello heroku</h1>
    <p>The music will play at 12/22/2018 at 2:34.</p>

    <img src="http://loremflickr.com/600/400" />
    """.format(time=the_time)

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)

