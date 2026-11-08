+++
id = "ref/spell/break"
kind = "spell"
title = "Break"
source_ids = ["advanced-players-guide", "mythic-adventures", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "break", path = "json/spells2.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a twig)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one Medium or smaller object" },
]
duration = "instantaneous"
saving_throw = "Fortitude negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bloodrager, Occultist, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a twig)
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Fortitude negates (object)
Spell resistance: yes (object)
Target: one Medium or smaller object
:::

**Sources:** Advanced Player's Guide pg 207

You can attempt to break or at least damage any one Medium or smaller object within range. If the
target fails its Fortitude saving throw, it gains the broken condition. If cast on a broken item,
that item is destroyed on a failed save.

### Mythic Break

**Sources:** Mythic Adventures pg 87

You can target up to 1 Medium or smaller object per caster level.

_Augmented (3rd):_ If you expend two uses of mythic power, target objects gain the broken condition
on a successful save and are destroyed on a failed save. This doesn't affect mythic objects or
objects held or carried by mythic creatures.
