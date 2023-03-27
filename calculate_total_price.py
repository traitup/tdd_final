#input quantity
#num_espresso = จำนวนแก้วของ espresso
#num_cappuccino = จำนวนแก้วของ cappuccino
#num_latte = จำนวนแก้วของ latte
#num_mocha = จำนวนแก้วของ mocha
#num_customer_bring_cups = จำนวนแก้วที่ลูกค้านำมา

def calculate_total_price(num_espresso, num_cappuccino, num_latte, num_mocha,num_customer_bring_cups=0):
    espresso_price = 55
    cappuccino_price = 60
    latte_price = 65
    mocha_price = 70


    total_espresso_price = num_espresso * espresso_price
    total_cappuccino_price = num_cappuccino * cappuccino_price
    total_latte_price = num_latte * latte_price
    total_mocha_price = num_mocha * mocha_price

    total_price = total_espresso_price + total_cappuccino_price + total_latte_price + total_mocha_price

    total_discount = num_customer_bring_cups * 5
    total_price -= total_discount

    return total_price