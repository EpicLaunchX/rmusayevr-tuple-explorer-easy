from src.pytemplate.entrypoints.cli.main import access_element, display_tuple, get_items, slice_tuple


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


def test_slice_tuple_out_of_range():
    # Test slice_tuple with out-of-range indices
    test_tuple = ("a", "b", "c")
    result = slice_tuple(test_tuple, 0, 10)
    expected = "Error: Indices [0:10] are out of range for a tuple of length 3."
    assert result == expected, f"Unexpected message: {result}"


def test_slice_tuple_negative_index():
    # Test slice_tuple with valid negative indices
    test_tuple = ("a", "b", "c", "d")
    result = slice_tuple(test_tuple, 1, 3)
    expected = ("b", "c")
    assert result == expected, f"Expected {expected}, but got {result}"
