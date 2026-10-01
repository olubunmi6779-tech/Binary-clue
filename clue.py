# BINARY CLUE INVESTIGATOR
# Bit Play 2

print("BINARY CLUE INVESTIGATOR")
a = 7

print("\nPART 1: XOR IDENTITY")

print("a =", a)
print("a ^ a =", a ^ a)
print("a ^ 0 =", a ^ 0)

clues = [3, 5, 3, 5, 9]

xor_result = 0

for clue in clues:
    xor_result = xor_result ^ clue

print("\nPART 2: XOR CANCELLATION")

print("Clues:", clues)
print("XOR result:", xor_result)
print("Odd-occurring number:", xor_result)

numbers = [4, 7, 4, 2, 7, 2, 9]

odd_number = 0

for number in numbers:
    odd_number = odd_number ^ number

print("\nPART 3: ONE ODD-OCCURRING NUMBER")

print("Numbers:", numbers)
print("Odd-occurring number:", odd_number)

pair_numbers = [3, 9, 3, 5, 5, 7]

xor_two = 0

for number in pair_numbers:
    xor_two = xor_two ^ number

print("\nPART 4: TWO ODD-OCCURRING NUMBERS")

print("Numbers:", pair_numbers)
print("XOR of all numbers:", xor_two)

rightmost_set_bit = xor_two & -xor_two

print("\nPART 5: RIGHTMOST SET BIT")

print("Rightmost set bit:", rightmost_set_bit)

first_odd = 0
second_odd = 0

for number in pair_numbers:

    if number & rightmost_set_bit:
        first_odd = first_odd ^ number
    else:
        second_odd = second_odd ^ number


print("\nPART 6: ODD-OCCURRING NUMBERS")

print("First odd-occurring number:", first_odd)
print("Second odd-occurring number:", second_odd)

print("BINARY CLUE INVESTIGATOR SUMMARY")

print("XOR identity: a ^ a = 0")
print("XOR identity: a ^ 0 = a")
print("XOR cancellation removes repeated pairs.")

print("One odd-occurring number:", odd_number)

print(
    "Two odd-occurring numbers:",
    first_odd,
    "and",
    second_odd
)

print()