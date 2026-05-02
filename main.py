import discord
import os
from flask import Flask
from threading import Thread

# 1. إنشاء خادم ويب بسيط لإبقاء الخدمة تعمل على Render
app = Flask('')

@app.route('/')
def home():
    return "I am alive!"

def run():
    # تشغيل الخادم على المنفذ 8080
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# 2. إعداد ديسكورد للحساب الشخصي
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'تم تسجيل الدخول كـ {self.user}')
        # ضبط الحالة لتكون متصل (Online)
        await self.change_presence(status=discord.Status.online)

# 3. تشغيل البرنامج
if __name__ == "__main__":
    keep_alive() # تشغيل خادم الويب في الخلفية
    
    client = MyClient()
    
    # جلب التوكن من إعدادات البيئة (Environment Variables) في Render
    token = os.getenv("TOKEN") 
    
    if token:
        try:
            client.run(token)
        except Exception as e:
            print(f"حدث خطأ أثناء تسجيل الدخول: {e}")
    else:
        print("خطأ: لم يتم العثور على TOKEN في إعدادات Environment الخاصة بـ Render")
