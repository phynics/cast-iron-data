+++
id = "ref/spell/pox-of-rumors"
kind = "spell"
title = "Pox of Rumors"
aon = "SpellDisplay.aspx?ItemName=Pox%20of%20Rumors"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "pox_of_rumors", path = "json/spells14.json" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "222"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["curse", "mind-affecting"]
levels = [
  { class = "Arcanist", level = 7 },
  { class = "Bard", level = 5 },
  { class = "Cleric", level = 7 },
  { class = "Mesmerist", level = 5 },
  { class = "Oracle", level = 7 },
  { class = "Psychic", level = 7 },
  { class = "Skald", level = 5 },
  { class = "Sorcerer", level = 7 },
  { class = "Spiritualist", level = 5 },
  { class = "Witch", level = 7 },
  { class = "Wizard", level = 7 },
]
casting_time = "8 hours"
components = "V, S, M (a physical connection to the target; see text)"
range = "see text"
effects = [
  { label = "Target", value = "one creature" },
]
duration = "1 day/level"
saving_throw = "Will negates, then Will partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 5: Bard, Mesmerist, Skald, Spiritualist\
7: Arcanist, Cleric, Oracle, Psychic, Sorcerer, Witch, Wizard
Casting time: 8 hours
Components: V, S, M (a physical connection to the target; see text)
Range: see text
Duration: 1 day/level
Saving throw: Will negates, then Will partial (see text)
Spell resistance: yes
Target: one creature
Subschool: Compulsion
Descriptors: curse, mind-affecting
:::

You curse the target to attract negative assumptions and rumors of a sort you specify when you cast
the spell. If the target fails the initial save to negate the curse, every day that it spends in a
settlement, it must attempt a Will save. If it fails, it accidentally says or does something that
makes others assume the rumor you specified is true in some way that is unflattering or
incriminating. If the creature is not aware of the nature of the rumors, it takes a -4 penalty on
these secondary saves. After the first failed save, the attitude each resident in the settlement has
regarding the target is worsened by one step. For each additional failure, the target becomes the
victim of focused harassment. A group of residents taunts or attacks the creature, potentially
sending the authorities to investigate if the rumor indicates criminal guilt.

The spell can be cast at any distance. The difficulty of the save depends on your knowledge of the
subject and what sort of physical connection you have to that creature. The target gains the same
bonuses and penalties on its Will save to resist this spell as the bonuses and penalties that apply
to the scrying spell (including a +5 bonus if the target is on another plane), except that you can't
cast pox of rumors without at least a possession or garment to use as the material component, and
the target takes no penalty when you use a possession or garment and only a -5 penalty when you use
a piece of the target's body. Pox of rumors is a curse, and until its duration expires, it can be
removed only by [remove curse](ref/spell/remove-curse) or similar magic.
