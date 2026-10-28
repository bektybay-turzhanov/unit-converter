
import unittest
from main import convert_value


class TestConverter(unittest.TestCase):
    def test_kilometers_to_meters(self):
        self.assertEqual(
            convert_value(2, "Расстояние", "Километры", "Метры"),
            2000
        )

    def test_kilograms_to_grams(self):
        self.assertEqual(
            convert_value(3, "Масса", "Килограммы", "Граммы"),
            3000
        )

    def test_celsius_to_fahrenheit(self):
        self.assertEqual(
            convert_value(20, "Температура", "Цельсий", "Фаренгейт"),
            68
        )

    def test_same_temperature_units(self):
        self.assertEqual(
            convert_value(20, "Температура", "Цельсий", "Цельсий"),
            20
        )

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(
            convert_value(68, "Температура", "Фаренгейт", "Цельсий"),
            20
        )


if __name__ == "__main__":
    unittest.main()
