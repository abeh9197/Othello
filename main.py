import argparse
from othello import game_start


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--autoplay", action='store_true')
    args = parser.parse_args()

    game_start(args.autoplay)


if __name__ == "__main__":
    main()
