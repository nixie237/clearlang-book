Chapter 2: The Core of ClearLang
Welcome to the foundation of ClearLang. Before we build complex rules or connect to apps, we need to understand the building blocks that power every ClearLang statement.
🧱 1. Variables: Storing Information
A variable in Clear-Lang holds a piece of information. Think of it like a labeled box where you can store something — a name, a number, a mood, a status.
Syntax:css
SET [variable_name] TO [value]
Examples:vbnet
SET temperature TO 27
SET status TO "busy"
SET verified TO true
Variables can store:
Numbers (27)
Text ("busy")
Boolean values (true, false)
Dates and times (coming soon!)

2. Conditions: Making Decisions
A condition checks if something is true. If it is, an action follows. If not, we can choose to do something else.
Syntax:css
IF [condition] THEN [action]
Examples:arduino
IF temperature > 30 THEN remind "Drink water"
IF status IS "busy" THEN delay notifications
You can also use:
= or IS for equality
> and < for numbers
AND / OR for combining multiple conditions

 3. Actions: Doing Things
Actions are what your rule does. These are predefined verbs that the ClearLang engine understands.
Examples of built-in actions:
remind — Send a reminder
grant_access — Allow a user into something
log — Save something to history
say — Output a message
send — Deliver a message, notification, or email
change — Update a variable or setting
delay_notifications — Temporarily pauses notifications
Example:vbnet
IF verified IS true THEN grant_access "dashboard"

🔍 4. Comparisons: How We Evaluate
ClearLang supports the most common comparison operators:
Operator	Meaning	Example
IS / =	Equals	IF mood IS "happy"
>	Greater than	IF age > 18
<	Less than	IF count < 5
>=	Greater than or equal	IF score >= 80
<=	Less than or equal	IF balance <= 100
!=	Not equal to	IF status != "offline"
Combine comparisons using:
AND: All must be true
OR: At least one must be true

5. Logic Flow: Creating Full Thought Chains
Let’s combine everything into a full logic flow:plaintext
SET weather TO "rainy"
IF weather IS "rainy" THEN remind "Carry an umbrella"
ELSE remind "Enjoy the sunshine!"
Or with multiple conditions:Plain-text
IF age > 18 AND verified IS true THEN grant_access "adult_section"ELSE say "Access denied"
These kinds of readable statements are what make ClearLang powerful — it’s code that speaks like a conversation.

Pro Tip: You Can Chain Actions Too
You’re not limited to just one action per rule:
Perl code
IF time IS "7AM" THEN remind "Stretch" AND say "Good morning!"


NOTE
Comments are ignored by the ClearLang engine


