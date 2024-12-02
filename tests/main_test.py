from src.pytemplate.entrypoints.cli.main import access_element, display_tuple, get_items


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


def test_access_element_valid():
    # Test access_element with a valid index
    test_tuple = ("a", "b", "c")
    result = access_element(test_tuple, 1)
    assert result == "b", f"Expected 'b', but got {result}"


def test_access_element_invalid():
    # Test access_element with an out-of-range index
    test_tuple = ("a", "b", "c")
    result = access_element(test_tuple, 5)
    assert result == "Error: Index 5 is out of range.", f"Unexpected message: {result}"


def test_access_element_negative_index():
    # Test access_element with a negative index
    test_tuple = ("a", "b", "c")
    result = access_element(test_tuple, -1)
    assert result == "c", f"Expected 'c', but got {result}"
