+++
id = "ref/spell/redcaps-touch"
kind = "spell"
title = "Redcap's Touch"
aon = "SpellDisplay.aspx?ItemName=Redcap%27s%20Touch"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "redcaps_touch", path = "json/spells8.json" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "18"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 6 },
  { class = "Bloodrager", level = 4 },
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Shaman", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Witch", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (1 ounce of blood)"
range = "touch"
effects = [
  { label = "Target", value = "one non-magical hat touched" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Antipaladin, Bloodrager, Hunter, Ranger\
6: Arcanist, Druid, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (1 ounce of blood)
Range: touch
Duration: 1 minute/level (D)
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: one non-magical hat touched
:::

You infuse the target with the blood used as a material component, imparting malicious power. As
long as the hat is worn (occupying the wearer's [head slot](ref/rule/magic-items-on-the-body) as
though it were a magic item), it grants its wearer a +2 bonus on damage rolls and causes the wearer
to regain 1d4 hit points whenever they deal the killing blow to a living creature.
