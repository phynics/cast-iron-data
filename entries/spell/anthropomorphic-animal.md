+++
id = "ref/spell/anthropomorphic-animal"
kind = "spell"
title = "Anthropomorphic Animal"
aon = "SpellDisplay.aspx?ItemName=Anthropomorphic%20Animal"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "anthropomorphic_animal", path = "json/spells.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "206"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Red Mantis Assassin", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a humanoid thumb bone)"
range = "touch"
effects = [
  { label = "Target", value = "animal touched" },
]
duration = "1 hour/level"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Arcanist, Druid, Hunter, Red Mantis Assassin, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a humanoid thumb bone)
Range: touch
Duration: 1 hour/level
Saving throw: Fortitude negates
Spell resistance: yes
Target: animal touched
Subschool: Polymorph
:::

You transform the touched animal into a bipedal hybrid of its original form with a humanoid form,
similar to how a lycanthrope's hybrid form is a mix of a humanoid and animal form. The animal's
size, type, and ability scores do not change. It loses its natural attacks except for bite (if it
had one as an animal), all types of movement other than its land speed, and special attacks that
rely on its natural attacks. One pair of its limbs is able to manipulate objects and weapons as well
as human hands do; limbless animals like snakes temporarily grow a pair of arms. The creature's
Intelligence increases to 3, and it gains the ability to speak one language you know. It is not
considered proficient in any manufactured weapons. It can attack with unarmed strikes, dealing
unarmed strike damage for a creature of its size (unless it has a bite attack, which is a natural
attack).

Anthropomorphic animal can be made permanent with a [permanency](ref/spell/permanency) spell cast by
a caster of 11th level or higher at a cost of 7,500 gp.
