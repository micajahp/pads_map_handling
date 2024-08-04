import CksTotal
import CksInternal
import decrypt
import Reencrypt

print("Prepare config file and allow editing")
decrypt.undo_encoding()
CksInternal.cks_do_internal()
print("map ready for editing")

print("editing complete check sums and reencode")
CksInternal.cks_do_internal()
CksTotal.cks_do_total()

Reencrypt.redo_encoding()

