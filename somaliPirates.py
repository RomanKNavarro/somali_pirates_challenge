# Somali Pirates!
# The SS Gustav makes an annual journey across the Indian Ocean to export goods.
# Before making it's next voyage, you, the captain, want to install a 360° auto-
# turret to defend against Somali pirates that the SS Gustav encountered numerously
# on it's previous voyages.

'''Given the speed of the Somali pirates in kph, program the turret to detect them
from a specific distance, fire warning shots as they close in, and sink/disable
them once a specific boundary has been reached. For Somali pirates travelling at
30 kph or less, program the turret to detect them from a distance of X meters,
where X is 6 times the kph at which they travel. The turret should give a volley
of three warning shots for every 10 meters they close in on the ship. Once they reach
a 60 meter boundary, the auto turret will begin firing at the Somali ship itself.
If they are travelling at a faster rate, then program the turret to detect them from
a distance of Y meters, where Y is 4 times their kph. A 5 warning shot volley will be
given for every 12 meters they close in. The Somali Pirates will be fired at once a
110 meter boundary has been reached. In both cases, 3 more volleys are fired to
sink/disable the ship once the respective boundary has been crossed. Return the
(whole) number of total volleys of warning shots, and the total amount of the warning
shots themselves.'''



def turret(speed):
   shots = 0
   volleys = 0
   if speed <= 30:
      distance = speed * 6            
      for i in range(-distance, -60, 10):
         shots += 3
         if i <= 60:
            shots += 9
            volleys += 3
            
   else:
      distance = speed * 4
      for i in range(-distance, -110, 12):
         shots += 5
         if i <= 110:
            shots += 15
            volleys += 5

   print(volleys, 'volleys, ', shots, 'shots')
            
   
   
turret(12)
turret(11)

'''def turret(speed):
   shots = 0
   volleys = 0
   if speed <=30:
      distance = (speed * 6)//10             # speed * 6 is the distance, and 10 is to make it easier to 
      for i in range(distance):
         shots += 3
         if i <= 60:
            shots += 9
            volleys = (shots // 3) + 3
   else:
      distance = (speed * 4)//12
      for i in range(distance):
         shots += 5
         if i <= 110:
            shots += 15
            volleys = (shots // 5) + 5'''
