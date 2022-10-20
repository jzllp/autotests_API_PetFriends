from api import PetFriends
from settings import valid_email, valid_password, invalid_auth_key, empty_auth_key

pf = PetFriends()


def test_get_all_pets_01(filter=''):
    """Authorization. Request a list of all pets.
    Check status code 200. Checking that a query for all pets returns a non-empty list"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_get_all_my_pets_02(filter='my_pets'):
    """Request a list of my pets. Applying a filter='my_pets'.
Checking that the number of pets in my list is different from the number in the list of all pets"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)
    status_all_pets, result_all_pets = pf.get_list_of_pets(auth_key, filter='')

    assert status == 200
    assert status_all_pets == 200
    assert len(result_all_pets['pets']) != len(result['pets'])


def test_get_all_pets_03(filter=''):
    """Request a list of all pets with an invalid key"""

    status, result = pf.get_list_of_pets(invalid_auth_key, filter)

    assert status == 403
    assert 'pets' not in result


def test_get_all_my_pets_04(filter='my_pets'):
    """Request a list of all my pets with an invalid key. Applying a filter='my_pets'."""

    status, result = pf.get_list_of_pets(invalid_auth_key, filter)

    assert status == 403
    assert 'pets' not in result


def test_get_all_pets_05(filter=''):
    """Request a list of all pets with an empty key"""

    status, result = pf.get_list_of_pets(empty_auth_key, filter)

    assert status == 403
    assert 'pets' not in result


def test_get_all_my_pets_06(filter='my_pets'):
    """Request a list of all my pets with an empty key. Applying a filter='my_pets'."""

    status, result = pf.get_list_of_pets(empty_auth_key, filter)

    assert status == 403
    assert 'pets' not in result


def test_get_pets_07(filter='pets'):
    """Request a list of all my pets with an invalid filter"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 400
    assert 'pets' not in result


def test_get_pets_08(filter=' '):
    """Request a list of all my pets with a 'space' filter parameter"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 400
    assert 'pets' not in result
