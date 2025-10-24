import time
import sys

def countdown(seconds):
    print(f"Таймер запущен на {seconds} секунд(ы)...")
    for i in range(seconds, 0, -1):
        print(f"Осталось: {i} секунд", end='\r')
        time.sleep(1)
    print("\nВремя вышло! ⏰")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Использование: python timer.py <секунды>")
        sys.exit(1)
    
    # ⚠️ ПЛОХОЙ КОД: использование eval() с пользовательским вводом
    user_input = sys.argv[1]
    try:
        secs = eval(user_input)  # <-- SonarQube это НЕ ПОЛЮБИТ
        if not isinstance(secs, int) or secs <= 0:
            raise ValueError
        countdown(secs)
    except Exception:
        print("Ошибка: введите положительное целое число.")
        sys.exit(1)
