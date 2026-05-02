import discord
import os
from flask import Flask
from threading import Thread

# إنشاء خادم ويب بسيط لإقناع Render أن البرنامج "تطبيق ويب"
app = Flask('')

@app.route('/')
def home():
    return "I am alive!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

# كود الديسكورد للحساب الشخصي
class MyClient(discord.Client):
    async def on_ready(self):
        print(f'تم تسجيل الدخول كـ {self.user}')
        # جعل الحالة "متصل"
        await self.change_presence(status=discord.Status.online)

if __name__ == "__main__":
    keep_alive() # تشغيل الخادم في الخلفية
    client = MyClient()
    
    # التعديل هنا: يجب أن نستخدم اسم المتغير الذي وضعته في إعدادات Render
    # نحن اتفقنا أن نسميه TOKEN
    token = os.getenv("TOKEN") 
    
    if token:
        client.run(token)
        # ... نهاية الكود ...
if __name__ == "__main__":
    keep_alive()
    client = MyClient()
    
    # هذا السطر يخبر البرنامج أن يبحث عن التوكن في إعدادات الموقع السرية
    token = os.getenv("TOKEN") 
    
    client.run(token)
    else:
        print("خطأ: لم يتم العثور على TOKEN في إعدادات Environment")
