from api import PetFriends
from settings import valid_email, valid_password, invalid_auth_key, empty_auth_key
import os

pf = PetFriends()


def test_add_new_pet_with_a_photo_01(name='Ron', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Photo format 'jpg'.
    Check status code 200.
    Checking the successful addition of a new pet with the filled fields name, breed, age.
    Verifying the successful addition of a pet photo"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_02(name='RON', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the uppercase name field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_03(name='ron', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the name field in lowercase"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_04(name='рон', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the name field in Cyrillic"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_05(name='羅恩', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding Chinese characters to the name field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_06(name='😇', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding an emoji to the name field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_07(name='', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding an empty value to the name field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_08(name=' ', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding only a space to the name field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_09(name='122', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding three digits to the name field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_10(name='Ron122', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding numbers and Latin letters to the name field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_11(name='R-o-n', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo.
    Adding information to the name field in Latin letters with a hyphen"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_12(name='!@#$%^&*()_+{}[];,./*-', animal_type='British',
                                     age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding Information to the name Field with Special Characters.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_13(name='R', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding one latin letter to the name field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_14(name='Ro' * 128, animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the name field 256 characters"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_15(name='Ron' * 334, animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the name field in 1002 characters.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_16(name='-1', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a negative number to the name field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_17(name='0', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a zero character to the name field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_18(name='0.8', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a floating point number to the name field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_19(name=' Ron', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo.
    Adding information to the name field with a space at the beginning of the line.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_20(name='Ron ', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo.
    Adding information to the name field with a space at the end of the line.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_21(name='Ron', animal_type='BRITISH', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the uppercase breed field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_22(name='Ron', animal_type='british', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the breed field in lowercase"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_23(name='Ron', animal_type='Британский', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the breed field in Cyrillic"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_24(name='Ron', animal_type='英國', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding Chinese characters to the breed field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_25(name='Ron', animal_type='😇', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding an emoji to the breed field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_26(name='Ron', animal_type='', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding an empty value to the breed field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_27(name='Ron', animal_type=' ', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding only a space to the breed field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_28(name='Ron', animal_type='123', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding three digits to the breed field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_29(name='Ron', animal_type='British999', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding numbers and Latin letters to the breed field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_30(name='Ron', animal_type='B-r-i-t-i-s-h', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo.
    Adding information to the breed field in Latin letters with a hyphen"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_31(name='Ron', animal_type='!@#$%^&*()_+{}[];,./*-',
                                     age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding Information to the breed Field with Special Characters.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_32(name='Ron', animal_type='B', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding one latin letter to the breed field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_33(name='Ron', animal_type='Br' * 128, age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the breed field 256 characters"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_34(name='Ron', animal_type='Bri' * 334, age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the breed field in 1002 characters.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_35(name='Ron', animal_type='-1', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a negative number to the breed field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_36(name='Ron', animal_type='0', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a zero character to the breed field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_37(name='Ron', animal_type='0.8', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a floating point number to the breed field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_38(name='Ron', animal_type=' British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo.
    Adding information to the breed field with a space at the beginning of the line.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_39(name='Ron', animal_type='British ', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo.
    Adding information to the breed field with a space at the end of the line.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_40(name='Ron', animal_type='British', age='two', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding three latin characters to the age field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_41(name='Ron', animal_type='British', age='два', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding information to the age field in Cyrillic.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_42(name='Ron', animal_type='British', age='二', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding Chinese characters to the age field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_43(name='Ron', animal_type='British', age='😇', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding an emoji to the age field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_44(name='Ron', animal_type='British', age='', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding an empty value to the age field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_45(name='Ron', animal_type='British', age=' ', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding only a space to the age field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_46(name='Ron', animal_type='British', age='123', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding three digits to the age field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_47(name='Ron', animal_type='British', age='ag2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding numbers and Latin letters to the age field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_48(name='Ron', animal_type='British', age='2-2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding numbers and a hyphen to the age input field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_49(name='Ron', animal_type='British', age='!"№', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding Information to the age Field with Special Characters.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_50(name='Ron', animal_type='British', age='22', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding two digits to the age input field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_51(name='Ron', animal_type='British', age='22' * 128, pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding 256 digits to the age input field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_52(name='Ron', animal_type='British', age='123' * 334, pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding 1002 digits to the age input field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_53(name='Ron', animal_type='British', age='-2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a negative number to the age field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_54(name='Ron', animal_type='British', age='0', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a zero character to the age field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_55(name='Ron', animal_type='British', age='0.8', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a floating point number to the age field"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['animal_type'] == animal_type
    assert result['age'] == age
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_56(name='Ron', animal_type='British', age='0.88', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo.
    Adding a floating point number with two digits to the age field.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_57(name='Ron', animal_type='British', age=' 2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo.
    Adding information to the age field with a space at the beginning of the line.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_58(name='Ron', animal_type='British', age='2 ', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo.
    Adding information to the age field with a space at the end of the line.
    Invalid value"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_59(name='Ron', animal_type='British', age='2', pet_photo='images/02.png'):
    """Add information about a new pet with a photo. Photo format 'png'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_60(name='Ron', animal_type='British', age='2', pet_photo='images/03.JPG'):
    """Add information about a new pet with a photo. Photo format 'jpeg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 200
    assert result['name'] == name
    assert result['pet_photo'] != ''


def test_add_new_pet_with_a_photo_61(name='Ron', animal_type='British', age='2', pet_photo='images/04.GIF'):
    """Add information about a new pet with a photo. Photo format 'GIF'
    Invalid format photo."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_62(name='Ron', animal_type='British', age='2', pet_photo='images/05.MHT'):
    """Add information about a new pet with a photo. Photo format 'MHTML-doc'
    Invalid format photo."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_63(name='Ron', animal_type='British', age='2', pet_photo='images/06.txt'):
    """Add information about a new pet with a photo. File format 'txt'
    Invalid format."""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 400
    assert 'name' not in result
    assert 'animal_type' not in result
    assert 'age' not in result
    assert 'pet_photo' not in result


def test_add_new_pet_with_a_photo_64(name='Ron', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a new pet with an invalid key"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.add_new_pet(invalid_auth_key, name, animal_type, age, pet_photo)

    assert status == 403
    assert 'name' not in result


def test_add_new_pet_with_a_photo_65(name='Ron', animal_type='British', age='2', pet_photo='images/01.jpg'):
    """Add information about a new pet with a photo. Adding a new pet with an empty key"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    status, result = pf.add_new_pet(empty_auth_key, name, animal_type, age, pet_photo)

    assert status == 403
    assert 'name' not in result
