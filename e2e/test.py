USERS = []
__STUB__USER_LOGIN__ = 'user28713876'

def __stub__register_user(login):
    user = {'id': 24, 'login': login, 'country_code': 'UA'}
    USERS.append(user)
    return user



def __test__get_current_user():
    # ...
    # <<< select user from db
    # ...
    user = __STUB__USER_LOGIN__
    return user

def __test__create_user(login):
    # ...
    # >>> creates user in db
    # ...

    # stub
    user = __stub__register_user(login, hash(login))
    return True if 'id' in user else False

# --------------------------------------------

def __test__scenario_1():
    if __test__create_user(__STUB__USER_LOGIN__):
        user = __test__get_current_user()
    else:
        print("user creation error")
        return 5
    return 0


def __test__scenario_2():
    user = __test__get_current_user()
    (category_valid, category_invalid) = (
      {'id': 6, 'name': 'category2398471207', 'is_availabe': True},
      {'id': 666, 'name': 'category02175497932', 'is_availabe': False}
     )
    if not category_valid.is_availabe or category_invalid.is_availabe: return 1
    return 0


def __test__scenario_3():
    return 0

def main():
    if __test__scenario_1() == 0:
        if __test__scenario_2() == 0:
            __test__scenario_3()
    return 0


