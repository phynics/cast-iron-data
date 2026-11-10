+++
id = "ref/spell/calm-spirit"
kind = "spell"
title = "Calm Spirit"
aon = "SpellDisplay.aspx?ItemName=Calm%20Spirit"
source_ids = ["occult-adventures", "occult-mysteries"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "calm_spirit", path = "json/spells2.json" },
]
[[sources]]
publication = "occult-adventures"
page = "160"
[[sources]]
publication = "occult-mysteries"
page = "55"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Medium", level = 1 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one incorporeal undead creature or haunt" },
]
duration = "1 minute or 1 round/level; see text"
saving_throw = "Will negates or none, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 1: Medium\
2: Cleric, Oracle, Shaman, Spiritualist, Warpriest
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 minute or 1 round/level; see text
Saving throw: Will negates or none, see text
Spell resistance: yes
Target: one incorporeal undead creature or haunt
:::

This spell temporarily calms agitated haunts and incorporeal undead such as ghosts. You have no
control over the affected creatures, but calm spirit postpones hostile action by the affected
spirits for the duration of the spell. Entities so affected cannot take violent actions or do
anything destructive, including triggering persistent haunt abilities, though they can defend
themselves. Any aggressive action against or damage dealt to a calmed spirit or haunt immediately
ends the effect.

Haunts do not receive a saving throw against the spell, but the caster must succeed at a caster
level check whose difficulty is equal to at least 10 + the haunt's CR in order to temporarily calm
the angry entity. The spell's duration changes to concentration (up to 1 round/level) when affecting
a haunt.
