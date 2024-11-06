import pytest
from func import es_primo

class TestEsPrimo:
    # Test for prime numbers
    def test_returns_true_for_prime_numbers(self):
        assert es_primo(2) is True
        assert es_primo(3) is True
        assert es_primo(5) is True
        assert es_primo(7) is True
        assert es_primo(104729) is True  # Large prime number

    # Test for non-prime numbers
    def test_returns_false_for_non_prime_numbers(self):
        assert es_primo(4) is False
        assert es_primo(6) is False
        assert es_primo(8) is False
        assert es_primo(9) is False
        assert es_primo(1000000) is False  # Large non-prime number

    # Test for numbers less than 2
    def test_returns_false_for_numbers_less_than_2(self):
        assert es_primo(0) is False
        assert es_primo(1) is False
        assert es_primo(-1) is False
        assert es_primo(-10) is False

    # Test for non-integer inputs
    @pytest.mark.parametrize("non_integer", [2.3, 3.9, "tres", None, True, False])
    def test_raises_typeerror_for_non_integer_inputs(self, non_integer):
        with pytest.raises(TypeError):
            es_primo(non_integer)

    # Test for perfect squares
    def test_handles_perfect_squares(self):
        assert es_primo(4) is False
        assert es_primo(9) is False
        assert es_primo(16) is False
        assert es_primo(25) is False
        assert es_primo(36) is False

    # Test for smallest prime number
    def test_handles_smallest_prime_number(self):
        assert es_primo(2) is True

    # Test for smallest non-prime number
    def test_returns_false_for_smallest_non_prime_number(self):
        assert es_primo(4) is False
 # Test for unusual inputs
    @pytest.mark.parametrize("unusual_input", ["cinco", None, [], 2.3, 3.9])
    def test_raises_typeerror_for_unusual_inputs(self, unusual_input):
        with pytest.raises(TypeError):
            es_primo(unusual_input)

 # Test for floating-point numbers close to integers
    @pytest.mark.parametrize("num, expected", [
        (19.000000000000004, True),
        (23.000000000000004, True),
        (18.999999999999996, True),  # Adjusted to True because it rounds to 19
        (22.999999999999996, True)   # Adjusted to True because it rounds to 23
    ])
    def test_handles_floating_point_numbers_close_to_integers(self, num, expected):
        assert es_primo(num) == expected, f"Error: {num} (punto flotante) falló en devolver {expected}"
        
    # Test for prime numbers
    def test_returns_true_for_prime_numbers(self):
        assert es_primo(2) is True
        assert es_primo(3) is True
        assert es_primo(5) is True
        assert es_primo(7) is True
        assert es_primo(104729) is True  # Large prime number

    # Test for non-prime numbers
    def test_returns_false_for_non_prime_numbers(self):
        assert es_primo(4) is False
        assert es_primo(6) is False
        assert es_primo(8) is False
        assert es_primo(9) is False
        assert es_primo(1000000) is False  # Large non-prime number

    # Test for numbers less than 2
    def test_returns_false_for_numbers_less_than_2(self):
        assert es_primo(0) is False
        assert es_primo(1) is False
        assert es_primo(-1) is False
        assert es_primo(-10) is False

