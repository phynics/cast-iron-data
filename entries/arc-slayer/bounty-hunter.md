+++
id = "ref/arc-slayer/bounty-hunter"
kind = "archetype"
title = "Bounty Hunter"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Bounty%20Hunter"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bounty_hunter", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "advanced-class-guide"
page = "118"

[fields]
kind = "archetype"
features = [
  { anchor = "dirty-trick", level = 2 },
  { anchor = "submission-hold", level = 6 },
  { anchor = "incapacitate", level = 10 },
]
trades = [
  { replaces = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { replaces = "Slayer talent gained at 2nd level", feature = "slayer-talents", levels = [2], by = ["dirty-trick"] },
  { replaces = "Slayer talent gained at 6th level", feature = "slayer-talents", levels = [6], by = ["submission-hold"] },
  { replaces = "The advanced slayer talent gained at 10th level", feature = "advanced-talents", levels = [10], by = ["incapacitate"] },
]
+++

Whether tasked with bringing in wanted criminals or paid to drag debtors back to their loan sharks,
bounty hunters are valued for their ability to capture targets alive.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

A bounty hunter is proficient with all simple and martial weapons plus the
[aklys](ref/eq-weapon/aklys), [bolas](ref/eq-weapon/bolas), [dan bong](ref/eq-weapon/dan-bong),
[lasso](ref/eq-weapon/lasso), and [net](ref/eq-weapon/net). Bounty hunters are proficient with light
armor, light shields, and bucklers, but not heavy shields or tower shields. This ability replaces
the slayer's weapon and armor proficiencies.

## Dirty Trick (Ex) {#dirty-trick}

At 2nd level, anytime a bounty hunter is able to deal sneak attack damage to a studied target, he
can instead attempt to hamper the target. The bounty hunter must declare that he's using this
ability before the attack roll is made. If the attack hits, it deals damage normally, but instead of
rolling sneak attack damage, the bounty hunter can attempt a [dirty trick](ref/rule/dirty-trick)
combat maneuver against the studied target as a free action, adding 1 to the combat maneuver check
for each die of the bounty hunter's sneak attack damage. This combat maneuver does not provoke
attacks of opportunity. This ability replaces the slayer talent gained at 2nd level.

## Submission Hold (Ex) {#submission-hold}

At 6th level, when a bounty hunter attempts a [grapple](ref/rule/grapple) combat maneuver check to
deal damage, he can choose to add his sneak attack damage to the grapple damage for that attack. He
takes a -5 penalty on the combat maneuver check if he does this. This sneak attack damage is
nonlethal damage, unless the bounty hunter is able to deal normal damage with a grapple and chooses
to do so. This ability replaces the slayer talent gained at 6th level.

## Incapacitate (Ex) {#incapacitate}

At 10th level, a bounty hunter can incapacitate a studied target. This functions like the
[assassinate](ref/slayertalent/assassinate) slayer talent, except instead of killing the target, the
bounty hunter's successful attack knocks the target unconscious for 1d6 rounds unless it succeeds at
its saving throw. If the target does succeed at its saving throw, it still takes the sneak attack
damage as normal, but the damage is nonlethal, and the target is immune to that slayer's
incapacitate ability for 24 hours. This ability replaces the advanced slayer talent gained at 10th
level.

## Slayer Talents {#slayer-talents}

The following slayer talents (and rogue talents) complement the bounty hunter archetype: camouflage,
fast stealth, hard to fool, slowing strike, snap shot, surprise attack, and terrain mastery. (Those
with asterisks \[\*\] are detailed in the slayer class, starting on page 53.)

## Advanced Slayer Talents {#advanced-slayer-talents}

The following advanced slayer talents (and advanced rogue talents) complement the bounty hunter
archetype: hunter's surprise, knock-out blow, master of disguise, and woodland stride.
