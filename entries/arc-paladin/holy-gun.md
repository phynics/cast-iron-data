+++
id = "ref/arc-paladin/holy-gun"
kind = "archetype"
title = "Holy Gun"
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
replaces = ["Detect evil", "Smite evil", "Divine bond"]
alters = ["Holy champion"]
replaces_features = ["detect-evil", "smite-evil", "divine-bond"]
alters_features = ["holy-champion"]
+++

Not all paladins are knights in shining armor. Holy guns roam the world searching for evil. And
where they find it, they put it down.

**Weapon and Armor Proficiency**

**Info:** Holy guns are proficient with all simple and martial weapons, firearms, and light armor.

**Have Gun**

**Ability:** The holy gun gains the [Amateur Gunslinger](ref/feat/amateur-gunslinger) feat and
[Gunsmithing](ref/feat/gunsmithing) as a bonus feat. She also gains a battered gun identical to the
one gained by the [gunslinger](ref/class/gunslinger).

**Gained:** At 1st Level

**Replaces:** Detect evil

**Divine Deed**

**Ability:** The holy gun gains the following deed. This deed works and interacts with grit the same
way as gunslinger deeds, but only the holy gun can use it. If the holy gun also has levels in
gunslinger, she can spend grit points from that class to use this deed.

**Gained:** At 2nd Level

**Replaces:** Smite evil

**Smiting Shot (Su)**

**Standard:** A holy gun can spend 1 grit point to make a _smiting shot_ with a firearm attack. If
the target is evil, the holy gun adds her Charisma bonus and her paladin level to the damage of the
firearm attack. If the target of the _smiting shot_ is an outsider with the evil subtype, an
evil-aligned dragon, or an undead creature, the bonus to damage increases to the Charisma modifier
plus 2 points of damage per level the paladin possess. Regardless of the target, _smiting shot_
automatically bypasses any DR the creature might have.

**Divine Bond**

**Ability:** A holy gun forms a bond with her deity. This functions as the paladin's _divine bond_
ability, except the bond must always take the form of a firearm. In addition to the listed
abilities, a holy gun can add the [distance](ref/magic-enh/distance),
[reliable](ref/magic-enh/reliable), or [seeking](ref/magic-enh/seeking) special abilities to her
weapon, but she cannot add the _defending_ or _disruption_ special abilities.

**Gained:** At 5th Level

**Replaces:** Divine bond

**Holy Grit (Ex)**

**Ability:** A holy gun gains a number of grit points equal to her Charisma modifier (minimum 1) and
gains the use of a single gunslinger deed. She can select any deed that a 7th-level gunslinger could
use.

**Gained:** At 11th Level

**Special:** If she already has levels in gunslinger, she gains a bonus to the maximum amount of
grit she can have each day, equal to her Charisma bonus (if any) but gains no extra grit as the
start of each day.

At 14th level: The holy gun gains another point of grit and another gunslinger deed that a
10th-level gunslinger could use.

At 17th level: The holy gun gains another point of grit and another gunslinger deed that a
13th-level gunslinger could use.

At 20th level: The holy gun gains another point of grit and another gunslinger deed that a
16th-level gunslinger could use.

**Holy Slinger (Ex)**

**Alters:** Holy champion

**Info:** This ability function like the _holy champion_ paladin class feature, but the banishment
occurs when she hits an evil outsider with the _smiting shot_ deed.
