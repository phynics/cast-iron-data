+++
id = "ref/spell/deflect-blame"
kind = "spell"
title = "Deflect Blame"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "deflect_blame", path = "json/spells3.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "210"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Mesmerist", level = 2 },
  { class = "Psychic", level = 2 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Witch", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 immediate action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "instantaneous"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Mesmerist, Psychic, Skald\
3: Arcanist, Sorcerer, Witch, Wizard
Casting time: 1 immediate action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: instantaneous
Saving throw: Will negates
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You can cast this spell immediately after attacking a creature, causing that creature to believe
that a different creature that threatens it was responsible for the attack rather than you. You can
instead cast this spell immediately after a failed Bluff, Diplomacy, or Intimidate check, causing
the target of that check to believe that a different creature you designate within spell range was
responsible for the content of that failed check. Using the spell in these ways doesn't compel the
target to undertake a specific action in response to its belief of where the blame lies.
