+++
id = "ref/spell/antipathy"
kind = "spell"
title = "Antipathy"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "antipathy", path = "json/spells.json" },
]

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
components = "V, S, M/DF (a lump of alum soaked in vinegar)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one location (up to a 10-ft. cube/level) or one object" },
]
duration = "2 hours/level (D)"
saving_throw = "Will partial"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Occultist, Summoner\
8: Arcanist, Psychic, Sorcerer, Witch, Wizard\
9: Druid
Casting time: 1 hour
Components: V, S, M/DF (a lump of alum soaked in vinegar)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 2 hours/level (D)
Saving throw: Will partial
Spell resistance: yes
Target: one location (up to a 10-ft. cube/level) or one object
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 243

You cause an object or location to emanate magical vibrations that repel either a specific kind of
intelligent creature or creatures of a particular alignment, as defined by you. The kind of creature
to be affected must be named specifically. A creature subtype is not specific enough. Likewise, the
specific alignment to be repelled must be named.

Creatures of the designated kind or alignment feel an urge to leave the area or to avoid the
affected item.

A compulsion forces them to abandon the area or item, shunning it and never willingly returning to
it while the spell is in effect. A creature that makes a successful saving throw can stay in the
area or touch the item but feels uncomfortable doing so. This distracting discomfort reduces the
creature's Dexterity score by 4 points.

Antipathy counters and dispels [sympathy](ref/spell/sympathy).
