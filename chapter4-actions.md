Chapter 4: Testing and Debugging Your Logic
ClearLang isn't just about writing readable logic — it's also about making sure it works as expected. In this chapter, you’ll learn how to:
Test your rules before deployment
Understand what triggered an action (and why)
Trace logic flow step-by-step
Simulate inputs and time to predict behavior
Debug faulty or unexpected outcomes

🔍 1. Testing Your Rules in the Playground
ClearLang comes with a built-in web-based playground (and eventually CLI/IDE tools) where you can:
Write rules
Input test data
See exactly which rule ran
Get logs explaining why something happened
✅ Example Test Session:
# Rules
IF temperature > 30 THEN say "It's hot"
ELSE say "It's cool"

# Test input:
SET temperature TO 32
🧪 Output:
perl code
✓ Rule matched: temperature > 30
→ Action: say "It's hot"
Now try temperature TO 25, and the ELSE rule will be triggered instead.

🧭 2. Explaining Rule Triggers (Trace Mode)
Every ClearLang action can include trace information — like a decision log.
This answers questions like:
“Why did this action happen?”
“Which rule did it come from?”
“What were the input values?”
✅ Example:
TRACE ON

IF weather IS "raining" THEN remind "Carry an umbrella"
 Output:
csharp
[TRACE] weather = "raining"
[TRACE] Rule matched → remind "Carry an umbrella"
You can enable or disable TRACE globally or per block for performance.

 3. Simulating Time and Inputs
The playground (or future engine) lets you simulate events like:
Changing variables
Time-based triggers (e.g. "Monday", "6PM")
System inputs like user_logged_in = true
This helps you test rules without waiting in real life.
✅ Example:
# Simulate:
SET day TO "Sunday"
SET user_logged_in TO true

# Rule:
IF day IS "Sunday" AND user_logged_in IS true THEN say "Weekend login bonus!"
✓ Rule matched: say "Weekend login bonus!"

🛠️ 4. Debugging Tips and Tools
Here are some ways to catch and fix logic bugs:
Issue	Tip
A rule isn’t triggering	Use TRACE ON to check input values
Too many rules firing	Add specificity, or group into blocks
Rule is skipped	Check spacing, spelling, and logic operators (IS, >, AND, etc.)
Action doesn’t work	Make sure it’s defined properly or exists in your engine

🧪 Project Example 1: Health Reminder Bot Debugger
Rule Setup:
plaintext code
DEFINE BLOCK meds_reminder
  IF time IS "8AM" THEN remind "Take your blood pressure pill"
  IF time IS "9PM" THEN remind "Take your cholesterol pill"
END
SET time TO "8AM"
TRACE ON
run meds_reminder
[TRACE] time = "8AM"
[TRACE] Matched: remind "Take your blood pressure pill"
✅ This confirms that time triggers are working correctly.

🧪 Project Example 2: NGO Eligibility Trace Check
Plaintext code
DEFINE BLOCK check_support
  IF income < 10000 AND dependents > 3 THEN grant "FoodSupport"
  ELSE deny_support
END

SET income TO 12000
SET dependents TO 4
TRACE ON
run check_support
 Output:
csharp code
[TRACE] income = 12000, dependents = 4
[TRACE] Condition failed: income < 10000
[TRACE] ELSE triggered: deny_support
✅ Clear feedback tells you exactly why support was denied.

🔚 Wrap-Up
Testing and debugging is the heart of reliable logic:
You write it once ✅
You test it safely ✅
You trust it forever ✅
In Chapter 5, we’ll explore building logic for real-world devices, apps, and platforms — turning ClearLang from theory into action
