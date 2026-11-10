+++
id = "ref/spell/hypnotism"
kind = "spell"
title = "Hypnotism"
source_ids = ["core-rulebook", "blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hypnotism", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "298"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "several living creatures, no two of which may be more than 30 ft. apart" },
]
duration = "2d4 rounds (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2d4 rounds (D)
Saving throw: Will negates
Spell resistance: yes
Area: several living creatures, no two of which may be more than 30 ft. apart
Subschool: Compulsion
Descriptors: mind-affecting
:::

Your gestures and droning incantation fascinate nearby creatures, causing them to stop and stare
blankly at you. In addition, you can use their rapt attention to make your suggestions and requests
seem more plausible. Roll 2d4 to see how many total HD of creatures you affect. Creatures with fewer
HD are affected before creatures with more HD. Only creatures that can see or hear you are affected,
but they do not need to understand you to be fascinated.

If you use this spell in combat, each target gains a +2 bonus on its saving throw. If the spell
affects only a single creature not in combat at the time, the saving throw has a penalty of -2.

While the subject is fascinated by this spell, it reacts as though it were two steps more friendly
in attitude. This allows you to make a single request of the affected creature (provided you can
communicate with it). The request must be brief and reasonable. Even after the spell ends, the
creature retains its new attitude toward you, but only with respect to that particular request.

A creature that fails its saving throw does not remember that you enspelled it.
