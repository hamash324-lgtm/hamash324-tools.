import os

index_path = "index.html"
if not os.path.exists(index_path):
    index_path = "src/index.html"

with open(index_path, "r", encoding="utf-8") as f:
    content = f.read()

# بطاقة الأداة الجديدة التي ستضاف بجانب الأدوات الأخرى
apk_card = """
        <!-- أداة فك وتعديل APK -->
        <div class="bg-gray-800 border border-gray-700 rounded-xl p-6 mb-6 shadow-lg">
            <h2 class="text-xl font-bold text-cyan-400 mb-2">أداة فك وتعديل تطبيقات APK</h2>
            <p class="text-gray-300 mb-4">فك حزمة التطبيقات، استخراج الموارد وملفات الـ Smali، وإعادة البناء والتوقيع الرقمي للتثبيت المباشر.</p>
            <a href="apk-tool.html" class="inline-block bg-cyan-500 hover:bg-cyan-600 text-gray-950 font-bold px-6 py-2 rounded-lg transition">
                افتح الأداة وابدأ العمل
            </a>
        </div>
"""

# إذا لم تكن الأداة موجودة مسبقاً، أضفها قبل إغلاق الوسم المناسب أو في نهاية قسم الأدوات
if "apk-tool.html" not in content:
    # نبحث عن مكان مناسب لإدراجها (مثلا قبل نهاية الـ body أو في قسم الأدوات)
    if "<!-- الأدوات المساعدة -->" in content:
        content = content.replace("<!-- الأدوات المساعدة -->", "<!-- الأدوات المساعدة -->" + apk_card)
    else:
        # إضافتها قبل نهاية الصفحة
        content = content.replace("</body>", apk_card + "\n</body>")
    
    with open(index_path, "w", encoding="utf-8") as f:
        f.write(content)
    print("[+] تم إضافة أداة الـ APK إلى الموقع بنجاح!")
else:
    print("[!] الأداة مضافة مسبقاً في الموقع.")
