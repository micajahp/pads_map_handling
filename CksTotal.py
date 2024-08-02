import crcmod
y = 58989     #### 58989 for 660 platform
              #### 58402 for V4 platform

B = 0
E = 4000000

with open("./p80ead13_3DECCKS.bin", "rb") as f:
    byte = f.read(2)
    addr = 0
    #if(y==58989):
        #print("Calculating For 660 Platform")
        
    #if(y==58402):
        #print("Calculating For V4 Platform")
    crc16_func = crcmod.mkCrcFun(0x11021, rev=True , initCrc=0x0000, xorOut=0xFFFF) #crcmod.mkCrcFun(0x11021, rev=True , initCrc=0x0000, xorOut=0xFFFF)
    Kcrc = 0                                                                               #Function For Making Writable map from source
    x = 0
    bite =0
    
    while byte:
        
        
        if(B<=addr<=E):
            Kcrc= Kcrc+int.from_bytes(byte,"little")
            Kcrc= Kcrc%65535
            #if(Kcrc == 58989):
            #    print(Kcrc,hex(addr))
        byte = f.read(1)
        addr=addr+1




    #print(hex(Kcrc), Kcrc)
    #Eab = Kcrc
    #Find Coefficient
    Kcrc=(Kcrc-4884)%65535
    
    print("CKS_DOWNLOAD ", hex(Kcrc))
