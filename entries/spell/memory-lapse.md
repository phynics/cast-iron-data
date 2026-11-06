+++
id = "ref/spell/memory-lapse"
kind = "spell"
title = "Memory Lapse"
source_ids = ["advanced-players-guide", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "memory_lapse", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Arcanist, Bard, Mesmerist, Occultist, Skald, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Descriptors: mind-affecting
:::

**Sources:** Advanced Player's Guide pg 232

You cause the target to forget what happened from the casting of the spell back to the beginning of
its last turn. This may allow a retry on a Diplomacy, Intimidate, or opposed skill check, though
only with respect to the target, not other creatures that may be present.

### Mythic Memory Lapse

**Sources:** Mythic Adventures pg 100\
The target forgets an additional round, back to the beginning of the turn before its last turn.

_Augmented (3rd):_ If you expend two uses of mythic power, you can spend 1 round implanting a false
memory in the affected target. This false memory is limited to events that could have occurred
during the time it just forgot, as if using [modify memory](ref/spell/modify-memory) but limited to
that short period of time. For example, you couldn't implant the memory of a lengthy conversation,
as that couldn't happen in the forgotten length of time.

The target can attempt a Will saving throw (DC equal to the mythic memory lapse DC plus your tier)
to resist this implanted memory. Success means no memory is implanted, but the target still forgets
the allotted time.
