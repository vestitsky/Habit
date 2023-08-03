import datetime
from tinydb import TinyDB, Query
import os


'''
Choose id and check your habit

1234567890 - +1 count to habit
add - add a new habit
rem - remove habit
null - count to zero habit
done - exit
'''


db = TinyDB("db.json")
habit = Query()
now = datetime.datetime.now().strftime("%A %d. %B %Y")


def read_progress():
    for item in db:
        print(item.doc_id, item.get(
            "name"), item.get("count"), "days,", "last check:", item.get("time"), "| record:", item.get("record"), "days")


def add_habit(habit_name):
    db.insert({"name": habit_name, "time": now, "count": 0})


def remove_habbit(habit_name):
    db.remove(habit.name == habit_name)


def null_habit(habit_name):
    db.update({"count": 0, "time": now}, habit.name ==
              habit_name)


def check_task(habit_name, habit_count):
    for item in db:
        if item.get("record") == None:
            db.update({"count": habit_count + 1, "time": now, "record": habit_count + 1}, habit.name == habit_name)
        elif item.get("count") > item.get("record"):
            db.update({"count": habit_count + 1, "time": now, "record": habit_count + 1}, habit.name == habit_name)
        else:
            db.update({"count": habit_count + 1, "time": now}, habit.name == habit_name)

def main_update():
        os.system('cls' if os.name == 'nt' else 'clear')
        main()


def main():

    print("Welcome")
    print("Today is:", now)
    print("Your score:")
    read_progress()
    task = input("What do check today?: ")

    if task == 'add':
        habit_name = input("What's the name of the new habit ?: ")
        add_habit(habit_name)
        print(habit_name, "added!")
        main_update()

    if task == 'rem':
        habit_name = input("Habit name: ")
        remove_habbit(habit_name)
        main_update()

    if task == 'null':
        habit_id = input("Habit id: ")
        habit_name = db.get(doc_id=int(habit_id))['name']
        null_habit(habit_name)
        main_update()

    if task in "123456789010":
        print(int(task))
        habit_name = db.get(doc_id=int(task))['name']
        habit_count = db.get(doc_id=int(task))['count']
        check_task(habit_name, habit_count)
        main_update()

    if task == "done":
        return 0


main()
