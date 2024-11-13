def expr1(A, B, C):
    return (A and B) or C

def expr2(A, B, C):
    return (A and B) or (A and C)

def expr3(A, B, C, D):
    return (A or B or C) and (B or D)

print("A ∧ B ∨ C")
print("A B C | Result")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            result = expr1(A, B, C)
            print(f"{A} {B} {C} | {int(result)}")

print("(A ∧ B) ∨ (A ∧ C)")
print("A B C | Result")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            result = expr2(A, B, C)
            print(f"{A} {B} {C} | {int(result)}")

print("(A ∨ B ∨ C) ∧ (B ∨ D)")
print("A B C D | Result")
for A in [0, 1]:
    for B in [0, 1]:
        for C in [0, 1]:
            for D in [0, 1]:
                result = expr3(A, B, C, D)
                print(f"{A} {B} {C} {D} | {int(result)}")

