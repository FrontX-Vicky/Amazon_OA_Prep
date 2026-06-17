# Amazon Leadership Principles (LP) - Work Simulation Guide

The **Work Simulation (15 minutes)** evaluates how you respond to typical situations faced by an Amazon SDE. You will be given scenarios (like a tight deadline, a failing service, a disagreement with a PM) and asked to choose the best and worst actions. 

**Every correct answer is rooted in one of Amazon's 16 Leadership Principles.**

Here are the most critical ones for an SDE 2 and how to apply them in the Work Simulation:

### 1. Customer Obsession
*Leaders start with the customer and work backwards.*
- **Scenario:** A product manager wants to rush a feature that has a clunky UI, but engineering wants to delay to make it perfect.
- **Action:** Prioritize what the customer actually needs. If the customer needs it *now* to solve a critical issue, ship a functional MVP. If the clunky UI breaks the customer experience, push back. **Always choose the option that gathers customer feedback or prioritizes their immediate pain points.**

### 2. Ownership
*Leaders are owners. They think long term and don't sacrifice long-term value for short-term results.*
- **Scenario:** You notice a bug in a piece of code owned by another team that is causing your service to fail.
- **Action:** **Never say "that's not my job."** The best action is to reach out to the other team, offer to help fix it, or submit a pull request to their repository yourself. Take responsibility for the end-to-end outcome.

### 3. Deliver Results
*Leaders focus on the key inputs for their business and deliver them with the right quality and in a timely fashion.*
- **Scenario:** You are falling behind on a sprint and won't make the deadline.
- **Action:** Communicate early. Don't hide the delay. Prioritize the most critical features (MVP) to deliver *something* on time, and communicate the trade-offs to stakeholders.

### 4. Bias for Action
*Speed matters in business. Many decisions and actions are reversible and do not need extensive study.*
- **Scenario:** You have 80% of the data needed to make a technical decision, but getting the last 20% will take a week.
- **Action:** Make the decision now based on the data you have. If it's a "two-way door" (a reversible decision like an internal API structure), move fast. (Note: Don't use Bias for Action for irreversible "one-way doors" like dropping a production database).

### 5. Insist on Highest Standards
*Leaders have relentlessly high standards.*
- **Scenario:** A teammate submits a pull request with messy code but it works and fixes a P1 bug.
- **Action:** For a P1 (system down), ship the fix (Customer Obsession/Deliver Results), but immediately create a follow-up ticket to refactor the code and insist they fix it. Do not let bad code live in the codebase permanently.

### 6. Dive Deep
*Leaders operate at all levels, stay connected to the details, audit frequently.*
- **Scenario:** A metric drops by 5% and no one knows why.
- **Action:** Don't guess. Pull the logs, look at the code, and trace the issue to the root cause. Choose the option that involves gathering hard data and metrics over relying on intuition.

## Answering Strategy for the OA
When given a multiple-choice scenario:
1. Identify the core conflict (e.g., Speed vs. Quality = Bias for Action vs. Highest Standards).
2. Look for the "Amazon" answer: It usually involves taking ownership, communicating transparently with data, and keeping the customer happy.
3. **Avoid:** Ignoring the problem, blaming others, making assumptions without data, or building features customers didn't ask for.
