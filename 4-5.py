#Are a,b,c,d in order?
a = 4
b = 2
c = 2
d = 4
in_order = True
if a <= b:
    if b<= c:
        if c <= d:
            in_order = True
        else:
            in_order = False
    else:
        in_order = False
else:
    in_order = False

if in_order == True:
    print("In order")
else:
    print("Not in order")

#5.8
duck = "Duckberg"
gourd = "Big Guy"
spitz = "I don't know what a spitz is"

print(f"The winner of best duck at this years state fair is... {duck}. What a quality duck right there \n"
      f"Next up, the winner of best gourd goes to Farmer John's {gourd}. \n"
      f"And finally winner of best spitz(?) is {spitz}")

