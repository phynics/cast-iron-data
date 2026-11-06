+++
id = "ref/spell/damnation"
kind = "spell"
title = "Damnation"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "damnation", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "evocation"
descriptors = ["good"]
levels = [
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Paladin", level = 3 },
  { class = "Warpriest", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a drop of holy water)"
range = "personal"
effects = [
  { label = "Area", value = "30-ft.-radius burst centered on you" },
]
duration = "instantaneous"
saving_throw = "Will half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Cleric, Inquisitor, Oracle, Paladin, Warpriest
Casting time: 1 standard action
Components: V, S, M/DF (a drop of holy water)
Range: personal
Duration: instantaneous
Saving throw: Will half
Spell resistance: yes
Area: 30-ft.-radius burst centered on you
Descriptors: good
:::

**Sources:** Horror Adventures pg 115

You pass judgment on your enemies' intentions and punish them with holy power. Each creature in the
spell's area takes 1d8 points of damage per spell level, determined by the most powerful effect with
the evil descriptor either affecting that creature or in its spell repertoire. A caster who prepares
spells takes this damage based on the highest-level evil spell he prepared that day, even if he
already cast that spell. A spontaneous spellcaster takes this damage based on the highest-level evil
spell she knows, even if she has no remaining spell slots available to cast that spell. A creature
with evil [spell-like abilities](ref/umr/spell-like-abilities) takes this damage based on the
highest-level evil spell-like ability it can use. A creature who doesn't cast spells but is the
willing beneficiary of evil spells takes this damage based on the highest-level evil spell currently
affecting it, including spells that affect an area such as desecrate. A creature subject to the
harmful effects of an evil spell are unaffected unless it voluntarily accepted the spell's effects.
