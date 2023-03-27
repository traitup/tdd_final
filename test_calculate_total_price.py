from calculate_total_price import calculate_total_price

def test_result_espresso_qty_1():
    num_espresso = 1
    num_cappuccino = 0
    num_latte = 0
    num_mocha = 0
    customer_bring_cups = 0
    expected_result = "55"
    actual_result = str(calculate_total_price(num_espresso, num_cappuccino, num_latte, num_mocha,customer_bring_cups))
    assert expected_result == actual_result

def test_result_espresso_qty_2():
    num_espresso = 2
    num_cappuccino = 0
    num_latte = 0
    num_mocha = 0
    customer_bring_cups = 0
    expected_result = "110"
    actual_result = str(calculate_total_price(num_espresso, num_cappuccino, num_latte, num_mocha,customer_bring_cups))
    assert expected_result == actual_result

def test_result_espresso_cappuccino_qty_1_1():
    num_espresso = 1
    num_cappuccino = 1
    num_latte = 0
    num_mocha = 0
    customer_bring_cups = 0
    expected_result = "115"
    actual_result = str(calculate_total_price(num_espresso, num_cappuccino, num_latte, num_mocha,customer_bring_cups))
    assert expected_result == actual_result

def test_result_espresso_cappuccino_latte_mocha_qty_1_1_1_1_2():
    num_espresso = 1
    num_cappuccino = 1
    num_latte = 1
    num_mocha = 1
    customer_bring_cups = 2
    expected_result = "240"
    actual_result = str(calculate_total_price(num_espresso, num_cappuccino, num_latte, num_mocha,customer_bring_cups))
    assert expected_result == actual_result

def test_result_espresso_cappuccino_latte_mocha_qty_1_2_3_4_5():
    num_espresso = 1
    num_cappuccino = 2
    num_latte = 3
    num_mocha = 4
    customer_bring_cups = 5
    expected_result = "625"
    actual_result = str(calculate_total_price(num_espresso, num_cappuccino, num_latte, num_mocha,customer_bring_cups))
    assert expected_result == actual_result

# def test_result_espresso_cappuccino_latte_mocha_qty_1_1_1_1():
#     num_espresso = 1
#     num_cappuccino = 2
#     num_latte = 3
#     num_mocha = 4
#     customer_bring_cups = 5
#     expected_result = "625"
#     actual_result = str(calculate_total_price(num_espresso, num_cappuccino, num_latte, num_mocha,customer_bring_cups))
#     assert expected_result == actual_result