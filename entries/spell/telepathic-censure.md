+++
id = "ref/spell/telepathic-censure"
kind = "spell"
title = "Telepathic Censure"
aon = "SpellDisplay.aspx?ItemName=Telepathic%20Censure"
source_ids = ["demon-hunters-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "telepathic_censure", path = "json/spells10.json" },
]
[[sources]]
publication = "demon-hunters-handbook"
page = "27"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Bard", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Skald", level = 2 },
]
casting_time = "1 standard action"
components = "V"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature (see text)" },
]
duration = "1 minute/level (D)"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Bard, Inquisitor, Skald
Casting time: 1 standard action
Components: V
Range: medium (100 ft. + 10 ft./level)
Duration: 1 minute/level (D)
Saving throw: Will negates
Spell resistance: yes
Target: one creature (see text)
:::

This spell creates an invisible psychic interference that inhibits telepathic communication. When
cast upon a creature that can communicate via telepathy, this spell prevents that ability's use:
either to receive or project thoughts. When cast upon a creature without telepathy, the spell merely
prevents the target from receiving telepathic communication. Those affected by this spell or that
attempt to telepathically communicate with creatures under its effects are not innately aware that
their communication is being inhibited. This spell temporarily disrupts spells and effects like
[telepathic bond](ref/spell/telepathic-bond) or telepathic messages sent by a
[helm of telepathy](ref/magic-wondrous/helm-of-telepathy), but not attacks and effects unrelated to
communication like [detect thoughts](ref/spell/detect-thoughts) or a
[neothelid's](ref/monster/neothelid) psychic crush.
