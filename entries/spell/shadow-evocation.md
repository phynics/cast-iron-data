+++
id = "ref/spell/shadow-evocation"
kind = "spell"
title = "Shadow Evocation"
aon = "SpellDisplay.aspx?ItemName=Shadow%20Evocation"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_evocation", path = "json/spells15.json" },
]
[[sources]]
publication = "core-rulebook"
page = "340"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Shadow"]
descriptors = ["shadow"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "see text"
effects = [
  { label = "Effect", value = "see text" },
]
duration = "see text"
saving_throw = "Will disbelief (if interacted with)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 5: Arcanist, Bard, Mesmerist, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 1 standard action
Components: V, S
Range: see text
Duration: see text
Saving throw: Will disbelief (if interacted with)
Spell resistance: yes
Effect: see text
Subschool: Shadow
Descriptors: shadow
:::

You tap energy from the Plane of Shadow to cast a quasi-real, illusory version of a sorcerer or
wizard evocation spell of 4th level or lower. Spells that deal damage have normal effects unless an
affected creature succeeds on a Will save. Each disbelieving creature takes only one-fifth damage
from the attack. If the disbelieved attack has a special effect other than damage, that effect is
one-fifth as strong (if applicable) or only 20% likely to occur. If recognized as a shadow
evocation, a damaging spell deals only one-fifth (20%) damage. Regardless of the result of the save
to disbelieve, an affected creature is also allowed any save (or
[spell resistance](ref/rule/spell-resistance)) that the spell being simulated allows, but the save
DC is set according to shadow evocation's level (5th) rather than the spell's normal level.

Non-damaging effects have normal effects except against those who disbelieve them. Against
disbelievers, they have no effect.

Objects automatically succeed on their Will saves against this spell.
