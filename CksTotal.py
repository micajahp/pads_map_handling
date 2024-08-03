import crcmod
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

        crc16_func = crcmod.mkCrcFun(0x11021, rev=True , initCrc=0x0000, xorOut=0xFFFF) #crcmod.mkCrcFun(0x11021, rev=True , initCrc=0x0000, xorOut=0xFFFF)
        Kcrc = 0                                                                               #Function For Making Writable map from source
        x = 0
        bite =0
        
        while byte:
            
            
            if(B<=addr<=E):
                Kcrc= Kcrc+int.from_bytes(byte,"little")
                Kcrc= Kcrc%65535

            byte = f.read(1)
            addr=addr+1




        #print(hex(Kcrc), Kcrc)
        #Eab = Kcrc
        #Find Coefficient
        # 4884 = HW001
        # Num = HW002
        Kcrc=(Kcrc-4884)%65535
        
        print("CKS_DOWNLOAD ", hex(Kcrc))

    print(filepath[-8])


if __name__ == "__main__":
    cks_do_total()