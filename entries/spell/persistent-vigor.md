+++
id = "ref/spell/persistent-vigor"
kind = "spell"
title = "Persistent Vigor"
aon = "SpellDisplay.aspx?ItemName=Persistent%20Vigor"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "persistent_vigor", path = "json/spells7.json" },
]
[[sources]]
publication = "advanced-class-guide"
page = "190"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Cleric", level = 4 },
  { class = "Inquisitor", level = 4 },
  { class = "Investigator", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (ginseng root shavings)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Alchemist, Cleric, Inquisitor, Investigator, Oracle, Psychic, Shaman, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, M/DF (ginseng root shavings)
Range: personal
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: no
Target: you
:::

You are filled with a persistent vigor. You gain [fast healing](ref/umr/fast-healing) 2 and are
immune to bleed effects as well as the sickened and nauseated conditions. When you succeed at a
saving throw against a disease or poison effect, that disease or poison effect ends (as if you had
succeeded at enough saving throws to cure that effect).

If you fail a saving throw against a disease or poison effect, you can instantly dismiss this spell
to reroll that saving throw with a +4 bonus; you must take the result of this reroll, even if it is
lower.
