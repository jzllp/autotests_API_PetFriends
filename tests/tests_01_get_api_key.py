from api import PetFriends
from settings import valid_email, valid_password, caps_email, mix_caps_email, without_specifying_the_mail_domain, \
    showing_only_the_mail_domain, invalid_email, invalid_password, empty_email_value, empty_password_value, \
    caps_password, invalid_password_1, invalid_password_2, invalid_email_2

pf = PetFriends()


def test_get_api_key_01(email=valid_email, password=valid_password):
    """Get an API key with a valid email and password.
    Check status code 200. Checking the successful receipt of the key"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result


def test_get_api_key_02(email=caps_email, password=valid_password):
    """Get an API key with a valid email and password. Email in upper case"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result


def test_get_api_key_03(email=mix_caps_email, password=valid_password):
    """Get an API key with a valid email and password. An email with a mix of upper and lower case"""

    status, result = pf.get_api_key(email, password)

    assert status == 200
    assert 'key' in result


def test_get_api_key_04(email=without_specifying_the_mail_domain, password=valid_password):
    """Get an API key with invalid email and valid password. Without specifying the mail domain"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_05(email=showing_only_the_mail_domain, password=valid_password):
    """Get an API key with invalid email and valid password. Showing only the mail domain"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_06(email=invalid_email, password=valid_password):
    """Get an API key with invalid email and valid password"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_07(email=invalid_email, password=invalid_password):
    """Get an API key with invalid email and password"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_08(email=empty_email_value, password=valid_password):
    """Get an API key with invalid email and valid password. An empty email value"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_09(email=invalid_email_2, password=valid_password):
    """Get an API key with invalid email and valid password. Email with two dots before 'ru'"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_10(email=empty_email_value, password=empty_password_value):
    """Get an API key with invalid email and password. An empty email and password value"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_11(email=valid_email, password=empty_password_value):
    """Get an API key with invalid password and valid email. An empty password value"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_12(email=valid_email, password=invalid_password):
    """Get an API key with valid email and invalid password."""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_13(email=valid_email, password=caps_password):
    """Get an API key with valid email and invalid password. Password in upper case"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_14(email=valid_email, password=invalid_password_1):
    """Get an API key with valid email and invalid password. Password in Latin letters in lowercase"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result


def test_get_api_key_15(email=valid_email, password=invalid_password_2):
    """Get an API key with valid email and invalid password. Password in Latin letters in upper case"""

    status, result = pf.get_api_key(email, password)

    assert status == 403
    assert 'key' not in result
