import pyttsx3

engine = pyttsx3.init()
def speak(audio):

    engine.say(audio)
    engine.runAndWait()
print('''
to talk = just wright
to stop talk = just wright bye
''')

# sweet voice and functionality of talk or exit/bye
while True:

    audio = input('talk or bye \n')
    if audio.upper() == 'BYE':
        break
    voices = engine.getProperty('voices')
    voice = input('male or female: ')

    if voice == '1':
        engine.setProperty('voice', voices[0].id)
        speak(audio)
    elif voice == '0':
        engine.setProperty('voice', voices[1].id)
        speak(audio)
    else:
        print('press 1 or 0')





'''
rough code 
'''


# while True:
#
#     audion = input('talk or say bye \n')
#
#
#
#     voices = engine.getProperty('voices')
#     # print(voices[0].id) to show the change of voices
#     if audion.upper() == 'BYE':
#         break
#     voice = input("male or female \n")
#     if voice == '1':
#             engine.setProperty('voice', voices[0].id)
#             speak(audion)
#     elif voice == '0':
#             engine.setProperty('voice', voices[1].id)
#             speak(audion)
#     # else:
#     #     break
# # else:
# #     break
#
#         # if audio == ('exit' or 'EXIT'):
#         #     while True:
#         #         break
#
# else:
#     while True:
#         break