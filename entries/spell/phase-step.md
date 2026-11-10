+++
id = "ref/spell/phase-step"
kind = "spell"
title = "Phase Step"
aon = "SpellDisplay.aspx?ItemName=Phase%20Step"
source_ids = ["core-rulebook", "potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "phase_step", path = "json/spells3.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/dimension-door" },
]
[[sources]]
publication = "potions-and-poisons"
page = "17"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Teleportation"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Magus", level = 4 },
  { class = "Medium", level = 3 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "you and touched objects or other touched willing creatures" },
]
duration = "instantaneous"
saving_throw = "none and Will negates (object)"
spell_resistance = "no and yes (object)"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Medium, Summoner\
4: Arcanist, Bard, Magus, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Spiritualist, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: none and Will negates (object)
Spell resistance: no and yes (object)
Target: you and touched objects or other touched willing creatures
Subschool: Teleportation
:::

### Phase Step

You instantly transfer the touched creature to a point you designate within range. This otherwise
functions as [the spell dimension door](ref/spell/dimension-door), except that you must have line of
sight and line of effect to the target's destination for this spell's effects to properly function.
