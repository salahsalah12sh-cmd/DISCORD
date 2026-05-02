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
        await self.change_presence(status=discord.Status.online)

if __name__ == "__main__":
    keep_alive() # تشغيل الخادم في الخلفية
    client = MyClient()
    # استدعاء التوكن من "البيئات" وليس كتابته مباشرة للأمان
    token = os.getenv("MTQyNDg0MzQ0NzUxMjIwMzI4NA.G_pl6X.0Jy2B2j3iJmIyXlPCllAFt7Gd84EdRiUbDAlN4")
    client.run(token)