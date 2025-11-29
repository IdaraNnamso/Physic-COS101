def show_menu():
    print("\n===== Physics Formulas =====")
    print("1. Gravitational Potential Energy (GPE = m * g * h)")
    print("2. Kinetic Energy (KE = 0.5 * m * v^2)")
    print("3. Ohm's Law (V = I * R)")
    print("4. Wave Speed (v = f * λ)")
    print("5. Momentum (p = m * v)")
    print("q. Quit")

while True:
    show_menu()
    choice = input("\nWhich formula do you want to use? (1-5 or q): ")

    if choice.lower() == 'q':
        print("Thanks for using my Physics Calculator")
        break

    elif choice == '1':
        m = float(input("Enter mass (kg): "))
        g = float(input("Enter gravity (m/s², usually 9.8): "))
        h = float(input("Enter height (m): "))
        gpe = m * g * h
        print(f"Gravitational Potential Energy = {gpe} Joules")

    elif choice == '2':
        m = float(input("Enter mass (kg): "))
        v = float(input("Enter velocity (m/s): "))
        ke = 0.5 * m * v ** 2
        print(f"Kinetic Energy = {ke} Joules")

    elif choice == '3':
        I = float(input("Enter current (Amps): "))
        R = float(input("Enter resistance (Ohms): "))
        V = I * R
        print(f"Voltage = {V} Volts")

    elif choice == '4':
        f = float(input("Enter frequency (Hz): "))
        wavelength = float(input("Enter wavelength (m): "))
        v = f * wavelength
        print(f"Wave speed = {v} m/s")

    elif choice == '5':
        m = float(input("Enter mass (kg): "))
        v = float(input("Enter velocity (m/s): "))
        p = m * v
        print(f"Momentum = {p} kg·m/s")

    else:
        print("ERROR.")z
