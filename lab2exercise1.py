favored = float(input("How much is your team favored:"))
home = input("Is it a(h/H)ome game?:")
bengals = input("Are they the Bengals?:")

#convert response
is_home = home.lower() == 'h'
is_bengals = bengals.lower() == 'y'

#apply decision rules
if is_bengals:
    advice = "NO! NO! NO!"
elif favored <= 0:
    advice = "Don't bet!"
elif favored >= 7.5:
    advice = "SLAM IT!"
elif 3 <= favored < 7.5:
    if is_home:
        advice = "Good bet"
    else:
        advice = "Okay bet"
elif 0 < favored < 3:
    if is_home:
        advice = "Highly risky"
    else:
        advice = "Don't bet!"
else:
    advice = "Don't bet!"

    #print result
print("Advice:", advice)