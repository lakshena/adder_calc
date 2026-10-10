from half_adder import half_adder


def full_adder(a, b, cin):
    if any(type(bit) is not int or bit not in (0, 1) for bit in (a, b, cin)):
        raise ValueError("Inputs must be single bits: 0 or 1")

    partial_sum, carry1 = half_adder(a, b)
    sum_bit, carry2 = half_adder(partial_sum, cin)
    cout = carry1 | carry2

    return sum_bit, cout


def display_truth_table():
    print("Full Adder Truth Table")
    print("A  B  Cin  Sum  Cout")
    print("--------------------")

    for a in range(2):
        for b in range(2):
            for cin in range(2):
                sum_bit, cout = full_adder(a, b, cin)
                print(f"{a}  {b}   {cin}    {sum_bit}    {cout}")


if __name__ == "__main__":
    display_truth_table()
