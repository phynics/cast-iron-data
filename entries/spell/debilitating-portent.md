+++
id = "ref/spell/debilitating-portent"
kind = "spell"
title = "Debilitating Portent"
aon = "SpellDisplay.aspx?ItemName=Debilitating%20Portent"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "debilitating_portent", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "227"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Cleric", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level (d) see text"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Cleric, Oracle, Psychic, Spiritualist, Warpriest, Witch
Casting time: 1 standard action
Components: V, S, DF
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (d) see text
Saving throw: none
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

The target is surrounded by a glowing green aura of ill fate. Each time the spell's subject makes an
attack or casts a spell, it must succeed at a Will saving throw with a DC = 10 + 1/2 caster level +
Charisma (in the case of oracles), Intelligence (in the case of witches), or Wisdom (in the case of
clerics). If it fails the saving throw, it deals half damage with the attack or spell. You can
dismiss this spell as an immediate action when the target confirms a critical hit; doing so negates
the critical hit. The attack that you negated still hits, but only deals half damage.
