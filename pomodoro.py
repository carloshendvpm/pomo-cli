import argparse

def main():
    parser = argparse.ArgumentParser(description="Pomodoro CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("start", help="Inicia um ciclo Pomodoro")

    subparsers.add_parser("status", help="Mostra histórico de sessões")

    subparsers.add_parser("reset", help="Reseta histórico de sessões")

    args = parser.parse_args()
    if not args.command:
        parser.print_help()

if __name__ == "__main__":
    main()
