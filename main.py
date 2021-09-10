def on_forever():
    global Allapot, TojasOszlop, Elkapott
    Allapot = 1
    TojasOszlop = randint(0, 4)
    TojasLehullas()
    SebessegNoveles()
    if KosarPozicio == TojasOszlop:
        TojasElkapas()
        Elkapott += 1
    else:
        Allapot = 2
        TojasLeeses()
        EredmenyMutatas()
basic.forever(on_forever)

def TojasLehullas():
    global TojasSor
    TojasSor = 0
    for index in range(5):
        led.plot(TojasOszlop, TojasSor)
        led.unplot(TojasOszlop, TojasSor - 1)
        TojasSor += 1
        if TojasSor < 5:
            basic.pause(Sebesseg)
def EredmenyMutatas():
    while True:
        basic.show_number(Elkapott)
        basic.pause(50)

def on_button_pressed_a():
    GombKezeles("BAL")
input.on_button_pressed(Button.A, on_button_pressed_a)

def TojasLeeses():
    soundExpression.sad.play()
    led.unplot(TojasOszlop, TojasSor - 1)
    led.plot(TojasOszlop, 4)
    for index2 in range(3):
        for index22 in range(9):
            led.set_brightness(index22 * 25)
            basic.pause(50)
    led.set_brightness(Fenyero)
    basic.clear_screen()
def SebessegNoveles():
    global Sebesseg
    if Sebesseg > 100:
        Sebesseg += -10
def KosarMozgat(Irany: str):
    global KosarPozicio
    if Irany == "BAL":
        if KosarPozicio > 0:
            led.unplot(KosarPozicio, 4)
            KosarPozicio += -1
            led.plot(KosarPozicio, 4)
    elif KosarPozicio < 4:
        led.unplot(KosarPozicio, 4)
        KosarPozicio += 1
        led.plot(KosarPozicio, 4)
def TojasElkapas():
    soundExpression.hello.play()
    led.set_brightness(255)
    basic.pause(500)
    led.set_brightness(Fenyero)
def GombKezeles(Irany2: str):
    if Allapot == 1:
        KosarMozgat(Irany2)
    elif Allapot == 2:
        control.reset()

def on_button_pressed_b():
    GombKezeles("JOBB")
input.on_button_pressed(Button.B, on_button_pressed_b)

def InduloAnimacio():
    soundExpression.giggle.play_until_done()
    basic.show_icon(IconNames.SQUARE)
    basic.show_icon(IconNames.SMALL_SQUARE)
    basic.show_icon(IconNames.SMALL_DIAMOND)
    basic.clear_screen()
Elkapott = 0
TojasOszlop = 0
TojasSor = 0
KosarPozicio = 0
Fenyero = 0
Sebesseg = 0
Allapot = 0
Allapot = 0
Sebesseg = 500
Fenyero = 50
led.set_brightness(Fenyero)
music.set_volume(20)
InduloAnimacio()
basic.pause(1000)
KosarPozicio = 2
led.plot(KosarPozicio, 4)