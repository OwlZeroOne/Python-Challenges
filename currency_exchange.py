def exchange_money(budget, exchange_rate):
    """Calculate conversion rate

    :param budget: float - amount of money you are planning to exchange.
    :param exchange_rate: float - unit value of the foreign currency.
    :return: float - exchanged value of the foreign currency you can receive.
    """
    return budget/exchange_rate


def get_change(budget, exchanging_value):
    """Calculate change from value taken from budget

    :param budget: float - amount of money you own.
    :param exchanging_value: float - amount of your money you want to exchange now.
    :return: float - amount left of your starting currency after exchanging.
    """
    return budget - exchanging_value


def get_value_of_bills(denomination, number_of_bills):
    """ Calculate value of bills

    :param denomination: int - the value of a bill.
    :param number_of_bills: int - amount of bills you received.
    :return: int - total value of bills you now have.
    """
    return denomination * number_of_bills


def get_number_of_bills(budget, denomination):
    """ Calculate number of bills

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: int - number of bills after exchanging all your money.
    """
    return int(budget / denomination)


def get_leftover_of_bills(budget, denomination):
    """Calculate leftover after exchanging into bills

    :param budget: float - the amount of money you are planning to exchange.
    :param denomination: int - the value of a single bill.
    :return: float - the leftover amount that cannot be exchanged given the current denomination.
    """
    number_of_bills = get_number_of_bills(budget, denomination)
    return budget - number_of_bills * denomination


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """Calculate value after exchange

    :param budget: float - the amount of your money you are planning to exchange.
    :param exchange_rate: float - the unit value of the foreign currency.
    :param spread: int - percentage that is taken as an exchange fee.
    :param denomination: int - the value of a single bill.
    :return: int - maximum value you can get.
    """
    exchange_fee = spread / 100
    rate = exchange_rate + (exchange_rate * exchange_fee)
    new_money = exchange_money(budget, rate)

    number_of_bills = get_number_of_bills(new_money, denomination)
    value_of_bills = get_value_of_bills(denomination, number_of_bills)

    return value_of_bills