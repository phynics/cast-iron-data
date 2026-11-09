+++
id = "ref/spell/wracking-ray"
kind = "spell"
title = "Wracking Ray"
source_ids = ["champions-of-corruption"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "wracking_ray", path = "json/spells16.json" },
]
[[sources]]
publication = "champions-of-corruption"
page = "25"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil", "pain"]
levels = [
  { class = "Arcanist", level = 5 },
  { class = "Sorcerer", level = 5 },
  { class = "Witch", level = 5 },
  { class = "Wizard", level = 5 },
]
casting_time = "1 standard action"
components = "V, M (an old bone, broken in the casting)"
range = "medium (100 ft. + 10 ft./level)"
effects = [
  { label = "Effect", value = "ray" },
]
duration = "instantaneous"
saving_throw = "Fortitude half"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 5: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, M (an old bone, broken in the casting)
Range: medium (100 ft. + 10 ft./level)
Duration: instantaneous
Saving throw: Fortitude half
Spell resistance: yes
Effect: ray
Descriptors: evil, pain
:::

A ray of sickly greenish-gray negative energy issues forth from the palm of your hand. Make a ranged
touch attack against the target. A creature hit by this spell is wracked by painful spasms as its
muscles and sinews wither and twist. The subject takes 1d4 points of Dexterity and Strength damage
per 3 caster levels you possess (maximum 5d4 each). This spell cannot reduce an ability score
below 1. A successful Fortitude save halves the damage.
