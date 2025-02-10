import requests
import sys
import random


def get_user_attempted_problems(username):
    url = f"https://codeforces.com/api/user.status?handle={username}"
    response = requests.get(url).json()
    if response.get("status") != "OK":
        print("Error al obtener las sumisiones del usuario.")
        sys.exit(1)
    attempted = set()
    for submission in response["result"]:
        problem = submission.get("problem", {})
        key = (problem.get("contestId"), problem.get("index"))
        attempted.add(key)
    return attempted


def get_gym_contest_with_icpc():
    url = "https://codeforces.com/api/contest.list?gym=true"
    response = requests.get(url).json()
    if response.get("status") != "OK":
        print("Error al obtener la lista de concursos.")
        sys.exit(1)
    contests = response.get("result", [])
    gym_icpc_contests = [contest for contest in contests if "ICPC" in contest.get("type", "") and contest.get("difficulty", "") == 4]
    contest = gym_icpc_contests[- int(random.randint(1, 100))]
    return contest


def get_contest_problems(contest_id):
    url = f"https://codeforces.com/api/contest.standings?contestId={contest_id}&from=1&count=1"
    response = requests.get(url).json()
    if response.get("status") != "OK":
        print("Error al obtener los standings del contest.")
        sys.exit(1)
    problems = response.get("result", {}).get("problems", [])
    return problems


def get_contest_status_submissions(contest_id):
    url = f"https://codeforces.com/api/contest.status?contestId={contest_id}&from=1&count=100000&showUnofficial=true"
    response = requests.get(url).json()
    if response.get("status") != "OK":
        print("Error al obtener las sumisiones del contest.")
        sys.exit(1)
    submissions = response.get("result", [])
    return submissions


def compute_accepted_counts(submissions):
    accepted_counts = {}
    for sub in submissions:
        if sub.get("verdict") == "OK":
            prob = sub.get("problem", {})
            key = (prob.get("contestId"), prob.get("index"))
            members = sub.get("author", {}).get("members", [])
            if members:
                user = members[0].get("handle")
            else:
                user = None
            if not user:
                continue
            if key not in accepted_counts:
                accepted_counts[key] = set()
            accepted_counts[key].add(user)
    counts = {key: len(users) for key, users in accepted_counts.items()}
    return counts


def main():
    username = "RauPro"
    user_attempted = get_user_attempted_problems(username)
    contest = get_gym_contest_with_icpc()
    contest_id = contest.get("id")
    print(f"GYM: {contest.get('name')} (ID: {contest_id})")
    problems = get_contest_problems(contest_id)
    candidate_problems = []
    for prob in problems:
        key = (prob.get("contestId"), prob.get("index"))
        if key not in user_attempted:
            candidate_problems.append(prob)

    if not candidate_problems:
        print("No se encontraron problemas candidatos que cumplan con los criterios.")
        return
    submissions = get_contest_status_submissions(contest_id)
    accepted_counts = compute_accepted_counts(submissions)

    for prob in candidate_problems:
        key = (prob.get("contestId"), prob.get("index"))
        prob["solvedCount"] = accepted_counts.get(key, 0)

    candidate_problems_sorted = sorted(candidate_problems, key=lambda p: p["solvedCount"], reverse=True)

    top_4 = candidate_problems_sorted[:4]

    print("\nTop 4:")
    for p in top_4:
        print(
            f"{p['contestId']}{p['index']} - {p['name']}, Accepted Rate: {p['solvedCount']})")


if __name__ == "__main__":
    main()