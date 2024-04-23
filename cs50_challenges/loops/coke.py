total_sum = 50

while total_sum > 0:
    inserted_coin = int(input("Insert coin: "))

    if inserted_coin not in[5, 10, 25]:
        continue
    else:
        total_sum -= inserted_coin
        if total_sum == 0:
            print("Change owed: ", total_sum)
        else:
            print("Amount due: ", total_sum)