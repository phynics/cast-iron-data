+++
id = "ref/spell/shadow-of-doubt"
kind = "spell"
title = "Shadow of Doubt"
aon = "SpellDisplay.aspx?ItemName=Shadow%20of%20Doubt"
source_ids = ["inner-sea-races"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shadow_of_doubt", path = "json/spells15.json" },
]
[[sources]]
publication = "inner-sea-races"
page = "222"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["darkness", "emotion", "evil", "mind-affecting"]
levels = [
  { class = "Antipaladin", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Targets", value = "one creature/3 levels" },
]
duration = "1 round/level"
saving_throw = "Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Antipaladin, Bard, Skald
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will partial (see text)
Spell resistance: yes
Targets: one creature/3 levels
Subschool: Compulsion
Descriptors: darkness, emotion, evil, mind-affecting
:::

> _The following spell is available to the indicated race or ethnicity:
> [Tiefling](ref/race/tiefling)_

You create a shadowy aura of doubt fueled by a foe's own inner flaws. Targets perceive all
illumination as if it were one light level darker, to a minimum light level of darkness (not
supernatural darkness), even on a successful saving throw.

Fleeting mental shadows of regrets and anxieties distract the spell's targets; at the start of each
of their turns, they must each succeed at a Will save or be staggered for 1 round. A good-aligned
target takes a -4 penalty on saving throws against this effect; an evil-aligned target gains a +4
bonus instead.
