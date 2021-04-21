from datetime import *

# מציג תאריך ושעה עכשווי
print(datetime.now())

# מציג תאריך ושעה לפי הנתונים שהזנתי
# במקרה הזה הוא יציג: 2021-04-13 14:31:10
print(datetime(2021,4,13,14,31,10))

# נותן לי רק את התאריך
print((datetime.now().date()))

# נותן לי רק את השעה
print((datetime.now().time()))

# נותן לי 10 ימים/שעות/דקות/שניות
# (אפשר להוסיף ולהחסיר מתאריך אחר לדוגמא)
print(timedelta(days=10,hours=10,minutes=10,seconds=10))
