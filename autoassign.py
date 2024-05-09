from collections import defaultdict

def assign_topics():
    preferences = {
        1: [4, 7, 5],
        2: [3, 2, 5],
        3: [4, 3, 1],
        4: [2, 6, 8],
        5: [4, 6, 7],
        6: [4, 5, 6]
    }
    
    assignment = {}
    topic_count = defaultdict(int)
    def assign(student, topic):
        assignment[student] = topic
        topic_count[topic] += 1

    for student, prefs in preferences.items():
        first_choice = prefs[0]
        if topic_count[first_choice] == 0:  # If no one has taken this topic yet
            assign(student, first_choice)

    for student, prefs in preferences.items():
        if student not in assignment:
            second_choice = prefs[1]
            if topic_count[second_choice] == 0:
                assign(student, second_choice)

    for student, prefs in preferences.items():
        if student not in assignment:
            third_choice = prefs[2]
            if topic_count[third_choice] == 0:
                assign(student, third_choice)

    available_topics = {i for i in range(1, 9)} - set(assignment.values())
    for student in preferences:
        if student not in assignment:
            assign(student, available_topics.pop())

    return assignment

assignments = assign_topics()
print(assignments)
