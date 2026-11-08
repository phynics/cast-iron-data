+++
id = "ref/spell/hunger-for-flesh-mass"
kind = "spell"
title = "Mass Hunger for Flesh"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hunger_for_flesh_mass", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hunger-for-flesh" },
]

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Cleric", level = 7 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Shaman", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Spiritualist", level = 6 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a ghoul fang)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid, magical beast, or monstrous humanoid/level, no two of which can be more than 30 feet apart" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 6: Spiritualist\
7: Arcanist, Cleric, Oracle, Psychic, Shaman, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a ghoul fang)
Range: close (25 ft. + 5 ft./2 levels)
Target: one humanoid, magical beast, or monstrous humanoid/level, no two of which can be more than 30 feet apart
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Descriptors: evil, mind-affecting
:::

## Hunger for Flesh

**Sources:** Horror Adventures pg 120

Your target's belly distends and its front teeth grow longer and sharper. The creature ravenously
craves the flesh of its own kind, gaining the staggered condition as hunger pangs rack its altered
body. The target gains a bite attack as a primary natural attack that deals damage appropriate for
its size (1d6 if Medium, 1d4 if Small). There's a 25% chance on each of the creature's turns that it
can't overcome its hunger. If so, it must move directly toward the nearest corporeal creature of its
type and subtype (if applicable) and make a bite attack against it. If the target lacks enough
actions to attack on that turn, it moves as close to the creature as it can, but on its next turn,
if the percentile dice indicate it overcomes its hunger, the target is not forced to pursue or
attack further.

On any round after the target deals damage to another creature of its own type and subtype (if
applicable) with its bite attack, the target loses the staggered condition. If it doesn't continue
dealing bite damage to applicable creatures, the target regains the staggered condition at the
beginning of its next turn.

### Mass Hunger for Flesh

**Sources:** Horror Adventures pg 121

This spell functions like [hunger for flesh](ref/spell/hunger-for-flesh), except that it affects
multiple targets. When forced to feed by the spell, affected creatures attack creatures not affected
by this spell if there are any such appropriate creatures nearby, but otherwise they attack other
affected creatures.
