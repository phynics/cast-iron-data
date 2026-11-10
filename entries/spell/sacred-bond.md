+++
id = "ref/spell/sacred-bond"
kind = "spell"
title = "Sacred Bond"
aon = "SpellDisplay.aspx?ItemName=Sacred%20Bond"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sacred_bond", path = "json/spells8.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "240"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 round"
components = "V, S, F (a pair of golden bracelets worth 100 gp each worn by both you and the target)"
range = "touch; see text"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Inquisitor, Paladin\
3: Cleric, Oracle, Warpriest
Casting time: 1 round
Components: V, S, F (a pair of golden bracelets worth 100 gp each worn by both you and the target)
Range: touch; see text
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched
Subschool: Healing
:::

To use this spell, you first touch the intended recipient, creating a sympathetic field of healing
energies between you. Once the spell has been cast, you and the target may cast conjuration
(healing) spells with a range of touch upon each other so long as you are within close range (25
ft. + 5 ft./2 levels). Should either you or the target remove your bracelet, the spell immediately
ends.
