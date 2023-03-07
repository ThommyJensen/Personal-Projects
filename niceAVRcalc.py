def delayCalc(b,a,Sysclock, rez, scale, delay):

    if b == True:                                                       #Sets specs
        Sysclock = int(input('\nInput system clock freq (MHz):   '))
        Sysclock *= 1000000
        rez = 2 ** int(input('Input register size (bits):   '))
        scale = int(input('input prescaler (1 - 1024):  '))

    if a == True:                                                       #Sets delay    
        delay = float(input('Input desired delay (s):   '))
    

    if delay > 0:                                                       #If delay is set, ticks (and overflows) are calculated
        overflows = 0
        
        ticks = delay/(1/(Sysclock/scale)) - 1
        if ticks >= rez:
            overflows = int(ticks/rez)
            remTicks = ticks - overflows * rez
        if overflows > 0:
            print(f"overflows: {overflows}, remaining ticks:  {remTicks}")
        else:
            print("ticks: ",ticks)
    return Sysclock, rez, scale, delay                                  #Python is made by some wise men, who decided I can't use global variables for anything



if __name__ == '__main__':

    clock = 0
    rez = 0
    scale = 0
    delay = 0.0


    name = "e"
    while name != "jeff":                                               #Do I really need to explain how a menu works:))?
        try:
            namme = input("\nPress 'a' to set specs, 's' to set delay, 'q' to quit)   ")
            if namme == "q":
                name = "jeff"
            elif namme == "a":
                clock, rez, scale, delay = delayCalc(True,False, clock, rez, scale, delay)
            elif namme == "s":
                clock, rez, scale, delay = delayCalc(False, True, clock, rez, scale, delay)
        except Exception as e:
            print(e)
            
