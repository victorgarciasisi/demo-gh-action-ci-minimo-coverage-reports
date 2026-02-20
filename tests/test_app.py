import unittest

from app import classify_age, safe_divide


class TestApp(unittest.TestCase):
    def test_classify_age_minor(self) -> None:
        self.assertEqual(classify_age(3), "minor")

    def test_classify_age_adult(self) -> None:
        self.assertEqual(classify_age(30), "adult")

    def test_classify_age_senior(self) -> None:
        self.assertEqual(classify_age(80), "senior")

    def test_safe_divide_normal(self) -> None:
        self.assertEqual(safe_divide(10.0, 2.0), 5.0)

    # Nota: dejamos sin testear el caso b == 0 para que coverage marque líneas sin cubrir.
