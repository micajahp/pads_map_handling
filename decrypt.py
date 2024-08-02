##Version Decryption 0.2
##
##
##
import easygui as eg
import os



if __name__ == "__main__":

    _files = []
    _folder = os.listdir('./')
    for fi in _folder:
        if os.path.isfile(fi) and 'bIn' in fi:
            _files.append(fi)

    if len(_files) > 1:
        filepath = eg.choicebox("","",_files)
    else:
        filepath = _files[0]

    print(filepath)
    with open(f"./{filepath}", "rb") as f:
        with open(f"./{filepath}DEC", "wb") as w:
            byte = f.read(1)
            x = 0
            addr = 0
            encbit = 0
            
            while byte:
                x = x+1
                bite = int.from_bytes(byte,"big")
                
        # ######################################################################################################          
                
                if (x == 1):                # 
                    encbit = (119 - (2*bite))%255
                    if(60 <= bite <= 127):
                        encbit = encbit +1
                    if(188 <= bite <= 255):
                        encbit = encbit +1
                    
                    #print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                    w.write(encbit.to_bytes(1,"little"))
        # ######################################################################################################             
                    
                if (x == 2):                            # 
                    encbit = (57+(2*bite))%255
                    if (bite == 99):
                        encbit = 255
                    if(bite>99):
                        if(128 <= bite <= 226):
                            encbit = encbit +1
                        encbit = encbit -1
                        
                    #print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                    w.write(encbit.to_bytes(1,"little"))
                    
        # ######################################################################################################              
                if (x == 3):            # 
                    encbit = (217-(8*bite))%255
                    if(28 <= bite <= 31):
                        encbit = encbit+1
                    if(60 <= bite <= 63):
                        encbit = encbit+1
                    if(91 <= bite <= 95):
                        encbit = encbit+1
                    if(123 <= bite <= 127):
                        encbit = encbit+1
                    if(155 <= bite <= 159):
                        encbit = encbit+1
                    if(187 <= bite <= 191):
                        encbit = encbit+1
                    if(bite == 215):                            ## added in 0.2 Previously no case for 215
                        encbit = encbit+0
                    if(219 <= bite <= 223):
                        encbit = encbit+1
                    if(251 <= bite <= 255):
                        encbit = encbit+1
                    
                    #print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                    w.write(encbit.to_bytes(1,"little"))
        # ######################################################################################################                   
                if(x ==4):                              #
                    encbit = (90-(32*bite))%255
                    if(bite<215):
                        if(bite%8 > 2):
                            encbit = encbit +1
                    if (bite == 215):
                        encbit = encbit +1
                    if(bite>215):                               ## added in 0.2 Previously no case for 215
                        if(bite%8 > 1):
                            encbit = encbit +1
                            
                        
                        
                    #print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                    w.write(encbit.to_bytes(1,"little"))
        # ######################################################################################################              
                if(x==5):
                    encbit= ((148+(4*bite))%255)
                    if(27 <= bite <= 63):
                        encbit = encbit -1
                    if(91 <= bite <= 127):
                        encbit = encbit -1
                    if(155 <= bite <= 191):
                        encbit = encbit -1
                    if(219 <= bite <= 255):
                        encbit = encbit -1
                    if(bite == 218):
                        encbit = 255
                       
                    
                    #print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                    w.write(encbit.to_bytes(1,"little"))
                
        # ######################################################################################################         
                if(x==6):               # 
                    if(bite == 170):
                        encbit = 191
                    if(bite<170):
                        encbit = (21+(64*bite))%255
                    if(bite>170):
                        encbit = ((21+((64*bite)-1))%255)+1
                        if(bite>172):
                            if(bite%4 == 3):
                                encbit = encbit-1
                        
                        
                        
                    #print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                    w.write(encbit.to_bytes(1,"little"))
        # ######################################################################################################    
                if(x==7):                   # 
                    encbit = ((245-(bite*64))%255)
                    if(bite >218):
                        if(bite%4 == 3):
                            encbit = encbit +1
                            
                            
                    #print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                    w.write(encbit.to_bytes(1,"little"))
        # ######################################################################################################  
                if(x==8):                   # 
                    
                    encbit = ((102-(bite*16))%255)
                    if(bite < 117):
                        if(bite%16>6):
                            encbit = encbit+1
                    if(bite > 116):
                        if(bite%16>5):
                            encbit = encbit+1
                        
                        
                    #print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                    w.write(encbit.to_bytes(1,"little"))






        # ######################################################################################################  
                
                addr = addr +1
                if ( x > 7):
                    x = 0
                byte = f.read(1) 
                    