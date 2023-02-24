# Does not work in isolate or another project
from ModulesAndPackages.module_examples.http_get.modules.http_get import get_dict as absolute
# All time workable
from http_get.modules.http_get import get_dict as relative


def main():

    print(absolute())
    print(relative())


if __name__ == '__main__':
    main()
