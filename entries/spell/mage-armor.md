+++
id = "ref/spell/mage-armor"
kind = "spell"
title = "Mage Armor"
aon = "SpellDisplay.aspx?ItemName=Mage%20Armor"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mage_armor", path = "json/spells6.json" },
]
[[sources]]
publication = "core-rulebook"
page = "306"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, F (a piece of cured leather)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Bloodrager, Occultist, Psychic, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F (a piece of cured leather)
Range: touch
Duration: 1 hour/level (D)
Saving throw: Will negates (harmless)
Spell resistance: no
Target: creature touched
Subschool: Creation
Descriptors: force
:::

An invisible but tangible field of force surrounds the subject of a mage armor spell, providing a +4
armor bonus to AC.

Unlike mundane armor, mage armor entails no armor check penalty, arcane spell failure chance, or
speed reduction. Since mage armor is made of force, incorporeal creatures can't bypass it the way
they do normal armor.
