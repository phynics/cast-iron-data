+++
id = "ref/spell/icicle-dagger"
kind = "spell"
title = "Icicle Dagger"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "icicle_dagger", path = "json/spells5.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["cold"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Summoner", level = 1 },
  { class = "Unchained Summoner", level = 1 },
  { class = "Witch", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "one icicle" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 1: Arcanist, Bloodrager, Occultist, Sorcerer, Summoner, Unchained Summoner, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: 0 ft.
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Effect: one icicle
Subschool: Creation
Descriptors: cold
:::

**Sources:** Ultimate Magic pg 224

You create a masterwork dagger out of ice. The dagger deals 1 point of cold damage in addition to
normal dagger damage. If the dagger leaves your hand for more than 1 round, it melts and the spell
ends. At 6th level, the dagger functions as a +1 [frost](ref/magic-enh/frost) dagger. At 11th level,
it gains the returning property when thrown, melting away and reforming in your hand just before
your next turn.
