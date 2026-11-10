+++
id = "ref/spell/imbue-with-spell-ability"
kind = "spell"
title = "Imbue with Spell Ability"
aon = "SpellDisplay.aspx?ItemName=Imbue%20with%20Spell%20Ability"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "imbue_with_spell_ability", path = "json/spells14.json" },
]
[[sources]]
publication = "core-rulebook"
page = "299"

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched; see text" },
]
duration = "permanent until discharged (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 4: Cleric, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 10 minutes
Components: V, S, DF
Range: touch
Duration: permanent until discharged (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: creature touched; see text
:::

You transfer some of your currently prepared spells, and the ability to cast them, to another
creature. Only a creature with an Intelligence score of at least 5 and a Wisdom score of at least 9
can receive this boon. Only cleric spells from the schools of abjuration, divination, and
conjuration (healing) can be transferred. The number and level of spells that the subject can be
granted depends on its Hit Dice; even multiple castings of imbue with spell ability can't exceed
this limit.

|HD of Recipient|Spells Imbued|
| --- | --- |
|2 or lower|One 1st-level spell|
|3-4|One or two 1st-level spells|
|5 or higher|One or two 1st-level spells and one 2nd-level spell|

The transferred spell's variable characteristics (range, duration, area, and the like) function
according to your level, not the level of the recipient.

Once you cast imbue with spell ability, you cannot prepare a new 4th-level spell to replace it until
the recipient uses the imbued spells or is slain, or until you dismiss the imbue with spell ability
spell. In the meantime, you remain responsible to your deity or your principles for the use to which
the spell is put. If the number of 4th-level spells you can cast decreases, and that number drops
below your current number of active imbue with spell ability spells, the more recently cast imbued
spells are dispelled.

To cast a spell with a verbal component, the subject must be able to speak. To cast a spell with a
somatic component, it must be able to move freely. To cast a spell with a material component or
focus, it must have the materials or focus.
