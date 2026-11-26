+++
id = "ref/arc-slayer/spawn-slayer"
kind = "archetype"
title = "Spawn Slayer"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Spawn%20Slayer"
source_ids = ["blood-of-the-ancients"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spawn_slayer", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "blood-of-the-ancients"
page = "24"

[fields]
kind = "archetype"
features = [
  { anchor = "studied-spawn" },
  { anchor = "gain-leverage", level = 7 },
  { anchor = "force-vulnerability", level = 20 },
]
trades = [
  { replaces = "The ability to study an opponent as a swift action at 7th level", feature = "studied-target", levels = [7], by = ["studied-spawn"] },
  { replaces = "Stalker", feature = "stalker", by = ["gain-leverage"] },
  { replaces = "Master slayer", feature = "master-slayer", by = ["force-vulnerability"] },
  { alters = "Studied target", feature = "studied-target", by = ["studied-spawn"] },
]
+++

Generations of Ninshaburian warriors fought the Spawn of Rovagug, holding the line against
impossible odds. Some of their ancient techniques persist to this day.

## Studied Spawn (Ex) {#studied-spawn}

A spawn slayer specializes in fighting against larger, single targets. At 5th, 10th, 15th, and 20th
levels, the bonuses on weapon attack rolls, damage rolls, and skill checks against a studied target
increase by 1, as do the DCs of slayer abilities against a studied target. He can also ignore size
restrictions against a studied target when attempting combat maneuvers against larger foes. At 5th
level, if the target is Large or larger, these bonuses increase by an additional 1. At 10th level,
if the target is Huge or larger, the bonuses increase by an additional 2. At 15th level, if the
target is Gargantuan or larger, the bonuses increase by an additional 3. At 20th level, if the
target is Colossal in size, the bonuses increase by an additional 4. A spawn slayer cannot maintain
these bonuses against more than one target at a time. He does not gain the ability to study an
opponent as a swift action at 7th level.

This alters studied target.

## Gain Leverage (Ex) {#gain-leverage}

At 7th level, a spawn slayer learns techniques to counteract a foe's size advantage. When performing
a combat maneuver against a studied target of Large or larger size, the spawn slayer gains a bonus
on the check equal to the creature's size modifier to CMB (Large +1, Huge +2, Gargantuan +4, and
Colossal +8). The spawn slayer adds this same bonus to his CMD when defending against combat
maneuvers from a Large or larger studied target.

This replaces stalker.

## Force Vulnerability (Ex) {#force-vulnerability}

At 20th level, a spawn slayer can create an opening in even an invulnerable foe's defenses. As a
standard action, he can make a single attack against a studied target at his full attack bonus. If
the attack hits, the damage bypasses any [damage reduction](ref/rule/damage-reduction) and the
target must succeed at a Will saving throw (DC 10 + half the slayer's level + the slayer's
Intelligence modifier) or lose one of its defensive abilities for 2d6 rounds. The slayer can choose
which defensive ability is lost from the following options: a single immunity, all resistances,
regeneration, or [spell resistance](ref/rule/spell-resistance). Whether or not the target fails this
save, it cannot be targeted by force vulnerability again (by you or another slayer) for 24 hours.

This replaces master slayer.
