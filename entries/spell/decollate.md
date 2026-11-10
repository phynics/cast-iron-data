+++
id = "ref/spell/decollate"
kind = "spell"
title = "Decollate"
aon = "SpellDisplay.aspx?ItemName=Decollate"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "decollate", path = "json/spells3.json" },
]
[[sources]]
publication = "horror-adventures"
page = "116"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Alchemist", level = 4 },
  { class = "Antipaladin", level = 4 },
  { class = "Arcanist", level = 5 },
  { class = "Cleric", level = 5 },
  { class = "Investigator", level = 4 },
  { class = "Oracle", level = 5 },
  { class = "Psychic", level = 6 },
  { class = "Sorcerer", level = 5 },
  { class = "Spiritualist", level = 4 },
  { class = "Warpriest", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, S, F (a red wax pencil)"
range = "touch"
effects = [
  { label = "Target", value = "one willing humanoid or monstrous humanoid creature" },
]
duration = "24 hours"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 4: Alchemist, Antipaladin, Investigator, Spiritualist\
5: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard\
6: Psychic
Casting time: 1 standard action
Components: V, S, F (a red wax pencil)
Range: touch
Duration: 24 hours
Saving throw: none
Spell resistance: yes
Target: one willing humanoid or monstrous humanoid creature
:::

A thin red line circles the target's neck. The target's head becomes detachable so long as she
removes it willingly. While the target's head is detached, she gains DR 2/- and immunity to
decapitation effects and other effects that require their target to have a head or a particular
facial feature. The target is blind so long as she has no head, but she gains
[blindsense](ref/rule/blindsight-and-blindsense) to a distance of 15 feet. The target hears normally
even without its head.

While detached, the target's head appears to be dead. The target can't see through its eyes or hear
events around the head. The target's body knows the direction and distance to its head. Without
additional protection, the severed head has AC 7, [hardness](ref/umr/hardness) 5, and 10 hit points.
Destroying the head while the spell is in effect kills the target of the spell. If the spell's
duration expires normally without the head being reattached, the target dies. If either the target
or the head are removed to a different plane, or if the spell is dispelled, the head teleports back
to its owner and reattaches without further harm.
