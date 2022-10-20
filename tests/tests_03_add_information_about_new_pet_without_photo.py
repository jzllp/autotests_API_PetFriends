from api import PetFriends
from settings import valid_email, valid_password, invalid_auth_key, empty_auth_key

pf = PetFriends()


def test_add_new_pet_without_photo_01(name='Ron', animal_type='British', age='2'):
    """Add information about new pet without photo. Check status code 200.
    Checking the successful addition of a new pet with the filled fields name, breed, age"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_02(name='RON', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding information to the uppercase name field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_03(name='ron', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding information to the name field in lowercase"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_04(name='рон', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding information to the name field in Cyrillic"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_05(name='羅恩', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding Chinese characters to the name field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_06(name='😇', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding an emoji to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_07(name='', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding an empty value to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_08(name=' ', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding only a space to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_09(name='122', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding three digits to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_10(name='Ron122', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding numbers and Latin letters to the name field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_11(name='R-o-n', animal_type='British', age='2'):
    """Add information about new pet without photo.
    Adding information to the name field in Latin letters with a hyphen"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_12(name='!@#$%^&*()_+{}[];,./*-', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding Information to the name Field with Special Characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_13(name='R', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding one latin letter to the name field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_14(name='Ro' * 128, animal_type='British', age='2'):
    """Add information about new pet without photo. Adding information to the name field 256 characters"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_15(name='Ron' * 334, animal_type='British', age='2'):
    """Add information about new pet without photo. Adding information to the name field in 1002 characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_16(name='-1', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding a negative number to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_17(name='0', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding a zero character to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_18(name='0.8', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding a floating point number to the name field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_19(name=' Ron', animal_type='British', age='2'):
    """Add information about new pet without photo.
    Adding information to the name field with a space at the beginning of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_20(name='Ron ', animal_type='British', age='2'):
    """Add information about new pet without photo.
    Adding information to the name field with a space at the end of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_21(name='Ron', animal_type='BRITISH', age='2'):
    """Add information about new pet without photo. Adding information to the uppercase breed field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_22(name='Ron', animal_type='british', age='2'):
    """Add information about new pet without photo. Adding information to the breed field in lowercase"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_23(name='Ron', animal_type='Британский', age='2'):
    """Add information about new pet without photo. Adding information to the breed field in Cyrillic"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_24(name='Ron', animal_type='英國', age='2'):
    """Add information about new pet without photo. Adding Chinese characters to the breed field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_25(name='Ron', animal_type='😇', age='2'):
    """Add information about new pet without photo. Adding an emoji to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_26(name='Ron', animal_type='', age='2'):
    """Add information about new pet without photo. Adding an empty value to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_27(name='Ron', animal_type=' ', age='2'):
    """Add information about new pet without photo. Adding only a space to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_28(name='Ron', animal_type='123', age='2'):
    """Add information about new pet without photo. Adding three digits to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_29(name='Ron', animal_type='British999', age='2'):
    """Add information about new pet without photo. Adding numbers and Latin letters to the breed field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_30(name='Ron', animal_type='B-r-i-t-i-s-h', age='2'):
    """Add information about new pet without photo.
    Adding information to the breed field in Latin letters with a hyphen"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_31(name='Ron', animal_type='!@#$%^&*()_+{}[];,./*-', age='2'):
    """Add information about new pet without photo. Adding Information to the breed Field with Special Characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_32(name='Ron', animal_type='B', age='2'):
    """Add information about new pet without photo. Adding one latin letter to the breed field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_33(name='Ron', animal_type='Br' * 128, age='2'):
    """Add information about new pet without photo. Adding information to the breed field 256 characters"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_34(name='Ron', animal_type='Bri' * 334, age='2'):
    """Add information about new pet without photo. Adding information to the breed field in 1002 characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_35(name='Ron', animal_type='-1', age='2'):
    """Add information about new pet without photo. Adding a negative number to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_36(name='Ron', animal_type='0', age='2'):
    """Add information about new pet without photo. Adding a zero character to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_37(name='Ron', animal_type='0.8', age='2'):
    """Add information about new pet without photo. Adding a floating point number to the breed field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_38(name='Ron', animal_type=' British', age='2'):
    """Add information about new pet without photo.
    Adding information to the breed field with a space at the beginning of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_39(name='Ron', animal_type='British ', age='2'):
    """Add information about new pet without photo.
    Adding information to the breed field with a space at the end of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_40(name='Ron', animal_type='British', age='two'):
    """Add information about new pet without photo. Adding three latin characters to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_41(name='Ron', animal_type='British', age='два'):
    """Add information about new pet without photo. Adding information to the age field in Cyrillic.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_42(name='Ron', animal_type='British', age='二'):
    """Add information about new pet without photo. Adding Chinese characters to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_43(name='Ron', animal_type='British', age='😇'):
    """Add information about new pet without photo. Adding an emoji to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_44(name='Ron', animal_type='British', age=''):
    """Add information about new pet without photo. Adding an empty value to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_45(name='Ron', animal_type='British', age=' '):
    """Add information about new pet without photo. Adding only a space to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_46(name='Ron', animal_type='British', age='123'):
    """Add information about new pet without photo. Adding three digits to the age field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_47(name='Ron', animal_type='British', age='ag2'):
    """Add information about new pet without photo. Adding numbers and Latin letters to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_48(name='Ron', animal_type='British', age='2-2'):
    """Add information about new pet without photo. Adding numbers and a hyphen to the age input field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_49(name='Ron', animal_type='British', age='!"№'):
    """Add information about new pet without photo. Adding Information to the age Field with Special Characters.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_50(name='Ron', animal_type='British', age='22'):
    """Add information about new pet without photo. Adding two digits to the age input field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_51(name='Ron', animal_type='British', age='22' * 128):
    """Add information about new pet without photo. Adding 256 digits to the age input field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_52(name='Ron', animal_type='British', age='123' * 334):
    """Add information about new pet without photo. Adding 1002 digits to the age input field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_53(name='Ron', animal_type='British', age='-2'):
    """Add information about new pet without photo. Adding a negative number to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_54(name='Ron', animal_type='British', age='0'):
    """Add information about new pet without photo. Adding a zero character to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_55(name='Ron', animal_type='British', age='0.8'):
    """Add information about new pet without photo. Adding a floating point number to the age field"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age


def test_add_new_pet_without_photo_56(name='Ron', animal_type='British', age='0.88'):
    """Add information about new pet without photo.
    Adding a floating point number with two digits to the age field.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_57(name='Ron', animal_type='British', age=' 2'):
    """Add information about new pet without photo.
    Adding information to the age field with a space at the beginning of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_58(name='Ron', animal_type='British', age='2 '):
    """Add information about new pet without photo.
    Adding information to the age field with a space at the end of the line.
    Invalid value"""

    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result


def test_add_new_pet_without_photo_59(name='Ron', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding a new pet with an invalid key"""

    status, result = pf.add_new_pet_without_photo(invalid_auth_key, name, animal_type, age)

    assert status == 403
    assert 'name' not in result


def test_add_new_pet_without_photo_60(name='Ron', animal_type='British', age='2'):
    """Add information about new pet without photo. Adding a new pet with an empty key"""

    status, result = pf.add_new_pet_without_photo(empty_auth_key, name, animal_type, age)

    assert status == 403
    assert 'name' not in result
