+++
id = "ref/arc-ranger/hooded-champion"
kind = "archetype"
title = "Hooded Champion"
aon = "ArchetypeDisplay.aspx?FixedName=Ranger%20Hooded%20Champion"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hooded_champion", path = "json/archetypes_ranger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/ranger" },
]
[[sources]]
publication = "advanced-class-guide"
page = "108"

[fields]
kind = "archetype"
features = [
  { anchor = "panache", level = 1 },
  { anchor = "deeds", level = 1 },
  { anchor = "dead-aim", level = 1 },
  { anchor = "hooded-champion-s-initiative", level = 3 },
  { anchor = "combat-style", level = 2 },
]
trades = [
  { replaces = "Favored enemy at 1st level", feature = "favored-enemy", levels = [1], by = ["panache"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["combat-style"] },
  { replaces = "endurance", feature = "endurance", by = ["combat-style"] },
  { replaces = "evasion", feature = "evasion", by = ["combat-style"] },
  { replaces = "improved evasion", feature = "improved-evasion", by = ["combat-style"] },
]
+++

The hooded champion lives on the periphery of civilized lands, and is often at odds with the forces
of law and order. He is frequently a hero of oppressed peoples, lurking in the woods near their
homes and trying to right the injustices inflicted upon them by the wealthy and powerful.

## Panache (Ex) {#panache}

At 1st level, the hooded champion gains the [swashbuckler's](ref/class/swashbuckler) panache class
feature. He regains panache through critical hits and killing blows when using a bow of any kind,
rather than when using a light or one-handed piercing melee weapon. If the hooded champion has this
ability and the panache ability from another class or archetype, the panache points from the two
sources do not stack, but the hooded champion regains panache in any way either class feature allows
him to. For example, a character with a Charisma score of 16 who has both the hooded champion's and
the swashbuckler's panache has a base of 3 panache points, and regains panache from critical hits
and killing blows from both bows and light or one-handed piercing melee weapons. This ability
replaces favored enemy at 1st level.

## Deeds {#deeds}

At 1st level, the hooded champion gains the swashbuckler's [derring-do](ref/swashdeed/derring-do)
and [dodging panache](ref/swashdeed/dodging-panache) deeds, as well as the following deeds. For all
deeds, treat the hooded champion's ranger level as his swashbuckler level.

## Dead Aim (Ex) {#dead-aim}

At 1st level, the hooded champion's can spend 1 panache point when making a single ranged attack
(not a full attack) with a bow to make a ranged touch attack instead. The target must be in the
bow's first range increment.

At 3rd level, the hooded champion gains the swashbuckler's [kip-up](ref/swashdeed/kip-up) deed as
well as the following deed.

## Hooded Champion's Initiative (Ex) {#hooded-champion-s-initiative}

At 3rd level, while the hooded champion has at least 1 panache point, he gains a +2 bonus on
initiative checks. In addition, if he has the [Quick Draw](ref/feat/quick-draw) feat, his hands are
free and unrestrained, and his weapon isn't hidden, he can draw a single bow as part of the
initiative check.

## Combat Style {#combat-style}

At 2nd level, the hooded champion must select the archery [combat style](ref/ability/combat-styles).
At 9th level, the hooded champion gains the
[swashbuckler's grace](ref/swashdeed/swashbucklers-grace) and [evasive](ref/swashdeed/evasive)
deeds. At 16th level, the hooded champion gains the
[swashbuckler's edge](ref/swashdeed/swashbucklers-edge) and [cheat death](ref/swashdeed/cheat-death)
deeds. This ability replaces wild empathy, endurance, evasion, and improved evasion.
