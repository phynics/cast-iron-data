+++
id = "ref/spell/animal-aspect-greater"
kind = "spell"
title = "Greater Animal Aspect"
aon = "SpellDisplay.aspx?ItemName=Animal%20Aspect%2C%20Greater"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "animal_aspect_greater", path = "json/spells.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/animal-aspect" },
]
[[sources]]
publication = "ultimate-combat"
page = "223"

[fields]
kind = "spell"
school = "transmutation"
subschools = ["Polymorph"]
levels = [
  { class = "Alchemist", level = 3 },
  { class = "Arcanist", level = 4 },
  { class = "Bloodrager", level = 3 },
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Investigator", level = 3 },
  { class = "Magus", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Ranger", level = 3 },
  { class = "Red Mantis Assassin", level = 4 },
  { class = "Sorcerer", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (a part of the animal)"
range = "personal"
effects = [
  { label = "Target", value = "you" },
]
duration = "1 minute/level (D)"
saving_throw = "none"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 3: Alchemist, Bloodrager, Druid, Hunter, Investigator, Magus, Ranger\
4: Arcanist, Psychic, Red Mantis Assassin, Sorcerer, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (a part of the animal)
Range: personal
Target: you
Duration: 1 minute/level (D)
Saving throw: none
Spell resistance: yes (harmless)
Subschool: Polymorph
:::

### Greater Animal Aspect

This spell functions like [animal aspect](ref/spell/animal-aspect), except you can either gain two
aspects at once or one aspect that adds effects to the aspects that animal aspect grants, as
described below.

_Frog:_ You gain a Swim speed equal to half your normal speed, and all the benefits of having a swim
speed.

_Gorilla:_ You gain a +2 competence bonus on Perception checks, and a +1 competence bonus on
Fortitude saves.

_Monkey:_ You gain a +4 competence bonus on Acrobatics checks.

_Otter:_ Your swim speed increases to your full normal speed, and you need not make concentration
checks to cast spells underwater.

_Raccoon:_ Your competence bonuses on Disable Device, Sleight of Hand, and Stealth checks increase
to +4.

_Raptor:_ Your enhancement bonus to speed increases to +30 feet, and you gain the benefit of the
[Run](ref/feat/run) feat.

_Tree Lizard:_ You gain a +4 competence bonus on Stealth checks.
