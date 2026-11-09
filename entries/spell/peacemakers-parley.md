+++
id = "ref/spell/peacemakers-parley"
kind = "spell"
title = "Peacemaker's Parley"
source_ids = ["dwarves-of-golarion"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "peacemakers_parley", path = "json/spells7.json" },
]
[[sources]]
publication = "dwarves-of-golarion"
page = "23"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Charm"]
descriptors = ["language-dependant", "mind-affecting"]
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 swift action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Area", value = "creatures in a 20-ft.-radius spread" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Cleric, Oracle, Warpriest
Casting time: 1 swift action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Area: creatures in a 20-ft.-radius spread
Subschool: Charm
Descriptors: language-dependant, mind-affecting
:::

> _In order to prepare this spell, the caster must spend an hour performing a ritual in which he
> beseeches [Torag](ref/faith/torag) (or a member of his family) for the aid of
> [Grundinnar](ref/faith/grundinnar). For 24 hours after the ritual, the caster may prepare spells
> of the requested deity. The caster may only attune himself to one additional deity at a time._

You can attempt to influence unfriendly or hostile creatures, altering their attitudes toward you.
After casting, make a Diplomacy check against the creatures as a free action; you gain a +2 sacred
bonus on this check against creatures that failed their saves against the spell. Even if you
favorably manipulate the attitude of the affected targets, they quickly revert to their previous
attitude if threatened or treated poorly.
