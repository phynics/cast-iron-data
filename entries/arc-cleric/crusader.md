+++
id = "ref/arc-cleric/crusader"
kind = "archetype"
title = "Crusader"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Crusader"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "crusader", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "ultimate-combat"
page = "40"

[fields]
kind = "archetype"
features = [
  { anchor = "diminished-spellcasting" },
  { anchor = "bonus-feat" },
  { anchor = "legion-s-blessing", level = 8 },
]
trades = [
  { alters = "Domain", feature = "domains", by = ["diminished-spellcasting"] },
  { alters = "spellcasting", feature = "spells", by = ["diminished-spellcasting"] },
]
+++

Crusaders serve the militant arm of a church, ready to stand guard over the religion's holy places
and to be its swift, avenging arm against those who resist its truth.

## Diminished Spellcasting {#diminished-spellcasting}

A crusader chooses only one domain and gains one fewer spell of each level than normal. If this
reduces the number to 0, she may cast spells of that level only if they are domain spells or if her
Wisdom allows [bonus spells](ref/rule/determine-bonuses) of that level.

## Bonus Feat {#bonus-feat}

A crusader gains a bonus feat at 1st level, then again at 5th level and every five levels thereafter
(to a maximum of five at 20th level). These bonus feats must be chosen from the following list:
[Heavy Armor Proficiency](ref/feat/armor-proficiency-heavy),
[Improved Shield Bash](ref/feat/improved-shield-bash),
[Martial Weapon Proficiency](ref/feat/martial-weapon-proficiency),
[Saving Shield](ref/feat/saving-shield), [Shield Focus](ref/feat/shield-focus),
[Tower Shield Proficiency](ref/feat/tower-shield-proficiency), and
[Weapon Focus](ref/feat/weapon-focus). At 10th level, a crusader may also choose from the following
feats: [Exotic Weapon Proficiency](ref/feat/exotic-weapon-proficiency),
[Greater Shield Focus](ref/feat/greater-shield-focus),
[Greater Weapon Focus](ref/feat/greater-weapon-focus),
[Improved Critical](ref/feat/improved-critical), [Shield Slam](ref/feat/shield-slam),
[Shield Specialization](ref/feat/shield-specialization), and
[Weapon Specialization](ref/feat/weapon-specialization). At 20th level, a crusader may also choose
from the following feats: [Greater Shield Specialization](ref/feat/greater-shield-specialization)
and [Greater Weapon Specialization](ref/feat/greater-weapon-specialization). Bonus feats marked with
an asterisk (\*) must be applied to the favored weapon of the crusader's deity. A crusader need not
meet the normal class-or level-based prerequisites for these bonus feats.

## Legion's Blessing (Su) {#legion-s-blessing}

At 8th level, a crusader gains the ability to confer beneficial spells quickly to a large group of
allies. As a full-round action, the crusader may confer the effects of a single harmless spell with
a range of touch to a number of creatures equal to [half](ref/misc/fractions-and-rounding) her
cleric level. The spell's range remains touch, so all intended recipients must be within the
crusader's reach when the spell is cast. Using the legion's blessing expends the prepared spell, but
it also requires the crusader to sacrifice another prepared spell three levels higher, as when
spontaneously using a cure or inflict spell. The higher-level spell is not cast but is simply lost,
its magical energy used to power the legion's blessing.
