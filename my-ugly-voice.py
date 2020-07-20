import sounddevice as sd
import keyboard



def callback(indata, outdata, frames, time, status):
    outdata[:] = indata



print("Press P to start hearing your voice ")


keyboard.wait("p")




with sd.Stream(channels=2, callback=callback):
    sd.sleep(1000)
    print("Press Q to exit")
    keyboard.wait("q")



    

     
   