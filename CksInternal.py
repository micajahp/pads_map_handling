import os
import easygui as eg



def cks_do_internal():
    


    y = 58989       #### 58989 for 660 platform
                    #### 58402 for V4 platform
                    #### 60213 = eaf

    B = 3145728 
    E = 3899999

    _files = []
    _folder = os.listdir('./')
    for fi in _folder:
        if os.path.isfile(fi) and 'DEC' in fi:
            _files.append(fi)

    if len(_files) > 1:
        filepath = eg.choicebox("","",_files)
    else:
        filepath = _files[0]


    try:    
        with open(f"{filepath[:-7]}.config", 'r') as arr:
            
            noconfig = 0
            offset = 1
            while offset:
                offset = arr.readline()
                
                
                if f"{filepath[:-7]}" in offset:
                    
                    offset = offset.split('?')
                    offset = int(offset[0])
                    
                    break
    except Exception as e:
        print(e)
        noconfig = 1
        offset = 0

    with open(f"./{filepath}", "rb") as f:

        byte = f.read(1)
        addr = 0


        Kcrc = 0                                                                          
        x = 0
        bite =0
        addr = 0
        while byte:
            
            if (addr == 3145798): 
                #print(byte)
                firstdigit = int.from_bytes(byte,"little")
                #print(firstdigit)
                firstdigit *= 256
            if (addr == 3145799):
                #print(byte)
                seconddigit = int.from_bytes(byte,"little")
                #print(seconddigit)
                checksum = firstdigit+seconddigit
                
            if(addr == 3145800 or addr == 3145801):
                pass
                #print(byte)
                #print(int.from_bytes(byte,"little"))
            if(B<=addr<=E):
                Kcrc= Kcrc+int.from_bytes(byte,"little")
                Kcrc= Kcrc%65535
            
            byte = f.read(1)
            addr=addr+1

        
        # working map file at 0x300046-Kcrc = add
        # modded  map file Kcrc+add = new kcrc
        Eab = (Kcrc+offset)%65535
        Eabb = Eab^65535
        
        if noconfig == 0:
            print("Internal CKS at 0x300047  :  ",hex(Eab), " ", hex(Eab^65535))
            with open(f"{filepath[:-7]}.config", 'a+') as w:
                w.write(f"?{str(hex(Eab))[2:].upper()}")
    if noconfig == 1:
        offset = checksum+(65535-Kcrc)
        print("\n\n")

        print(checksum)
        print(((Kcrc + offset) % 65535))

        print("\n\n")
        if (checksum == ((Kcrc + offset) % 65535)):
            with open(f"{filepath[:-7]}.config", 'w+') as w:
                w.write(f"{offset}?{filepath[:-7]}")
                w.flush()
            print("config ready, edit map and recheck")    
            return
        
        #print(f"{filepath} = {hex(Kcrc%65535)}: {Kcrc} Adjusted = {Eab}:{Eab^65536}")
        
    


    with open(f"./{filepath}", "rb") as fi:
        with open(f"./{filepath.replace('DEC','CKS')}", "wb") as w:
            byte = fi.read(2)
            addr = 0
            ##3145798

            Kcrc = 0                                                                          
            addr = 0
            while byte:      
                
                
                
                if(addr == 3145798):
                    w.write(Eab.to_bytes(2,"big"))
                if(addr == 3145800):
                    w.write(Eabb.to_bytes(2,"big"))
                if(addr != 3145798 and addr != 3145800):
                    w.write(byte)
                byte = fi.read(2)
                addr=addr+2
    print("Internal CKS complete")

if __name__ == "__main__":
    cks_do_internal()     