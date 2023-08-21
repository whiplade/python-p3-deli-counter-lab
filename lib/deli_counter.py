katz_deli = []

def line(queue):
    if not queue:
        print("The line is currently empty.")
    else:
        positions = [f"{index + 1}. {customer}" for index, customer in enumerate(queue)]
        print("The line is currently:", " ".join(positions))

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        served_person = queue.pop(0)
        print(f"Currently serving {served_person}.")
