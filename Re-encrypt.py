##Version Encryption 0.2
##
##
##
import os
import easygui as eg
_files = []
_folder = os.listdir('./')
for fi in _folder:
    if os.path.isfile(fi) and 'CKS' in fi:
        _files.append(fi)

if len(_files) > 1:
    filepath = eg.choicebox("","",_files)
else:
    filepath = _files[0]









with open(f"./{filepath}", "rb") as f:
    with open(f"./{filepath.replace('CKS','').replace('bIn','bin')}", "wb") as w:
        byte = f.read(1)
        x = 0
        addr = 0
        encbit = 0
        
        while byte:
            x = x+1
            bite = int.from_bytes(byte,"big")
            
    # ######################################################################################################          
            
            if (x == 1):                            # IF(Mod(byte,2) ,IF(H94<0,H94+128,H94),IF(H94<128,H94+128,H94))
                if(bite % 2 == 1):                                      
                    encbit = (255-195)-(int((bite/2)+1))
                    if (encbit < 0):              # IF(H129<128,H129+128,H129))
                        encbit = encbit+128
                if(bite % 2 == 0):
                    encbit = (255-68)-(int(bite/2)) 
                    if(encbit<128):                   # IF(H129<0,H129+128,H129)
                        encbit=encbit+128
                # print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                w.write(encbit.to_bytes(1,"little"))
    # ######################################################################################################             
                
            if (x == 2):                            # =if(Mod(M2,2), 255-(156-int(M2/2+1)),255-(28-int((M2/2))))
                if(bite % 2 == 1):
                    encbit = 255-(156-int(bite/2+1)) 
                    if(encbit > 127):
                        encbit = encbit-128
                if(bite % 2 == 0):
                    encbit = 255-(28-int((bite/2)))  
                    if(encbit>255):                   # IF(P2>255,P2-128,P2)
                        encbit=encbit-128
                # print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                w.write(encbit.to_bytes(1,"little"))
                
    # ######################################################################################################              
            if (x == 3):                # =MOD(91-(32*(HEX2DEC(U5)+1)),255)
                encbit=(91-(32*(bite+1)))%255
                if(bite > 217):                   # =IF(T5>217, Y5+32, Y5)
                    encbit=encbit+32
                    if(bite > 220):
                        encbit=encbit%255
                # print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                w.write(encbit.to_bytes(1,"little"))
    # ######################################################################################################                   
            if(x ==4):
                if(bite <91):
                    encbit=(210-(bite*8))%255
                if(bite==91):
                    encbit = 255
                if(bite >91):
                    encbit=(210-((bite-1)*8))%255
                # print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                w.write(encbit.to_bytes(1,"little"))
    # ######################################################################################################              
            if(x==5):
                if(bite>147):
                    encbit = ((27+(64*bite))-64)%255
                if(bite<148):
                    encbit=((27+(64*bite)-1)%255)+1
                # print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                w.write(encbit.to_bytes(1,"little"))
            
    # ######################################################################################################         
            if(x==6):                   # =IF(HEX2DEC(I23)<21,(MOD(175+(4*HEX2DEC(I23))-1,255))+1,(MOD(175+(4*(HEX2DEC(I23)-1)),255)))
                if(bite<21):
                    encbit=((175+(4*bite)-1)%255)+1
                if(bite>20):
                    encbit=((175+(4*(bite-1)))%255)
                # print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                w.write(encbit.to_bytes(1,"little"))
    # ######################################################################################################    
            if(x==7):                   # =IF(HEX2DEC(P248)<246,  (MOD(215-(4*(HEX2DEC(P248))),255)) , MOD(215-4*(HEX2DEC(P248)-1)-1,255)+1)
                if (bite<246):
                    encbit=(215-(4*bite))%255
                if (bite>245):
                    encbit = (((215-(4*(bite-1)))-1)%255)+1
                # print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                w.write(encbit.to_bytes(1,"little"))
    # ######################################################################################################  
            if(x==8):                   # =IF(HEX2DEC(W2)<103,MOD(102-(16*HEX2DEC(W2)),255),MOD(102-(16*(HEX2DEC(W2)-1))-1,255)+1)
                if(bite<103):
                    encbit = ((102-(16*bite))%255)
                if(bite>102):
                    encbit = ((102-(16*(bite-1))-1)%255)+1
                # print(bite , x , hex(addr), encbit, encbit.to_bytes(1,"little"))
                w.write(encbit.to_bytes(1,"little"))






    # ######################################################################################################  
            
            addr = addr +1
            if ( x > 7):
                x = 0
            byte = f.read(1) 
            