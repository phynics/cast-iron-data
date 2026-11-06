+++
id = "ref/spell/feather-fall"
kind = "spell"
title = "Feather Fall"
source_ids = ["core-rulebook", "mythic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "feather_fall", path = "json/spells4.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Spiritualist", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 immediate action"
components = "V"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one Medium or smaller freefalling object or creature/level, no two of which may be more than 20 ft. apart" },
]
duration = "until landing or 1 round/level"
saving_throw = "Will negates (harmless) or Will negates (object)"
spell_resistance = "yes (object)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bloodrager, Bard, Magus, Occultist, Psychic, Red Mantis Assassin, Skald, Sorcerer, Spiritualist, Summoner, Unchained Summoner, Wizard
Casting time: 1 immediate action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: until landing or 1 round/level
Saving throw: Will negates (harmless) or Will negates (object)
Spell resistance: yes (object)
Targets: one Medium or smaller freefalling object or creature/level, no two of which may be more than 20 ft. apart
:::

**Sources:** PRPG Core Rulebook pg 281

The affected creatures or objects fall slowly. Feather fall instantly changes the rate at which the
targets fall to a mere 60 feet per round (equivalent to the end of a fall from a few feet), and the
subjects take no damage upon landing while the spell is in effect. When the spell duration expires,
a normal rate of falling resumes.

The spell affects one or more Medium or smaller creatures (including gear and carried objects up to
each creature's maximum load) or objects, or the equivalent in larger creatures: a Large creature or
object counts as two Medium creatures or objects, a Huge creature or object counts as four Medium
creatures or objects, and so forth.

This spell has no special effect on ranged weapons unless they are falling quite a distance. If the
spell is cast on a falling item, the object does half normal damage based on its weight, with no
bonus for the height of the drop.

Feather fall works only upon free-falling objects. It does not affect a sword blow or a charging or
flying creature.

### Mythic Feather Fall

**Sources:** Mythic Adventures pg 93\
The spell affects one additional target per level. The targets don't have to be within 20 feet of
each other.

_Augmented (4th):_ If you expend two uses of mythic power, the spell absorbs the targets' velocity
and transforms it into a concussive blast. Targets fall at the normal rate (not slowed) but land
safely. When a target lands, it creates a 10-foot-radius burst of force that deals 1d6 points of
damage per caster level (maximum 5d6, Reflex half, DC equal to the DC of feather fall). The targets
of this spell are unaffected by these concussive blasts.
