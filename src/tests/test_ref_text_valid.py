from package.reference_text import read_text_from_user, clean_inp_text


def test_read_text_from_user():
    assert read_text_from_user() > 0


def test_clean_inp_text():
    assert clean_inp_text() > 0

