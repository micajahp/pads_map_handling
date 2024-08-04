#import crcmod
import os
import easygui as eg

def cks_do_total():

    _files = []
    _folder = os.listdir('./')
    for fi in _folder:
        if os.path.isfile(fi) and 'CKS' in fi:
            _files.append(fi)

    if len(_files) > 1:
        filepath = eg.choicebox("","",_files)
    else:
        filepath = _files[0]

    B = 0
    E = 4000000

    with open(f"./{filepath}", "rb") as f:
        byte = f.read(2)
        addr = 0

        #crc16_func = crcmod.mkCrcFun(0x11021, rev=True , initCrc=0x0000, xorOut=0xFFFF) #crcmod.mkCrcFun(0x11021, rev=True , initCrc=0x0000, xorOut=0xFFFF)
        Kcrc = 0                                                                               #Function For Making Writable map from source
        x = 0
        bite =0
        
        while byte:
            
            if (addr == 3145813):
                HDW = int(byte.decode())
            if(B<=addr<=E):
                Kcrc= Kcrc+int.from_bytes(byte,"little")
                Kcrc= Kcrc%65535

            byte = f.read(1)
            addr=addr+1




        #print(hex(Kcrc), Kcrc)
        #Eab = Kcrc
        #Find Coefficient

        # boot loader size, not included in download, is included in checksum 
        # and is different between hw numbers
        # 4884 = HW001 
        # 5121 = HW002
        if HDW == 2:
            Kcrc: int = (Kcrc-5121)%65535
        if HDW == 1:
            Kcrc: int = (Kcrc-4884)%65535
        
        print("CKS_DOWNLOAD ", str(hex(Kcrc))[2:].upper())
    with open(f"{filepath[:-7]}.config",'r') as r:
        offset = r.readline()
        offset = offset.split('?')
        offset = offset[-1]
    
    qq = 'init'
    writetofile = []
    try:
        with open(f"{filepath[:-7]}.cks",'r') as r:
            while qq:
                qq = r.readline()                
                if "CKS_DOWNLOAD " in qq:
                    qq = f"CKS_DOWNLOAD:    from: 0x80080000 to: 0x803FFFFF Cks = {str(hex(Kcrc))[2:].upper()} -- B cks computed"
                
                writetofile.append(qq)
    except:
        writetofile = [
            f"CKS_TOTAL_B:     from: 0x80020000 to: 0x803FFFFF Cks = 0000 -- B cks computed\n",
            f"CKS_APPLICATION: from: 0x80080000 to: 0x803FFFFF Cks = {offset.upper()} -- B cks computed\n",
            f"CKS_SAFETY:      from: 0x80130000 to: 0x8013F30F Cks = 0000 -- B cks computed\n",
            f"CKS_SAFETY_CAL:  from: 0x80380084 to: 0x8038054B Cks = 0000 -- B cks computed\n",
            f"CKS_DOWNLOAD:    from: 0x80080000 to: 0x803FFFFF Cks = {str(hex(Kcrc))[2:].upper()} -- B cks computed"
            ]

    with open(f"{filepath[:-7]}.cks",'w') as w:
        for i in writetofile:
            w.write(i)

if __name__ == "__main__":
    cks_do_total()