+++
id = "ref/spell/wall-of-light"
kind = "spell"
title = "Wall of Light"
source_ids = ["the-dragons-demand"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wall_of_light", path = "json/spells11.json" },
]
[[sources]]
publication = "the-dragons-demand"
page = "24"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["light"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Druid", level = 5 },
  { class = "Hunter", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a chip of mica)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft.-high vertical sheet of light up to 5 ft. long/level" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude partial, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 5: Arcanist, Druid, Hunter, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a chip of mica)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: Fortitude partial, see text
Spell resistance: yes
Effect: 10-ft.-high vertical sheet of light up to 5 ft. long/level
Descriptors: light
:::

An immobile, blinding curtain of white light that blocks line of sight springs into existence. The
wall sheds bright light to a range of 60 feet in all directions. A creature adjacent to the wall is
blinded as long as it remains adjacent plus an additional 1d4 rounds thereafter-closing its eyes or
succeeding at a Fortitude save negates the effect for 1 round. A creature that passes through the
wall is automatically blinded, even if its eyes are closed. A creature from the Plane of Shadow
gains 1d4 negative levels each round it spends within 5 feet of the wall (Fortitude negates).
Passing through the wall imposes a -4 penalty on the save for that round. Twenty-four hours after
gaining these negative levels, the subject must attempt a new Fortitude saving throw for each
negative level. If a save succeeds, 1 negative level is removed. If it fails, the negative level
becomes permanent. Wall of light can be made permanent with [permanency](ref/spell/permanency) (with
a minimum caster level of 13th and cost of 11,000 gp).
