import CksTotal
import CksInternal
import Decrypt
import Reencrypt
import gui

from colorama import init, Fore
init(autoreset=True)
import os
import easygui as eg
import shutil
import logging
import sys

logging.basicConfig(filename="m_.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

print(dir(Fore))

def print(overload, end="\n", level='info', color='white'):
    color: str = color.upper()
    overload = str(overload)
    colors: dict[str, str] = {"RED": Fore.RED,
                              "YELLOW": Fore.YELLOW,
                              "CYAN": Fore.CYAN,
                              "WHITE": Fore.WHITE,
                              "MAGENTA": Fore.MAGENTA
                              } 
    color = colors[color]
    
        
    sys.stdout.write(color + f"{overload}")
    match level.lower()[0:3]:
        # information
        case 'inf':

            logging.info(overload)
        # debug
        case 'deb':
            
            logging.debug(overload)
        # critical
        case 'cri':
            
            logging.critical(overload)
        # warning
        case 'war':
            
            logging.warning(overload)
        # error
        case 'err':
            
            logging.error(overload)
    sys.stdout.write(end)

def moveto():
    logging.info("Moveto")
    filepath ="C:\\Piaggio\\PADS 4.0\\plugins\\temp\\maps"

    filepath = filepath.split("\\")
    maptype = "P88EAD13"
    complete = ""
    for i in filepath:
        try:
            os.mkdir(complete+i)
        except FileExistsError:
            print("path already exists, moving on") 
        complete = complete + i + "\\"
    try:
        os.mkdir(complete+maptype)
    except:
        pass

    # TODO 
    # Add sql for adding p88 to all 3 vehicle types RSV4, 660, and 457
    # map all bikes through 660
    _cksfiles = []
    _binfiles = []
    _folder = os.listdir('./')
    for fi in _folder:
        if os.path.isfile(fi) and '.cks' in fi.lower():
            _cksfiles.append(fi)
        if os.path.isfile(fi) and '.bin' in fi.lower() and 'cks' not in fi.lower() and 'dec' not in fi.lower():
            _binfiles.append(fi)

    if len(_cksfiles) > 1:
        _cksfiles = eg.choicebox("Select checksum file","CKS", _cksfiles)
    else:
        _cksfiles = _cksfiles[0]
        
    if len(_binfiles) > 1:
        _binfiles = eg.choicebox("Select bin for loading in pads","BIN",_binfiles)
    else:
        if len(_binfiles) == 0:
            print("No supplied file")
            return 0
        _binfiles = _binfiles[0]

    shutil.copyfile(_binfiles, complete+maptype + "\\" + "p88ead13.bin")
    shutil.copyfile(_cksfiles, complete+maptype + "\\" + "p88ead13.cks")

choice = 'init'
while (choice != 'C') and (choice != []):
    print(choice)
    del choice
    choice = ''
    choice = gui.ask()
    
    if len(choice.result) > 0:
        choice = choice.result[-1]
    else:
        sys.exit()
    
    if choice == 'D':
        s = {}
        print("Prepare config file and allow editing")

        s['Decrypt'] = Decrypt.undo_encoding()
        if s["Decrypt"] == 0:
            print("Decrypt Failed", color='red')
        else:
            print("Decrypt Successful")
        
        s["CKS internal"] = CksInternal.cks_do_internal()
        if s["CKS internal"] == 0:
            print("CKS Config Failed", color='red')
        else:
            print("CKS Config Built")
        
        if all(x > 0 for x in list(s.values())):
            print("map ready for editing")
    if choice == 'R':
        s = {}
        print("Editing complete\tcalculate check sums and re-encode")

        s["Post CKS"] = CksInternal.cks_do_internal()
        if s["Post CKS"] == 0:
            print("CKS Solve Failed", color='red')
        else:
            print("CKS Solve Successful")
            
        s["CKS Total"] = CksTotal.cks_do_total()
        if s["CKS Total"] == 0:
            print("File Checksum Calculation Failed", color='red')
        else:
            print("File Checksum Calculation Successful")
            
        s['encode'] = Reencrypt.redo_encoding()
        if s['encode'] == 0:
            print("File Re-encoding Failed", color='red')
        else:
            print("File recoded successfully")
            
        if all(x > 0 for x in list(s.values())):
            print("map ready for editing")
        moveto()

