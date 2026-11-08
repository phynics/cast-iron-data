+++
id = "ref/spell/flame-steed"
kind = "spell"
title = "Flame Steed"
source_ids = ["core-rulebook", "mythic-adventures", "wilderness-origins", "ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flame_steed", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/phantom-steed" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Bard", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "10 minutes"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "one quasi-real, horse-like creature" },
]
duration = "1 hour/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Summoner, Unchained Summoner\
3: Arcanist, Bloodrager, Bard, Magus, Occultist, Skald, Sorcerer, Spiritualist, Wizard
Casting time: 10 minutes
Components: V, S
Range: 0 ft.
Duration: 1 hour/level (D)
Saving throw: none
Spell resistance: no
Effect: one quasi-real, horse-like creature
Subschool: Creation
:::

### Mythic Phantom Steed

**Sources:** Mythic Adventures pg 103

The steed's rider automatically succeeds at Ride checks to remain mounted. The mount's hit points
increase to 10 plus 2 per caster level, and its speed increases to 30 feet per 2 caster levels
(maximum 150 feet).

_Augmented (3rd):_ If you expend two uses of mythic power, the phantom steed is incorporeal, but its
rider can interact with it normally.

### Flame Steed

**Sources:** Wilderness Origins pg 28

You conjure a Large, quasi-real creature made of flame. It functions like
[phantom steed](ref/spell/phantom-steed), except as follows.

The flame steed is immune to fire and has acid, cold, and electricity resistance 10. If it or its
rider is attacked, it automatically exhales a 15-foot cone of smoke and ash on your turn as a free
action. Anyone in the cone must succeed at a Fortitude save (DC equal to the spell DC) or become
sickened for 1d6 rounds after leaving the area. This smoke acts as
[obscuring mist](ref/spell/obscuring-mist) for the purpose of [concealment](ref/rule/concealment).
The smoke persists for 1 round.
