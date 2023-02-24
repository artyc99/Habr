from package import get_data
from package_2 import get_data as get_data_2


def main():
    # Does not work in isolate or another project
    print(get_data())

    # All time workable
    print(get_data_2())


if __name__ == '__main__':
    main()
