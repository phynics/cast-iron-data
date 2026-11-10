+++
id = "ref/spell/antithetical-constraint"
kind = "spell"
title = "Antithetical Constraint"
aon = "SpellDisplay.aspx?ItemName=Antithetical%20Constraint"
source_ids = ["champions-of-balance"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "antithetical_constraint", path = "json/spells.json" },
]
[[sources]]
publication = "champions-of-balance"
page = "26"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 4 },
  { class = "Skald", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Witch", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 4: Arcanist, Bard, Skald, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You constrain the target such that the target automatically misses with all attacks made against
creatures that are not of the opposite alignment of it. For example, a lawful evil target would
automatically fail at all attacks except those made against chaotic good creatures, and a neutral
good target would automatically fail at all attacks except those made against neutral evil
creatures. For the purposes of antithetical constraint, creatures that are chaotic evil, chaotic
good, lawful evil, or lawful good are all considered to have the opposite alignment of a target
whose alignment is neutral with no other alignment components. This restriction doesn't apply to
effects that do not require attack rolls, such as [magic missile](ref/spell/magic-missile).
