+++
id = "ref/spell/mages-private-sanctum"
kind = "spell"
title = "Mage's Private Sanctum"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mages_private_sanctum", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Medium", level = 4 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "10 minutes"
components = "V, S, M (a sheet of lead, a piece of glass, a wad of cotton, and powdered chrysolite)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "30-ft. cube/level (S)" },
]
duration = "24 hours (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 4: Medium\
5: Arcanist, Mesmerist, Psychic, Sorcerer, Spiritualist, Wizard
Casting time: 10 minutes
Components: V, S, M (a sheet of lead, a piece of glass, a wad of cotton, and powdered chrysolite)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 24 hours (D)
Saving throw: none
Spell resistance: no
Area: 30-ft. cube/level (S)
:::

**Sources:** PRPG Core Rulebook pg 307

This spell ensures privacy. Anyone looking into the area from outside sees only a dark, foggy mass.
[Darkvision](ref/rule/darkvision) cannot penetrate it. No sounds, no matter how loud, can escape the
area, so nobody can eavesdrop from outside. Those inside can see out normally.

Divination (scrying) spells cannot perceive anything within the area, and those within are immune to
detect thoughts. The ward prevents speech between those inside and those outside (because it blocks
sound), but it does not prevent other communication, such as a sending or message spell, or
telepathic communication, such as that between a wizard and her familiar.

The spell does not prevent creatures or objects from moving into and out of the area.

Mage's private sanctum can be made permanent with a [permanency](ref/spell/permanency) spell.
