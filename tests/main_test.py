from src.pytemplate.entrypoints.cli.main import get_items


def test_get_items(monkeypatch):
    # Simulate user input
    user_input = "apple,banana,cherry"
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    # Call the function and get the result
    result = get_items()

    # Assert the result is as expected
    expected = ("apple", "banana", "cherry")
    assert result == expected, f"Expected {expected}, but got {result}"
