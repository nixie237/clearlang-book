Chapter 6: Organizing Logic in Big Projects
✨ What You’ll Learn in This Chapter
As your ClearLang rules grow, it becomes important to organize your logic for clarity, teamwork, and reuse. In this chapter, you’ll learn:
➤ How to group logic into reusable parts (BLOCK, ACTION, FILE)
➤ How to avoid clutter with clean structure
➤ How to collaborate and share rules across projects
➤ How to make your logic modular, readable, and scalable

📦 1. Why Organize Logic?
Without structure, logic becomes hard to debug and scale. By using blocks, actions, and logic files, you gain:
✅ Cleaner, easier-to-read projects
✅ Fewer repeated rules
✅ Reusable modules
✅ Easier teamwork and updates
✅NOTE: Even small projects benefit from good structure!

🧩 2. Blocks: Grouping Logic Steps
Use BLOCK to group related rules together.
DEFINE BLOCK nighttime_rules
  IF time IS "night" THEN
    turn_on "security_lights"
    arm "alarm"
END
✅ LOGIC USED: Grouped conditional logic that runs together.
 REMINDER: You can run a block using another rule:
WHEN house_locked IS true THEN run nighttime_rules

⚙️ 3. Actions: Defining a Sequence
Use ACTION when you want to describe what to do, not just conditions.
plaintext
Copy code
DEFINE ACTION welcome_user
  say "Welcome!"
  call "https://myapp.com/log/welcome"
END
Then trigger it like this:
WHEN user_logged_in IS true THEN welcome_user
 NB: ACTION focuses on what happens. BLOCK can have logic decisions inside it.

 4. Using Logic Files
As projects grow, split logic into separate files:
security.lang → for alarm and door rules
user.lang → for login, signup, user actions
aid_rules.lang → for NGO-based logic
 NOTE: You can include one file into another using:
INCLUDE "user.lang"

🛠️ 5. Logic Libraries
You can create reusable libraries like:
DEFINE BLOCK is_eligible
  IF age > 18 AND verified IS true THEN allow_entry
  ELSE deny_entry
END
Import is_eligible anywhere. This saves time when building similar systems.
✅ LOGIC USED: Reusability, modular thinking

👥 6. Team Collaboration Tips
Task	Best Practice
Working in teams	Split files by role or function
Testing rules	Use TRACE ON and mock data
Explaining logic	Add comments and use clear names
Updating logic	Version your logic files (v1, v2, etc.)
 WARNING: Avoid deeply nested logic unless necessary — keep it readable!

🧪 Project Example: NGO Aid Eligibility System
Files:
base_rules.lang
household_rules.lang
income_check.lang
Inside household_rules.lang:
DEFINE BLOCK check_household_size
  IF dependents > 3 THEN tag "large_household"
  ELSE tag "small_household"
END
In base_rules.lang:
INCLUDE "household_rules.lang"

WHEN application_received IS true THEN
  run check_household_size
✅ LOGIC USED
Modular rule logic
Separation of concern
File-based rule architecture
❓ QUESTION: What other modules might you add to this system? (e.g. health check, location filter)

🎓 Wrap-Up
Organizing logic is the secret to managing complexity. With BLOCKs, ACTIONs, and logic files, you build:
➤ Scalable systems
➤ Collaborative projects
➤ Reusable, smart logic libraries
Now your ClearLang projects are ready to grow without becoming messy spaghetti! 


