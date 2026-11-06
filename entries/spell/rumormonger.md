+++
id = "ref/spell/rumormonger"
kind = "spell"
title = "Rumormonger"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rumormonger", path = "json/spells8.json" },
]

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Effect", value = "1 rumor" },
]
duration = "1 day/level (D)"
saving_throw = "Will negates (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 1: Medium\
2: Bard, Inquisitor, Mesmerist, Skald\
3: Psychic
Casting time: 1 standard action
Components: V
Range: long (400 ft. + 40 ft./level)
Duration: 1 day/level (D)
Saving throw: Will negates (see text)
Spell resistance: yes
Effect: 1 rumor
:::

**Sources:** Ultimate Intrigue pg 224

You utter a brief anecdote or bit of news as the verbal component of this spell and track its
progress through a social gathering or other crowd. When someone who heard the rumor directly from
you and repeated the rumor is within your range, they glow silver to your sight, though this glow
doesn't occur if the creature is in disguise (unless it was in the same disguise at the time of
casting). You can choose to follow the rumor by selecting any such creature in range, at which point
the creatures who heard the rumor from you no longer glow silver, and now the creatures who heard
the rumor from your chosen creature glow silver instead. You can follow the rumor's path until you
reach a creature that heard the rumor but didn't repeat it (or repeated it incorrectly). The glow
identifies only creatures who heard the same information you conveyed. Minor cosmetic changes in the
rumor don't interrupt the chain, but when the rumor no longer resembles the information you
imparted, the trail stops and the spell ends.

You can instead use this spell to trace a rumor back to its source once you hear it. In this case,
you repeat the rumor as you heard it for the spell's verbal component. The person who told you the
rumor can attempt a Will save to end the effect. Failure indicates the silver glow leads to the
individual that told her. This process continues each time you locate the next individual spreading
the same information. Each individual attempts the save until one of them succeeds (in which case
the spell ends and you can't attempt to trace this particular rumor again) or you trace the rumor to
its original source. As with the other application of the spell, tracing a rumor back fails to cause
a creature to glow if it is in disguise, unless it was in the same disguise at the time of speaking
the rumor.
