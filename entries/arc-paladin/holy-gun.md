+++
id = "ref/arc-paladin/holy-gun"
kind = "archetype"
title = "Holy Gun"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Holy%20Gun"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "holy_gun", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "ultimate-combat"
page = "63"

[fields]
kind = "archetype"
features = [
  { anchor = "have-gun", level = 1 },
  { anchor = "divine-deed", level = 2 },
  { anchor = "smiting-shot" },
  { anchor = "divine-bond", level = 5 },
  { anchor = "holy-grit", level = 11 },
  { anchor = "holy-slinger" },
]
trades = [
  { replaces = "Detect evil", feature = "detect-evil", by = ["have-gun"] },
  { replaces = "Smite evil", feature = "smite-evil", by = ["smiting-shot"] },
  { replaces = "Divine bond", feature = "divine-bond", by = ["divine-bond"] },
  { alters = "Holy champion", feature = "holy-champion", by = ["holy-slinger"] },
]
+++

Not all paladins are knights in shining armor. Holy guns roam the world searching for evil. And
where they find it, they put it down.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Holy guns are proficient with all simple and martial weapons, firearms, and light armor.

## Have Gun {#have-gun}

At 1st level, the holy gun gains the [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat and
[Gunsmithing](ref/feat/gunsmithing) as a bonus feat. She also gains a battered gun identical to the
one gained by the [gunslinger](ref/class/gunslinger). This ability replaces detect evil.

## Divine Deed {#divine-deed}

At 2nd level, the holy gun gains the following deed. This deed works and interacts with grit the
same way as gunslinger deeds, but only the holy gun can use it. If the holy gun also has levels in
gunslinger, she can spend grit points from that class to use this deed.

## Smiting Shot (Su) {#smiting-shot}

A holy gun can spend 1 grit point to make a smiting shot with a firearm attack as a standard action.
If the target is evil, the holy gun adds her Charisma bonus and her paladin level to the damage of
the firearm attack. If the target of the smiting shot is an outsider with the evil subtype, an
evil-aligned dragon, or an undead creature, the bonus to damage increases to the Charisma modifier
plus 2 points of damage per level the paladin possess. Regardless of the target, smiting shot
automatically bypasses any DR the creature might have. This ability replaces smite evil.

## Divine Bond {#divine-bond}

At 5th level, a holy gun forms a bond with her deity. This functions as the paladin's divine bond
ability, except the bond must always take the form of a firearm. In addition to the listed
abilities, a holy gun can add the _[distance](ref/magic-enh/distance)_,
_[reliable](ref/magic-enh/reliable)_, or _[seeking](ref/magic-enh/seeking)_ special abilities to her
weapon, but she cannot add the _defending_ or _disruption_ special abilities. This ability replaces
the standard paladin's divine bond.

## Holy Grit (Ex) {#holy-grit}

At 11th level, a holy gun gains a number of grit points equal to her Charisma modifier (minimum 1)
and gains the use of a single gunslinger deed. She can select any deed that a gunslinger of her
paladin level -4 could use. At 14th level, and every three levels beyond 14th, the holy gun gains
another point of grit and another gunslinger deed that a gunslinger of her level -4 could use. If
she already has levels in gunslinger, she gains a bonus to the maximum amount of grit she can have
each day, equal to her Charisma bonus (if any) but gains no extra grit as the start of each day.

## Holy Slinger (Ex) {#holy-slinger}

This ability function like the holy champion paladin class feature, but the _banishment_ occurs when
she hits an evil outsider with the smiting shot deed.
