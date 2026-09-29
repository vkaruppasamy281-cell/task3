variables = ["Maths", "Python", "DBMS", "AI"]

time_slots = ["9:00 AM", "11:00 AM", "2:00 PM"]
domains = {subject: list(time_slots) for subject in variables}

conflicts = [
    ("Maths", "Python"),
    ("DBMS", "AI"),
]


def is_consistent(subject, slot, assignment):
    for a, b in conflicts:
        if subject == a and assignment.get(b) == slot:
            return False
        if subject == b and assignment.get(a) == slot:
            return False
    return True


def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    subject = next(v for v in variables if v not in assignment)

    for slot in domains[subject]:
        if is_consistent(subject, slot, assignment):
            assignment[subject] = slot
            result = backtrack(assignment)
            if result is not None:
                return result
            del assignment[subject]

    return None


def display(solution):
    print("Final Assignment")
    print("-" * 30)
    for subject in variables:
        print(f"{subject:<8} -> {solution[subject]}")

    print("\nTimetable")
    print("-" * 30)
    for slot in time_slots:
        subjects = [s for s in variables if solution[s] == slot]
        print(f"{slot:<9}: {', '.join(subjects) if subjects else 'Free'}")

    print("\nConstraint Verification")
    print("-" * 30)
    for a, b in conflicts:
        ok = solution[a] != solution[b]
        print(f"{a} & {b} in different slots: {'SATISFIED' if ok else 'VIOLATED'}")
    print("Each subject has exactly one slot: SATISFIED")


if __name__ == "__main__":
    solution = backtrack({})
    if solution:
        display(solution)
    else:
        print("No valid timetable exists.")