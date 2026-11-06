+++
id = "ref/spell/sleep"
kind = "spell"
title = "Sleep"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sleep", path = "json/spells9.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 round"
components = "V, S, M (fine sand, rose petals, or a live cricket)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Area", value = "one or more living creatures within a 10-ft.-radius burst" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Adept, Arcanist, Bard, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S, M (fine sand, rose petals, or a live cricket)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Area: one or more living creatures within a 10-ft.-radius burst
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 344

A sleep spell causes a magical slumber to come upon 4 HD of creatures. Creatures with the fewest HD
are affected first. Among creatures with equal HD, those who are closest to the spell's point of
origin are affected first. HD that are not sufficient to affect a creature are wasted. Sleeping
creatures are helpless. Slapping or wounding awakens an affected creature, but normal noise does
not. Awakening a creature is a standard action (an application of the aid another action). Sleep
does not target unconscious creatures, constructs, or undead creatures.

### Mythic Sleep

**Sources:** Mythic Adventures pg 108\
The spell affects up to 8 Hit Dice of creatures, and you can choose the order in which creatures are
affected by the spell. Any effect that would automatically awaken a sleeping creature instead allows
it to attempt a new Will saving throw to awaken.

_Augmented (8th):_ If you expend three uses of mythic power, you can target all living creatures
other than you that have 8 Hit Dice or fewer in a 1-mile radius centered on you. Creatures that fail
their saving throws fall asleep for a number of days equal to your tier. You can select a number of
creatures up to your tier to not be affected by the spell.
