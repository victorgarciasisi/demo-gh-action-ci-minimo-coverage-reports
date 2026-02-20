"""Demo repo para cobertura y reports en CI.

La idea es tener una función con ramas para que coverage muestre líneas no cubiertas.
"""

from __future__ import annotations


def classify_age(age: int) -> str:
    """Clasifica una edad.

    - age < 0: error
    - 0..17: minor
    - 18..64: adult
    - 65+: senior
    """

    if age < 0:
        raise ValueError("age must be >= 0")

    if age < 18:
        return "minor"

    if age < 65:
        return "adult"

    return "senior"


def safe_divide(a: float, b: float) -> float:
    """Divide a entre b.

    A propósito, contiene un caso que no se testea al principio para ilustrar cobertura.
    """

    if b == 0:
        return 0.0

    return a / b
