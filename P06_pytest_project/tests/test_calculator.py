from calculator import Calculator 
import pytest

class TestCalculator:
    def test_add(self):
        # arrange
        a = 4321
        b = 1234
        cal = Calculator()

        # act
        result = cal.add(a, b)

        # assert
        expected = 5555
        assert result == expected


    def test_subtract(self):
        # arrange
        a = 2
        b = 2
        cal = Calculator()

        # act
        result = cal.subtract(a, b)

        # assert
        expected = 4
        assert result == expected


    def test_multiply(self):
        # arrange
        a = -1
        b = -2
        cal = Calculator()

        # act
        result = cal.multiply(a, b)

        # assert
        expected = 2
        assert result == expected


    def test_divide(self):
        # arrange
        a = 10
        b = 5
        cal = Calculator()

        # act
        with pytest.raises(ZeroDivisionError, match = "Division by zero error"):
            cal.divide(a, b)

            result = cal.divide(a, b)

            # assert
            expected = 2
            assert result == expected


