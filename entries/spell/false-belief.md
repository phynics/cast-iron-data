+++
id = "ref/spell/false-belief"
kind = "spell"
title = "False Belief"
aon = "SpellDisplay.aspx?ItemName=False%20Belief"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "false_belief", path = "json/spells4.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "214"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "10 minutes, plus length of memory to be altered"
components = "V, S, M (lemon juice and a scrap of parchment)"
range = "touch"
effects = [
  { label = "Target", value = "willing creature touched" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Mesmerist, Psychic, Skald
Casting time: 10 minutes, plus length of memory to be altered
Components: V, S, M (lemon juice and a scrap of parchment)
Range: touch
Duration: 1 hour/level
Saving throw: none
Spell resistance: yes
Target: willing creature touched
Subschool: Compulsion
Descriptors: mind-affecting
:::

You temporarily alter the target's memory (similar to [modify memory](ref/spell/modify-memory)) to
eliminate, change, or implant a memory of up to 1 hour in length. When the duration of this expires,
the target's real memory returns, and the false memory fades to little more than a vague outline,
like a dream. This false memory seems true to the target, so effects that detect lies or force the
target to speak the truth (as the subject understands it) don't detect the falsehood.
