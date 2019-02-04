import os
def  walk(dirnam3):    
     for name in os.listdir(dirname):
        path = os.path.join(dirname, name)        
        if os.path.isfile(path):
            print(path)        
        else:            
            walk(path)

walk(os.getcwd())

