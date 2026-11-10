+++
id = "ref/spell/control-summoned-creature"
kind = "spell"
title = "Control Summoned Creature"
aon = "SpellDisplay.aspx?ItemName=Control%20Summoned%20Creature"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "control_summoned_creature", path = "json/spells12.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "212"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 4 },
  { class = "Bard", level = 3 },
  { class = "Cleric", level = 4 },
  { class = "Mesmerist", level = 3 },
  { class = "Occultist", level = 3 },
  { class = "Oracle", level = 4 },
  { class = "Psychic", level = 4 },
  { class = "Skald", level = 3 },
  { class = "Sorcerer", level = 4 },
  { class = "Summoner", level = 3 },
  { class = "Unchained Summoner", level = 3 },
  { class = "Warpriest", level = 4 },
  { class = "Wizard", level = 4 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one summoned creature" },
]
duration = "1 round/level"
saving_throw = "Will negates"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 3: Bard, Mesmerist, Occultist, Skald, Summoner, Unchained Summoner\
4: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates
Spell resistance: yes
Target: one summoned creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

You seize control of a summoned creature by disrupting the bond between it and the caster who
summoned it. If the creature fails its save, you may command it as if you had summoned it. The
original caster can attempt to regain control of the creature as a standard action by making an
opposed Spellcraft check against you. When your spell ends, control reverts to the original
summoner. If the summoning spell ends before this spell ends, the remaining duration of this spell
is lost.
