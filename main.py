import json
from Backend.logic.budget import validate_user, compare_spending_rec

def main():
    with open("/Users/noahatanda/Desktop/Budget/Backend/Data/fake_data.json") as f:
        data = json.load(f)
    for user in data["users"]:
        try:
            validate_user(user)
            result = compare_spending_rec(user)
            print(f"\n{result['name']}:\n------------------")
            print("Needs:", result["summary"]["needs"])
            print("Wants:", result["summary"]["wants"])
            print("Expected Return by 65:", result["expected_index_return"]["expected_return"])
            print("Monthly Investment", result["expected_index_return"]["monthly_investment"])
        except Exception as e:
            print(f"Error with user {user.get('name', 'Unknown')}: {e}")


if __name__ == "__main__":
    main()