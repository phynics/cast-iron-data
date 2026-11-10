+++
id = "ref/spell/stave-off-corruption"
kind = "spell"
title = "Stave Off Corruption"
aon = "SpellDisplay.aspx?ItemName=Stave%20Off%20Corruption"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "stave_off_corruption", path = "json/spells9.json" },
]
[[sources]]
publication = "horror-adventures"
page = "128"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Cleric", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Paladin", level = 2 },
  { class = "Warpriest", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, M (see text)"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/2 caster levels"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 2: Cleric, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, M (see text)
Range: touch
Duration: 1 day/2 caster levels
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
:::

You ward the target to slow the advancement of its corruption. The target receives a +2 circumstance
bonus on saving throws against the advancement of its corruption, as described in the catalyst
section of each corruption. Multiple applications of this spell do not stack, nor does the bonus
stack with morale, profane, or sacred bonuses on saving throws against the advancement of the
target's corruption.

The material components for this spell vary with the type of corruption. For example, garlic is used
for a vampirism corruption, a sprig of wolfsbane is used for a lycanthropy corruption, and so on.
The GM can determine appropriate material components, but the components should cost at least 25 gp.
