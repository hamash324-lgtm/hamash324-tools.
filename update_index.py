import os

html_content = """<!DOCTYPE html>
<html lang="ar" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Hamash Tools</title>
    <script src="https://cdn.jsdelivr.net/npm/@tailwindcss/browser@4"></script>
</head>
<body class="bg-gray-900 text-white p-6">
    <div class="max-w-md mx-auto">
        <h1 class="text-2xl font-bold mb-4">Available Utility & Code Tools</h1>
        
        <!-- APK Signer & Editor Tool -->
        <div class="bg-gray-800 p-4 rounded-xl border border-gray-700 mt-4">
            <h3 class="text-white font-bold text-lg">APK Editor & Signer</h3>
            <p class="text-gray-400 text-sm mt-1">تعديل تطبيقات APK وتوقيعها بشهادة جديدة لتصبح جاهزة للتثبيت.</p>
            <button onclick="alert('جارٍ فتح أداة التعديل والتوقيع...');" class="mt-3 bg-blue-600 text-white px-4 py-2 rounded-lg text-sm font-semibold hover:bg-blue-500 transition">افتح الأداة وقُم بتحميل الإعدادات</button>
        </div>
    </div>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("تم تحديث الملف وإضافة الأداة بنجاح!")
