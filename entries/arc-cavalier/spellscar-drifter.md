+++
id = "ref/arc-cavalier/spellscar-drifter"
kind = "archetype"
title = "Spellscar Drifter"
aon = "ArchetypeDisplay.aspx?FixedName=Cavalier%20Spellscar%20Drifter"
source_ids = ["inner-sea-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellscar_drifter", path = "json/archetypes_cavalier.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cavalier" },
]
[[sources]]
publication = "inner-sea-combat"
page = "45"

[fields]
kind = "archetype"
features = [
  { anchor = "have-gun", level = 1 },
  { anchor = "daring-deeds", level = 3 },
  { anchor = "worn-banner", level = 5 },
  { anchor = "notorious-deeds", level = 9 },
  { anchor = "old-reliable", level = 11 },
  { anchor = "spell-severed", level = 12 },
  { anchor = "infamous-deeds", level = 17 },
  { anchor = "tough-as-nails", level = 20 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Tactician", feature = "tactician", by = ["have-gun"] },
  { replaces = "Cavalier's charge", feature = "cavalier-s-charge", by = ["daring-deeds"] },
  { replaces = "The cavalier's normal bonus feats", feature = "bonus-feat" },
  { replaces = "Greater tactician", feature = "greater-tactician", by = ["notorious-deeds"] },
  { replaces = "Mighty charge", feature = "mighty-charge", by = ["old-reliable"] },
  { replaces = "Demanding challenge", feature = "demanding-challenge", by = ["spell-severed"] },
  { replaces = "Master tactician", feature = "master-tactician", by = ["infamous-deeds"] },
  { replaces = "Supreme charge", feature = "supreme-charge", by = ["tough-as-nails"] },
  { replaces = "Banner", feature = "banner", by = ["worn-banner"] },
]
+++

The Spellscar Desert is a dangerous wasteland into which few venture without a guide. Spellscar
drifters have made themselves at home in these badlands. When not scouring the desert for forgotten
treasures or magic hidden by the region's shifting magic-dead zones, a Spellscar drifter might hire
himself out as a guide, bodyguard, or assassin. There are even a few Spellscar drifters who are
temporarily deputized by the Grand Duchy of Alkenstar to perform law enforcement tasks beyond the
reach of the city's normal constabulary. Spellscar drifters are self-reliant and always keep their
firearms loaded—in the Spellscar Desert, a rider with a slow draw doesn't live long.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

Spellscar drifters are proficient with all simple and martial weapons, the
[whip](ref/eq-weapon/whip), and with all firearms. They are proficient with all light armor. This
replaces the cavalier's normal weapon and armor proficiencies.

## Have Gun {#have-gun}

At 1st level, the Spellscar drifter gains [Amateur Gunslinger](ref/feat/amateur-gunslinger) and
[Gunsmithing](ref/feat/gunsmithing) as bonus feats. The Spellscar drifter uses his Charisma modifier
(minimum 1) in place of his Wisdom modifier when determining his maximum grit points and for any
other abilities which use grit. Additionally, he also gains a battered gun identical to the one
gained by the [gunslinger](ref/class/gunslinger). This ability replaces tactician.

## Daring Deeds (Ex) {#daring-deeds}

At 3rd level, a Spellscar drifter gains [Rapid Reload](ref/feat/rapid-reload) as a bonus feat. The
Spellscar drifter must choose a firearm to associate with this feat. Additionally, the Spellscar
drifter can select one additional 1st-level gunslinger deed which he can use with his Amateur
Gunslinger feat. This ability replaces cavalier's charge.

## Worn Banner (Ex) {#worn-banner}

At 5th level, a Spellscar drifter can choose to use his hat as his banner. If the drifter does not
wear a hat, another iconic accessory—such as an eyemask, bandana, or distinguishing coat—can instead
serve as his banner. In all other ways, this ability functions as and replaces the banner cavalier
ability.

## Bonus Feats {#bonus-feats}

At 6th level, and at every 6 levels thereafter, a Spellscar drifter gains a bonus feat in addition
to those gained from normal advancement. These bonus feats must be either combat or grit feats, and
the Spellscar drifter must meet the prerequisites as normal. This replaces the cavalier's normal
bonus feats.

## Notorious Deeds (Ex) {#notorious-deeds}

At 9th level, a Spellscar drifter can select two additional gunslinger deeds which he can use with
his Amateur Gunslinger feat. The Spellscar drifter can choose one deed from the list of deeds
available to 3rd-level gunslingers and one from the list available to 7th-level gunslingers. This
ability replaces greater tactician.

## Old Reliable (Ex) {#old-reliable}

At 11th level, whenever a Spellscar drifter declares a challenge, the threat range of the Spellscar
drifter's firearm is doubled against the target of his challenge. This increase only affects one
weapon and does not stack with other effects that increase the threat range of the weapon. In
addition, if the Spellscar drifter rolls a misfire during his challenge, the Spellscar drifter can
spend 1 grit point to reroll the attack roll. The Spellscar drifter must accept the results of the
second roll, even if it is worse. This ability replaces mighty charge.

## Spell Severed (Ex) {#spell-severed}

At 12th level, a Spellscar drifter becomes permanently marked by long exposure to the Spellscar
Desert. The Spellscar drifter gains [spell resistance](ref/rule/spell-resistance) equal to 10 + his
character level. The Spellscar drifter can drop this [spell resistance](ref/rule/spell-resistance)
for 1 round as a standard action, or he can spend 1 grit point to drop it as a swift action. This
ability replaces demanding challenge.

## Infamous Deeds (Ex) {#infamous-deeds}

At 17th level, a Spellscar drifter can select two additional gunslinger deeds which he can use with
his Amateur Gunslinger feat. The Spellscar drifter can choose one deed from the list of deeds
available to 7th-level gunslingers and one from the list available to 11th-level gunslingers. This
ability replaces master tactician.

## Tough as Nails (Ex) {#tough-as-nails}

At 20th level, a Spellscar drifter is able to select three additional deeds for use with his Amateur
Gunslinger feat—two from the list of deeds available to 15th-level gunslingers, and one from the
list available to 19th-level gunslingers.

In addition, if the Spellscar drifter confirms a critical hit on an attack made with a firearm, the
target is [stunned](ref/misc/stunned) for 1d4 rounds. A successful Will saving throw (DC = 10 + the
Spellscar drifter's base attack bonus) reduces this effect to [staggered](ref/misc/staggered)
instead of stunned. This ability replaces supreme charge.
