+++
id = "ref/spell/magic-vestment"
kind = "spell"
title = "Magic Vestment"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_vestment", path = "json/spells6.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Shaman", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "armor or shield touched" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless) (object)"
spell_resistance = "yes (harmless) (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Cleric, Inquisitor, Occultist, Oracle, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: touch
Duration: 1 hour/level
Saving throw: Will negates (harmless) (object)
Spell resistance: yes (harmless) (object)
Target: armor or shield touched
:::

**Sources:** PRPG Core Rulebook pg 310

You imbue a suit of armor or a shield with an enhancement bonus of +1 per four caster levels
(maximum +5 at 20th level).

An outfit of regular clothing counts as armor that grants no AC bonus for the purpose of this spell.

### Mythic Magic Vestment

**Sources:** Mythic Adventures pg 100\
You can add one armor special ability to the target if it's armor or one shield special ability if
it's a shield. The special ability must have a base price modifier no greater than a +1 enhancement
bonus or 4,000 gp.

_Augmented (3rd):_ If you expend two uses of mythic power, you can add any number of special
abilities with a total base price modifier no greater than a +2 enhancement bonus or 15,000 gp.
