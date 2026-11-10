+++
id = "ref/spell/grasping-hand"
kind = "spell"
title = "Grasping Hand"
aon = "SpellDisplay.aspx?ItemName=Grasping%20Hand"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grasping_hand", path = "json/spells5.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/interposing-hand" },
]
[[sources]]
publication = "core-rulebook"
page = "291"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, F (a soft glove)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "10-ft. hand" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 7: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, F (a soft glove)
Range: medium (100 ft. + 10 ft./level)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Effect: 10-ft. hand
Descriptors: force
:::

This spell functions as [interposing hand](ref/spell/interposing-hand), except that it can also
grapple one opponent you select. The grasping hand gets one grapple attack per round. This attack
does not provoke an attack of opportunity. Its CMB and CMD for grapple checks use your caster level
in place of its base attack bonus, with a +10 bonus for its Strength (31) score and a +1 bonus for
being Large (its Dexterity is 10, granting no bonus on the Combat Maneuver Defense). The hand holds
but does not harm creatures that it grapples. Directing the spell to a new target is a move action.
The grasping hand can instead be directed to bull rush a target, using the same bonuses outlined
above, or it can be directed to interpose itself, as interposing hand does.
