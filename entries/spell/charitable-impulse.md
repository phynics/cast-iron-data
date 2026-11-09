+++
id = "ref/spell/charitable-impulse"
kind = "spell"
title = "Charitable Impulse"
source_ids = ["chronicle-of-the-righteous"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "charitable_impulse", path = "json/spells2.json" },
]
[[sources]]
publication = "chronicle-of-the-righteous"
page = "50"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, F/DF (a miniature collection plate)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one humanoid creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Skald\
3: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, F/DF (a miniature collection plate)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one humanoid creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell makes a creature more charitable, compelling it to aid others rather than use violence.
An affected creature practices non-violent combat behaviors according to the following list of
priorities, beginning with the first priority. The subject continues to perform a priority until he
can no longer fulfill its demands (at which point he moves to the next priority) or until the spell
ends, whichever comes first.

_1st Priority:_ Heal injured creatures within 30 feet, beginning with the closest creatures and
using whatever methods the subject has at hand (including potions, spells, and so on).

_2nd Priority:_ The subject gives his weapon away to the nearest creature within 30 feet who will
accept it. If no creature accepts the weapon, the subject drops the weapon on the ground.

_3rd Priority:_ Cast beneficial spells and/or use beneficial magic items (including potions, wands,
and so on) on creatures within 30 feet, starting with the closest creatures.

_4th Priority:_ The subject gives away his non-worn possessions - the contents of a backpack or
similar item count as one item each, as does the container itself - to creatures within 30 feet. If
no creature accepts the items, the subject drops the items on the ground.

_5th Priority:_ The subject gives away his remaining possessions (including his armor, boots, cloak,
and so on) to creatures within 30 feet. If no creature accepts the items, the subject drops them on
the ground.

If the subject fulfills all five priorities, the spell effect ends. The subject cannot attack or
take attacks of opportunity, but can defend himself as normal. If the subject is attacked, the
spell's effect immediately ends.
