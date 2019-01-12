def any_character_predicate(string, predicate):
    for i in range(len(string)):
        if predicate(string[i]):
            return True
    return False


if __name__ == '__main__':
    string = input().strip()
    print(any_character_predicate(string, lambda s: s.isalnum()))
    print(any_character_predicate(string, lambda s: s.isalpha()))
    print(any_character_predicate(string, lambda s: s.isdigit()))
    print(any_character_predicate(string, lambda s: s.islower()))
    print(any_character_predicate(string, lambda s: s.isupper()))
