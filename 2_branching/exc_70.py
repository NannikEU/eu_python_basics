# 70. Даны целые числа h, m (0 <= h <= 12, 0 < m < 60),
# указывающие момент времени: « h часов, m минут». Определить наименьшее время (число полных минут), которое
# должно пройти до того момента, когда часовая и минутная стрелки на циферблате
# а) совпадут
# б) расположатся перпендикулярно друг к другу.

m = int(input("min: ")) % 60
h = int(input("hour: ")) % 12

timeToCoincide = (60 - (m - (h * 5))) % 60
timeToPerpendicularPoint1 = (60 - (m - ((h - 3) % 12 * 5))) % 60
timeToPerpendicularPoint2 = (60 - (m - ((h + 3) % 12 * 5))) % 60

timeToPerpendicular = timeToPerpendicularPoint1
if timeToPerpendicularPoint2 < timeToPerpendicularPoint1:
    timeToPerpendicular = timeToPerpendicularPoint1

print("a) time to coincide:     ", timeToCoincide)
print("b) time to perpendicular:", timeToPerpendicular)

