from api import PetFriends
from settings import valid_email, valid_password, invalid_auth_key, empty_auth_key, invalid_id, empty_id

pf = PetFriends()


def test_update_information_about_pet_01(name='Rock', animal_type='Scottish', age='5'):
    """Update information about pet. Successfully updated the fields name, breed, age of my pet.
    Check status code 200. Checking that all fields have been updated"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    """Adding a pet without a photo"""
    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_02(name='ROCK', animal_type='Scottish', age='5'):
    """Update information about pet. Adding information to the uppercase name field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_03(name='rock', animal_type='Scottish', age='5'):
    """Update information about pet. Adding information to the name field in lowercase"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_04(name='рок', animal_type='Scottish', age='5'):
    """Update information about pet. Adding information to the name field in Cyrillic"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_05(name='羅恩', animal_type='Scottish', age='5'):
    """Update information about pet. Adding Chinese characters to the name field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_06(name='😇', animal_type='Scottish', age='5'):
    """Update information about pet. Adding an emoji to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_07(name='', animal_type='Scottish', age='5'):
    """Update information about pet. Adding an empty value to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_08(name=' ', animal_type='Scottish', age='5'):
    """Update information about pet. Adding only a space to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_09(name='122', animal_type='Scottish', age='5'):
    """Update information about pet. Adding three digits to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_10(name='Rock122', animal_type='Scottish', age='5'):
    """Update information about pet. Adding numbers and Latin letters to the name field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_11(name='R-o-c-k', animal_type='Scottish', age='5'):
    """Update information about pet. Adding information to the name field in Latin letters with a hyphen"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_12(name='!@#$%^&*()_+{}[];,./*-', animal_type='Scottish', age='5'):
    """Update information about pet. Adding Information to the name Field with Special Characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_13(name='R', animal_type='Scottish', age='5'):
    """Update information about pet. Adding one latin letter to the name field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_14(name='Ro' * 128, animal_type='Scottish', age='5'):
    """Update information about pet. Adding information to the name field 256 characters"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_15(name='Roc' * 334, animal_type='Scottish', age='5'):
    """Update information about pet. Adding information to the name field in 1002 characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_16(name='-1', animal_type='Scottish', age='5'):
    """Update information about pet. Adding a negative number to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_17(name='0', animal_type='Scottish', age='5'):
    """Update information about pet. Adding a zero character to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_18(name='0.8', animal_type='Scottish', age='5'):
    """Update information about pet. Adding a floating point number to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_19(name=' Rock', animal_type='Scottish', age='5'):
    """Update information about pet.
    Adding information to the name field with a space at the beginning of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_20(name='Rock ', animal_type='Scottish', age='5'):
    """Update information about pet.
    Adding information to the name field with a space at the end of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_21(name='Rock', animal_type='SCOTTISH', age='5'):
    """Update information about pet. Adding information to the uppercase breed field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_22(name='Rock', animal_type='scottish', age='5'):
    """Update information about pet. Adding information to the breed field in lowercase"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_23(name='Rock', animal_type='Шотландский', age='5'):
    """Update information about pet. Adding information to the breed field in Cyrillic"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_24(name='Rock', animal_type='英國', age='5'):
    """Update information about pet. Adding Chinese characters to the breed field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_25(name='Rock', animal_type='😇', age='5'):
    """Update information about pet. Adding an emoji to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_26(name='Rock', animal_type='', age='5'):
    """Update information about pet. Adding an empty value to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_27(name='Rock', animal_type=' ', age='5'):
    """Update information about pet. Adding only a space to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_28(name='Rock', animal_type='123', age='5'):
    """Update information about pet. Adding three digits to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_29(name='Rock', animal_type='Scottish55', age='5'):
    """Update information about pet. Adding numbers and Latin letters to the breed field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_30(name='Rock', animal_type='S-c-o-t-t-i-s-h', age='5'):
    """Update information about pet. Adding information to the breed field in Latin letters with a hyphen"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_31(name='Rock', animal_type='!@#$%^&*()_+{}[];,./*-', age='5'):
    """Update information about pet. Adding Information to the breed Field with Special Characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_32(name='Rock', animal_type='S', age='5'):
    """Update information about pet. Adding one latin letter to the breed field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_33(name='Rock', animal_type='Sc' * 128, age='5'):
    """Update information about pet. Adding information to the breed field 256 characters"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_34(name='Rock', animal_type='Sco' * 334, age='5'):
    """Update information about pet. Adding information to the breed field in 1002 characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_35(name='Rock', animal_type='-1', age='5'):
    """Update information about pet. Adding a negative number to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_36(name='Rock', animal_type='0', age='5'):
    """Update information about pet. Adding a zero character to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_37(name='Rock', animal_type='0.8', age='5'):
    """Update information about pet. Adding a floating point number to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_38(name='Rock', animal_type=' Scottish', age='5'):
    """Update information about pet.
    Adding information to the breed field with a space at the beginning of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_39(name='Rock', animal_type='Scottish ', age='5'):
    """Update information about pet.
    Adding information to the breed field with a space at the end of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_40(name='Rock', animal_type='Scottish', age='two'):
    """Update information about pet. Adding three latin characters to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_41(name='Rock', animal_type='Scottish', age='два'):
    """Update information about pet. Adding information to the age field in Cyrillic.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_42(name='Rock', animal_type='Scottish', age='二'):
    """Update information about pet. Adding Chinese characters to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_43(name='Rock', animal_type='Scottish', age='😇'):
    """Update information about pet. Adding an emoji to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_44(name='Rock', animal_type='Scottish', age=''):
    """Update information about pet. Adding an empty value to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_45(name='Rock', animal_type='Scottish', age=' '):
    """Update information about pet. Adding only a space to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_46(name='Rock', animal_type='Scottish', age='321'):
    """Update information about pet. Adding three digits to the age field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_47(name='Rock', animal_type='Scottish', age='ag2'):
    """Update information about pet. Adding numbers and Latin letters to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_48(name='Rock', animal_type='Scottish', age='2-2'):
    """Update information about pet. Adding numbers and a hyphen to the age input field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_49(name='Rock', animal_type='Scottish', age='!"№'):
    """Update information about pet. Adding Information to the age Field with Special Characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_50(name='Rock', animal_type='Scottish', age='22'):
    """Update information about pet. Adding two digits to the age input field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_51(name='Rock', animal_type='Scottish', age='22' * 128):
    """Update information about pet. Adding 256 digits to the age input field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_52(name='Rock', animal_type='Scottish', age='123' * 334):
    """Update information about pet. Adding 1002 digits to the age input field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_53(name='Rock', animal_type='Scottish', age='-2'):
    """Update information about pet. Adding a negative number to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_54(name='Rock', animal_type='Scottish', age='0'):
    """Update information about pet. Adding a zero character to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_55(name='Rock', animal_type='Scottish', age='0.8'):
    """Update information about pet. Adding a floating point number to the age field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_56(name='Rock', animal_type='Scottish', age='0.88'):
    """Update information about pet.
    Adding a floating point number with two digits to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_57(name='Rock', animal_type='Scottish', age=' 2'):
    """Update information about pet.
    Adding information to the age field with a space at the beginning of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_58(name='Rock', animal_type='Scottish', age='2 '):
    """Update information about pet.
    Adding information to the age field with a space at the end of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_59(name='Rock', animal_type='Scottish', age='2'):
    """Update information about pet.
    Changing information in the field name, breed, age of the second pet from the list of pets"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")
    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_update_information_about_pet_60(name='Rock', animal_type='Scottish', age='2'):
    """Update information about pet. Changing information in the field name,
    breed, age of a pet with an invalid pet id"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, invalid_id, name, animal_type, age)

    assert status == 400
    assert invalid_id not in str(my_pets)
    assert my_pets['pets'][0]['name'] == "Ron"
    assert my_pets['pets'][0]['animal_type'] == "British"
    assert my_pets['pets'][0]['age'] == "2"


def test_update_information_about_pet_61(name='Rock', animal_type='Scottish', age='2'):
    """Update information about pet. Update information in the input field name, breed, age of a pet with a valid ID,
    at the beginning of the line of which there is a space."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    space_pet_id = ' ' + my_pets['pets'][0]['id']
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, space_pet_id, name, animal_type, age)

    assert status == 400
    assert pet_id in str(my_pets)
    assert my_pets['pets'][0]['name'] == "Ron"
    assert my_pets['pets'][0]['animal_type'] == "British"
    assert my_pets['pets'][0]['age'] == "2"


def test_update_information_about_pet_62(name='Rock', animal_type='Scottish', age='2'):
    """Update information about pet. Update information in the input field name, breed, age of a pet with a valid ID,
     at the end of the line of which there is a space."""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = my_pets['pets'][0]['id']
    space_pet_id = my_pets['pets'][0]['id'] + ' '
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, space_pet_id, name, animal_type, age)

    assert status == 400
    assert pet_id in str(my_pets)
    assert my_pets['pets'][0]['name'] == "Ron"
    assert my_pets['pets'][0]['animal_type'] == "British"
    assert my_pets['pets'][0]['age'] == "2"


def test_update_information_about_pet_63(name='Rock', animal_type='Scottish', age='2'):
    """Update information about pet. Changing information in the field name,
    breed, age of a pet with an empty pet id"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.update_pet_info(auth_key, empty_id, name, animal_type, age)

    assert status == 400
    assert invalid_id not in str(my_pets)
    assert my_pets['pets'][0]['name'] == "Ron"
    assert my_pets['pets'][0]['animal_type'] == "British"
    assert my_pets['pets'][0]['age'] == "2"


def test_update_information_about_pet_64(name='Rock', animal_type='Scottish', age='5'):
    """Update information about pet. Update the fields name, breed, age of my pet with an invalid key"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(invalid_auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 403
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_65(name='Rock', animal_type='Scottish', age='5'):
    """Update information about pet. Update the fields name, breed, age of my pet with an empty key"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    pf.add_new_pet_without_photo(auth_key, "Ron", "British", "2")

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    status, result = pf.update_pet_info(empty_auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 403
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_update_information_about_pet_66(name='Rock', animal_type='Scottish', age='5'):
    """Update information about pet. Update the field name, breed, age of a pet not from my list"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)

    _, all_pets = pf.get_list_of_pets(auth_key, "")
    status, result = pf.update_pet_info(auth_key, all_pets['pets'][0]['id'], name, animal_type, age)

    assert status == 400
    assert all_pets['pets'][0]['id'] in str(all_pets)
    assert all_pets['pets'][0]['name'] != "Rock"
    assert all_pets['pets'][0]['animal_type'] != "Scottish"
    assert all_pets['pets'][0]['age'] != "5"
