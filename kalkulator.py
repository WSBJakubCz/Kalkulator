def dodaj(a, b): return a + b
def odejmij(a, b): return a - b
def pomnóz(a, b): return a * b
def podziel(a, b): 
    if b == 0:
        return "Błąd! Dzielenie przez zero."
    return a / b

def menu():
    print("\n--- PROSTY KALKULATOR ---")
    print("1. Dodawanie")
    print("2. Odejmowanie")
    print("3. Mnożenie")
    print("4. Dzielenie")
    print("5. Wyjście")

while True:
    menu()
    wybor = input("Wybierz opcję (1-5): ")
    
    if wybor == '5':
        print("Koniec programu. Do widzenia!")
        break
        
    if wybor in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Podaj pierwszą liczbę: "))
            num2 = float(input("Podaj drugą liczbę: "))
        except ValueError:
            print("To nie jest poprawna liczba!")
            continue
            
        if wybor == '1': print(f"Wynik: {dodaj(num1, num2)}")
        elif wybor == '2': print(f"Wynik: {odejmij(num1, num2)}")
        elif wybor == '3': print(f"Wynik: {pomnóz(num1, num2)}")
        elif wybor == '4': print(f"Wynik: {podziel(num1, num2)}")
    else:
        print("Niepoprawny wybór, spróbuj ponownie.")
