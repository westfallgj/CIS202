import coin

def main():

    my_coin = coin.Coin()

    print('I am tossing the coin.')
    my_coin.toss()

    print('This side up:', my_coin.get_sideup())
    print(my_coin)

main()