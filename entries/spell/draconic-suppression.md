+++
id = "ref/spell/draconic-suppression"
kind = "spell"
title = "Draconic Suppression"
aon = "SpellDisplay.aspx?ItemName=Draconic%20Suppression"
source_ids = ["dragonslayers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "draconic_suppression", path = "json/spells13.json" },
]
[[sources]]
publication = "dragonslayers-handbook"
page = "28"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one dragon" },
]
duration = "1 round/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Target: one dragon
:::

A dragon that fails its saving throw cannot use its breath weapon for the duration of the spell and
is treated as one age category younger for determining which special abilities it can use. For
example, an ancient green dragon would revert to the special abilities of a very old dragon and lose
access to its miasma ability and its dominate person
[spell-like ability](ref/umr/spell-like-abilities). This spell has no effect on a dragon's armor
class, feats, frightful presence, hit points, physical attacks, saving throws, senses, size, skills,
spellcasting, or statistics.
