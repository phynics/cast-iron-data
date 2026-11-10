+++
id = "ref/spell/mirror-mantis"
kind = "spell"
title = "Mirror Mantis"
aon = "SpellDisplay.aspx?ItemName=Mirror%20Mantis"
source_ids = ["adventurers-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mirror_mantis", path = "json/spells14.json" },
]
[[sources]]
publication = "adventurers-guide"
page = "160"

[fields]
kind = "spell"
school = "illusion"
subschools = ["Phantasm"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 1 },
  { class = "Bard", level = 1 },
  { class = "Cleric", level = 1 },
  { class = "Mesmerist", level = 1 },
  { class = "Occultist", level = 1 },
  { class = "Oracle", level = 1 },
  { class = "Psychic", level = 1 },
  { class = "Skald", level = 1 },
  { class = "Sorcerer", level = 1 },
  { class = "Warpriest", level = 1 },
  { class = "Wizard", level = 1 },
]
casting_time = "1 standard action"
components = "S, F (a hand mirror stained with a dried drop of blood)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 hour/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: illusion
Level: 1: Arcanist, Bard, Cleric, Mesmerist, Occultist, Oracle, Psychic, Skald, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: S, F (a hand mirror stained with a dried drop of blood)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 hour/level
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Phantasm
Descriptors: mind-affecting
:::

Whenever the target of this spell looks into a mirror or other reflective surface where it can see
its own visage clearly, it sees a Red Mantis assassin (in full armor, face hidden by a mantis mask)
looking back at it. The reflection is harmless and mimics the target's motions perfectly; no one
else can see this illusion. The first time the target sees the Red Mantis reflection, it must
succeed at a Will save be or shaken and take a -2 penalty on saves against fear effects for as long
as it can see the altered image and for 3 rounds thereafter. A new save must be attempted each time
the creature views its reflection during the spell's duration. Once a creature successfully saves,
it becomes immune to being shaken by the caster's mirror mantis spell for 24 hours, though it will
still see the Red Mantis reflection until the spell ends.
