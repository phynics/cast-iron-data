+++
id = "ref/rule/contingency-services"
kind = "rule"
title = "Contingency Services"
source_ids = ["cohorts-and-companions"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contingency_services", path = "json/rules_subsystems01.json" },
]
[[sources]]
publication = "cohorts-and-companions"
page = "28"

[fields]
kind = "none"
+++

Contingency services are similar to contacts, but represent paying hirelings in advance for future
services that begin after a specified signal or time limit. Unlike contacts, most contingency
services are arranged as a single transaction, buying one service performed in case of a specific
event. The first step to arranging for such services is finding appropriate hirelings to pay for the
job. With a successful DC 15 Diplomacy check, a character locates 1st-level commoners, experts, or
warriors in a small town or larger settlement. At the GM's discretion, you can recruit higher-level
hirelings by increasing the DC by 5 per level above 1st. Enlisting hirelings with PC classes or rare
skills increases the DC by 5. The highest-level hireling you can find in a settlement is at most
twice the level of spellcasting available in that settlement. The modifiers for settlement size also
apply on Diplomacy checks to hire contingency services (Pathfinder RPG GameMastery Guide 205). A
successful check locates 1d6 skeptical or 2d6 wary hirelings. Exceeding the DC by 5 allows you to
add 1d6 hirelings or increase the Trust of your hirelings by 1.

Characters with [Leadership](ref/feat/leadership) can use followers to perform contingency services.
Though followers wish to help their leader, they can still decide a specific task is too dangerous
or questionable for them, and refuse to undertake it. Followers have a base Trust of 4 and charge
one-tenth the normal wages.

**Negotiation:** When hiring contingency services, you need to outline what you want your hirelings
to do, and under what circumstances you want them to do it. Examples include watching over an ally
(or animal companion or mount) or business and defending it if attacked, attempting to recover your
body from a dungeon and have you raised from the dead if you don't return to town in 2 weeks, paying
your fines to get you out of jail if you send word you've been arrested, or sending reinforcements
to a specified location if contacted by carrier pigeon.

Negotiation checks work as for contacts, though the Risk of contingency services comes from the
danger involved in performing the task (should it prove necessary), even if the task is perfectly
legal and moral. While you can arrange for illegal contingency services (such as paying an assassin
to murder anyone who kills you), the risk of the task is more important than the legality. If Risk
exceeds a hireling's Trust, a hireling will not automatically refuse the job, but this adds 5 to the
result of her opposed Diplomacy check per category of difference. Tasks generally have a Risk of 1,
adjusted as follows.

|Danger Modifier|Condition|
| --- | --- |
|+1|Challenging wilderness terrain (coastalwaters, hills, plains, forests)|
|+1|Hostile nonsentient inhabitants (CR equal to or less than hireling's level)|
|+1|Unfriendly sentient inhabitants (CR exceeding hireling's level)|
|+2|Harsh climate/terrain (arctic, cavern, deep water, desert, mountain, swamp)|
|+2|Hostile sentient inhabitants (CR exceeding hireling's level)|

**Cost:** You must pay hirelings up front for all the work you expect them to do. Hireling wages are
based on the most dangerous work they perform each day - if you arrange for a group of mercenaries
to watch over your horses and defend the horses if attacked, you must pay them both for the amount
of time you wish them to watch over the stable, and for engaging in a fight. Securing service
requires at least one week's wages paid in advance, though you can put more into this retainer fund.
Once service begins, hirelings deduct their wages from the fund automatically.

|Risk Level|Category|Base Cost per Hireling^[1](ref/rule/contingency-services#footnote-b)^|
| --- | --- | --- |
|1|Harmless|3 sp/day|
|2|Questionable|6 sp/day|
|3|Hazardous|1 gp/day|
|4|Deadly|3 gp/day|
|5|Suicidal|3 pp/day|

When funds run out, hirelings may remain on duty. Attempt a new negotiation check (even if you are
not physically present) each day or your hirelings abandon their task. Hirelings who remain expect
double pay for unpaid days worked. Failure to pay immediately reduces the hirelings' Trust to 1.

|Trust Modifier|Condition|
| --- | --- |
|+1|Retainer exceeds one month's wages|
|-1|You are absent over a month|
|-1|Retainer runs out of money|

**Emergency Funds:** You may entrust emergency funds to your hirelings for spellcasting, bribes,
etc. If their Trust is below 4, make an opposed Diplomacy check each month with a -5 penalty per
Trust level below 3. Failure results in embezzlement squandering 1d10×10% of your emergency funds.

**Success:** Determining if hirelings can successfully carry out the contingency service you pay
them for is handled with a skill or ability check, as it is with contacts (for more information see
Negotiation Checks on page 151 of Ultimate Campaign). A failed check can be retried 1d6 hours later,
with a -1 penalty per failed check that day. Failure by 5 or more typically results in a failure so
severe the hirelings give up or are incapable of trying again. The GM is the ultimate arbiter of
what skill checks are appropriate, with a few examples given below as guidance.

|Relevant Check|Task|
| --- | --- |
|Bluff, Diplomacy, or Intimidate|Negotiate ransom for hostages or corpses|
|Disable Device or Strength check|Break into locked building|
|Perception|Guard against ambush or theft|
|Disguise or Stealth|Sneak into or out of enemy camp or lair|
|Survival|Find creature or body in wilderness, move safely through wilderness|
|Strength check (+BAB)|Fight past enemy guards to reach PCs|

###### ^1^ {#footnote-b}

Multiply cost by the level of each hireling squared.
