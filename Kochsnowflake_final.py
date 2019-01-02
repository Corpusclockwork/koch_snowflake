import turtle 
wn=turtle.Screen()
wn.bgcolor("#CBF8F9")

move = turtle.Turtle()

def sequence():
    flake = "FLFRFLF"
    snowflake = "FRFRF"
    n = 5
    while n != 0:
        snowflake = snowflake.replace("F", flake)
        n = n - 1
    return snowflake

def snowflake():
    move.color("#0CB4B8")
    move.speed("fastest")
    turtle.begin_fill()
    for step in sequence():
        if step == "F":
            move.forward(1)
        elif step == "R":
            move.right(120)
        elif step == "L":
            move.left(60)
    turtle.end_fill()
        
snowflake()


