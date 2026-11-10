+++
id = "ref/spell/glibness"
kind = "spell"
title = "Glibness"
aon = "SpellDisplay.aspx?ItemName=Glibness"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "glibness", path = "json/spells5.json" },
]
[[sources]]
publication = "core-rulebook"
page = "290"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Bard", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Skald", level = 3 },
]
casting_time = "1 standard action"
components = "S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Bard, Mesmerist, Skald
Casting time: 1 standard action
Components: S
Range: personal
Duration: 10 minutes/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

Your speech becomes fluent and more believable, causing those who hear you to believe every word you
say. You gain a +20 bonus on Bluff checks made to convince another of the truth of your words. This
bonus doesn't apply to other uses of the Bluff skill, such as feinting in combat, creating a
diversion to hide, or communicating a hidden message via innuendo.

If a magical effect is used against you that would detect your lies or force you to speak the truth,
the user of the effect must succeed on a caster level check (1d20 + caster level) against a DC of
15 + your caster level to succeed. Failure means the effect does not detect your lies or force you
to speak only the truth.
