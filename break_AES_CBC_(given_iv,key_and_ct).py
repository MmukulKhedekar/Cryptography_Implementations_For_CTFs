from Cryptodome.Util.number import long_to_bytes, bytes_to_long
from Cryptodome.Util.Padding import pad
from Cryptodome.Cipher import AES

super_sec = 233294031172328
iv = "c3599b694d81ca069cefdbd7c8f06812"
iv_new = bytes.fromhex(iv)
key = pad(long_to_bytes(super_sec), 16)
ct = "8e291e6ea5eb6f186949c8d25c5e6dc30c1869a7abf1078d26792dc846f2ffb9b5793fe92036fe55c9f8a6c61f4f516e"
cipher = AES.new(key, AES.MODE_CBC, iv=iv_new)
print(cipher.decrypt(bytes.fromhex(ct)))