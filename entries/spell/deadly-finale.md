+++
id = "ref/spell/deadly-finale"
kind = "spell"
title = "Deadly Finale"
aon = "SpellDisplay.aspx?ItemName=Deadly%20Finale"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deadly_finale", path = "json/spells3.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "214"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["sonic"]
levels = [
  { class = "Bard", level = 6 },
  { class = "Skald", level = 6 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "1 creature/3 levels no two of which can be more than 30 ft. apart" },
]
duration = "instantaneous"
saving_throw = "Fortitude partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 6: Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude partial
Spell resistance: yes
Targets: 1 creature/3 levels no two of which can be more than 30 ft. apart
Descriptors: sonic
:::

You must have a bardic performance in effect to cast this spell. With a flourish, you immediately
end your performance, dealing 2d8 points of sonic damage to each target. In addition, each target
takes 3d6 points of bleed damage for 1d6 rounds. A save negates the bleed damage but not the sonic
damage.
