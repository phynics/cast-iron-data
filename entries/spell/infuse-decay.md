+++
id = "ref/spell/infuse-decay"
kind = "spell"
title = "Infuse Decay"
aon = "SpellDisplay.aspx?ItemName=Infuse%20Decay"
source_ids = ["curse-of-the-crimson-throne"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "infuse_decay", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/imbue-with-spell-ability" },
]
[[sources]]
publication = "curse-of-the-crimson-throne"
page = "453"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, F (a set of fine mortician's tools worth 100 gp)"
range = "touch"
effects = [
  { label = "Area", value = "corporeal undead touched; see text" },
]
duration = "permanent until discharged (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Arcanist, Sorcerer, Witch, Wizard
Casting time: 10 minutes
Components: V, S, F (a set of fine mortician's tools worth 100 gp)
Range: touch
Duration: permanent until discharged (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Area: corporeal undead touched; see text
Descriptors: evil
:::

This spell functions as per [imbue with spell ability](ref/spell/imbue-with-spell-ability), except
it can only target corporeal undead creatures, and can only transfer touch spells. The number and
level of spells the subject can be granted depends on the undead creature's Hit Dice; even multiple
castings of infuse decay can't exceed this limit.

|HD of Undead|Touch Spells Infused|
| --- | --- |
|5 or lower|One 1st-level spell|
|06-10|One or two 1st-level spells|
|11 or higher|One or two 1st-level spells and one 2nd-level spell|

Once you cast infuse decay, you can't prepare a new 4th-level spell to replace it (see
_[imbue with spell ability](ref/spell/imbue-with-spell-ability)_ for further details). The infused
spell is automatically triggered the next time the undead creature makes a successful touch attack
or attack with a natural weapon. An intelligent undead can choose not to trigger the spell on a hit.
Only one infused spell can be triggered per attack. An intelligent undead can choose which spell to
trigger if it has more than one infused spell. A nonintelligent undead triggers a random spell when
it hits with a natural weapon. Only one spell can be triggered per round, regardless of the number
of attacks the undead makes.
