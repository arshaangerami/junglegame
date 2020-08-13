#Jungle games new list

print("Dear player, your adventure starts right here, please choose one of the animals listed below")
print("Bear")
print("Snake")
print("Tiger")
print("Lion")
print("Wolf")
print("Rhinoceros")

animals = {"Rhinoceros":5 , "Lion":4 , "Tiger":3 , "Bear":2 , "Wolf":1 , "Snake":0}

player1 = input("player1 choose your animal:")
player2 = input("player2 choose your animal:")
player3 = input("player3 choose your animal:")


a = animals[player1]
b = animals[player2]
c = animals[player3]

if a >= b:
    max = a
else:
    max = b

if c >= max:
    max = c

if a == max :
    print("Player1 is winner")

if b == max:
    print("Player2 is winner")

if c == max:
    print("Player3 is winner")
