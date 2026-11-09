+++
id = "ref/spell/placebo-effect"
kind = "spell"
title = "Placebo Effect"
aon = "SpellDisplay.aspx?ItemName=Placebo%20Effect"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "placebo_effect", path = "json/spells7.json" },
]
[[sources]]
publication = "occult-adventures"
page = "180"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
]
casting_time = "1 standard action"
components = "V, M (a sugar cube)"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 minute/level"
saving_throw = "Will disbelief (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 2: Medium, Mesmerist, Psychic
Casting time: 1 standard action
Components: V, M (a sugar cube)
Range: touch
Duration: 1 minute/level
Saving throw: Will disbelief (harmless)
Spell resistance: yes
Target: creature touched
Subschool: Phantasm
Descriptors: mind-affecting
:::

The subject temporarily ceases to feel the ill effects of a single ongoing affliction or condition
from the following list: blinded, cursed, dazed, deafened, diseased, fatigued, frightened,
nauseated, panicked, paralyzed, poisoned, shaken, sickened, staggered, or stunned. If that
affliction or condition has a duration, it is suspended until this spell expires. If the subject has
multiple instances of the same type of affliction (such as multiple diseases), a single casting of
this spell can suspend only one of them. Placebo effect doesn't remove or temporarily negate any
damage that the affliction may have already caused, nor does it provide protection against receiving
such conditions again.
