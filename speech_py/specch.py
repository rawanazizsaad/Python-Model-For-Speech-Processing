import speech_recognition as sr
import pyttsx3

r = sr.Recognizer()
# function takes audio as input and converts it to text
def speakText(commnd):
    engine = pyttsx3.init()
    engine.say(commnd)
    engine.runAndWait
# use microphene to get audio, recognize and print it in text
with sr.Microphone() as source2:
    # wait for a second to let recognizer
    # #adjust the energy threshold based on 
    # # the surrounding noise level
    r.adjust_for_ambient_noise(source2,duration=0.2)
    # listen user input
    audio2 = r.listen(source2)
    # use google to reconize input
    myText = r.recognize_google(audio2)
    myText = myText.lower()

    print("Did You say " + myText)
    speakText(myText)

    import speech_recognition as sr 
    import webbrowser as web

    def main():
        path ="C:\Program Files\Google\Chrome\Application\chrome.exe %s"

        r = sr.Recognizer()
        with sr.Microphone() as source:
         r.adjust_for_ambient_noise(source)
         print("Please Say Something ^.^")

         audio = r.listen(source)
         print("Recognizing...")

         try:
             dest = r.recognize_google(audio)
             print("You Have Said : " + dest)
             web.get(path).open(dest)
         except Exception as e :
            print("Error : "+ str(e))


         if __name__ == "__main__":
            main()

import random
import time
import speech_recognition as sr 

def recognize_speech_from_mic(recognizer, microphone):
   if not isinstance(recognizer, sr.Recognizer):
      raise TypeError("recognizer must be 'Recognizer' instance")
   if not isinstance(microphone, sr.Microphone):
      raise TypeError("microphone must be 'Microphone' instance")
   with microphone as source:
      recognizer.adjust_for_ambient_noise(source)
      audio = recognizer.listen(source)
   response ={
       "success":True
       ,"error":None
       ,"transcription": None
    }  
   
   try:
      response["transcription"]= recognizer.recognize_google(audio)
   except sr.RequestError:
      response["success"] = False
      response["error"] = "API Unavailable"
   except sr.UnknownValueError:
      response["error"] ="Unable to Recognize speech :(' "
   return response

if __name__ =="__main__":
   WORDS =["apple","banana","grape","orange","mango","lemon"]
   NUM_GUESSES = 3
   PROMPT_LIMIT = 5

   recognizer = sr.Recognizer()
   microphone = sr.Microphone()

   word = random.choice(WORDS)

   instructions =(
      "I'm thinking of one of these words: \n"
      "{words}\n"
      "you have {n} tries to guess witch one.\n"
   ).format(words = ' , '.join(WORDS), n = NUM_GUESSES)

   print(instructions)
   time.sleep(3)
   for i in range(NUM_GUESSES):
      for j in range(PROMPT_LIMIT):
         print('Guess {}. speak! '.format(i + 1))
         guess = recognize_speech_from_mic(recognizer, microphone)
         if guess["transcription"]:
            break
         if not guess["success"]:
            break
         if guess["error"]:
            print("Error: {}".format(guess["error"])) 
            break
         print(" You Said :{}".format(guess["transcription"]))

         if guess_is_correct:
            print("Correct!. You win! ".format(word))
            break
         elif user_has_more_attempts:
            print("Incorrect, try again")
         else:
            print("Sorry you lose! {}".format(word))
            break   
         
                           
             

