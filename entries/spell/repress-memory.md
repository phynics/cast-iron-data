+++
id = "ref/spell/repress-memory"
kind = "spell"
title = "Repress Memory"
aon = "SpellDisplay.aspx?ItemName=Repress%20Memory"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "repress_memory", path = "json/spells8.json" },
]
[[sources]]
publication = "occult-adventures"
page = "184"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Mesmerist", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Skald", level = 5 },
]
casting_time = "1 round"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Mesmerist, Skald\
6: Psychic
Casting time: 1 round
Components: V, S
Range: personal
Duration: instantaneous
Saving throw: none
Spell resistance: no
Target: you
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell allows you to safeguard important knowledge, even from yourself. When casting this spell,
you recount one piece of knowledge you possess (up to a maximum of 50 words). This knowledge
disappears utterly from your mind, and you might not realize you forgot something. The magic of the
spell patches omissions in your memory with indistinct haze. Repress memory protects against detect
thoughts, discern lies, zone of truth, and similar spells, though careful questioning may reveal the
gaps in your memory, or that your memory has been affected by the spell.

A repressed memory can be restored only by [break enchantment](ref/spell/break-enchantment),
[psychic surgery](ref/spell/psychic-surgery), [limited wish](ref/spell/limited-wish),
[miracle](ref/spell/miracle), or [wish](ref/spell/wish). If you use this spell to negate the memory
of a magical compulsion, it doesn't remove the compulsion, nor does it remove procedural memories
that might affect your skills or class abilities.

At the GM's discretion, multiple castings of this spell might erase memories of a lengthier event or
all memory of a place or individual from your memory.
