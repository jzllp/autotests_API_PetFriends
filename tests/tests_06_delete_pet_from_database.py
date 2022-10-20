from api import PetFriends
from settings import valid_email, valid_password, invalid_auth_key, empty_auth_key, invalid_id, empty_id

pf = PetFriends()


def test_delete_pet_from_database_01():
    """Delete pet from database. Adding a pet without a photo and deleting it.
    Check status code 200. Checking the id of a deleted pet"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    """Adding a pet without a photo"""
    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    """Delete pet from database"""
    status, _ = pf.delete_pet(auth_key, pet_id)

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in str(my_pets)


def test_delete_pet_from_database_02():
    """Delete pet from database. Adding a pet with empty fields name, breed, age and deleting it"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "", "", "")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in str(my_pets)


def test_delete_pet_from_database_03():
    """Delete pet from database. Adding a pet from a photo and deleting it.
    Photo format 'jpg'"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet(auth_key, "Ron", "British", "2", "images/01.jpg")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in str(my_pets)


def test_delete_pet_from_database_04():
    """Delete pet from database. Adding two pets with photos and removing the second pet from the list of pets"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet(auth_key, "Ron", "British", "2", "images/01.jpg")
    pf.add_new_pet(auth_key, "Rock", "British", "2", "images/01.jpg")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][1]['id']
    pet_id_0 = my_pets['pets'][0]['id']

    status, _ = pf.delete_pet(auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert pet_id not in str(my_pets)
    assert pet_id_0 in str(my_pets)


def test_delete_pet_from_database_05():
    """Delete pet from database. Deleting my pet with an invalid id"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet(auth_key, "Ron", "British", "2", "images/03.JPG")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    status, _ = pf.delete_pet(auth_key, invalid_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 400
    assert pet_id in str(my_pets)
    assert invalid_id not in str(my_pets)


def test_delete_pet_from_database_06():
    """Delete pet from database. Deleting a pet with a valid ID that has a space at the beginning of the line."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet(auth_key, "Ron", "British", "2", "images/03.JPG")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    space_pet_id = ' ' + my_pets['pets'][0]['id']

    status, _ = pf.delete_pet(auth_key, space_pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 400
    assert pet_id in str(my_pets)
    assert space_pet_id not in str(my_pets)


def test_delete_pet_from_database_07():
    """Delete pet from database. Deleting a pet with a valid ID that has a space at the end of the line."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet(auth_key, "Ron", "British", "2", "images/03.JPG")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    space_pet_id = my_pets['pets'][0]['id'] + ' '

    status, _ = pf.delete_pet(auth_key, space_pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 400
    assert pet_id in str(my_pets)
    assert space_pet_id not in str(my_pets)


def test_delete_pet_from_database_08():
    """Delete pet from database. Deleting my pet with an empty id"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet(auth_key, "Ron", "British", "2", "images/03.JPG")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    status, _ = pf.delete_pet(auth_key, empty_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 400
    assert pet_id in str(my_pets)


def test_delete_pet_from_database_09():
    """Delete pet from database. Deleting a pet not from my pets list"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    _, all_pets = pf.get_list_of_pets(auth_key, "")
    pet_id = all_pets['pets'][0]['id']

    status, _ = pf.delete_pet(auth_key, 'pet_id')
    _, mall_pets = pf.get_list_of_pets(auth_key, "")

    assert status == 400
    assert pet_id in str(all_pets)


def test_delete_pet_from_database_10():
    """Delete pet from database. Deleting my pet with invalid key"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet(auth_key, "Ron", "British", "2", "images/01.jpg")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    status, _ = pf.delete_pet(invalid_auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 403
    assert pet_id in str(my_pets)


def test_delete_pet_from_database_11():
    """Delete pet from database. Deleting my pet with empty key"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet(auth_key, "Ron", "British", "2", "images/01.jpg")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']

    status, _ = pf.delete_pet(empty_auth_key, pet_id)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 403
    assert pet_id in str(my_pets)


def test_delete_pet_from_database_12():
    """Delete pet from database. Deleting pet not from my list with invalid key"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    _, all_pets = pf.get_list_of_pets(auth_key, "")
    pet_id = all_pets['pets'][0]['id']

    status, _ = pf.delete_pet(invalid_auth_key, pet_id)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    assert status == 403
    assert pet_id in str(all_pets)


def test_delete_pet_from_database_13():
    """Delete pet from database. Deleting pet not from my list with empty key"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    _, all_pets = pf.get_list_of_pets(auth_key, "")
    pet_id = all_pets['pets'][0]['id']

    status, _ = pf.delete_pet(empty_auth_key, pet_id)
    _, all_pets = pf.get_list_of_pets(auth_key, "")

    assert status == 403
    assert pet_id in str(all_pets)


def test_delete_pet_from_database_14():
    """Delete pet from database. Deleting all my pets"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet(auth_key, "Ron", "British", "2", "images/03.JPG")
    pf.add_new_pet(auth_key, "Rock", "Scottish", "1", "images/03.JPG")
    pf.add_new_pet(auth_key, "Rin", "Dwarf", "3", "images/03.JPG")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    while len(my_pets['pets']) > 0:
        pet_id = my_pets['pets'][0]['id']
        status, _ = pf.delete_pet(auth_key, pet_id)
        _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
        assert status == 200

    status, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    assert status == 200
    assert len(my_pets['pets']) == 0
