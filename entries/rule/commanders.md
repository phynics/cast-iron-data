+++
id = "ref/rule/commanders"
kind = "rule"
title = "Commanders"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "commanders", path = "json/rules_campaign_types05.json" },
]
[[sources]]
publication = "ultimate-campaign"
page = "239"

[fields]
kind = "none"
+++

An army's commander helps maximize its effectiveness and can provide special bonuses to an army. The
commander can be a PC or NPC. Unless you decide to command an army personally or the GM allows you
to recruit an exceptional commander through adventuring and roleplaying, a new army's commander is
an unexceptional leader who provides no bonuses to the army.

The Mass Combat Army Sheet has a space to record information about the commander of each of your
armies. In addition, there's also a space to record information for a general - a general is a
character (often you) assigned to administrate your armies, but is primarily a figurehead and grants
no bonuses herself unless actively leading a particular army. The relevant information is as follows
(assume a value of 0 unless otherwise specified).

**Name:** This lists the commander's name (and class and level, if notable).

**Charisma Modifier:** This lists the commander's Charisma modifier. It is added to the army's
Morale checks.

**Profession (soldier):** This is the commander's ranks in Profession (soldier). Divide the number
of ranks by 5 (minimum 0) and add that number to the army's Morale checks.

**Leadership:** The commander's character level + Charisma modifier. If the commander is a monster,
use HD instead of character level. If the commander has the [Leadership](ref/feat/leadership) feat,
increase this value by 3. This number is a prerequisite for some boons.

**Boons:** This lists the [boons](ref/rule/boons) the commander knows. A commander's maximum number
of boons known is 1, plus 1 for every 5 ranks in Profession (soldier). A new or unexceptional
commander might know no boons at first, but can gain them from victories in battle. If you're a
[kingdom leader](ref/rule/kingdom-leader-commanders) acting as a commander, you automatically have
one boon appropriate to your leadership role.

The commander must be active with the army to grant a bonus on Morale checks or a boon to the army.
Being active requires spending at least 3 days per week with the army. An army without a commander
(whether because the commander is dead or because she isn't spending enough time with the army)
loses 1 Morale per week. You may offset this loss by doubling the army's Consumption that week.

If you have an army without a commander and you have no commanders available to fill that role, you
may promote a unit from the army to be an unexceptional commander. This commander has a +0 Charisma
modifier, 0 ranks in Profession (soldier), and a Leadership score based on the level or HD of a
typical unit in that army.
