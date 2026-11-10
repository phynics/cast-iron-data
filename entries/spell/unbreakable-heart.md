+++
id = "ref/spell/unbreakable-heart"
kind = "spell"
title = "Unbreakable Heart"
source_ids = ["inner-sea-world-guide", "gods-and-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "unbreakable_heart", path = "json/spells11.json" },
]
[[sources]]
publication = "inner-sea-world-guide"
page = "296"
[[sources]]
publication = "gods-and-magic"
page = "37"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Ranger", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Witch", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "1 creature" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Bard, Cleric, Hunter, Oracle, Paladin, Ranger, Shaman, Skald, Warpriest, Witch
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Effect: 1 creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

The target creature gains a +4 morale bonus on saving throws against mind-affecting effects that
rely on negative emotions (such as crushing despair, rage, or fear effects) or that would force him
to harm an ally (such as confusion). If the target is already under such an effect when receiving
this spell, that effect is suppressed for the duration of this spell. It does not affect
mind-affecting effects based on positive emotions (such as good hope or the inspire courage bard
ability). A creature can still be charmed or otherwise magically controlled while under this spell's
effects, but if such a creature ever receives a new saving throw against that effect as a result of
being ordered to attempt to harm or otherwise oppose a true ally, he can roll that saving throw
twice and take the better result as his actual roll. [Calm emotions](ref/spell/calm-emotions)
counters and dispels unbreakable heart.
