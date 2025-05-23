
 Chapter 14: Creating Custom Actions & Extending ClearLang
 What You’ll Learn:
How to define your own custom actions
How to modify or extend the interpreter
How to build specialized behavior
🛠️ Why Extend It?
Imagine wanting to
Send an email
Update a database
Open a browser tab You can extend ClearLang to do that.
 Adding a Custom Action
Modify run_action():
python
elif action.startswith("email"):
    print("📧 Sending email:", action.replace("email", "").strip('" '))
Then use in your .clr file:
clr
IF tasks_done >= 5 THEN email "Well done! Task completed 🎉"
➡️ You can add any action: save to file, connect to Telegram bot, trigger IoT devices, etc.

🧠 Advanced Logic Idea: Chains
clr
IF weather IS "raining" THEN
    remind "Close the windows"
    email "It's raining at home!"
With engine updates, we can allow multiple actions per condition block.