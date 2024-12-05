def get_number(a, b, c, d):
    return 1000 * a + 100 * b + 10 * c + d


# Loop through all possible combinations of A, B, C, and D
for A in range(1, 10):
    for B in range(10):
        for C in range(10):
            for D in range(1, 10):
                # Calculate DCBA and ABCD
                DCBA = get_number(D, C, B, A)
                ABCD = get_number(A, B, C, D)

                # Check if DCBA is equal to 4 times ABCD
                if DCBA == 4 * ABCD:
                    print(f"The digits: A = {A}, B = {B}, C = {C}, D = {D}")
