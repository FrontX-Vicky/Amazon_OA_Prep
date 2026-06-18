# Amazon Work Simulation - Mock Scenarios & Answers

The Work Simulation is a 15-minute interactive test where you receive emails or instant messages from virtual colleagues and must select the best (and sometimes worst) course of action from a multiple-choice list. 

Here are the most common scenario archetypes you will face, and how to apply the Leadership Principles (LPs) to solve them.

---

### Scenario 1: The Tight Deadline vs. Quality (Bias for Action vs. Insist on Highest Standards)
**Situation:** You are building a new internal tool. The deadline is in 2 days. You realize that to make the code truly scalable for future use, you need to refactor a major component, which will take 5 days. 
**Options:**
1. Refactor the code and delay the launch by 3 days. Quality is the most important thing.
2. Launch on time with the current code, but document the technical debt and schedule a refactor for the next sprint.
3. Work 24 hours straight to try and finish the refactor on time.
4. Ask the customer to push the deadline back.

**Best Action:** **Option 2.** 
**Why:** *Deliver Results* and *Bias for Action*. For an internal tool, launching a working MVP on time is usually better than delaying for "perfect" future-proof code, as long as you take *Ownership* of the technical debt by documenting it and scheduling the fix. Option 3 is a red flag for burnout, and Option 1 ignores the deadline without attempting a compromise.

---

### Scenario 2: The Cross-Team Dependency (Ownership)
**Situation:** Your feature launch is blocked because Team B hasn't delivered the API you need. They are busy and say it will take them another week. Your deadline is tomorrow.
**Options:**
1. Tell your manager that Team B is blocking you and there's nothing you can do.
2. Escalate to Team B's manager and demand they finish it immediately.
3. Look at Team B's repository, write the API code yourself, and submit a Pull Request to them so they only have to review and approve it.
4. Launch your feature with mock data so it looks finished.

**Best Action:** **Option 3.**
**Why:** *Ownership* and *Bias for Action*. "That's not my job" is the worst possible answer at Amazon. By writing the code for the other team and submitting a PR, you remove the blocker while respecting their time. 

---

### Scenario 3: Disagreement with a Stakeholder (Customer Obsession)
**Situation:** A Product Manager wants to add a pop-up ad to the checkout page because it will increase short-term revenue by 5%. You believe this ruins the user experience.
**Options:**
1. Do what the PM says because they own the product decisions.
2. Refuse to build it because you are the engineer.
3. Suggest running an A/B test on a small percentage of users to see if the pop-up causes cart abandonment, and use the data to make the decision.
4. Complain to your manager about the PM's bad idea.

**Best Action:** **Option 3.**
**Why:** *Customer Obsession* and *Dive Deep*. Amazon is heavily data-driven. Instead of arguing based on opinions, the best answer always involves gathering metrics to see what actually benefits the customer. 

---

### Scenario 4: The Vague Requirements (Dive Deep)
**Situation:** A senior manager asks you to "make the search bar faster." They don't provide any metrics or specifics. 
**Options:**
1. Start rewriting the search algorithm to be as optimal as possible.
2. Ask the manager to clarify exactly what "faster" means before doing anything.
3. Set up monitoring on the search bar to measure current latency (P50, P90, P99) to establish a baseline, then analyze where the bottlenecks are.
4. Add a caching layer because that usually speeds things up.

**Best Action:** **Option 3.**
**Why:** *Dive Deep*. You shouldn't blindly act (Option 1 & 4) without data, but you also shouldn't just push the work back to the manager (Option 2). Gathering your own data to establish a baseline is the Amazon way.

---

### Strategy Tips for the OA
- If a scenario involves a **security flaw** or **double-charging a customer**, you MUST delay the launch. Customer Trust is paramount. 
- If a scenario involves **minor UI bugs**, you should usually launch on time and patch later (Bias for Action).
- Whenever an option says "Gather data/metrics", it is usually the right answer.
