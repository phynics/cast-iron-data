+++
id = "ref/spell/cushioning-bands"
kind = "spell"
title = "Cushioning Bands"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cushioning_bands", path = "json/spells3.json" },
]

[fields]
kind = "spell"
school = "conjuration"
subschools = ["Creation"]
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Summoner", level = 2 },
  { class = "Unchained Summoner", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, S"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "1 hour/level or until discharged (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: conjuration
Level: 2: Arcanist, Psychic, Sorcerer, Summoner, Unchained Summoner, Wizard
Casting time: 1 standard action
Components: V, S
Range: touch
Duration: 1 hour/level or until discharged (D)
Saving throw: Will negates (harmless)
Spell resistance: yes
Target: creature touched
Subschool: Creation
Descriptors: force
:::

**Sources:** Ultimate Magic pg 215

Invisible bands of force encircle vital areas of the target. The bands resist crushing forces and
impacts without interfering with movement. The target gains DR 2/piercing or slashing and takes half
damage from constriction, falling, and being buried, as well as from similar crushing effects such
as crushing hand. Grapple checks for attacks other than constricting (such as pinning or swallowing
whole) are not affected. Once the spell has blocked 12 points of damage per caster level (to a
maximum of 120 points at 10th level), it is discharged. The bands have no effect on incorporeal
attacks unless they deal damage from constriction or crushing, or unless the attacks would be
subject to [damage reduction](ref/rule/damage-reduction).
