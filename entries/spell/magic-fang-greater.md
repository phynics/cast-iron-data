+++
id = "ref/spell/magic-fang-greater"
kind = "spell"
title = "Greater Magic Fang"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "magic_fang_greater", path = "json/spells6.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/magic-fang" },
]
[[sources]]
publication = "core-rulebook"
page = "309"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Ranger", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Druid, Hunter, Ranger, Spiritualist, Summoner, Unchained Summoner
Casting time: 1 standard action
Components: V, S, DF
Range: close (25 ft. + 5 ft./2 levels)
Target: one living creature
Duration: 1 hour/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

### Greater Magic Fang

This spell functions like [magic fang](ref/spell/magic-fang), except that the enhancement bonus on
attack and damage rolls is +1 per four caster levels (maximum +5). This bonus does not allow a
natural weapon or unarmed strike to bypass [damage reduction](ref/rule/damage-reduction) aside from
magic.

Alternatively, you may imbue all of the creature's natural weapons with a +1 enhancement bonus
(regardless of your caster level).

Greater magic fang can be made permanent with a [permanency](ref/spell/permanency) spell.
