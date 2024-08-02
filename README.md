Must maintain an un edited decrypted resource map file for checksum auth
I did not get actual ranges for the internal checksum, 
only around what is usually edited and use the stock checksum for offset
eg.
    # working map file at 0x300046 - calculated_crc = adder_offset
    # modded  map file calculated_crc + adder_offset = new calculated_crc 
    insert new calculated_crc at 0x300046 and inverse immediately after





flow
decrypt -> edit -> Internal Checksums -> Total Checksums -> re-encrypt

if you are not using pads, only Internal and Total checksums apply


XDF lists are incomplete and are only in working condition for some tables (use at risk)