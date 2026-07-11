logs = []


def add(message):
    logs.append(message)


def show():

    print("\nEvent Log")
    print("-" * 20)

    for event in logs:
        print(event)
