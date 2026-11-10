+++
id = "ref/spell/bless"
kind = "spell"
title = "Bless"
aon = "SpellDisplay.aspx?ItemName=Bless"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bless", path = "json/spells12.json" },
]
[[sources]]
publication = "core-rulebook"
page = "249"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Adept", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Inquisitor", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Paladin", level = 1 },
  { class = "Shaman", level = 1 },
  { class = "Warpriest", level = 1 },
]
casting_time = "1 standard action"
components = "V, S, DF"
range = "50 ft."
effects = [
  { label = "Area", value = "The caster and all allies within a 50-ft. burst, centered on the caster" },
]
duration = "1 minute/level"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 1: Adept, Cleric, Inquisitor, Oracle, Paladin, Shaman, Warpriest
Casting time: 1 standard action
Components: V, S, DF
Range: 50 ft.
Duration: 1 minute/level
Saving throw: none
Spell resistance: yes
Area: The caster and all allies within a 50-ft. burst, centered on the caster
Subschool: Compulsion
Descriptors: mind-affecting
:::

Bless fills your allies with courage. Each ally gains a +1 morale bonus on attack rolls and on
saving throws against fear effects.

Bless counters and dispels [bane](ref/spell/bane).
