import pyttsx3

engine = pyttsx3.init()
engine.say(
    '''
  
    my anme is nadim
    ami bangla bolta pare nah
    tumi ekhan balgna leklao ami bojbo nah ha ha ah
    
    '''
)
engine.runAndWait()

# amra ke baba eyta ka ekta reuseable function create korta pare ta necha dekbo


def speak(audio):

    engine.say(audio)
    engine.runAndWait()


audio = input('Input you text i conver it into a specch \n ')

speak(audio)

# conver this unlimited use able function by using while loop

while audio.upper() != 'EXIT':
    speak(audio)
    audio = input('Enter text \n')
        # if audio == ('exit' or 'EXIT'):
        #     while True:
        #         break

else:
    while True:
        break

