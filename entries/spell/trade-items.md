+++
id = "ref/spell/trade-items"
kind = "spell"
title = "Trade Items"
aon = "SpellDisplay.aspx?ItemName=Trade%20Items"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "trade_items", path = "json/spells10.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "226"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, F (any held object weighing no more than 5 lbs./level)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one object weighing no more than 5 lbs./level" },
]
duration = "instantaneous"
saving_throw = "Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Bard, Mesmerist, Skald, Summoner, Unchained Summoner\
4: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (any held object weighing no more than 5 lbs./level)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (object)
Spell resistance: yes (object)
Target: one object weighing no more than 5 lbs./level
Subschool: Teleportation
:::

You cause the target object and the object used as a focus for the spell to immediately swap places.
The target object appears in your hand (or falls to the ground in your square if you are unable to
hold it). The stronger the connection between the two objects, the more difficult the spell is to
resist, as indicated on the table below. The modifiers are cumulative.

|Similarity|DC|
| --- | --- |
|The two objects are the same type of object (such as "keys," "swords," "scrolls")|+1|
|The two objects are made of the same material|+1|
|The two objects have the same weight (accurate to the nearest ounce)|+1|
|The two objects are part of the same set or made in the exact same mold|+2|
|The target object has a higher gp value than the focus item|-2|
|The target object is tied its holder, such as a bonded item|-2|
