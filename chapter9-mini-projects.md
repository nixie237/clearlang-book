
Chapter 9: Extending ClearLang with Custom Actions
📘 What You’ll Learn in This Chapter
In this chapter, you’ll learn how to: ➤ Create custom actions in ClearLang to extend its functionality
➤ Register these actions with the ClearLang engine
➤ Use custom actions in your rules just like built-in ones
➤ Build reusable logic components for greater efficiency
By the end, you’ll be able to expand ClearLang’s capabilities to match your unique needs and use cases.

🧱 1. Why Use Custom Actions?
Custom actions allow you to define new verbs and commands that are specific to your system. This lets you:
Create tailored behavior for your app or process
Avoid repetition in your rules by reusing actions
Make logic rules even more human-readable
For example, instead of writing:
IF age > 65 THEN send_email "Offer senior discount"
You could create a custom action send_discount_email that simplifies your rule:
IF age > 65 THEN send_discount_email

🏗️ 2. How to Create a Custom Action
Custom actions are defined by their name and behavior. Here's how:
Step 1: Define the Action
You create an action by specifying what it does. Let’s say we want to define send_discount_email:
DEFINE ACTION send_discount_email
  send_email "Senior Discount"
END
Step 2: Register the Action
After defining your action, you need to register it with the engine so it can be used anywhere in your rules. You do this with a simple register command:
REGISTER send_discount_email
Step 3: Use the Action in Your Logic
Now, you can use it just like any built-in ClearLang action!
IF age > 65 THEN send_discount_email

 3. Example: Custom Action for Payment Processing
Let’s imagine you want to automate payment processing. You could define a custom action like process_payment:
DEFINE ACTION process_payment
  charge "credit_card"
  send_receipt "email"
END
Now you can use it in your rules:
IF order_amount > 100 THEN process_payment
Logic Breakdown:
charge — triggers the payment process
send_receipt — sends the receipt email after successful payment

🧩 4. Creating More Complex Actions
You can also define actions that accept parameters. For example, a send_message action might accept a message and a recipient:
DEFINE ACTION send_message (recipient, message)
  send_email recipient WITH message
END
And in your rules:
IF user_status IS "inactive" THEN send_message user_email "We miss you!"
This keeps your logic neat and scalable, allowing you to pass different inputs to your custom actions.

🧠 5. Reusable Action Templates
Once defined, your custom actions can be reused in multiple rules. This is efficient and prevents redundancy.
DEFINE ACTION notify_admin (alert_type)
  log alert_type
  send_email "admin@example.com" WITH alert_type
END
You can now use notify_admin in multiple rules:
IF server_down THEN notify_admin "Server Down"
IF user_error THEN notify_admin "User Error"
 6. Best Practices for Custom Actions
Keep actions focused: Each action should do one thing well. Don't try to overload them.
Use parameters wisely: Limit the number of parameters to make your actions easier to reuse.
Name actions intuitively: Choose names that describe what the action does (e.g., send_confirmation_email).
🧪 7. Project Example: Inventory System
You’re building an inventory system for a store, and you want to create custom actions for restocking and order alerts.
Define custom actions:
DEFINE ACTION restock_item (item_id, quantity)
  update_inventory item_id WITH +quantity
  log "Restocked item {item_id} with {quantity}"
END

DEFINE ACTION alert_low_stock (item_id)
  send_email "manager@example.com" WITH "Low stock alert: {item_id}"
END
1.
Use them in your logic:
IF item_quantity < 5 THEN alert_low_stock item_id
IF order_quantity > 50 THEN restock_item item_id 50
How It Helps:
Restock action automatically updates inventory.
Low stock alerts ensure the manager is notified promptly.

🧠 Wrap-Up
By defining your own actions, you can:
Tailor ClearLang to meet your exact needs
Simplify complex workflows
Make your rules cleaner and more intuitive
Reuse actions to keep logic DRY (Don’t Repeat Yourself)
Now you’re not just using ClearLang — you’re extending it to suit any real-world scenario.

❓ Quick Question + Solution
Q: Can I create an action that triggers other actions in ClearLang?
A: Absolutely! You can define a "composite action" that calls multiple actions in sequence. For example:
DEFINE ACTION process_order (order_id)
  verify_order order_id
  charge_payment order_id
  send_confirmation_email order_id
END
This makes complex workflows seamless and reusable.

