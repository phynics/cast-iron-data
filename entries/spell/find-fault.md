+++
id = "ref/spell/find-fault"
kind = "spell"
title = "Find Fault"
aon = "SpellDisplay.aspx?ItemName=Find%20Fault"
source_ids = ["arcane-anthology"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "find_fault", path = "json/spells4.json" },
]
[[sources]]
publication = "arcane-anthology"
page = "24"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Medium", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "1 creature" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 3: Arcanist, Bloodrager, Bard, Inquisitor, Magus, Medium, Oracle, Psychic, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: 1 creature
:::

You instantly learn many of the target's weaknesses, as if you had made an appropriate Knowledge
skill check with a result equal to 20 + your caster level. Additionally, your first melee or ranged
attack roll against the creature before the end of your next turn gains a +5 insight bonus. If the
creature is polymorphed, disguised, or hidden by an illusion and you are not aware of it's true
form, this spell fails as if the target has [spell resistance](ref/rule/spell-resistance) you failed
to penetrate (the GM may have you attempt a caster level check to conceal the true reason for the
spell's failure).
