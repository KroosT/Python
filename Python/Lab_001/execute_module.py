import argparse
import module_1
import module_2
import module_3
import module_4


def main():
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('module', type=int, choices=range(1, 5), help='task to '
                                                                    'execute')
    args = parser.parse_known_args()
    if args[0].module == 1:
        module_1.main(args[1])
    elif args[0].module == 2:
        module_2.main(args[1])
    elif args[0].module == 3:
        module_3.main()
    elif args[0].module == 4:
        module_4.main(args[1])

if __name__ == "__main__":
    main()
