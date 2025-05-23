Chapter 11: Debugging and Testing ClearLang Rules
 What You’ll Learn in This Chapter: In this chapter, you’ll learn how to test and debug your ClearLang rules to make sure they behave as expected. We’ll introduce strategies to:
Identify logic errors and missing variables
Use built-in output messages for feedback
Simulate different input conditions
Improve rule reliability for real-world use
🛠️ Why Debugging Matters
Even simple logic can fail if:
A variable wasn’t set correctly
A rule was skipped due to a typo
Conditions don’t match what you expected
That’s why testing and debugging are core parts of using ClearLang effectively.

🧪 Testing a Rule: Example
SET temperature TO "high"
IF temperature IS "high" THEN warn "Heat alert!"
ELSE remind "Stay warm"
✅ This works because we’ve defined the variable temperature before using it.
❌ If we removed SET temperature TO "high", the rule would do nothing — or worse, throw an error.

 NB: Always Set Your Variables First
Before testing any rules, make sure your .clr file includes all the required SET lines at the top.

🧰 Basic Debugging Tips
 Tip 1: Print Your Variables Use a debug action like:
say "Temperature is ${temperature}"
 Tip 2: Test Each Rule One at a Time If a rule isn’t firing, comment out others and focus on one:
plaintext
Copy code
# IF mood IS "sad" THEN remind "Cheer up"
 Tip 3: Add Logs to Track Flow
log "Checking temperature condition"
 Tip 4: Try Different Inputs Change the SET values and re-run the program to simulate real cases:
SET temperature TO "low"

✅ Sample Debug Session
Let’s say this rule isn’t working:
IF mood IS "excited" THEN remind "Have fun!"
 Ask yourself:
Is mood set? 
Is the value "excited" (check spelling and quotes)? ✅
Is the rule being skipped because of another error? 🤔
Add a debug line:
say "Mood now is ${mood}"
 Output:
💬 Mood now is happy
 You’ll realize the condition mood IS "excited" isn’t true, so the rule won’t fire.

📦 Mini Project Example: Rule Test Kit
Create a .clr file that tests multiple rule types:
SET time TO "night"
SET lights TO "off"
SET is_home TO true

WHEN time IS "night" AND is_home IS true THEN grant "Turn on lights"
IF lights IS "on" THEN log "House is lit"
ELSE warn "Lights are still off"
Run this in your interpreter and check if it prints the correct output.

🧠 Logic Breakdown
 We use:
AND to check combined states
ELSE to handle opposite outcomes
log, warn, and g