from datetime import *

# מכניס את התאריך ושעה למשתנה
now=datetime.now()

# נותן לי רק את השנה/החודש/היום
print(now.strftime("%d"))
print(now.strftime("%m"))
print(now.strftime("%y"))

# נותן לי רק את השעה/הדקה/השנייה (אותיות גדולות)
print(now.strftime("%H:%M:%S"))

# נותן לי תאריך ושעה מלאים לפי הבקשה
print(now.strftime("%d/%m/%y, %H:%M:%S"))