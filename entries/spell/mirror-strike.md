+++
id = "ref/spell/mirror-strike"
kind = "spell"
title = "Mirror Strike"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mirror_strike", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bloodrager", level = 1 },
  { class = "Magus", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Red Mantis Assassin", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, M (a shard of mirror)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "see text"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 1: Arcanist, Bloodrager, Magus, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (a shard of mirror)
Range: personal
Duration: see text
Saving throw: none
Spell resistance: no
Target: you
:::

**Sources:** Ultimate Combat pg 236

You briefly alter the flow of time to split a melee attack into two attacks. Before the end of your
next turn, when you make your next melee attack roll, compare the result to the AC of two opponents
within your reach. If the selected opponents are flanking you, you gain a +2 bonus on your attack
roll (and confirmation attack roll, see below). If you hit both enemies, you can deal half damage to
each. Hitting only one opponent allows you to deal that opponent normal damage for your attack. On a
critical threat, you can make only one attack roll to confirm the critical hit against both
opponents. If you confirm against both, you deal half your critical hit damage to each. Your hit is
a normal hit rather than a critical if you confirm against only one opponent. If you fail to use the
effect before the end of your next turn, the spell ends.
