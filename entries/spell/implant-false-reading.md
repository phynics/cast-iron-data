+++
id = "ref/spell/implant-false-reading"
kind = "spell"
title = "Implant False Reading"
aon = "SpellDisplay.aspx?ItemName=Implant%20False%20Reading"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "implant_false_reading", path = "json/spells14.json" },
]
[[sources]]
publication = "occult-adventures"
page = "173"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Glamer"]
descriptors = ["glamer"]
levels = [
  { class = "Mesmerist", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Psychic", level = 2 },
]
casting_time = "1 minute"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "object touched" },
]
duration = "1 day/level"
saving_throw = "none, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Mesmerist, Occultist, Psychic
Casting time: 1 minute
Components: V, S
Range: touch
Duration: 1 day/level
Saving throw: none, see text
Spell resistance: no
Target: object touched
Subschool: Glamer
Descriptors: glamer
:::

You implant a false psychometric reading into an object, imbuing the item with misleading
information that might be learned from the [object reading](ref/spell/object-reading) spell or
through the [psychometry](ref/skill/appraise) occult skill unlock. This information might fool
enemies, create a false history, or pass on secret messages through objects to psychically attuned
allies. You can implant any information you wish that could be implanted by the charge object spell,
as well as up to one piece of information per 3 levels that could be attained using psychometry or
the object reading spell. You can detail this information in any way you see fit, either making up a
previous owner and circumstances involving the object from whole cloth, or attempting to emulate the
biographical information and fictional accounts of a specific individual's experience with the
object.

During the spell's duration, creatures reading the object through the object reading spell or the
psychometry occult skill unlock receive this false information in place of an item's true history if
they fail a Will saving throw. Creatures that succeed at their saves still detect and receive the
false information, but recognize it for what is and are able to discern the fictitious information
from the item's true history without difficulty.

This spell masks its own magical aura, causing the target to not register as magical to detect
spells and similar effects. This masking doesn't conceal any other magical auras on the object, and
can be overcome in the same ways as magic aura.
