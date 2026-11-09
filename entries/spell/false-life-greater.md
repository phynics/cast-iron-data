+++
id = "ref/spell/false-life-greater"
kind = "spell"
title = "Greater False Life"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_life_greater", path = "json/spells4.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/false-life" },
]
[[sources]]
publication = "ultimate-magic"
page = "219"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M (a drop of blood)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level or until discharged; see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Medium, Mesmerist\
4: Alchemist, Arcanist, Bloodrager, Investigator, Occultist, Psychic, Shaman, Sorcerer, Spiritualist, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a drop of blood)
Range: personal
Target: you
Duration: 1 hour/level or until discharged; see text
Saving throw: none
Spell resistance: no
:::

### Greater False Life

This spell functions as [false life](ref/spell/false-life), except you gain temporary hit points
equal to 2d10 + 1 point per caster level (maximum +20). The effects of this spell do not stack with
those of false life.
