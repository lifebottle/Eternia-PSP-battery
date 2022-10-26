import sys
import hashlib

def remove_battery():
    if readable_hash == 'af119fbc49cc7c1472da143749d466198234398c6044814b4168e87d90372ac4':
        print("Patching Tales of Eternia (EU)")
        iso.seek(0x02CF9380)
        iso.write(b'\xff\xff\x02\x24')
        iso.close()
        print("Battery removal patch applied successfully")
    elif readable_hash == '62ed330c8ab5a1f241486ab7dd2f19e923c30a182a19bb40c0ab76da52d4808c':
        print("Patching Tales of Eternia (Undub)")
        iso.seek(0x0016D380)
        iso.write(b'\xff\xff\x02\x24')
        iso.seek(0x015EE380)
        iso.write(b'\xff\xff\x02\x24')
        iso.close()
        print("Battery removal patch applied successfully")
    else:
        print("Bad ROM")

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage:")
        print("python toe_battery.py ToE_EU.iso")
        print("python toe_battery.py \"C:/ToE_EU.iso\"")
        sys.exit()
    
    iso = open(sys.argv[1], 'r+b')
    bytes = iso.read()
    readable_hash = hashlib.sha256(bytes).hexdigest()
    remove_battery()

