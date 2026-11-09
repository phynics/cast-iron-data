+++
id = "ref/spell/sense-madness"
kind = "spell"
title = "Sense Madness"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "sense_madness", path = "json/spells15.json" },
]
[[sources]]
publication = "horror-adventures"
page = "127"

[fields]
kind = "spell"
school = "divination"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "creatures in range (see text)" },
]
duration = "concentration, up to 1 round/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: divination
Level: 2: Cleric, Inquisitor, Medium, Occultist, Oracle, Paladin, Psychic, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: concentration, up to 1 round/level
Saving throw: none
Spell resistance: no
Target: creatures in range (see text)
:::

You can sense the presence of mental disturbance in creatures within range, focusing your detection
on one creature each round. If the target is currently suffering from any form of
[madness](ref/rule/madness) or addiction, has total sanity damage greater than or equal to its
[sanity edge](ref/rule/sanity-score-edge-and-thresholds), or is under a magical compulsion that
could be detected by [detect magic](ref/spell/detect-magic), you can detect the presence of such a
disturbance on the first round of concentration.

If you concentrate on the same creature for an additional round, you learn if the creature's total
sanity damage is greater than or equal to its sanity edge, and you can attempt a Sense Motive check
against a DC equal to 10 + the save DC of the target's madness or addiction to determine the exact
nature of a madness or addiction. Additionally, you can attempt a Spellcraft check with a DC equal
to 11 + the caster level of the compulsion against each magical compulsion currently affecting the
target that could be detected by detect magic. If successful, you can identify the specific spell
affecting the target. You gain a +4 bonus on your Spellcraft check if the effect is confusion,
insanity, or a similar effect that explicitly causes madness or insanity. If you successfully
identify such an effect with sense madness, the insights provided by this spell grant you a +1
circumstance bonus on your next caster level check in the following 1 minute made to counter,
dispel, or remove that specific effect. After attempting a check to identify a madness, addiction,
or compulsion, you can't attempt that check against the same creature again, even if you concentrate
on the creature again.
