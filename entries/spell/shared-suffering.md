+++
id = "ref/spell/shared-suffering"
kind = "spell"
title = "Shared Suffering"
aon = "SpellDisplay.aspx?ItemName=Shared%20Suffering"
source_ids = ["champions-of-corruption"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "shared_suffering", path = "json/spells9.json" },
]
[[sources]]
publication = "champions-of-corruption"
page = "25"

[fields]
kind = "spell"
school = "necromancy"
descriptors = ["evil"]
levels = [
  { class = "Antipaladin", level = 2 },
  { class = "Arcanist", level = 2 },
  { class = "Inquisitor", level = 2 },
  { class = "Sorcerer", level = 2 },
  { class = "Witch", level = 2 },
  { class = "Wizard", level = 2 },
]
casting_time = "1 standard action"
components = "V, F (a silver dagger inlaid with onyx and jade worth 100 gp)"
range = "long (400 ft. + 40 ft./level)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "instantaneous"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: necromancy
Level: 2: Antipaladin, Arcanist, Inquisitor, Sorcerer, Witch, Wizard
Casting time: 1 standard action
Components: V, F (a silver dagger inlaid with onyx and jade worth 100 gp)
Range: long (400 ft. + 40 ft./level)
Duration: instantaneous
Saving throw: none
Spell resistance: yes
Target: one living creature
Descriptors: evil
:::

You infuse a dagger with necromantic energy, then plunge the dagger into your own body. You take 1d6
points of negative energy damage plus 1d6 points of damage for every 2 caster levels you possess
beyond 1st (to a maximum of 5d6 at 9th level). The target takes an amount of damage equal to the
damage you took this way, plus an amount equal to your Intelligence modifier (if you're a witch or
wizard), Wisdom modifier (if you're an inquisitor), or Charisma modifier (if you're an antipaladin
or sorcerer).

Damage from this spell cannot be divided by effects such as [shield other](ref/spell/shield-other)
or unwilling shield; it cuts through such protections completely.
