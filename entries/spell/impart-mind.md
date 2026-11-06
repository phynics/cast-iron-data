+++
id = "ref/spell/impart-mind"
kind = "spell"
title = "Impart Mind"
source_ids = ["inner-sea-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "impart_mind", path = "json/spells14.json" },
]

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Arcanist", level = 6 },
  { class = "Cleric", level = 6 },
  { class = "Magus", level = 5 },
  { class = "Oracle", level = 6 },
  { class = "Sorcerer", level = 6 },
  { class = "Warpriest", level = 6 },
  { class = "Wizard", level = 6 },
]
casting_time = "2 rounds"
components = "V, S, M (diamond dust worth at least 1,000 gp)"
range = "touch"
effects = [
  { label = "Target", value = "permanent nonintelligent magic item touched" },
]
duration = "1 hour/level"
saving_throw = "none"
spell_resistance = "no"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 5: Magus\
6: Arcanist, Cleric, Oracle, Sorcerer, Warpriest, Wizard
Casting time: 2 rounds
Components: V, S, M (diamond dust worth at least 1,000 gp)
Range: touch
Duration: 1 hour/level
Saving throw: none
Spell resistance: no
Target: permanent nonintelligent magic item touched
:::

**Sources:** Inner Sea Magic pg 57

This spell grants the target magic item temporary intelligence by siphoning off a tiny portion of
your own mind to infuse the object. Only permanent magic items may be enhanced by this spell-one-use
items and charged items cannot be affected by impart mind. Intelligent magic items cannot be
affected by impart mind.

When you cast impart mind on a magic item, the item gains an Intelligence, Wisdom, and Charisma
score of 10 and gains your alignment. You have no special control over the item once it becomes
intelligent, although since it has your alignment, personality conflicts with items you wield won't
be a problem. Determine the item's ego normally, as per the rules on intelligent items in the Core
Rulebook.

An item made intelligent via impart mind communicates via speech and has normal senses to a range of
60 feet. It speaks and reads one language known by you - if you know multiple languages, you may
choose which language the item knows.

When you cast impart mind on an item, roll once on [Table 15-24](ref/rule/intelligent-item-powers)
to randomly determine the item's power-add your caster level to this roll. By expending additional
diamond dust in excess of the 1,000 gp worth of material components required to cast this spell, you
can gain further bonuses on the d% roll made to determine the item's power. Every additional 100 gp
in diamond dust you use in excess grants a cumulative +1 bonus to the roll, up to a maximum
additional bonus equal to your caster level. If the item gains the ability to cast a spell,
determine the spell it can cast randomly from spells you know of the appropriate level. If the item
gains ranks in a skill, it gains ranks in a random skill in which you have at least 1 rank.

If you roll above 100, then you can choose one item power on Table 15-24 to grant the item, and the
item gains a special purpose. Roll once on Tables [15-25](ref/rule/special-purpose-items) and
[15-26](ref/rule/dedicated-powers) to determine what the item's special purpose and dedicated powers
are. These d% rolls are not modified by your caster level or any additional powdered gems you used
to cast the spell.

Once this spell ends, the item reverts to its previous nature - if you cast this spell on the item
again, it gains entirely different powers as determined by a new set of rolls.
