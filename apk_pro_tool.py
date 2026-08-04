import os
import sys
import subprocess

def run_cmd(command):
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr

def decompile(apk_path):
    print("[+] جاري فك حزمة APK واستخراج الملفات والموارد...")
    code, out, err = run_cmd(f"apktool d {apk_path} -o decompiled_project -f")
    if code == 0:
        print("[+] تم فك التطبيق بنجاح في مجلد: decompiled_project")
    else:
        print(f"[-] حدث خطأ أثناء الفك:\n{err}")

def rebuild_and_sign(apk_name):
    print("[+] جاري إعادة بناء الـ APK من الملفات المعدلة...")
    code, out, err = run_cmd("apktool b decompiled_project -o unsigned.apk")
    if code != 0:
        print(f"[-] خطأ في إعادة البناء:\n{err}")
        return

    print("[+] جاري إنشاء شهادة توقيع رقمية مؤقتة...")
    if not os.path.exists("key.keystore"):
        run_cmd("keytool -genkey -v -keystore key.keystore -alias signkey -keyalg RSA -keysize 2048 -validity 10000 -passpass pass:password -storepass password -dname \"CN=User, O=Dev, C=US\"")

    print("[+] جاري توقيع التطبيق الجديد...")
    code, out, err = run_cmd(f"apksigner sign --ks key.keystore --ks-pass pass:password --out {apk_name} unsigned.apk")
    
    if code == 0:
        print(f"[عاش] تم إنشاء وتوقيع التطبيق بنجاح جاهز للتثبيت: {apk_name}")
    else:
        print(f"[-] خطأ أثناء التوقيع:\n{err}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("الاستخدام الصحيح:")
        print("  للفك: python apk_pro_tool.py d <file.apk>")
        print("  لإعادة البناء والتوقيع: python apk_pro_tool.py b <output_name.apk>")
    else:
        action = sys.argv[1]
        if action == "d" and len(sys.argv) > 2:
            decompile(sys.argv[2])
        elif action == "b" and len(sys.argv) > 2:
            rebuild_and_sign(sys.argv[2])
        else:
            print("[-] أمر غير معروف أو ناقص.")
