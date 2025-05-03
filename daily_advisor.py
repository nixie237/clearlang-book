def run_action(action, variables):
    if action.startswith("remind"):
        print("📝 Reminder:", action.replace("remind", "").strip('" '))
    elif action.startswith("grant"):
        print("✅ Granted:", action.replace("grant", "").strip('" '))
    elif action.startswith("warn"):
        print("⚠️ Warning:", action.replace("warn", "").strip('" '))
    elif action.startswith("log"):
        print("📋 Log:", action.replace("log", "").strip('" '))
    elif action.startswith("say"):
        print("💬", action.replace("say", "").strip('" '))

def evaluate_condition(condition, variables):
    condition = condition.strip()
    if " AND " in condition:
        parts = condition.split(" AND ")
        return all(evaluate_condition(p.strip(), variables) for p in parts)
    elif " IS " in condition:
        var, val = condition.split(" IS ")
        return variables.get(var.strip()) == val.strip('"')
    elif ">=" in condition:
        var, val = condition.split(">=")
        return int(variables.get(var.strip(), 0)) >= int(val.strip())
    return False

def main():
    # Initial state
    variables = {
        "time": "morning",
        "energy": "low",
        "mood": "neutral",
        "tasks_done": 1,
        "weather": "sunny",
        "goal": "exercise"
    }

    rules = [
        ('time IS "morning" AND energy IS "low"', 'remind "Start with a light warm-up and hydrate"'),
        ('weather IS "sunny" AND goal IS "exercise"', 'grant "Go for a morning jog"'),
        ('tasks_done >= 3', 'grant "Take a short break"'),
        ('ELSE', 'remind "Try finishing another task before taking a break"'),
        ('mood IS "neutral"', 'say "You’ve got this! Let’s make it a great day"'),
        ('energy IS "low"', 'warn "Avoid heavy mental tasks now"'),
        ('goal IS "exercise" AND mood IS "neutral"', 'log "Fitness mindset activated"')
    ]

    for condition, action in rules:
        if condition == 'ELSE':
            run_action(action, variables)
        elif evaluate_condition(condition, variables):
            run_action(action, variables)

if __name__ == "__main__":
    main()
