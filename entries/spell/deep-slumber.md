+++
id = "ref/spell/deep-slumber"
kind = "spell"
title = "Deep Slumber"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deep_slumber", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S, M (fine sand, rose petals, or a live cricket)"
range = "close (25 ft. + 5 ft./2 levels)"
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
Level: 3: Arcanist, Bard, Mesmerist, Occultist, Psychic, Shaman, Skald, Sorcerer, Witch, Wizard
Casting time: 1 round
Components: V, S, M (fine sand, rose petals, or a live cricket)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Area: one or more living creatures within a 10-ft.-radius burst
Subschool: Compulsion
Descriptors: mind-affecting
:::

**Sources:** PRPG Core Rulebook pg 265

This spell functions like [sleep](ref/spell/sleep), except that it affects 10 HD of targets.

### Mythic Deep Slumber

**Sources:** Mythic Adventures pg 90\
This spell works like mythic sleep, except that it affects up to 20 Hit Dice of creatures.
Alternatively, you may target one creature rather than an area, increasing the duration to 1 hour
per level.

_Augmented (5th):_ If you expend two uses of mythic power, creatures affected by the spell can be
awakened only by mythic effects. If you're 5th tier and expend three uses of mythic power, the
duration increases to 10 years per tier. If you're 5th tier and expend four uses of mythic power,
the spell has both augmented effects. Creatures sleeping for years because of this spell age and
breathe as normal, but don't need to eat or drink while the spell lasts.
