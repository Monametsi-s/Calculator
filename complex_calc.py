"""lab1_complex.py

Simple complex-number calculator module with functions suitable for unit testing.

Usage (CLI):
  python lab1_complex.py add "1+2j" "3-4j"
  python lab1_complex.py mul "2+3i" "4"   # 'i' is accepted as well as 'j'
"""
from __future__ import annotations
import argparse
from typing import Callable, Dict


def parse_complex(s: str) -> complex:
    """Parse a string into a complex number.

    Accepts forms Python's complex() accepts, and also allows 'i' as the
    imaginary unit (e.g. "1+2i").
    """
    if not isinstance(s, str):
        raise TypeError("parse_complex expects a string")
    s = s.strip().lower().replace(" ", "")
    # allow 'i' as imaginary unit by replacing with 'j'
    s = s.replace("i", "j")
    try:
        return complex(s)
    except ValueError as exc:
        raise ValueError(f"cannot parse complex number from '{s}'") from exc


def cadd(a: complex, b: complex) -> complex:
    return a + b


def csub(a: complex, b: complex) -> complex:
    return a - b


def cmul(a: complex, b: complex) -> complex:
    return a * b


def cdiv(a: complex, b: complex) -> complex:
    if b == 0:
        # Let Python raise the natural ZeroDivisionError for consistency,
        # but keep an explicit check for clearer semantics.
        raise ZeroDivisionError("complex division by zero")
    return a / b


_OPERATIONS: Dict[str, Callable[[complex, complex], complex]] = {
    "add": cadd,
    "sub": csub,
    "mul": cmul,
    "div": cdiv,
}


def format_complex(c: complex) -> str:
    """Return a compact string for a complex number.

    Examples:
      (3+0j) -> "3+0j"
      (1+2j) -> "1+2j"
      (0-3j) -> "-3j"
    """
    # Use Python's built-in str for simplicity; that's fine for CLI output.
    return str(c)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Simple complex-number calculator")
    parser.add_argument("op", choices=_OPERATIONS.keys(), help="operation (add, sub, mul, div)")
    parser.add_argument("a", help="first operand (e.g. '1+2j' or '3' or '4-2i')")
    parser.add_argument("b", help="second operand")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    a = parse_complex(args.a)
    b = parse_complex(args.b)
    func = _OPERATIONS[args.op]
    result = func(a, b)
    print(format_complex(result))


if __name__ == "__main__":
    main()
