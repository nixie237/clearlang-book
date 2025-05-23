 Chapter 3: Creating Your Own Actions and Logic Blocks
ClearLang is powerful not just because of its readability — but because it’s expandable. You’re not limited to built-in actions like remind, say, or grant_access. In this chapter, you’ll learn how to:
Define your own custom actions
Group logic into reusable blocks
Organize rules into namespaces or modules
Keep your logic clean, readable, and maintainable

🔧 1. Defining Your Own Actions
Sometimes, you want ClearLang to do something specific to your app, device, or domain — like open_gate, start_lesson, or flag_user.
Instead of waiting for a built-in command, just define it yourself.
📌 Syntax:
DEFINE ACTION [action_name]
  [logic]
END
✅ Example:
DEFINE ACTION open_gate
  say "Gate is opening"
  send_signal "GATE_MOTOR_START"
END

IF user_verified IS true THEN open_gate
This makes ClearLang more domain-aware: now it speaks your language.

 2. Creating Reusable Logic Blocks
When you have several related actions or rules, it’s smart to group them into a named block — like a function in traditional programming.
📌 Syntax:
DEFINE BLOCK [block_name]
  [rules...]
END
✅ Example:
DEFINE BLOCK morning_routine
  IF time IS "6AM" THEN remind "Wake up"
  IF time IS "6:15AM" THEN start "CoffeeMachine"
  IF time IS "6:30AM" THEN play "MorningPlaylist"
END

# Call the block
WHEN time IS "6AM" THEN run morning_routine
This makes your logic more modular and clean — easier to test, reuse, and share.

 3. Using Namespaces and Modules
As your rules grow, it helps to group them by theme — think of modules like "folders" for logic.
You can prefix actions or blocks with a category:
DEFINE ACTION security.lock_doors
  send_signal "LOCK_ALL"
END

DEFINE BLOCK security.night_mode
  run security.lock_doors
  turn_off "all_lights"
  say "Good night"
END
Now, your rules are neatly organized. This is perfect for larger projects like:
Home automation
School apps
Medical or emergency systems
NGO program logic

 4. Passing Data into Actions (Optional)
You can also make actions more dynamic by passing values into them.
📌 Syntax:
DEFINE ACTION greet_user WITH name
  say "Hello, " + name
END

greet_user "James"
In future versions, you’ll be able to:
Use multiple parameters
Do math or logic with inputs
Return values (like a function)

5. Why This Matters
Writing ClearLang should feel like assembling LEGO blocks:
Build small, name them clearly
Snap them together into bigger logic
Reuse them across your system
That’s how you scale a logic language — from one rule to hundreds, without losing clarity.

🏁 What’s Next?
In Chapter 4, we’ll explore:
How to test and debug ClearLang rules
How to see why something triggered
How to trace rule outcomes for explainable logic
You’ll be able to answer:
“Why did this happen?”
“What rule triggered this?”
“What would have happened if…?”
Project Example 1: Smart Classroom Assistant
Let’s build a ClearLang logic set for a smart classroom that manages lessons, reminders, and breaks.
🧩 Define Custom Actions
DEFINE ACTION start_lesson
  say "Welcome students. Today's lesson is starting."
  turn_on "projector"
  play "lesson_intro_video"
END

DEFINE ACTION break_time
  say "Time for a 10-minute break!"
  play "relaxing_music"
END
🧱 Group into a Block
DEFINE BLOCK daily_routine
  IF time IS "8:00AM" THEN start_lesson
  IF time IS "10:00AM" THEN break_time
  IF time IS "10:15AM" THEN start_lesson
  IF time IS "12:00PM" THEN say "Lesson complete. Have lunch!"
END
Run the Block
WHEN day IS "Monday" THEN run daily_routine
✅ Use case: Schools or training centers with scheduled activities — no need for full programming!

Project Example 2: NGO Aid Eligibility Checker
Let’s build a ClearLang system to check if a family qualifies for food support, based on dependents and income.
 Custom Action
DEFINE ACTION approve_support
  log "Family approved for food aid"
  notify "AidOffice" WITH "New family qualified"
END

DEFINE ACTION deny_support
  log "Family does not meet criteria"
  notify "AidOffice" WITH "Review needed"
END
🔁 Eligibility Block
DEFINE BLOCK check_eligibility
  IF dependents > 3 AND income < 10000 THEN approve_support
  ELSE deny_support
END

# Sample run
WHEN form_submitted IS true THEN run check_eligibility
✅ Use case: NGOs, social workers, or relief programs that need to define eligibility rules clearly and fairly — without writing code.
