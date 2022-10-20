from api import PetFriends
from settings import valid_email, valid_password, invalid_auth_key, empty_auth_key, invalid_id
from tests_03_add_information_about_new_pet_without_photo import test_add_new_pet_without_photo_01
from tests_04_add_information_about_new_pet import test_add_new_pet_with_a_photo_01
import os

pf = PetFriends()


def test_add_photo_to_pet_01(pet_photo='images/01.jpg'):
    """Add photo to pet. Adding a photo to a pet without a photo.
    Photo format 'jpg'. Check status code 200.
    Verifying the successful addition of a pet photo"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    """Adding a new pet without a photo"""
    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


def test_add_photo_to_pet_02(pet_photo='images/02.png'):
    """Add photo to pet. Adding a photo to a pet without a photo.
    Photo format 'png'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


def test_add_photo_to_pet_03(pet_photo='images/03.JPG'):
    """Add photo to pet. Adding a photo to a pet without a photo.
    Photo format 'jpeg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


def test_add_photo_to_pet_04(pet_photo='images/04.GIF'):
    """Add photo to pet. Adding a photo to a pet without a photo.
    Photo format 'GIF'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 400
    assert 'pet_photo' not in result


def test_add_photo_to_pet_05(pet_photo='images/05.MHT'):
    """Add photo to pet. Adding a photo to a pet without a photo.
    Photo format 'MHTML-doc'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 400
    assert 'pet_photo' not in result


def test_add_photo_to_pet_06(pet_photo='images/06.txt'):
    """Add photo to pet. Adding a photo to a pet without a photo.
    File format 'txt'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 400
    assert 'pet_photo' not in result


def test_add_photo_to_pet_07(pet_photo='images/01.jpg'):
    """Add photo to pet. Updating a photo for a pet with a photo.
    Photo format 'jpg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_with_a_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


def test_add_photo_to_pet_08(pet_photo='images/02.png'):
    """Add photo to pet. Updating a photo for a pet with a photo.
    Photo format 'png'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_with_a_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


def test_add_photo_to_pet_09(pet_photo='images/03.JPG'):
    """Add photo to pet. Updating a photo for a pet with a photo.
    Photo format 'jpeg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_with_a_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


def test_add_photo_to_pet_10(pet_photo='images/04.GIF'):
    """Add photo to pet. Updating a photo for a pet with a photo.
    Photo format 'gif'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_with_a_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 400
    assert 'pet_photo' not in result


def test_add_photo_to_pet_11(pet_photo='images/05.MHT'):
    """Add photo to pet. Updating a photo for a pet with a photo.
    Photo format 'MHTML-doc'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_with_a_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 400
    assert 'pet_photo' not in result


def test_add_photo_to_pet_12(pet_photo='images/06.txt'):
    """Add photo to pet. Updating a photo for a pet with a photo.
    File format 'txt'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_with_a_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 400
    assert 'pet_photo' not in result


def test_add_photo_to_pet_13(pet_photo='images/01.jpg'):
    """Add photo to pet. Adding a photo to the second pet in the list without a photo.
    Photo format 'jpg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()
    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][1]['id'], pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


def test_add_photo_to_pet_14(pet_photo='images/01.jpg'):
    """Add photo to pet. Updating a photo to the second pet in the list without a photo.
    Photo format 'jpg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_with_a_photo_01()
    test_add_new_pet_with_a_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, my_pets['pets'][1]['id'], pet_photo)

    assert status == 200
    assert result['pet_photo'] != ''


def test_add_photo_to_pet_15(pet_photo='images/01.jpg'):
    """Add photo to pet. Adding a pet photo with an invalid pet id.
    Photo format 'jpg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(auth_key, invalid_id, pet_photo)

    assert status == 400
    assert 'pet_photo' not in result


def test_add_photo_to_pet_16(pet_photo='images/01.jpg'):
    """Add photo to pet. Adding a pet photo with a valid id that has a space at the beginning of the line.
    Photo format 'jpg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")
    pet_id = ' ' + my_pets['pets'][0]['id']

    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)

    assert status == 400
    assert 'pet_photo' not in result


def test_add_photo_to_pet_17(pet_photo='images/01.jpg'):
    """Add photo to pet. Adding a photo of a pet with an invalid key.
    Photo format 'jpg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(invalid_auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 403
    assert 'pet_photo' not in result


def test_add_photo_to_pet_18(pet_photo='images/01.jpg'):
    """Add photo to pet. Adding a photo of a pet with an empty key.
    Photo format 'jpg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    test_add_new_pet_without_photo_01()

    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    status, result = pf.add_photo_of_pet(empty_auth_key, my_pets['pets'][0]['id'], pet_photo)

    assert status == 403
    assert 'pet_photo' not in result


def test_add_photo_to_pet_19(pet_photo='images/01.jpg'):
    """Add photo to pet. Adding a photo to a pet not on my pets list.
    Photo format 'jpg'"""

    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    _, all_pets = pf.get_list_of_pets(auth_key, "")

    status, result = pf.add_photo_of_pet(auth_key, all_pets['pets'][0]['id'], pet_photo)

    assert status == 400
    assert all_pets['pets'][0]['id'] in str(all_pets)
    assert all_pets['pets'][0]['pet_photo'] == ""
