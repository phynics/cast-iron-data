+++
id = "ref/spell/balance-of-suffering"
kind = "spell"
title = "Balance of Suffering"
aon = "SpellDisplay.aspx?ItemName=Balance%20of%20Suffering"
source_ids = ["healers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "balance_of_suffering", path = "json/spells12.json" },
]
[[sources]]
publication = "healers-handbook"
page = "8"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 6 },
  { class = "Inquisitor", level = 6 },
  { class = "Occultist", level = 6 },
  { class = "Oracle", level = 6 },
  { class = "Shaman", level = 6 },
  { class = "Spiritualist", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "1 living creature and another single living or undead creature" },
]
duration = "instantaneous"
saving_throw = "Will half; see text"
spell_resistance = "yes; see text"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 6: Cleric, Inquisitor, Occultist, Oracle, Shaman, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will half; see text
Spell resistance: yes; see text
Targets: 1 living creature and another single living or undead creature
Subschool: Healing
:::

You borrow life force from a living creature and infuse it into another living creature, potentially
wreaking destruction on the former and bolstering the life of the latter.

Choose an initial target, which must be alive, and a secondary target, which must be alive or
undead. The initial target is dealt a number of points of damage equal to 9d6 + 1 point per caster
level. A successful Will saving throw halves the damage dealt. The target might die from damage even
if it succeeds on its saving throw. If the secondary target is a living creature, it regains a
number of hit points equal to the amount of damage taken by the initial target. If the secondary
target is undead, it instead takes an amount of damage equal to that dealt to the initial target.
The secondary target can halve the healing imparted or harm inflicted to it with a successful Will
saving throw (although a secondary target receiving healing can forgo this saving throw as normal).
This spell is subject to the [spell resistance](ref/rule/spell-resistance) of the initial target; if
the secondary target is unwilling, this spell is also subject to the secondary target's spell
resistance. If the spell does not penetrate the initial target's spell resistance, it fizzles with
no effect. If it does not penetrate the secondary target's spell resistance, the initial target is
still harmed as described, but the secondary target is not healed or harmed.
