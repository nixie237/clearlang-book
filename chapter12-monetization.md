Chapter 12: Grouping and Reusing Logic in ClearLang
 What You’ll Learn in This Chapter: In this chapter, you’ll explore how to make your rules modular, organized, and reusable. You’ll learn to:
Group related rules into blocks
Reuse logic using templates or tags
Keep your ClearLang scripts clean and easy to manage
📦 Why Grouping Matters
As your ClearLang projects grow, having all rules in one long list becomes messy. Grouping: ✅ Makes rules easier to read
✅ Helps you debug related logic together
✅ Lets you reuse common patterns

🧱 Using Labels or Blocks
You can group related rules using a comment-style label:
# Morning Routine
SET time TO "7AM"
WHEN time IS "7AM" THEN remind "Start your day with water"
WHEN time IS "7AM" THEN log "Morning routine started"
Or:
# Safety Check
IF door IS "open" THEN warn "Close the door!"
 You can even add emojis to visually separate logic areas:
#  Morning Setup
# 🚪 Door Check
# 💡 Energy Saving

🔁 Reusing Logic Patterns
Sometimes you’ll want to reuse logic with different inputs.
# Template: Task Reward
IF tasks_done >= 3 THEN grant "Take a break"
Repeat this template across multiple categories:
# 🧹 Cleaning
SET tasks_done TO 4
IF tasks_done >= 3 THEN grant "Tea break"

# 📚 Studying
SET study_sessions TO 3
IF study_sessions >= 3 THEN grant "Music break"

💡 Tip: Prefix or Tag Your Rules
Give common actions a label in comments:
# [energy_saver]
IF lights IS "on" AND time IS "day" THEN warn "Turn off lights to save energy"
You can filter or manage all [energy_saver] logic together later.

📑 Example: Organized ClearLang File
# 📅 Daily Planner

# ☀️ Morning Routine
SET time TO "7AM"
WHEN time IS "7AM" THEN remind "Drink water"
WHEN time IS "7AM" THEN remind "Stretch"

# 🧠 Focus Boost
SET mood TO "tired"
IF mood IS "tired" THEN remind "Take a deep breath"

# 🔋 Energy Saving
SET lights TO "on"
SET time TO "day"
IF lights IS "on" AND time IS "day" THEN warn "Switch off unnecessary lights"

 Logic Used:
AND conditions
Reusable structure (remind, warn, grant)
Grouped categories by context (morning, focus, energy)
🛠️ Mini Project Idea: Smart Workspace Rules
Create a grouped .clr file with blocks like:
# Setup
# Productivity
# Break Reminders
# End of Day Cleanup
Try running your grouped logic and checking which ones fire based on the variables.
🚧 Reminder:
ClearLang doesn't yet support "functions" like programming languages, but smart grouping and templates let you mimic that concept cleanly.

