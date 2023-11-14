from importlib.machinery import SourceFileLoader

URLify_module = SourceFileLoader("URLify_module", "1.3 URLify.py").load_module()


def test_urlifyV1():
    u = URLify_module.URLifyV1

    # Basic cases
    assert u("Hello World") == "Hello%20World"
    assert u("Python is great") == "Python%20is%20great"

    # Edge cases
    assert u("") == ""  # Empty string remains empty
    assert u("NoSpaces") == "NoSpaces"  # No spaces, no changes
    assert u("  ") == "%20%20"  # Multiple consecutive spaces

    # Spaces at the beginning and end
    assert u("  Hello World  ") == "%20%20Hello%20World%20%20"

    # Special characters and numbers
    assert u("This is 123") == "This%20is%20123"
    assert u("!@#$%^&*()") == "!@#$%^&*()"

    # URL encoding of special characters
    assert u("Hello, world!") == "Hello,%20world!"
    assert u("Space at the end ") == "Space%20at%20the%20end%20"

    # Mix of spaces and other characters
    assert u("a b c d e") == "a%20b%20c%20d%20e"

    # Case sensitivity
    assert u("Case Sensitive") == "Case%20Sensitive"
    assert u("CASE sensitive") == "CASE%20sensitive"


def test_urlifyV2():
    u = URLify_module.URLifyV2

    # Basic cases
    assert u("Hello World") == "Hello%20World"
    assert u("Python is great") == "Python%20is%20great"

    # Edge cases
    assert u("") == ""  # Empty string remains empty
    assert u("NoSpaces") == "NoSpaces"  # No spaces, no changes
    assert u("  ") == "%20%20"  # Multiple consecutive spaces

    # Spaces at the beginning and end
    assert u("  Hello World  ") == "%20%20Hello%20World%20%20"

    # Special characters and numbers
    assert u("This is 123") == "This%20is%20123"
    assert u("!@#$%^&*()") == "!@#$%^&*()"

    # URL encoding of special characters
    assert u("Hello, world!") == "Hello,%20world!"
    assert u("Space at the end ") == "Space%20at%20the%20end%20"

    # Mix of spaces and other characters
    assert u("a b c d e") == "a%20b%20c%20d%20e"

    # Case sensitivity
    assert u("Case Sensitive") == "Case%20Sensitive"
    assert u("CASE sensitive") == "CASE%20sensitive"


def test_urlifyV3():
    u = URLify_module.URLifyV3

    # Basic cases
    assert u("Hello World") == "Hello%20World"
    assert u("Python is great") == "Python%20is%20great"

    # Edge cases
    assert u("") == ""  # Empty string remains empty
    assert u("NoSpaces") == "NoSpaces"  # No spaces, no changes
    assert u("  ") == "%20%20"  # Multiple consecutive spaces

    # Spaces at the beginning and end
    assert u("  Hello World  ") == "%20%20Hello%20World%20%20"

    # Special characters and numbers
    assert u("This is 123") == "This%20is%20123"
    assert u("!@#$%^&*()") == "!@#$%^&*()"

    # URL encoding of special characters
    assert u("Hello, world!") == "Hello,%20world!"
    assert u("Space at the end ") == "Space%20at%20the%20end%20"

    # Mix of spaces and other characters
    assert u("a b c d e") == "a%20b%20c%20d%20e"

    # Case sensitivity
    assert u("Case Sensitive") == "Case%20Sensitive"
    assert u("CASE sensitive") == "CASE%20sensitive"
