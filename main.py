from taskscore2.prioritizer import calculate_task_score


# Example tasks
tasks = {
    "Cleaning the house": (3, 4),  # (importance, effort)
    "Studying programming": (4, 2),
    "Paying the bills": (4, 1),
}

# Calculating and printing task scores
for task, (importance, effort) in tasks.items():
    score = calculate_task_score(importance, effort)
    print(f"Task: {task}, Score: {score}")
