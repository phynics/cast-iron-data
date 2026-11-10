+++
id = "ref/spell/vampiric-hunger"
kind = "spell"
title = "Vampiric Hunger"
source_ids = ["faiths-of-corruption"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "vampiric_hunger", path = "json/spells11.json" },
]
[[sources]]
publication = "faiths-of-corruption"
page = "29"

[fields]
kind = "spell"
school = "necromancy"
subschools = ["Polymorph"]
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 3 },
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 minute/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Antipaladin, Arcanist, Cleric, Druid, Hunter, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 round
Components: V, S
Range: touch
Duration: 1 minute/level
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Polymorph
Descriptors: evil
:::

The target of this spell grows the fangs of a vampire, as well as a thirst for blood. For the
duration of this spell, the target gains the ability to drain an opponent's blood during a grapple;
if the target establishes or maintains a pin, it drains blood, dealing 1d4 points of Constitution
damage. Each round it drains blood in this way, the target heals 5 hit points or gains 5 temporary
hit points for the duration of the spell (up to a maximum number of temporary hit points equal to
its full normal hit points). If the target does not drain blood in this way while under the effects
of this spell, it becomes exhausted at the end of the spell's duration.

**Note:** Normally, only [transmutation](ref/spelldef/transmutation) spells can be of the polymorph
subschool. No errata has been issued for this spell; it's unclear if the school and subschool were
an intentional design choice or a mistake.
