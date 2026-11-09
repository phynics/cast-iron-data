+++
id = "ref/spell/dominate-animal"
kind = "spell"
title = "Dominate Animal"
aon = "SpellDisplay.aspx?ItemName=Dominate%20Animal"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dominate_animal", path = "json/spells13.json" },
]
[[sources]]
publication = "core-rulebook"
page = "273"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Druid", level = 3 },
  { class = "Hunter", level = 3 },
  { class = "Mesmerist", level = 3 },
  { class = "Psychic", level = 4 },
  { class = "Shaman", level = 3 },
]
casting_time = "1 round"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one animal" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Druid, Hunter, Mesmerist, Shaman\
4: Psychic
Casting time: 1 round
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one animal
Subschool: Compulsion
Descriptors: mind-affecting
:::

This spell allows you to enchant the targeted animal and direct it with simple commands such as
"Attack," "Run," and "Fetch." Suicidal or self-destructive commands (including an order to attack a
creature two or more size categories larger than the dominated animal) are simply ignored.

Dominate animal establishes a mental link between you and the subject creature. The animal can be
directed by silent mental command as long as it remains in range. You need not see the creature to
control it. You do not receive direct sensory input from the creature, but you know what it is
experiencing. Because you are directing the animal with your own intelligence, it may be able to
undertake actions normally beyond its own comprehension. You need not concentrate exclusively on
controlling the creature unless you are trying to direct it to do something it normally couldn't do.
Changing your instructions or giving a dominated creature a new command is the equivalent of
redirecting a spell, so it is a move action.
