+++
id = "ref/spell/hypnotism-greater"
kind = "spell"
title = "Greater Hypnotism"
source_ids = ["core-rulebook", "blood-of-the-beast"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hypnotism_greater", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/hypnotism" },
]

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Mesmerist", level = 4 },
  { class = "Occultist", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "several living creatures, no two of which may be more than 30 ft. apart" },
]
duration = "2d4 rounds (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Arcanist, Bard, Mesmerist, Occultist, Psychic, Skald, Sorcerer, Witch
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Area: several living creatures, no two of which may be more than 30 ft. apart
Duration: 2d4 rounds (D)
Saving throw: Will negates
Spell resistance: yes
Subschool: Compulsion
Descriptors: mind-affecting
:::

## Hypnotism

**Sources:** PRPG Core Rulebook pg 298

Your gestures and droning incantation fascinate nearby creatures, causing them to stop and stare
blankly at you. In addition, you can use their rapt attention to make your suggestions and requests
seem more plausible. Roll 2d4 to see how many total HD of creatures you affect. Creatures with fewer
HD are affected before creatures with more HD. Only creatures that can see or hear you are affected,
but they do not need to understand you to be fascinated.

If you use this spell in combat, each target gains a +2 bonus on its saving throw. If the spell
affects only a single creature not in combat at the time, the saving throw has a penalty of -2.

While the subject is fascinated by this spell, it reacts as though it were two steps more friendly
in attitude. This allows you to make a single request of the affected creature (provided you can
communicate with it). The request must be brief and reasonable. Even after the spell ends, the
creature retains its new attitude toward you, but only with respect to that particular request.

A creature that fails its saving throw does not remember that you enspelled it.

### Greater Hypnotism

**Sources:** Blood of the Beast pg 19

> _The following spell is the result of generations of [nagaji](ref/race/nagaji) tradition, but
> spellcasters from elsewhere in Tian Xia have begun to learn these techniques and spread them
> further._

This functions as [hypnotism](ref/spell/hypnotism), except it affects 2 Hit Die of creatures per
caster level you have. You can make up to five requests (instead of a single request) to each
creature affected by the spell, and the requests can be as long and as complicated as you desire
(though they still must be reasonable).
