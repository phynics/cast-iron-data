+++
id = "ref/spell/break-greater"
kind = "spell"
title = "Greater Break"
source_ids = ["advanced-players-guide", "mythic-adventures", "ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "break_greater", path = "json/spells2.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/break" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Bloodrager", level = 4 },
  { class = "Occultist", level = 6 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "1 round"
components = "V, S, M (an unbroken platinum tuning fork worth 100 gp)"
range = "30 ft."
effects = [
  { label = "Target", value = "all Medium or smaller objects in a 30-ft. burst centered on you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Bloodrager\
6: Arcanist, Occultist, Psychic, Sorcerer, Wizard
Casting time: 1 round
Components: V, S, M (an unbroken platinum tuning fork worth 100 gp)
Range: 30 ft.
Target: all Medium or smaller objects in a 30-ft. burst centered on you
Duration: instantaneous
Saving throw: none
Spell resistance: yes (object)
:::

## Break

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

### Greater Break

**Sources:** Ultimate Intrigue pg 205

You release a burst of destructive energy. Each Medium or smaller object in the area gains the
broken condition unless it succeeds at a Fortitude saving throw. If a broken object fails this save,
it is instead destroyed. Magic items can be broken by this spell, but not destroyed. Objects in your
possession are not immune.
