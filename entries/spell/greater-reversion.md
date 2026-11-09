+++
id = "ref/spell/greater-reversion"
kind = "spell"
title = "Greater Reversion"
aon = "SpellDisplay.aspx?ItemName=Greater%20Reversion"
source_ids = ["plane-hoppers-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "greater_reversion", path = "json/spells14.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/minor-reversion" },
]
[[sources]]
publication = "plane-hoppers-handbook"
page = "28"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Healing"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 4 },
  { class = "Sorcerer", level = 5 },
  { class = "Warpriest", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "20 minutes"
components = "V, S"
range = "personal"
effects = [
  { label = "Target", value = "self" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 4: Psychic\
5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 20 minutes
Components: V, S
Range: personal
Target: self
Duration: 24 hours
Saving throw: none
Spell resistance: no
Subschool: Healing
:::

### Greater Reversion

You create a fine-tuned replica of yourself within the [Akashic Record](ref/rule/akashic-record) at
the time the spell is cast. You must currently have a number of hit points equal to or greater than
half your maximum hit points to cast the spell. If at any time during the duration of the spell you
are brought below half your maximum hit points, you can end this spell as an immediate action to
absorb strength from your replica and immediately regain a number of hit points equal to 3d8 plus 1
point per caster level (maximum +15).
