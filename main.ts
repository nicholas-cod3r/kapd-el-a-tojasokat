function TojasLehullas () {
    TojasSor = 0
    for (let index = 0; index < 5; index++) {
        led.plot(TojasOszlop, TojasSor)
        led.unplot(TojasOszlop, TojasSor - 1)
        TojasSor += 1
        if (TojasSor < 5) {
            basic.pause(Sebesseg)
        }
    }
}
input.onButtonPressed(Button.A, function () {
    GombKezeles("BAL")
})
function SebessegNoveles () {
    if (Sebesseg > 100) {
        Sebesseg += -10
    }
}
function KosarMozgat (Irany: string) {
    if (Irany == "BAL") {
        if (KosarPozicio > 0) {
            led.unplot(KosarPozicio, 4)
            KosarPozicio += -1
            led.plot(KosarPozicio, 4)
        }
    } else if (KosarPozicio < 4) {
        led.unplot(KosarPozicio, 4)
        KosarPozicio += 1
        led.plot(KosarPozicio, 4)
    }
}
function TojasLeesett () {
    soundExpression.sad.play()
    led.unplot(TojasOszlop, TojasSor - 1)
    led.plot(TojasOszlop, 4)
    for (let index = 0; index < 3; index++) {
        for (let index2 = 0; index2 <= 8; index2++) {
            led.setBrightness(index2 * 25)
            basic.pause(50)
        }
    }
    led.setBrightness(Fenyero)
    basic.clearScreen()
}
function TojasElkapas () {
    soundExpression.hello.play()
    led.setBrightness(255)
    basic.pause(500)
    led.setBrightness(Fenyero)
}
function GombKezeles (Irany: string) {
    if (Allapot == 1) {
        KosarMozgat(Irany)
    } else if (Allapot == 3) {
        control.reset()
    }
}
input.onButtonPressed(Button.B, function () {
    GombKezeles("JOBB")
})
function InduloAnimacio () {
    soundExpression.giggle.playUntilDone()
    basic.showIcon(IconNames.Square)
    basic.showIcon(IconNames.SmallSquare)
    basic.showIcon(IconNames.SmallDiamond)
    basic.clearScreen()
}
let Elkapva = 0
let TojasOszlop = 0
let TojasSor = 0
let KosarPozicio = 0
let Fenyero = 0
let Sebesseg = 0
let Allapot = 0
Allapot = 0
Sebesseg = 500
Fenyero = 50
led.setBrightness(Fenyero)
music.setVolume(20)
InduloAnimacio()
basic.pause(1000)
KosarPozicio = 2
led.plot(KosarPozicio, 4)
basic.forever(function () {
    Allapot = 1
    TojasOszlop = randint(0, 4)
    TojasLehullas()
    SebessegNoveles()
    if (KosarPozicio == TojasOszlop) {
        TojasElkapas()
        Elkapva += 1
    } else {
        Allapot = 2
        TojasLeesett()
        while (true) {
            basic.showNumber(Elkapva)
            basic.pause(50)
            Allapot = 3
        }
    }
})
