+++
id = "ref/spell/phase-step"
kind = "spell"
title = "Phase Step"
aon = "SpellDisplay.aspx?ItemName=Phase%20Step"
source_ids = ["potions-and-poisons"]
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
subschools = ["teleportation"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one willing creature touched" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Alchemist, Arcanist, Bard, Investigator, Magus, Skald, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one willing creature touched
Subschool: teleportation
:::

### Phase Step

You instantly transfer the touched creature to a point you designate within range. This otherwise
functions as [the spell dimension door](ref/spell/dimension-door), except that you must have line of
sight and line of effect to the target's destination for this spell's effects to properly function.
