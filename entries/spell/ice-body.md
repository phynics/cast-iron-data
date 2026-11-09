+++
id = "ref/spell/ice-body"
kind = "spell"
title = "Ice Body"
aon = "SpellDisplay.aspx?ItemName=Ice%20Body"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "ice_body", path = "json/spells5.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "224"

[fields]
kind = "spell"
school = "transmutation"
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 7: Arcanist, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: no
Target: you
Descriptors: cold
:::

Your form transmutes into living ice, granting you several abilities. You gain the cold subtype and
[damage reduction](ref/rule/damage-reduction) 5/magic. You are immune to ability score damage,
blindness, critical hits, deafness, disease, drowning, electricity, poison, stunning, and all spells
or attacks that affect your physiology or respiration, because you have no physiology or respiration
while this spell is in effect. You cannot drink (and thus can't use potions) or play wind
instruments.

Your unarmed attack deals damage equal to a club sized for you (1d4 for Small characters or 1d6 for
Medium characters) plus 1 point of cold damage, and you are considered armed when making unarmed
attacks. You may burrow through nonmagical ice or snow at your base speed as easily as a fish swims
through water. You can move through magical ice and snow if you succeed on a caster level check
(1d20 + caster level) against a DC of 11 + the caster level of the effect; you automatically succeed
on caster level checks against effects that you created. Your passage through snow and ice in this
fashion leaves behind no tunnel or hole.
