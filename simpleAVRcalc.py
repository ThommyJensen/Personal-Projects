def main():
    Sysclock = int(input('Input system clock freq (Hz):   '))
    rez = 2 ** int(input('Input register size (bits):   '))
    scale = int(input('input prescaler (1 - 1024):  '))
    delay = float(input('Input desired delay (s):   '))
    overflows = 0

    ticks = delay/(1/(Sysclock/scale)) - 1
    if ticks >= rez:
        overflows = int(ticks/rez)
        remTicks = ticks - overflows * rez
    if overflows > 0:
        print(f"overflows: {overflows}, remaining ticks:  {remTicks}")
    else:
        print("ticks: ",ticks)

if __name__ == '__main__':
    name = "jeff"
    while name == "jeff":
        try:
            main()
        except Exception as e:
            print(e)
        namme = input('continue? (y/n)   ')
        if namme == "n":
            name = "notJeff"
