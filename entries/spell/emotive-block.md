+++
id = "ref/spell/emotive-block"
kind = "spell"
title = "Emotive Block"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "emotive_block", path = "json/spells4.json" },
]
[[sources]]
publication = "occult-adventures"
page = "169"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 3 },
  { class = "Spiritualist", level = 2 },
]
casting_time = "1 standard action"
components = "S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Mesmerist, Spiritualist\
3: Psychic
Casting time: 1 standard action
Components: S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

You create an emotional block in the target's mind, adding an emotion component to each spell or
[spell-like ability](ref/umr/spell-like-abilities) he uses. This is in addition to any other
components the spell already requires, and doesn't replace the somatic component. The target's
spell-like abilities require this emotion component, even though they normally don't need spell
components.

As usual with emotion components, the target can't cast spells (or use
[spell-like abilities](ref/umr/spell-like-abilities), in this case) while affected by a non-harmless
emotion or fear effect.
