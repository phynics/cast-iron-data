+++
id = "ref/spell/flame-steed"
kind = "spell"
title = "Flame Steed"
aon = "SpellDisplay.aspx?ItemName=Flame%20Steed"
source_ids = ["core-rulebook", "wilderness-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "flame_steed", path = "json/spells7.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/phantom-steed" },
]
[[sources]]
publication = "wilderness-origins"
page = "28"

[fields]
kind = "spell"
school = "conjuration"
subschools = ["creation"]
levels = [
  { class = "Bloodrager", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Druid", level = 4 },
  { class = "Hunter", level = 4 },
  { class = "Oracle", level = 4 },
  { class = "Paladin", level = 3 },
  { class = "Shaman", level = 4 },
  { class = "Warpriest", level = 4 },
  { class = "Witch", level = 4 },
]
casting_time = "10 minutes"
components = "V, S"
range = "0 ft."
effects = [
  { label = "Effect", value = "one quasi-real creature suitable for a mount" },
]
duration = "1 hour/level (D)"
saving_throw = "none, see text"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 3: Bloodrager, Paladin\
4: Cleric, Druid, Hunter, Oracle, Shaman, Warpriest, Witch
Casting time: 10 minutes
Components: V, S
Range: 0 ft.
Duration: 1 hour/level (D)
Saving throw: none, see text
Spell resistance: no
Effect: one quasi-real creature suitable for a mount
Subschool: creation
:::

### Flame Steed

You conjure a Large, quasi-real creature made of flame. It functions like
[phantom steed](ref/spell/phantom-steed), except as follows.

The flame steed is immune to fire and has acid, cold, and electricity resistance 10. If it or its
rider is attacked, it automatically exhales a 15-foot cone of smoke and ash on your turn as a free
action. Anyone in the cone must succeed at a Fortitude save (DC equal to the spell DC) or become
sickened for 1d6 rounds after leaving the area. This smoke acts as
[obscuring mist](ref/spell/obscuring-mist) for the purpose of [concealment](ref/rule/concealment).
The smoke persists for 1 round.
