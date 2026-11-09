+++
id = "ref/carried/core-rulebook/spells/invisibility/mass"
kind = "spell"
title = "Invisibility, Mass"
aon = "SpellDisplay.aspx?ItemName=Invisibility%2C%20Mass"
source_ids = ["core-rulebook"]
section = ["Spells", "Invisibility"]
tags = ["illusion", "glamer"]
provenance = [
  { dataset = "psrd-data", record = "pfsrd://Core Rulebook/Spells/Invisibility/Mass", path = "core_rulebook/spell/invisibility_mass.json" },
]

[fields]
kind = "spell"
school = "illusion"
subschools = ["glamer"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Sorcerer", level = 7 },
  { class = "Summoner", level = 5 },
  { class = "Wizard", level = 7 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (an eyelash encased in gum arabic)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Targets", value = "any number of creatures, no two of which can be more than 180 ft. apart" },
]
duration = "1 min./level (D)"
saving_throw = "Will negates (harmless) or Will negates (harmless, object)"
spell_resistance = "yes (harmless) or yes (harmless, object)"
+++

::: statblock
School: illusion (glamer)
Level: 5: Summoner\
7: Arcanist, Sorcerer, Wizard
Casting Time: 1 standard action
Components: V, S, M/DF (an eyelash encased in gum arabic)
Range: long (400 ft. + 40 ft./level)
Targets: any number of creatures, no two of which can be more than 180 ft. apart
Duration: 1 min./level (D)
Saving Throw: Will negates (harmless) or Will negates (harmless, object)
Spell Resistance: yes (harmless) or yes (harmless, object)
:::

_As invisibility, but affects all in range._

This spell functions like _invisibility_, except that the effect moves with the group and is broken
when anyone in the group attacks. Individuals in the group cannot see each other. The spell is
broken for any individual who moves more than 180 feet from the nearest member of the group. If only
two individuals are affected, the one moving away from the other one loses its invisibility. If both
are moving away from each other, they both become visible when the distance between them exceeds 180
feet.
