+++
id = "ref/spell/contagious-zeal"
kind = "spell"
title = "Contagious Zeal"
aon = "SpellDisplay.aspx?ItemName=Contagious%20Zeal"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "contagious_zeal", path = "json/spells12.json" },
]
[[sources]]
publication = "occult-adventures"
page = "162"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["emotion", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bard", level = 2 },
  { class = "Cleric", level = 3 },
  { class = "Inquisitor", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Skald", level = 2 },
  { class = "Sorcerer", level = 3 },
  { class = "Spiritualist", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 round/level"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 2: Bard, Skald\
3: Arcanist, Cleric, Inquisitor, Oracle, Psychic, Sorcerer, Spiritualist, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
Target: one creature
Subschool: Compulsion
Descriptors: emotion, mind-affecting
:::

The target gains a +2 morale bonus on attack rolls and weapon damage rolls, 1d6 temporary hit
points, and a +4 morale bonus on saving throws against fear effects and to the DC of Intimidate
checks attempted against her. Once per round, the target can select one other creature to gain this
bonus as well. The chosen creature can be no farther from the target than 25 feet + 5 feet for every
2 caster levels you possess, and a creature can't be selected more than once in this way. Such
allies gain only the bonuses and temporary hit points; they don't continue to spread it to other
creatures. The additional creatures' bonuses and temporary hit points share the original spell's
duration, so when that duration ends, all affected creatures lose their bonuses and any remaining
temporary hit points from this spell.
