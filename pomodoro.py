import argparse
import time
import sys
import json
from pathlib import Path

SESSIONS_FILE = Path("sessions.json")

def load_sessions():
    if not SESSIONS_FILE.exists():
        return {"completed": 0}
    with open(SESSIONS_FILE, "r") as f:
        return json.load(f)

def save_sessions(data):
    with open(SESSIONS_FILE, "w") as f:
        json.dump(data, f)

def countdown(minutes: int, label: str):
    total_seconds = minutes * 60
    while total_seconds > 0:
        mins, secs = divmod(total_seconds, 60)
        sys.stdout.write(f"\r{label} ⏳ {mins:02d}:{secs:02d} restantes")
        sys.stdout.flush()
        time.sleep(1)
        total_seconds -= 1
    print(f"\n✅ {label} concluído!")

def pomodoro_cycle():
    print("🍅 Iniciando ciclo de Foco (25min)")
    countdown(25, "Foco")
    print("😌 Pausa curta (5min)")
    countdown(5, "Descanso")

    sessions = load_sessions()
    sessions["completed"] += 1
    save_sessions(sessions)

def main():
    parser = argparse.ArgumentParser(description="Pomodoro CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("start", help="Inicia um ciclo Pomodoro")
    subparsers.add_parser("status", help="Mostra histórico de sessões")
    subparsers.add_parser("reset", help="Reseta histórico de sessões")

    args = parser.parse_args()

    if args.command == "start":
        pomodoro_cycle()
    elif args.command == "status":
        sessions = load_sessions()
        print(f"📊 Ciclos concluídos: {sessions['completed']}")
    elif args.command == "reset":
        save_sessions({"completed": 0})
        print("🔄 Histórico resetado!")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
