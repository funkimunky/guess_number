function doSomething() {
    
}

basic.showLeds(`
    # . # . #
        . . . . .
        . # . # .
        . . . . .
        . # # # .
`)
basic.forever(function on_forever() {
    doSomething()
})
