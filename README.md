Must maintain an un edited decrypted resource map file for checksum auth</br>
I did not get actual ranges for the internal checksum, </br>
only around what is usually edited and use the stock checksum for offset </br>
eg.</br>
    &emsp;&emsp;# working map file at 0x300046 - calculated_crc = adder_offset</br>
    &emsp;&emsp;# modded  map file calculated_crc + adder_offset = new calculated_crc </br>
    &emsp;&emsp;# insert new calculated_crc at 0x300046 and inverse immediately after</br>
</br>
</br>
</br>
</br>

flow</br>
decrypt -> edit -> Internal Checksums -> Total Checksums -> re-encrypt</br>
</br>
if you are not using pads, only Internal and Total checksums apply</br>
</br>
</br>
XDF lists are incomplete and are only in working condition for some tables (use at risk)</br>
