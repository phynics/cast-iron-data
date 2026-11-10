+++
id = "ref/spell/enshroud-thoughts"
kind = "spell"
title = "Enshroud Thoughts"
aon = "SpellDisplay.aspx?ItemName=Enshroud%20Thoughts"
source_ids = ["occult-adventures", "blood-of-the-elements"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "enshroud_thoughts", path = "json/spells4.json" },
]
[[sources]]
publication = "occult-adventures"
page = "169"
[[sources]]
publication = "blood-of-the-elements"
page = "13"

[fields]
kind = "spell"
school = "abjuration"
descriptors = ["mind-affecting"]
levels = [
  { class = "Alchemist", level = 2 },
  { class = "Bard", level = 2 },
  { class = "Hunter", level = 3 },
  { class = "Inquisitor", level = 2 },
  { class = "Investigator", level = 2 },
  { class = "Medium", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Ranger", level = 3 },
  { class = "Shaman", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Witch", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "10 minutes/level (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Alchemist, Bard, Inquisitor, Investigator, Medium, Mesmerist, Psychic, Shaman, Skald, Witch\
3: Hunter, Ranger
Casting time: 1 standard action
Components: V, S
Range: personal
Duration: 10 minutes/level (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: you
Descriptors: mind-affecting
:::

You become warded against the mental prying of others, including the effects of divination spells
such as [detect thoughts](ref/spell/detect-thoughts) and [seek thoughts](ref/spell/seek-thoughts),
as well as enchantment spells such as [modify memory](ref/spell/modify-memory) and
[memory lapse](ref/spell/memory-lapse). If another creature attempts to target you with a
mind-affecting spell that detects or alters your thoughts or memories, the caster must succeed at a
caster level check against a DC equal to 11 + your caster level or the spell fails. Only spells that
detect or alter your thoughts or memories are blocked by this spell; effects such as
[clairaudience/clairvoyance](ref/spell/clairaudience-clairvoyance),
[detect evil](ref/spell/detect-evil), and [locate creature](ref/spell/locate-creature) continue to
affect you as normal.
