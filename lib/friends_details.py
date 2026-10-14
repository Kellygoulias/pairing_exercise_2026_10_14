from datetime import date

class Friends_details:
    # User-facing properties:
    #   name: string

    def __init__(self):
        # Parameters:
        # None
        # Side effects:
        #   set lists of friends to empty list
        self._list_of_friends = []

    def add(self, name, birthday):
        if type(name) != str or type(birthday) != str:
            raise TypeError("The Birthday type must be a string")
        if len(name) == 0 or len(birthday) == 0:
            raise Exception("Name and birthday must be provided")
        self._list_of_friends.append({"name": name, "birthday": birthday})

    def edit_date(self, name, new_birthday):
        if type(name) != str or type(new_birthday) != str:
            raise TypeError("The entries data type must be a string")
        if len(name) == 0 or len(new_birthday) == 0:
            raise Exception("Name and birthday must be provided")
        for entry in self._list_of_friends:
            if name == entry['name']:
                entry['birthday'] = new_birthday

    def edit_name(self, old_name, new_name):
        for entry in self._list_of_friends:
            if entry['name'] == old_name:
                entry['name'] = new_name

    def birthdays_coming_soon(self, notice_period):
        for entry in self._list_of_friends:
            birthday = entry['birthday']
            birthday_list = birthday.split("-")
            datetime_birthday = date(int(birthday_list[0]), int(birthday_list[1]), int(birthday_list[2]))
            print(datetime_birthday)

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