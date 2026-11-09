+++
id = "ref/spell/spirit-call"
kind = "spell"
title = "Spirit Call"
aon = "SpellDisplay.aspx?ItemName=Spirit%20Call"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spirit_call", path = "json/spells9.json" },
]
[[sources]]
publication = "advanced-class-origins"
page = "31"

[fields]
kind = "spell"
school = "enchantment"
levels = [
  { class = "Druid", level = 1 },
  { class = "Hunter", level = 1 },
  { class = "Shaman", level = 1 },
]
casting_time = "1 full-round action"
components = "V, S, DF"
range = "100 ft."
effects = [
  { label = "Effect", value = "100-ft.-radius spread centered on you" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Druid, Hunter, Shaman
Casting time: 1 full-round action
Components: V, S, DF
Range: 100 ft.
Duration: 1 minute/level
Saving throw: none
Spell resistance: no
Effect: 100-ft.-radius spread centered on you
:::

You call out to nature spirits associated with your spirit (not your wandering spirit) if you are a
shaman, or your domain if you are a druid, beckoning them forth to pay attention to your current
location. For the duration of the spell, all spells from your spirit magic list or domain list that
are cast within the affected area have their caster level increased by 1, and all spellcasters
casting such spells receive a +4 insight bonus on their [concentration](ref/rule/concentration)
checks for those spells only.
