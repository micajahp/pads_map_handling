import CksTotal
import CksInternal
import Decrypt
import Reencrypt
import gui

import os
import easygui as eg
import shutil
import logging

logging.basicConfig(filename="m_.log", level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

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
        _binfiles = _binfiles[0]

    shutil.copyfile(_binfiles, complete+maptype + "\\" + "p88ead13.bin")
    shutil.copyfile(_cksfiles, complete+maptype + "\\" + "p88ead13.cks")

choice = 'init'
while (choice != 'C'):
    del choice
    choice = ''
    choice = gui.ask()
    print(choice.result)
    choice = choice.result[-1]
    print(choice)
    if choice == 'D':
        print("Prepare config file and allow editing")
        Decrypt.undo_encoding()
        CksInternal.cks_do_internal()
        print("map ready for editing")
    if choice == 'R':
        print("Editing complete\ncalculate check sums and re-encode")
        CksInternal.cks_do_internal()
        CksTotal.cks_do_total()
        Reencrypt.redo_encoding()
        moveto()

