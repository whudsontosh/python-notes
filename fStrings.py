"""
f-strings (formatted string literals) demo.

An f-string is a string prefixed with f (or F). Anything inside {curly braces}
is evaluated as a Python expression at runtime and its result is inserted into
the string. Run this file to see every example's output.
"""

import datetime
import math

# ---------------------------------------------------------------------------
# 1. Basics: inserting variables
# ---------------------------------------------------------------------------
print("--- 1. Basics ---")
name = "Ada"
age = 36
print(f"My name is {name} and I am {age} years old.")
# Non-string values (like the int age) are converted with str() automatically.

# ---------------------------------------------------------------------------
# 2. Any expression works inside the braces
# ---------------------------------------------------------------------------
print("\n--- 2. Expressions ---")
a, b = 7, 3
print(f"{a} + {b} = {a + b}")                        # arithmetic
print(f"{name.upper()} has {len(name)} letters")      # method / function calls
print(f"{'even' if a % 2 == 0 else 'odd'}")           # conditional expression
print(f"Squares: {[n ** 2 for n in range(5)]}")       # comprehensions
data = {"key": "value", "n": 42}
print(f"Dict lookup: {data['key']}")                  # use different quotes inside than outside
print(f"Math: {math.sqrt(16)}")                       # calling imported modules

# ---------------------------------------------------------------------------
# 3. Conversion flags: !s, !r, !a
# ---------------------------------------------------------------------------
print("\n--- 3. Conversion flags ---")
text = "héllo\n"
print(f"{text!s}")   # str()   - the normal, human-friendly form (default)
print(f"{text!r}")   # repr()  - shows quotes and escape characters, good for debugging
print(f"{text!a}")   # ascii() - like repr() but escapes non-ASCII chars (é -> \xe9)

# ---------------------------------------------------------------------------
# 4. Debug specifier: {expr=}   (Python 3.8+)
# ---------------------------------------------------------------------------
print("\n--- 4. Debug specifier (=) ---")
x = 10
print(f"{x=}")            # prints: x=10  (expression text AND its value)
print(f"{x * 2=}")        # prints: x * 2=20
print(f"{name=}")         # strings are shown with repr(), so: name='Ada'
print(f"{x = }")          # whitespace around = is preserved: x = 10

# ---------------------------------------------------------------------------
# 5. Format spec: {value:spec}
#    General shape: [[fill]align][sign][#][0][width][grouping][.precision][type]
# ---------------------------------------------------------------------------
print("\n--- 5. Width, alignment and fill ---")
word = "hi"
print(f"[{word:10}]")      # width 10; strings default to left-aligned
print(f"[{word:<10}]")     # < left align
print(f"[{word:>10}]")     # > right align
print(f"[{word:^10}]")     # ^ center
print(f"[{word:*^10}]")    # any character before the align symbol is the fill
print(f"[{42:<8}]")        # numbers default to right-aligned, but you can override
print(f"[{42:08}]")        # leading 0 = zero-pad numbers to width 8

print("\n--- 6. Floats and precision ---")
pi = math.pi
print(f"{pi:.2f}")         # 2 digits after the decimal point: 3.14
print(f"{pi:10.3f}")       # width 10, 3 decimals
print(f"{pi:e}")           # scientific notation
print(f"{pi:.3e}")         # scientific with 3 decimals
print(f"{pi:g}")           # general format: picks the shorter of f / e
print(f"{0.256:.1%}")      # percentage: multiplies by 100 and adds % -> 25.6%
print(f"{'abcdefgh':.3}")  # precision on a string truncates it -> abc

print("\n--- 7. Integers: bases, signs, grouping ---")
n = 255
print(f"{n:d}")            # decimal
print(f"{n:b}")            # binary
print(f"{n:o}")            # octal
print(f"{n:x}")            # hex (lowercase)
print(f"{n:X}")            # hex (uppercase)
print(f"{n:#x}")           # # adds the prefix: 0xff
print(f"{n:#b}")           # 0b11111111
print(f"{n:08b}")          # zero-padded 8-bit binary: 11111111
print(f"{65:c}")           # c = character with that Unicode code point -> A
print(f"{5:+d}")           # + always show sign
print(f"{-5:+d}")
print(f"{5: d}")           # space = leading space for positives, '-' for negatives
big = 1234567890
print(f"{big:,}")          # comma thousands separator
print(f"{big:_}")          # underscore separator (also works with b/o/x groups of 4)
print(f"{big:,.2f}")       # combine grouping with precision -> 1,234,567,890.00
print(f"{0b10110011:_b}")  # 1011_0011

# ---------------------------------------------------------------------------
# 8. Dynamic format specs: nested braces inside the spec
# ---------------------------------------------------------------------------
print("\n--- 8. Dynamic width / precision ---")
width, precision = 12, 4
print(f"[{pi:{width}.{precision}f}]")   # width and precision come from variables
fmt = ">8.1f"
print(f"[{pi:{fmt}}]")                  # you can even store the entire spec in a variable
for label, value in [("apples", 3), ("kiwis", 12), ("watermelons", 105)]:
    print(f"{label:<12}{value:>5}")     # a simple aligned table

# ---------------------------------------------------------------------------
# 9. Dates and times: datetime supports its own format specs (strftime codes)
# ---------------------------------------------------------------------------
print("\n--- 9. Dates ---")
now = datetime.datetime(2024, 3, 9, 14, 5, 30)
print(f"{now}")                          # default str()
print(f"{now:%Y-%m-%d}")                 # 2024-03-09
print(f"{now:%H:%M:%S}")                 # 14:05:30
print(f"{now:%A, %B %d, %Y}")            # Saturday, March 09, 2024
print(f"{now:%I:%M %p}")                 # 12-hour clock with AM/PM

# ---------------------------------------------------------------------------
# 10. Escaping braces and special characters
# ---------------------------------------------------------------------------
print("\n--- 10. Escaping ---")
print(f"Literal braces: {{ and }}")      # double the brace to print one
print(f"Value in braces: {{{x}}}")       # {{ + {x} + }} -> {10}
print(f"Tab:\tNewline follows.\nDone")   # normal escapes work in the literal part
# Before Python 3.12 you could NOT use a backslash inside the {} expression part;
# from 3.12 on it is allowed (and so is reusing the same quote type).

# ---------------------------------------------------------------------------
# 11. Multi-line f-strings
# ---------------------------------------------------------------------------
print("\n--- 11. Multi-line ---")
item, price, qty = "Widget", 4.5, 3
receipt = f"""
Item:  {item}
Price: ${price:.2f}
Qty:   {qty}
Total: ${price * qty:.2f}
"""
print(receipt)

# Adjacent string literals are joined; each piece needs its own f prefix.
msg = (
    f"Hello {name}, "
    f"you are {age}. "
    "This last piece has no f, so {braces} stay literal."
)
print(msg)

# ---------------------------------------------------------------------------
# 12. Raw f-strings (rf"...") - backslashes are not treated as escapes
# ---------------------------------------------------------------------------
print("\n--- 12. Raw f-strings ---")
folder = "Notes"
print(rf"C:\Users\whuds\{folder}\file.txt")   # \U, \w etc. stay as typed

# ---------------------------------------------------------------------------
# 13. Objects and custom formatting with __format__
# ---------------------------------------------------------------------------
print("\n--- 13. Custom objects ---")


class Point:
    def __init__(self, x, y):
        self.x, self.y = x, y

    def __str__(self):                     # used by {p} and {p!s}
        return f"Point({self.x}, {self.y})"

    def __repr__(self):                    # used by {p!r}
        return f"Point(x={self.x!r}, y={self.y!r})"

    def __format__(self, spec):            # used by {p:spec}; spec is the text after ':'
        if spec == "polar":
            r = math.hypot(self.x, self.y)
            theta = math.degrees(math.atan2(self.y, self.x))
            return f"(r={r:.2f}, theta={theta:.1f}°)"
        return str(self)                   # fall back to the default


p = Point(3, 4)
print(f"{p}")           # __str__
print(f"{p!r}")         # __repr__
print(f"{p:polar}")     # __format__ with spec='polar'
print(f"{p.x} and {p.y}")   # attribute access works like any expression

# ---------------------------------------------------------------------------
# 14. Other handy tricks
# ---------------------------------------------------------------------------
print("\n--- 14. Misc ---")
print(f"{'nested ' + f'{name}'}")                  # f-strings can nest inside expressions
print(f"{(lambda v: v * 2)(21)}")                  # lambdas need parentheses
print(f"{1_000_000:,}")                            # underscores in literals are fine
print(f"{True!s:>6}|{None!s:<6}|")                 # flags and specs combine: !conv first, then :spec
items = ["a", "b", "c"]
print(f"Joined: {', '.join(items)}")               # join a list in place
print(f"{len(items) = }")                          # debug specifier on an expression

# ---------------------------------------------------------------------------
# 15. Performance / comparison note
# ---------------------------------------------------------------------------
# f-strings are usually the fastest and most readable option compared to:
#   "Hello %s" % name          (old printf-style)
#   "Hello {}".format(name)    (str.format)
# Use str.format or % only when the template must be stored/reused separately
# from the values (e.g. translations, logging config); f-strings are evaluated
# immediately where they are written.
print("\n--- 15. Comparison ---")
print("%s is %d" % (name, age))
print("{} is {}".format(name, age))
print(f"{name} is {age}")
