+++
id = "ref/arc-cleric/cloistered-cleric"
kind = "archetype"
title = "Cloistered Cleric"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Cloistered%20Cleric"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "cloistered_cleric", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "ultimate-magic"
page = "31"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting" },
  { anchor = "breadth-of-knowledge", level = 1 },
  { anchor = "well-read", level = 2 },
  { anchor = "verbal-instruction", level = 3 },
  { anchor = "scribe-scroll", level = 4 },
]
+++

Cloistered clerics typically live in a temple and rarely interact with the outside world. They are
bookish and well learned in the lore of the faith, paying less attention to its magical and martial
aspects. A cloistered cleric has the following class features.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Cloistered clerics are proficient with light armor and with the following weapons:
[club](ref/eq-weapon/club), [heavy mace](ref/eq-weapon/heavy-mace),
[light mace](ref/eq-weapon/light-mace), [quarterstaff](ref/eq-weapon/quarterstaff), and
[sling](ref/eq-weapon/sling). They are not proficient with shields.

## Class Skills {#class-skills}

The cloistered cleric's class skills are Appraise (Int), Craft (Int), Diplomacy (Cha), Heal (Wis),
Knowledge (all) (Int), Linguistics (Int), Profession (Wis), Sense Motive (Wis), and Spellcraft
(Int).

## Skill Ranks per Level {#skill-ranks-per-level}

4 + Int modifier.

## Diminished Spellcasting {#diminished-spellcasting}

A cloistered cleric chooses only one domain from her deity's list of domains, and her number of
non-domain spells per day for each spell level is one less than normal (for example, a 4th-level
cloistered cleric has three cantrips, two 1st-level spells, one 1st-level domain spell, one
2nd-level spell, and one 2nd-level domain spell). If this reduces the number of spells per day for
that level to 0, she gains only the bonus spells she would be entitled to based on her Wisdom score
for that level, plus her domain spell for that level.

## Breadth of Knowledge {#breadth-of-knowledge}

At 1st level, a cloistered cleric gains a bonus on Knowledge skill checks equal to
[half](ref/misc/fractions-and-rounding) her class level (minimum +1) and can make Knowledge skill
checks untrained.

## Well-Read (Ex) {#well-read}

At 2nd level, a cloistered cleric gains a +2 bonus on skill checks, caster level checks, and saving
throws if such rolls pertain to mundane or magical glyphs, runes, scrolls, symbols, and other
writings.

## Verbal Instruction (Ex) {#verbal-instruction}

At 3rd level, a cloistered cleric can use the [aid another](ref/rule/aid-another) action to assist
an ally within 30 feet on a skill or ability check. The ally must be able to hear and understand the
cleric's instructions. For every three class levels beyond 3rd, the cloistered cleric can instruct
one additional ally. If all allies are not engaged in the same task, using this ability is a
full-round action rather than a standard action.

## Scribe Scroll (Su) {#scribe-scroll}

At 4th level, a cloistered cleric gains [Scribe Scroll](ref/feat/scribe-scroll) as a bonus feat.
