+++
id = "ref/spell/animate-dead-lesser"
kind = "spell"
title = "Lesser Animate Dead"
aon = "SpellDisplay.aspx?ItemName=Animate%20Dead%2C%20Lesser"
source_ids = ["core-rulebook", "ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animate_dead_lesser", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/animate-dead" },
]
[[sources]]
publication = "ultimate-magic"
page = "205"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 2 },
  { class = "Occultist", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Shaman", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (an onyx gem worth at least 25 gp per Hit Die of the undead)"
range = "touch"
effects = [
  { label = "Target", value = "one corpse" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Cleric, Occultist, Oracle, Shaman, Spiritualist, Warpriest\
3: Arcanist, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M (an onyx gem worth at least 25 gp per Hit Die of the undead)
Range: touch
Target: one corpse
Duration: instantaneous
Saving throw: none
Spell resistance: no
Descriptors: evil
:::

### Lesser Animate Dead

This spell functions as [animate dead](ref/spell/animate-dead), except you can only create a single
Small or Medium skeleton or zombie. You cannot create variant skeletons or zombies with this spell.
