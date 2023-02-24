from ModulesAndPackages.package_examples.package_2.modules.http_get import get_dict
...


def get_data() -> dict:
    return get_dict()


...

# Does not work!
# Because init file in package could not have entry point
#
# if __name__ == '__main__':
#     get_data()
