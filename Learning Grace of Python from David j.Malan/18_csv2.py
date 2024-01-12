def outputingv1():
    import csv
    name = input("Enter your name: ")
    home = input("Enter Home name: ")
    with open("18_students.csv", "a") as file:
        writer = csv.writer(file)
        writer.writerow([name, home])

# dictionary writing


def outputingv2():
    import csv
    name = input("Enter your name: ")
    home = input("Enter Home name: ")
    with open("18_students.csv", "a",newline = "") as file:
        writer = csv.DictWriter(file, fieldnames=["name", "home"])
        writer.writerow({"name": name, "home": home})


outputingv2()
