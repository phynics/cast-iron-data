+++
id = "ref/spell/death-pact"
kind = "spell"
title = "Death Pact"
source_ids = ["occult-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "death_pact", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "enchantment"
descriptors = ["mind-affecting"]
levels = [
  { class = "Bard", level = 5 },
  { class = "Skald", level = 5 },
  { class = "Witch", level = 6 },
]
casting_time = "1 minute"
components = "V, S, M (a contract signed in blood)"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "24 hours"
saving_throw = "Will negates, see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Skald\
6: Witch
Casting time: 1 minute
Components: V, S, M (a contract signed in blood)
Range: touch
Duration: 24 hours
Saving throw: Will negates, see text
Spell resistance: yes
Target: one creature
Descriptors: mind-affecting
:::

**Sources:** Occult Origins pg 13

You take control of a creature's mind and implant deadly subconscious commands. This spell functions
as [dominate person](ref/spell/dominate-person), allowing you to control your subject and see
through her senses, but also implants a powerful burst of psychic energy in the subject's mind. At
any point during the spell's duration, you can trigger this burst as an immediate action, dealing
1d8 points of damage per caster level (Fortitude half) to the subject. If this damage is enough to
reduce to target to 0 or fewer hit points, the target dies instantly.

Your target can also willingly trigger this psychic burst as an immediate action. You can specify
conditions (such as being captured) when she should do so, though such orders are considered
dangerous and allow the subject a new Will saving throw with a +2 bonus.
