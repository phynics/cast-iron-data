+++
id = "ref/spell/holy-whisper"
kind = "spell"
title = "Holy Whisper"
source_ids = ["advanced-players-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_whisper", path = "json/spells5.json" },
]
[[sources]]
publication = "advanced-players-guide"
page = "228"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
levels = [
  { class = "Paladin", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "30 ft."
effects = [
  { label = "Area", value = "cone-shaped burst" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Paladin
Casting time: 1 standard action
Components: V, S
Range: 30 ft.
Duration: instantaneous
Saving throw: Fortitude negates, see text
Spell resistance: yes
Area: cone-shaped burst
Descriptors: good
:::

You whisper a single word in the primordial language of good that is anathema to the minions of evil
and strengthens the resolve of good creatures. Evil creatures within the burst must make a Fortitude
saving throw or become sickened for 1 round/level. Evil outsiders with the evil subtype,
evil-aligned dragons, and undead in the burst also take 2d8 points of damage if they fail their
saves. Good-aligned creatures in the burst gain a +2 sacred bonus on attack and damage rolls for 1
round.
