# Print "Hello, world!" to your terminal
print("Hello, world!")

def feed_phil():
    eating = [True, False, True, False, False]
    i = 0
    while i < len(eating):
        if i == 0:
            if eating[4]:
                eating[4] = False
                eating[i] = True
            else:
                if eating[i-1]:
                    eating[i-1] = False
                    eating[i] = True
            i = (i + 1) % 5
    print(eating)

            