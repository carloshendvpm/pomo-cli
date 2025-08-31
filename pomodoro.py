import argparse
import time
import sys

def countdown(minutes: int):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        sys.stdout.write(f"\r⏳ {mins:02d}:{secs:02d} restantes")
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1
    print("\n✅ Tempo concluído!")

def main():
    parser = argparse.ArgumentParser(description="Pomodoro CLI")
    subparsers = parser.add_subparsers(dest="command")

    start_cmd = subparsers.add_parser("start", help="Inicia um ciclo Pomodoro")
    start_cmd.add_argument("--minutes", type=int, default=25, help="Duração em minutos")

    subparsers.add_parser("status", help="Mostra histórico de sessões")
    subparsers.add_parser("reset", help="Reseta histórico de sessões")

    args = parser.parse_args()

    if args.command == "start":
        countdown(args.minutes)
    elif not args.command:
        parser.print_help()

if __name__ == "__main__":
    main()
