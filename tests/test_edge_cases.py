"""Challenge 1: Advanced edge-case tests for parse_guess.

Each test feeds an input that could plausibly break the game and confirms
parse_guess handles it gracefully: it returns ok=False with a helpful message
instead of crashing or accepting an invalid guess.
"""

from logic_utils import parse_guess

# The game's "Normal" difficulty range.
LOW, HIGH = 1, 100


def test_negative_number_is_rejected():
    # Edge case: a negative number is a valid integer but outside the range.
    ok, value, error = parse_guess("-5", LOW, HIGH)
    assert ok is False
    assert value is None
    assert "range" in error.lower()


def test_decimal_is_rejected():
    # Edge case: a decimal must not be silently truncated into a valid guess.
    ok, value, error = parse_guess("33.6", LOW, HIGH)
    assert ok is False
    assert value is None
    assert "whole number" in error.lower()


def test_extremely_large_value_is_rejected():
    # Edge case: a huge number should be out of range, not accepted or crash.
    ok, value, error = parse_guess("999999999999", LOW, HIGH)
    assert ok is False
    assert value is None
    assert "range" in error.lower()


def test_boundaries_are_accepted():
    # Sanity check: the exact edges of the range are still valid guesses.
    assert parse_guess(str(LOW), LOW, HIGH) == (True, LOW, None)
    assert parse_guess(str(HIGH), LOW, HIGH) == (True, HIGH, None)
