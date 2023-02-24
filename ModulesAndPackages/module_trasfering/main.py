from ModulesAndPackages.module_examples.http_get.modules.http_get import get_dict as absolute
from http_get.modules.http_get import get_dict as relative


def main():
    # Does not work in isolate or another project
    print(absolute())

    # All time workable
    print(relative())


if __name__ == '__main__':
    main()
