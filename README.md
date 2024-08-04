encoding type only works with lightly modified versions of advanced diagnostic software with mapping database modifications</br>

unmodified software require file encryption or signing of firmware, requiring keys which will not listed publicly</br></br>

Must maintain an un edited decrypted resource map file for checksum auth</br>
I did not get actual ranges for the internal checksum, </br>
only around what is usually edited and use the stock checksum for offset 
eg.</br>
    &emsp;&emsp;# working map file at 0x300046 - calculated_crc = adder_offset</br>
    &emsp;&emsp;# modded  map file calculated_crc + adder_offset = new calculated_crc </br>
    &emsp;&emsp;# insert new calculated_crc at 0x300046 and inverse immediately after</br>
</br>
</br>
</br>
</br>
</br>
if you are not using pads, only Internal and Total checksums apply</br> 
&emsp;&emsp;can bus communication harware required</br>
XDF lists are incomplete and are only in working condition for some tables (use at risk)</br>
</br></br>

<h1>Process</h1>
1. supply stock bin in folder with map handler</br>
&emsp;&emsp;a. run map handler option 1 to produce a bootloader checksum offset </br>
&emsp;&emsp;b. decode the map file</br>

2. make edits to map, external program, hex editor or editing program</br>

3. run map handler option 2</br>
&emsp;&emsp;a. solve internal checksums and write to location in bin</br>
&emsp;&emsp;b. solve total checksum and write both internal and total to the checksum file</br>
&emsp;&emsp;c. reencode map file for loading 