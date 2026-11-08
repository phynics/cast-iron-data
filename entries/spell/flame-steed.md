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

## Phantom Steed

**Sources:** PRPG Core Rulebook pg 319

You conjure a Large, quasi-real, horse-like creature (the exact coloration can be customized as you
wish). It can be ridden only by you or by the one person for whom you specifically created the
mount. A phantom steed has a black head and body, gray mane and tail, and smoke-colored,
insubstantial hooves that make no sound. It has what seems to be a saddle, bit, and bridle. It does
not fight, but animals shun it and refuse to attack it.

The mount is AC 18 (-1 size, +4 natural armor, +5 Dex) and 7 hit points + 1 hit point per caster
level. If it loses all its hit points, the phantom steed disappears. A phantom steed has a speed of
20 feet per two caster levels, to a maximum of 100 feet at 10th level. It can bear its rider's
weight plus up to 10 pounds per caster level.

These mounts gain certain powers according to caster level. A mount's abilities include those of
mounts of lower caster levels.

_8th Level:_ The mount can ride over sandy, muddy, or even swampy ground without difficulty or
decrease in speed.

_10th Level:_ The mount can use [water walk](ref/spell/water-walk) at will (as the spell, no action
required to activate this ability).

_12th Level:_ The mount can use [air walk](ref/spell/air-walk) at will (as the spell, no action
required to activate this ability) for up to 1 round at a time, after which it falls to the ground.

_14th Level:_ The mount can fly at its speed with a bonus on Fly skill checks equal to your caster
level.

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

### Communal Phantom Steed

**Sources:** Ultimate Combat pg 239

This spell functions like phantom steed, except you can summon up to six steeds, and you divide the
duration in 1-hour intervals among the steeds summoned.
