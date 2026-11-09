+++
id = "ref/spell/sympathy"
kind = "spell"
title = "Sympathy"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sympathy", path = "json/spells10.json" },
]
[[sources]]
publication = "core-rulebook"
page = "357"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Druid", level = 9 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 hour"
components = "V, S, M (a drop of honey and crushed pearls worth 1,500 gp)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one location (up to a 10-ft. cube/level) or one object" },
]
duration = "2 hours/level (D)"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Occultist, Summoner\
8: Arcanist, Psychic, Sorcerer, Witch, Wizard\
9: Druid
Casting time: 1 hour
Components: V, S, M (a drop of honey and crushed pearls worth 1,500 gp)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 hours/level (D)
Saving throw: Will negates; see text
Spell resistance: yes
Target: one location (up to a 10-ft. cube/level) or one object
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You cause an object or location to emanate magical vibrations that attract either a specific kind of
intelligent creature or creatures of a particular alignment, as defined by you. The particular kind
of creature to be affected must be named specifically. A creature subtype is not specific enough.
Likewise, the specific alignment must be named.

Creatures of the specified kind or alignment feel elated and pleased to be in the area or desire to
touch or possess the object. The compulsion to stay in the area or touch the object is overpowering.
If the save is successful, the creature is released from the enchantment, but a subsequent save must
be made 1d6 × 10 minutes later. If this save fails, the affected creature attempts to return to the
area or object.

Sympathy counters and dispels [antipathy](ref/spell/antipathy).
