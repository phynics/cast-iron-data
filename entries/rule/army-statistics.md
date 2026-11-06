+++
id = "ref/rule/army-statistics"
kind = "rule"
title = "Army Statistics"
source_ids = ["ultimate-campaign"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "army_statistics", path = "json/rules_campaign_types05.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Campaign pg 234

The description of each army is presented in a standard format. Each category of information is
explained and defined on the following pages.

**Name:** This is the name of the army. This could be a mercenary company's name, such as "Thokk's
Bloodragers," a formal regiment number such as "7th Royal Cavalry," or an informal name such as
"Thokk's Bloodragers,"

**XP:** This is the XP awarded to the PCs if their army defeats this army, and is the same as an XP
award for an encounter with a CR equal to the army's ACR (see below).

**Alignment:** An army's alignment has no effect on its statistics, and is just a convenient way to
summarize its attitude with two letters. It is usually the same alignment as a typical unit in that
army.

**Size:** The army's size determines not only how many individual units exist in the army, but also
the army's ACR. Table 4-15: Army Sizes

### Table 4-15: Army Size

|Army Size|Number of Units|ACR|
| --- | --- | --- |
|Fine|1|CR of individual creature -8|
|Diminutive|10|CR of individual creature -6|
|Tiny|25|CR of individual creature -4|
|Small|50|CR of individual creature -2|
|Medium|100|CR of individual creature|
|Large|200|CR of individual creature +2|
|Huge|500|CR of individual creature +4|
|Gargantuan|1,000|CR of individual creature +6|
|Colossal|2,000|CR of individual creature +8|

**Type:** This lists the nature of the army's individual units, such as "orcs (warrior 1)- or
-trolls." These rules assume all units in an army are essentially the same; if an army of 100 orc
warriors 1 (meaning 1st-level warriors) actually has a few half-orc warriors or some orc barbarians,
their presence has no effect on the army's statistics. If an army has a large number of units that
are different than the typical unit in that army, and these differences are enough to change the
army's stat block, it is generally best to treat the group as two separate armies with different
stat blocks.

**hp:** An army's hit points equal its ACR × the average hp value of 1 HD of the army's units (3.5
for d6 HD, 4.5 for d8 HD, 5.5 for d10 HD, and 6.5 for d12 HD). For example, warriors have d10 HD, so
an ACR 1 army of warriors has 5.5 × 1 = 5.5 hp, rounded down to 5 hp. Note that only damage from
other armies can reduce an army's hp; a non-army attacking an army is mostly ineffective, though you
can treat the attacker as a Fine army if you want to determine the outcome of the attack. As with
standard game effects that affect hit points, abilities that reduce hp damage or healing by half (or
any other fraction) have a minimum of 1 rather than 0.

**Army Challenge Rating (ACR):** This is based on the CR of an individual unit from the army and the
army's size, and scales like CRs for monsters. To determine ACR, see Table 4-15: Army Sizes and
apply the modifier for the army's size to the CR of an individual unit in the army. If an army is
cavalry, use the mount's CR or the rider's CR, whichever is higher. For example, an individual orc
warrior 1 is CR 1/3, so an army of 100 orc warriors 1 is ACR 1/3; an army of 500 orc warriors 1 is
ACR 3 (4 steps greater than the standard 100-unit army). If a group's ACR would be lower than 1/8,
it doesn't count as an army; add more troops until you reach an ACR of 1/8 or higher.

**Defense Value (DV):** This is a static number the army uses to resist attacks, much like an
individual creature's AC. The army's DV is equal to ACR + 10 + any bonuses from fortifications or a
settlement's [Defense score](ref/rule/defense).

**Offense Modifier (OM):** This is a modifier added to a d20 roll to determine the army's chance of
success, much like an individual creature's attack bonus. The army's OM is equal to its ACR. If the
army has the ability to make ranged attacks, that's mentioned here. Melee attacks and ranged attacks
use the same OM unless an ability says otherwise.

**Tactics:** These are any army tactics the army has at its disposal.

**Resources:** These are any [army resources](ref/rule/army-resources) the army has at its disposal.

**Special:** This section lists any [special abilities](ref/rule/special-abilities) the army has.

**Speed:** This number indicates how many 12-mile hexes the army traverses in a day's march.
Marching through difficult terrain halves the army's speed. Use
[Table 7-6: Movement and Distance](ref/rule/movement) to determine the army's speed based on the
speed of its individual units.

**Morale:** This number represents how confident the army is. Morale is used to determine changing
battle tactics, whether or not an army routs as a result of a devastating attack, and similar
effects. Morale is a modifier from -4 (worst) to +4 (best). A new army's starting morale is +0.
Morale can be further modified by the army's commander and other factors. If an army's Morale is
ever reduced to -5 or lower, the army disbands or deserts and you no longer control it.

**Consumption:** This is how many Build Points (BP) an army consumes each week (unlike most kingdom
expenses, this cost is per week, not per month), representing the cost to feed, hydrate, arm, train,
care for, and pay the units. An army's base Consumption is equal to its ACR divided by 2 (minimum
1). If you fall behind on paying the army's Consumption, reduce its Morale by 2; this penalty ends
when you catch up on the army's pay.

**Commander:** This entry lists the army's commander and the commander's Charisma modifier, ranks in
Profession (soldier), and Leadership score. The commander must be able to communicate with the army
(possibly using [message](ref/spell/message) spells and similar magical forms of communication) in
order to give orders or provide a bonus on the army's rolls.
