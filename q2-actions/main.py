import json
import matplotlib.pyplot as plt


def read_json_file(filename):
    with open(filename, 'r') as file:
        return json.load(file)


def write_json_file(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def process_actions(users, actions_file):
    with open(actions_file, 'r') as file:
        actions = file.readlines()

    for action in actions:
        parts = action.strip().split()
        command = parts[0]
        user = parts[1]

        if command == "ADD":
            amount = int(parts[2])
            if user in users:
                users[user]["balance"] += amount

        elif command == "CREATE":
            age = int(parts[2])
            if user not in users:
                users[user] = {"balance": 0, "age": age}
            else:
                users[user]["age"] = age

        elif command == "DELETE":
            if user in users:
                del users[user]

    return users


def generate_histogram(users, output_file):
    ages = [user["age"] for user in users.values()]
    plt.hist(ages, bins=range(min(ages), max(ages) + 2), edgecolor='black', align='left')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.title('Histogram of User Ages')
    plt.savefig(output_file)
    plt.close()


if __name__ == "__main__":
    users_file = 'users.json'
    actions_file = 'actions.log'
    users = read_json_file(users_file)
    updated_users = process_actions(users, actions_file)
    write_json_file(users_file, updated_users)
    generate_histogram(updated_users, 'hist.png')

