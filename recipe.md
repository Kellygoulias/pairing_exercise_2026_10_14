# {{PROBLEM}} Class Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem

As a user
So I don't forget the details
I want to keep a record of friends' names and birthdates #add

As a user
So I can make edits when I've got dates wrong
I want to be able to update a record by passing in a name and new date

As a user
So I can make edits when people change their name
I want to be able to update a record by passing in an old and a new name

As a user
So I can remember to send birthday cards at the right time
I want to be able to list friends whose birthdays are coming up soon and to whom I need to send a card

As a user
So I can buy age-appropriate birthday cards
I want to calculate the upcoming ages for friends with birthdays


## 2. Design the Class Interface

_Include the initializer, public properties, and public methods with all parameters, return values, and side-effects._

```python
# EXAMPLE

class Friends_details:
    # User-facing properties:
    #   name: string

    def __init__(self, name):
        # Parameters:
        # None
        # Side effects:
        #   set lists of friends to empty list
        self._list_of_friends = []

    def add(self, name, birthday):
        params:
        name : string
        birthday: string
        returns: None
        side effects: appends entry to the list of friends

    def edit_date(self, name, new_birthday):
        # Parameters:
        #   name: string 
        #   new_birthday : string
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the birthday to new_birthday
        pass # No code here yet

    def edit_name(self, old_name, new_name):
        # Parameters:
        #   old_name: string 
        #   new_name : string
        # Returns:
        #   Nothing
        # Side-effects
        #   updates the old_name to new_name
        pass # No code here yet

    def birthdays_coming_soon(self, notice_period):
        # Parameters:
        #   notice_period: string 
        # Returns:
        #   returns string with relevant names.
        # Side-effects
        #   None
        pass # No code here yet


    def calculate_upcoming_age(self, name):
        #Parameters: 
        #
        # name: A string
        # Returns:
        #  upcoming age: int
        # Side-effects:
        #   None
        pass # No code here yet
```

## 3. Create Examples as Tests

_Make a list of examples of how the class will behave in different situations._

``` python
# EXAMPLE

"""
Given an instance, an empty list is instantiated
"""
friend_list = Friends_details()
self._list_of_friends # => []

"""
Given a name and a birthday, calling the add() method will append it to the friend_list
"""

friend_list = Friends_details()
friend_list.add("Katie", "2025-10-17")
self._list_of_friends # => [Object: "Katie", "2025-10-17"]


"""
Given multiple names and a birthdays, calling the add() method will append them to the friend_list
"""

friend_list = Friends_details()
friend_list.add("Katie", "2025-10-17")
friend_list.add("Spencer", "2025-07-28")
self._list_of_friends # => [Object: "Katie", "2025-10-17" Object: "Spencer", "2025-07-28"]

"""
Given no name or birthday, when calling the add() method and exception is raised
"""
friend_list = Friends_details()
friend_list.add("", "") #=> throws exception "Name and birthday must be provided"

"""
Given the incorrect type with the add() method, and exception is raised.
"""
friend_list = Friends_details()
friend_list.add("Katie", 2) #=> throw TypeError => "The Birthday type must be a string"

"""
Given name is passed in and a new_date it updates the date
"""

friend_list = Friends_details()
friend_list.add("Katie", "2025-10-17")
friend_list.add("Spencer", "2025-07-28")
friend_list.edit_date("Spencer", "2025-06-27")
self._list_of_friends # => [Object: "Katie", "2025-10-17" Object: "Spencer", "2025-06-27"]

"""
Given no name provided or birthday and exception is raised when calling edit_date()
"""
friend_list = Friends_details()
friend_list.add("Katie", "2025-10-17")
friend_list.add("Spencer", "2025-07-28")
friend_list.edit_date("Spencer", "") # => raises exception "Name and birthday must be provided"

"""
Given the incorrect type with the edit_date() method, and exception is raised.
"""
friend_list = Friends_details()
friend_list.add("Spencer", "2025-07-28")
friend_list.edit_date("Spencer", 7) #=> throw TypeError => "The entries data type must be a string"


"""
Given name is passed in and a new_name it updates the name
"""
friend_list = Friends_details()
friend_list.add("Katie", "2025-10-17")
friend_list.add("Spencer", "2025-07-28")
friend_list.edit_name("Spencer", "Spensor")
self._list_of_friends # => [Object: "Katie", "2025-10-17" Object: "Spensor", "2025-06-27"]


"""
Given some entries and notice period and a birthdays_coming_up_soon called it returns formatted string including names that are remaining to happen during the year
"""
friend_list = Friends_details()
friend_list.add("Katie", "2025-10-17")
friend_list.add("Spencer", "2025-07-28")
friend_list.add("Sam", "2024-05-01")
friend_list.birthdays_coming_up_soon("2026-06-30") #=> "Birthdays yet to be had thid year: Katie Spencer"

"""
Given a name, the function returns the age that is upcoming for the person.
"""
friend_list = Friends_details()
friend_list.add("Katie", "2025-10-17")
friend_list.add("Spencer", "2025-07-28")
friend_list.calculate_upcoming_age("Katie") #=> 2


_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._
