+++
id = "ref/spell/cognitive-block"
kind = "spell"
title = "Cognitive Block"
aon = "SpellDisplay.aspx?ItemName=Cognitive%20Block"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cognitive_block", path = "json/spells2.json" },
]
[[sources]]
publication = "occult-adventures"
page = "161"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 3 },
]
casting_time = "1 standard action"
components = "V"
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
Level: 2: Medium, Mesmerist\
3: Psychic
Casting time: 1 standard action
Components: V
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You create a mental block in the target's mind, impeding the flow of his mental spellcasting process
and forcing him to incorporate a thought component into any spell or
[spell-like ability](ref/umr/spell-like-abilities) he uses. This is in addition to any other
components the spell already requires, and doesn't replace the verbal component. Spell-like
abilities require this thought component, even though they normally don't need spell components.

As usual with thought components, this addition increases the DC of any concentration checks the
target attempts by 10 unless the target takes a move action to center his mind and satisfy the
spell's thought component.
