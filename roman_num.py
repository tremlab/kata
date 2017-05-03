rom_arab_conversion = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def convert(roman):
    arabic_total = 0
    prev_letter_value = 500000

    for l in roman:
        current_letter_value = rom_arab_conversion[l]
        if prev_letter_value < current_letter_value:
            arabic_total -= prev_letter_value * 2
        arabic_total += current_letter_value
        prev_letter_value = current_letter_value

    return arabic_total
