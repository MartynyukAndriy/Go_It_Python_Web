from datetime import date, datetime

bth_now = date(datetime.now().year, datetime.now().month, datetime.now().day)
bth = date(1991, 1, 10)
bth_know = date(bth_now.year if bth_now.month < bth.month else bth_now.year + 1 if bth_now.day <
                bth.day else bth_now.year, bth.month, bth.day)
delta = bth_now - bth_know
print(bth_know)
print(delta.days)
print(bth_now)
# bth1 = date()
