+++
id = "ref/spell/transmute-wine-to-blood"
kind = "spell"
title = "Transmute Wine to Blood"
aon = "SpellDisplay.aspx?ItemName=Transmute%20Wine%20to%20Blood"
source_ids = ["blood-of-the-night"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "transmute_wine_to_blood", path = "json/spells10.json" },
]
[[sources]]
publication = "blood-of-the-night"
page = "30"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Red Mantis Assassin", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (drop of animal blood)"
range = "touch"
effects = [
  { label = "Target", value = "bottle of wine worth at least 10 gp" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 2: Arcanist, Cleric, Oracle, Red Mantis Assassin, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (drop of animal blood)
Range: touch
Duration: instantaneous
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: bottle of wine worth at least 10 gp
:::

You transform one bottle of fine wine into 1 pint of animal blood, sufficient for a creature with
the blood drain ability to feed upon as if it came from a Medium animal with 1 Hit Die. If you are
using the [optional hunger rules](ref/rule/hunger-rules), this blood satiates an undead creature's
hunger, negating any withdrawal effects, but does not grant the creature a feeding bonus. The blood
coagulates and spoils at the normal rate.
