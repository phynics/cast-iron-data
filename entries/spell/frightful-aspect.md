+++
id = "ref/spell/frightful-aspect"
kind = "spell"
title = "Frightful Aspect"
aon = "SpellDisplay.aspx?ItemName=Frightful%20Aspect"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "frightful_aspect", path = "json/spells13.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "230"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Cleric", level = 8 },
  { class = "Druid", level = 8 },
  { class = "Oracle", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Witch", level = 8 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 standard action"
components = "V, S, M (the skin of a toad)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 8: Arcanist, Cleric, Druid, Oracle, Psychic, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (the skin of a toad)
Range: personal
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Target: you
Subschool: Polymorph
:::

You become a larger, awful version of yourself. You grow to size Large, and take on features that
horrify your enemies. You gain the following abilities: a +6 size bonus to Strength, a +4 size bonus
to Constitution, a +6 natural armor bonus, DR 10/magic, and
[spell resistance](ref/rule/spell-resistance) equal to 10 + half your caster level. You also emit an
aura that emanates 30 feet from you. Enemy creatures within the aura are shaken. Each time a
creature shaken by this aura hits you with a melee attack, that creature becomes frightened for 1d4
rounds, though at the end of that duration it is no longer affected by this aura. The aura's effect
is a fear and mind-affecting effect.
