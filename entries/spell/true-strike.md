+++
id = "ref/spell/true-strike"
kind = "spell"
title = "True Strike"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "true_strike", path = "json/spells10.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Alchemist", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Investigator", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Medium", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, F (small wooden replica of an archery target)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Alchemist, Arcanist, Bloodrager, Inquisitor, Investigator, Magus, Medium, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, F (small wooden replica of an archery target)
Range: personal
Duration: see text
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** PRPG Core Rulebook pg 363

You gain temporary, intuitive insight into the immediate future during your next attack. Your next
single attack roll (if it is made before the end of the next round) gains a +20 insight bonus.
Additionally, you are not affected by the miss chance that applies to attackers trying to strike a
concealed target.

### Mythic True Strike

**Sources:** Mythic Adventures pg 110\
The affected attack bypasses all [damage reduction](ref/rule/damage-reduction).

_Augmented (2nd):_ If you expend two uses of mythic power, you gain a +10 insight bonus on your
second attack that round and a +5 insight bonus on your third attack that round. The second and
third attacks can be on your turn or on another creature's turn before your next turn (such as when
you attempt an attack of opportunity).
