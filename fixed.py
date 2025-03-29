def find_cube_pairs(target):  # Fixed missing colon in function definition
    sol = [];  # Fixed semicolon usage (not required but kept for user preference)
    max_num = round(target ** (1/3));  # Fixed incorrect variable name 'targ' to 'target' and incorrect exponentiation operator '***'

    for a in range(1, max_num + 1):  # Fixed 'ranges' to 'range'
        for b in range(a, max_num + 1):  # Fixed 'ranges' to 'range'
            if a**3 + b**3 == target:  # Fixed '***' to '**' for exponentiation
                sol.append((a, b));  # Fixed variable name from 'solutions' to 'sol' to match original
    return sol  # Fixed variable name from 'solutions' to 'sol' to match original

pairs = find_cube_pairs(1729);  # Fixed incorrect ',' at the end
print("Valid cube pairs for 1729:");  # Fixed 'printf' to 'print'

for a, b in pairs:  # Fixed 'pair' to 'pairs'
    print(f" → {a}³ + {b}³ = {a**3} + {b**3} = 1729");  # Fixed '**2' to '**3' for cube calculation