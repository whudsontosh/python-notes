"""
Hex codes in Python.

Covers:
  1. Hex literals and conversion functions
  2. Every byte value 0x00-0xFF with its meaning (ASCII + Latin-1)
  3. Hex escape sequences inside strings (\\x, \\u, \\U, \\N)
  4. Working with hex and bytes (bytes.hex, fromhex, int(x, 16))
  5. Bitwise operations, which hex makes easy to read
  6. Hex color codes

Run this file to print everything.
"""

import unicodedata

# ---------------------------------------------------------------------------
# 1. Hex literals and conversion
# ---------------------------------------------------------------------------
print("--- 1. Literals and conversion ---")
print(0xFF)                 # 0x prefix = hex integer literal (case-insensitive digits) -> 255
print(0xff == 0xFF)         # True: upper/lower case makes no difference
print(hex(255))             # int -> hex string with prefix: '0xff'
print(hex(-255))            # negatives keep the sign: '-0xff'
print(int("ff", 16))        # hex string -> int (base 16)
print(int("0xff", 16))      # the 0x prefix is allowed when base is 16
print(int("0xff", 0))       # base 0 = guess the base from the prefix (0x, 0o, 0b)
print(f"{255:x} {255:X} {255:#x} {255:04x} {255:#06X}")  # f-string hex formats
print(format(255, "02x"))   # format() works the same way -> 'ff'
print("%x %X %02x" % (255, 255, 10))  # old printf-style: 'ff FF 0a'

# ---------------------------------------------------------------------------
# 2. Every byte value 0x00 - 0xFF
#    Digits of a hex byte: the first digit (high nibble) is 0-F and the second
#    (low nibble) is 0-F, so 16 * 16 = 256 values.
# ---------------------------------------------------------------------------
print("\n--- 2. All byte values 0x00-0xFF ---")

# 0x00-0x1F and 0x7F are ASCII control characters (non-printable).
CONTROL_NAMES = {
    0x00: "NUL  null",
    0x01: "SOH  start of heading",
    0x02: "STX  start of text",
    0x03: "ETX  end of text (Ctrl+C)",
    0x04: "EOT  end of transmission (Ctrl+D)",
    0x05: "ENQ  enquiry",
    0x06: "ACK  acknowledge",
    0x07: "BEL  bell / beep          escape: \\a",
    0x08: "BS   backspace            escape: \\b",
    0x09: "HT   horizontal tab       escape: \\t",
    0x0A: "LF   line feed / newline  escape: \\n",
    0x0B: "VT   vertical tab         escape: \\v",
    0x0C: "FF   form feed            escape: \\f",
    0x0D: "CR   carriage return      escape: \\r",
    0x0E: "SO   shift out",
    0x0F: "SI   shift in",
    0x10: "DLE  data link escape",
    0x11: "DC1  device control 1 (XON)",
    0x12: "DC2  device control 2",
    0x13: "DC3  device control 3 (XOFF)",
    0x14: "DC4  device control 4",
    0x15: "NAK  negative acknowledge",
    0x16: "SYN  synchronous idle",
    0x17: "ETB  end of transmission block",
    0x18: "CAN  cancel",
    0x19: "EM   end of medium",
    0x1A: "SUB  substitute (Ctrl+Z, EOF on Windows)",
    0x1B: "ESC  escape (starts ANSI color codes)",
    0x1C: "FS   file separator",
    0x1D: "GS   group separator",
    0x1E: "RS   record separator",
    0x1F: "US   unit separator",
    0x7F: "DEL  delete",
}

# 0x80-0x9F are C1 control characters in Latin-1 (rarely used, non-printable).
# 0xA0 is a non-breaking space. Everything else is a visible character.
SPECIAL = {
    0x20: "space",
    0xA0: "non-breaking space",
    0xAD: "soft hyphen (invisible unless a line breaks)",
}

print("Hex  Dec  Char  Description")
print("---- ---- ----- -----------")
for code in range(256):
    if code in CONTROL_NAMES:
        char, desc = "  ", CONTROL_NAMES[code]
    elif 0x80 <= code <= 0x9F:
        char, desc = "  ", "C1 control character"
    elif code in SPECIAL:
        char, desc = "  ", SPECIAL[code]
    else:
        char = chr(code)                 # chr() turns a number into a character
        desc = unicodedata.name(char).lower()  # official Unicode name
    print(f"0x{code:02X} {code:>4} {char:^5} {desc}")

# ---------------------------------------------------------------------------
# 3. Hex escape sequences in strings
# ---------------------------------------------------------------------------
print("\n--- 3. Escape sequences ---")
print("\x41")                # \xHH        exactly 2 hex digits (0x00-0xFF)   -> A
print("\x48\x65\x6c\x6c\x6f")  # spell a word byte by byte                  -> Hello
print("é")              # \uHHHH      exactly 4 hex digits (0x0000-0xFFFF) -> é
print("€")              # euro sign
print("\U0001F600")          # \UHHHHHHHH  exactly 8 hex digits, any Unicode code point -> emoji
print("\N{GREEK SMALL LETTER PI}")   # \N{name} looks up the character by its Unicode name
print(b"\x41\x42\x43")       # in a bytes literal \x makes raw bytes (\u and \N do NOT work here)
print(r"\x41")               # raw string: the backslash is kept, so this prints \x41
print("A" == "\x41" == chr(0x41))    # True: all the same character
print(ord("A"), hex(ord("A")))       # ord() is the reverse of chr(): 65 0x41

# ---------------------------------------------------------------------------
# 4. Hex and bytes
# ---------------------------------------------------------------------------
print("\n--- 4. Hex and bytes ---")
data = b"Hi!\x00\xff"
print(data.hex())                    # bytes -> hex string: '48692100ff' (no spaces)
print(data.hex(" "))                 # separator between bytes: '48 69 21 00 ff'
print(bytes.fromhex("48 69 21"))     # hex string -> bytes (spaces are ignored): b'Hi!'
print(bytearray.fromhex("deadbeef")) # same for bytearray, which is mutable
print(list(b"\x01\x02\xff"))         # indexing/iterating bytes gives ints: [1, 2, 255]
print(int.from_bytes(b"\x01\x00", "big"))     # bytes -> int, big-endian: 256
print(int.from_bytes(b"\x01\x00", "little"))  # little-endian: 1
print((256).to_bytes(2, "big").hex())         # int -> bytes -> hex: '0100'
print("héllo".encode("utf-8").hex(" "))       # UTF-8 encodes é as two bytes: c3 a9
print("héllo".encode("latin-1").hex(" "))     # Latin-1 uses one byte per char: e9

# ---------------------------------------------------------------------------
# 5. Bitwise operations (hex maps neatly onto bits: 1 hex digit = 4 bits)
# ---------------------------------------------------------------------------
print("\n--- 5. Bitwise operations ---")
a, b = 0xF0, 0x3C
print(f"{a:#04x} & {b:#04x} = {a & b:#04x}")   # AND: bits set in both  -> 0x30
print(f"{a:#04x} | {b:#04x} = {a | b:#04x}")   # OR: bits set in either -> 0xfc
print(f"{a:#04x} ^ {b:#04x} = {a ^ b:#04x}")   # XOR: bits that differ  -> 0xcc
print(f"~{a:#04x} & 0xFF = {~a & 0xFF:#04x}")  # NOT (mask to a byte, since ~ gives negatives) -> 0x0f
print(f"{0x01:#x} << 4 = {0x01 << 4:#x}")      # shift left 4 bits = 1 hex digit  -> 0x10
print(f"{0xAB:#x} >> 4 = {0xAB >> 4:#x}")      # high nibble -> 0xa
print(f"{0xAB & 0x0F:#x}")                     # low nibble  -> 0xb
print(f"{0xDEADBEEF:#x} = {0xDEADBEEF:,}")     # big values are fine; Python ints never overflow
print(f"{0xFF:08b}  {0xA5:08b}")               # see the underlying bits

# ---------------------------------------------------------------------------
# 6. Hex color codes (#RRGGBB)
#    Two hex digits each for red, green, blue (0-255).
# ---------------------------------------------------------------------------
print("\n--- 6. Hex colors ---")


def hex_to_rgb(color):
    """'#ff8800' -> (255, 136, 0)"""
    color = color.lstrip("#")
    if len(color) == 3:                       # short form '#f80' means '#ff8800'
        color = "".join(c * 2 for c in color)
    return tuple(int(color[i:i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(r, g, b):
    """(255, 136, 0) -> '#ff8800'"""
    return f"#{r:02x}{g:02x}{b:02x}"


COLORS = {
    "black": "#000000", "white": "#FFFFFF", "red": "#FF0000",
    "green": "#00FF00", "blue": "#0000FF", "yellow": "#FFFF00",
    "cyan": "#00FFFF", "magenta": "#FF00FF", "gray": "#808080",
    "orange": "#FFA500", "purple": "#800080", "pink": "#FFC0CB",
}
for color_name, code in COLORS.items():
    print(f"{color_name:<8} {code}  {hex_to_rgb(code)}")
print(rgb_to_hex(255, 136, 0))   # '#ff8800'
print(hex_to_rgb("#f80"))        # (255, 136, 0)
