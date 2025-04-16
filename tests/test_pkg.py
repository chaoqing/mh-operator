import mh_operator


def test_version_variable():
    """
    Test that the top-level 'version' variable exists and is a string.
    """
    assert isinstance(mh_operator.version, str)
    assert mh_operator.version == mh_operator.get_version()


def test_main():
    from mh_operator.__main__ import app
