+++
id = "ref/spell/word-of-resolve"
kind = "spell"
title = "Word of Resolve"
aon = "SpellDisplay.aspx?ItemName=Word%20of%20Resolve"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "word_of_resolve", path = "json/spells16.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "249"

[fields]
kind = "spell"
school = "abjuration"
levels = [
  { class = "Paladin", level = 1 },
]
casting_time = "1 immediate action"
components = "V, DF"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one ally" },
]
duration = "instantaneous"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: abjuration
Level: 1: Paladin
Casting time: 1 immediate action
Components: V, DF
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one ally
:::

You focus your aura on one ally, allowing it to reroll a failed saving throw against a charm or fear
effect with a +4 sacred bonus. If you do not have the aura of courage class ability, this spell has
no effect on the target's fear. If you do not have the aura of resolve class ability, this spell has
no effect on any charm effects on the target.
