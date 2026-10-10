def half_adder(a, b):
    sum_bit = a ^ b
    carry = a & b
    return sum_bit, carry


def display_truth_table():
    print("Half Adder Truth Table")
    print("A  B  Sum  Carry")
    print("-----------------")

    for a in range(2):
        for b in range(2):
            sum_bit, carry = half_adder(a, b)
            print(f"{a}  {b}   {sum_bit}     {carry}")


if __name__ == "__main__":
    display_truth_table()
