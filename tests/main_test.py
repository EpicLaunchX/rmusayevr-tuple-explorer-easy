from src.pytemplate.entrypoints.cli.main import display_tuple, get_items


def test_get_items(monkeypatch, capsys):
    # Simulate user input
    user_input = "apple,banana,cherry"
    monkeypatch.setattr("builtins.input", lambda _: user_input)

    # Call the function and get the result
    result = get_items()

    # Assert the result is as expected
    expected = ("apple", "banana", "cherry")
    assert result == expected, f"Expected {expected}, but got {result}"

    # Capture and assert the printed output
    captured = capsys.readouterr()
    assert "The tuple is: ('apple', 'banana', 'cherry')" in captured.out


def test_display_tuple(capsys):
    # Test the display_tuple function directly
    test_tuple = ("x", "y", "z")
    display_tuple(test_tuple)

    # Capture and assert the printed output
    captured = capsys.readouterr()
    assert "The tuple is: ('x', 'y', 'z')" in captured.out
