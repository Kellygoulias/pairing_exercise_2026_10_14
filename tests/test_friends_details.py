from lib.friends_details import * 
import pytest

def test_instantiate_gives_empty_list():
    friend_list = Friends_details()
    assert friend_list._list_of_friends== []

def test_add_single_friend():
    friend_list = Friends_details()
    friend_list.add("Katie", "2025-10-17")
    assert friend_list._list_of_friends== [{"name": "Katie", "birthday":"2025-10-17"}]
    
def test_add_multiple_friends():
    friend_list = Friends_details()
    friend_list.add("Katie", "2025-10-17")
    friend_list.add("Spencer", "2025-07-28")
    assert friend_list._list_of_friends== [{"name": "Katie", "birthday":"2025-10-17"}, {"name":"Spencer", "birthday": "2025-07-28"}]

def test_inputs_present_when_adding():
    friend_list = Friends_details()
    with pytest.raises(Exception) as e:
        friend_list.add("", "")
    assert str(e.value) == "Name and birthday must be provided"


def test_inputs_corrects_type():
    friend_list = Friends_details()
    with pytest.raises(TypeError) as e:
        friend_list.add("Katie", 2)
    assert str(e.value) == "The Birthday type must be a string"

def test_edit_birthdate_when_new_date_is_given():
    friend_list = Friends_details()
    friend_list.add("Katie", "2025-10-17")
    friend_list.add("Spencer", "2025-07-28")
    friend_list.edit_date("Spencer", "2025-06-27")
    assert friend_list._list_of_friends== [{"name": "Katie", "birthday": "2025-10-17"}, {"name":"Spencer", "birthday": "2025-06-27"}]

def test_given_no_name_raises_exception():
    friend_list = Friends_details()
    friend_list.add("Katie", "2025-10-17")
    friend_list.add("Spencer", "2025-07-28")
    with pytest.raises(Exception) as e:
        friend_list.edit_date("", "Spensor")
    assert str(e.value) == "Name and birthday must be provided"

def test_given_incorrect_type_raises_type_error():
    friend_list = Friends_details()
    friend_list.add("Spencer", "2025-07-28")
    with pytest.raises(TypeError) as e:
        friend_list.edit_date("Spencer", 7) 
    assert str(e.value) == "The entries data type must be a string"

def test_given_a_name_it_updates_the_name():
    friend_list = Friends_details()
    friend_list.add("Katie", "2025-10-17")
    friend_list.add("Spencer", "2025-07-28")
    friend_list.edit_name("Spencer", "Spensor")
    assert friend_list._list_of_friends == [{"name": "Katie", "birthday": "2025-10-17"}, {"name":"Spensor", "birthday": "2025-07-28"}]

def test_birthdays_coming_up_soon():
    friend_list = Friends_details()
    friend_list.add("Katie", "2025-10-17")
    friend_list.add("Spencer", "2025-07-28")
    friend_list.add("Sam", "2024-05-01")
    assert friend_list.birthdays_coming_up_soon("2026-06-30") == "Birthdays yet to be had this year: Katie Spencer" 

