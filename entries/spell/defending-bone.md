+++
id = "ref/spell/defending-bone"
kind = "spell"
title = "Defending Bone"
aon = "SpellDisplay.aspx?ItemName=Defending%20Bone"
source_ids = ["inner-sea-gods", "gods-and-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "defending_bone", path = "json/spells3.json" },
]
[[sources]]
publication = "inner-sea-gods"
page = "232"
[[sources]]
publication = "gods-and-magic"
page = "31"

[fields]
kind = "spell"
school = "necromancy"
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Cleric", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Magus", level = 2 },
  { class = "Oracle", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Warpriest", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S, DF, F (a Medium creature's skull or femur)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 hour/level or until discharged"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Arcanist, Cleric, Inquisitor, Magus, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, DF, F (a Medium creature's skull or femur)
Range: personal
Duration: 1 hour/level or until discharged
Saving throw: none
Spell resistance: no
Target: you
:::

You animate a bone with necromantic energy, giving it the power to float near your body and
interpose itself against physical attacks. This gives you
[damage reduction](ref/rule/damage-reduction) 5/bludgeoning. Once the bone has prevented a total of
5 points of damage per caster level (maximum 50 points), it is destroyed and the spell is
discharged. This spell has no effect if you have damage reduction from another source.

Some spells are more common among the worshipers of a god. Worshipers of a spell's associated deity
always treat the spell as common, and need not research it in order to prepare or learn it. This
spell is available to members of other faiths, though some temples or religious organizations may
proscribe the use of specific spells.
