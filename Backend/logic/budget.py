import math

# validate the user to make sure all fields are present
def validate_user(user: dict) -> None:
    # check that all valid fields are present
    required_fields = ["name", "age", "monthly_income", "strategy", "needs", "wants"]
    for field in required_fields:
        if field not in user:
            raise ValueError(f"Missing required field: {field}")
    
    # Check strategy validity
    if user["strategy"] not in ["moderate", "aggressive"]:
        raise ValueError("Strategy must be 'moderate' or 'aggressive'.")
    # check for valid user age (above 0)                   
    elif user["age"] <= 0:
        raise ValueError("Age must be positive.")
# this function will handle the budgeting recommendation, the strategy will be decided here
# INPUT: Desired strategy chosen by the user, either moderate or aggressive
# OUTPUT: spending percentages per category in the form of needs, wants, saving/investing

def get_budget_percentage(strategy: str):
    if strategy == "moderate":
        #needs, wants, saving/investing
        return 0.5, 0.3, 0.2
    elif strategy == "aggressive":
        return 0.5, 0.2, 0.3

# this function will do the basic caluclation for to estimate recommended saving amounts for each individual user
# it will estimate the recommended spending for each one based on their chosen investment strategy, and their salary

def calculate_budget(user):
    if user["monthly_income"] <= 0:
        raise ValueError("Income must be positive.") 
    salary = user["monthly_income"]
    strategy = user["strategy"]

    needs_pct, wants_pct, invest_pct = get_budget_percentage(strategy)

    return {
        "needs": math.floor(needs_pct * salary),
        "wants": math.floor(wants_pct * salary),
        "invest_amt": math.floor(invest_pct * salary)
    }


# this function will return the estimated return from an index fund when the user is 65
def calculate_return(monthly_investment, age, target_age, annual_return=0.08):
    #return per month
    r = annual_return / 12
    # number of months invested
    n = (target_age - age) * 12

    future_value = monthly_investment * (((1 + r) ** n - 1) / r) * (1 + r)
    return round(future_value, 2)

# this function will compare the spending of the user, compared to the recommended amount based on their chosen strategy
def compare_spending_rec(user):
    #the recommended budget for the user
    recommended = calculate_budget(user)
    # the actual amount the user is spenidng on needs
    actual_needs = sum(user["needs"].values())
    #the amount of difference between the recommended needs and actual needs
    diff = actual_needs - recommended["needs"]

    # the actual amount that the user is spending on wants
    actual_wants = sum(user["wants"].values())
    #the difference between recommended needs and actual needs
    diff_w = actual_wants - recommended["wants"]
    
    return {
        # "name": user["name"],
        # "actual_needs": actual_needs,
        # "recommended_needs": recommended["needs"],
        # "needs_difference": diff,
        # "over_budget": diff > 0,
        # "comment_needs": f"You are {'over' if diff > 0 else 'under'} your recommended needs budget by ${abs(diff)}.",
        # "comment_wants": f"You are {'over' if diff_w > 0 else 'under'} your recommended needs budget by ${abs(diff_w)}."
        "name": user["name"],
        "actual": {
            "needs": actual_needs,
            "wants": actual_wants
        },
        "recommended": {
            "needs": recommended["needs"],
            "wants": recommended["wants"]
        },
        "difference": {
            "needs": diff,
            "wants": diff_w
        },
        "summary": {
            "needs": f"You are {'over' if diff > 0 else 'under'} your recommended needs budget by ${abs(diff)}.",
            "wants": f"You are {'over' if diff_w > 0 else 'under'} your recommended wants budget by ${abs(diff_w)}."
        },
        "expected_index_return": {
            "your_age": user["age"],
            "target_age": 65,
            "monthly_investment": recommended["invest_amt"],
            "expected_return": calculate_return(recommended["invest_amt"], user["age"], 65, annual_return=0.08)
        }
    }

    