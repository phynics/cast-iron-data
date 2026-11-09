+++
id = "ref/spell/aura-of-cannibalism"
kind = "spell"
title = "Aura of Cannibalism"
aon = "SpellDisplay.aspx?ItemName=Aura%20of%20Cannibalism"
source_ids = ["monster-codex"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "aura_of_cannibalism", path = "json/spells.json" },
]
[[sources]]
publication = "monster-codex"
page = "9"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M (a piece of flesh from another creature of your species)"
range = "personal"
effects = [
  { label = "Area", value = "20-ft.-radius emanation centered on you" },
]
duration = "1 minute/level (D)"
saving_throw = "Fortitude negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 3: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Witch, Wizard
Casting time: 1 standard action
Components: V, S, M (a piece of flesh from another creature of your species)
Range: personal
Duration: 1 minute/level (D)
Saving throw: Fortitude negates
Spell resistance: yes
Area: 20-ft.-radius emanation centered on you
Descriptors: evil
:::

You emanate an aura that saps the strength of others of your kind and channels their energy into
you. Each round that a creature starts its turn in the spell's area and shares both your creature
type and at least one subtype you possess (if any), that creature must succeed at a Fortitude save
or take 1d4 points of damage. You gain a number of temporary hit points equal to the amount of
damage you deal with this spell (maximum 10 + your caster level). These temporary hit points go away
when the spell ends.

As long as you have at least 5 temporary hit points while this spell is in effect, you gain a +1
competence bonus on attack rolls, saving throws, and skill checks. If you have 15 or more temporary
hit points, this competence bonus increases to +2.
