+++
id = "ref/arc-inquisitor/preacher"
kind = "archetype"
title = "Preacher"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Preacher"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "preacher", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-magic"
page = "46"

[fields]
kind = "archetype"
features = [
  { anchor = "determination", level = 3 },
]
trades = [
  { replaces = "Solo tactics", feature = "solo-tactics", by = ["determination"] },
  { alters = "Teamwork feats", feature = "teamwork-feat", by = ["determination"] },
]
+++

Some inquisitors wander the land to spread the true word of their faith. Often they come into
conflict with those hostile to their teachings or to the preacher's need to help those who cannot
help themselves. The leaders of evil or aggressive religions send these preachers into new
territories to win converts and hopefully allies. Often, they start uprisings against powers hostile
to their religion, or defend a group of honest believers from the depredations of the unfaithful.

## Determination (Ex) {#determination}

At 3rd level, the preacher is a person of few words on the battlefield, but those words hold great
power and authority. Once per day, the inquisitor can use this ability to create one of the
following effects. Each is a free action to use unless stated otherwise.

### Aggression {#aggression}

The preacher may reroll an attack roll that she just made before the results of the roll are
revealed. She must take the result of the reroll, even if it's worse than the original roll.

### Defense {#defense}

When the inquisitor would be hit by a melee or ranged attack, as an immediate action she may add a
+4 insight bonus to her Armor Class against that attack, and if this makes the inquisitor's AC
higher than the opponent's attack roll, the attack misses.

### Warning {#warning}

When a preacher's ally within line of sight would be hit by a melee or ranged attack, she may call
out a warning to that ally, and the attacker must reroll the attack and use the results of the
second roll. The ally must be able to hear the preacher and must not be
[helpless](ref/misc/helpless) for this ability to have any effect.

Whenever the preacher could select a bonus teamwork feat (at 3rd, 6th, 9th, 12th, 15th, and 18th
level), she can instead choose to increase her number of uses per day of this ability by one. This
ability replaces solo tactics.
