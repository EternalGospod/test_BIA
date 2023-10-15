def get_month_index(index):
    months = {
        "January": 2,
        "February": 0,
        "March": 2,
        "April": 1,
        "May": 2,
        "June": 1,
        "July": 2,
        "August": 2,
        "September": 1,
        "October": 2,
        "November": 1,
        "December": 2
    }
    a = months.get(index, None)
    if a is None:
        return None, None
    return a

days_in_month = [28, 30, 31]
index = input("Please enter the current month: ")
month_index = get_month_index(index)



class Worker:
    def __init__(self, name):
        self.name = name
        self.was_worked = 0  # отработанные часы

    def check_hours(self, hours):
        if self.was_worked + hours <= 144:
            self.was_worked += hours
            return True
        return False


class Day:
    def __init__(self, day_type):
        # day_type -  0 (воскресенье, -1 смена), 1 (понедельник, +1 смена), 2 (другие дни, 3 смены)
        self.shifts = []  
        self.day_type = day_type  

    def set_worker(self, worker, shift_start):
        if worker.check_hours(12):  
            self.shifts.append((worker, shift_start))
            return True
        return False

    def __repr__(self):
        return str([(worker.name, shift_start) for worker, shift_start in self.shifts])


class Scheduler:
    def __init__(self, num_days):
        self.workers = [Worker(f"worker{i+1}") for i in range(10)]
        self.days = [Day(i % 7) for i in range(num_days)]

    def min_worked(self):
        # возвращает сотрудника с min отработынных часов
        return sorted([w for w in self.workers if w.was_worked + 12 <= 144],
                      key=lambda w: w.was_worked)[0]

    def plan_schedule(self):
        for day in self.days:
            required_shifts = 3
            if day.day_type == 0:
                required_shifts = 2
            elif day.day_type == 1:
                required_shifts = 4

            for _ in range(required_shifts):
                worker = self.min_worked()
                day.set_worker(worker, 8 if _ % 2 == 0 else 10)

    def print_schedule(self):
        for i, day in enumerate(self.days):
            print(f"Day {i+1}: {day}")


num_days = days_in_month[month_index]
scheduler = Scheduler(num_days)
scheduler.plan_schedule()
scheduler.print_schedule()
