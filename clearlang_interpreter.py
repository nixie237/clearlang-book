# clearlang_interpreter.py

def load_rules(filename="rules.clr"):
    with open(filename, "r") as file:
        return file.readlines()

def interpret_line(line, variables):
    line = line.strip()
    if line.startswith("SET"):
        _, var, _, value = line.split(" ", 3)
        variables[var] = value.strip('"')
    elif "THEN" in line:
        condition, action = line.split("THEN")
        if evaluate_condition(condition.strip(), variables):
            run_action(action.strip(), variables)
    elif line.startswith("ELSE"):
        run_action(line.replace("ELSE", "").strip(), variables)

def evaluate_condition(condition, variables):
    if " IS " in condition:
        var, val = condition.split(" IS ")
        return variables.get(var.strip()) == val.strip('"')
    elif ">=" in condition:
        var, val = condition.split(">=")
        return int(variables.get(var.strip(), 0)) >= int(val.strip())
    return False

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

def main():
    rules = load_rules()
    variables = {}
    for line in rules:
        interpret_line(line, variables)

if __name__ == "__main__":
    main()
