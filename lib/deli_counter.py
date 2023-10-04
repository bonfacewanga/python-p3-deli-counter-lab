
def line(queue):
    if not queue:
        print("The line is currently empty.")
    else:
        line_message = "The line is currently:"
        for i, person in enumerate(queue, start=1):
            line_message += f" {i}. {person}"
        print(line_message)

def take_a_number(queue, name):
    queue.append(name)
    position = len(queue)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(queue):
    if not queue:
        print("There is nobody waiting to be served!")
    else:
        serving = queue.pop(0)
        print(f"Currently serving {serving}.")
