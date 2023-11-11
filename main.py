import re


def is_valid_hex_color(color):
    pattern = re.compile(r"^#[a-fA-F0-9]{6}$")

    return bool(pattern.match(color))


hex_color = input('Введите цвет в формате HEX: ')

if is_valid_hex_color(hex_color):
    print(f"{hex_color} - это корректный цвет в формате HEX.")
else:
    print(f"{hex_color} - не является корректным цветом в формате HEX.")
