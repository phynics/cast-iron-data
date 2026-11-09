+++
id = "ref/arc-cleric/undead-lord"
kind = "archetype"
title = "Undead Lord"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Undead%20Lord"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "undead_lord", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "ultimate-magic"
page = "32"

[fields]
kind = "archetype"
replaces = ["Domains"]
+++

An undead lord is a cleric focused on using necromancy to control undead. Her flock is the walking
dead and her choir the keening spirits of the damned. This unliving congregation is the
manifestation of her unceasing love affair with death.

**Prerequisites:** Deity's portfolio must include the Death domain, or a similar domain that
promotes undeath.

**Death Magic**

**Info:** An undead lord must select the Death domain (and the Undead subdomain, if available in the
campaign). She does not gain a second domain. In all other respects, this works like the standard
cleric's domain ability.

**Replaces:** Domains

**Corpse Companion (Su)**

**Ability:** With a ritual requiring 8 hours, an undead lord can animate a single
[skeleton](ref/template/skeleton) or [zombie](ref/template/zombie) whose Hit Dice do not exceed her
cleric level. This corpse companion automatically follows her commands and does not need to be
controlled by her. She cannot have more than one corpse companion at a time. It does not count
against the number of Hit Dice of undead controlled by other methods. She can use this ability to
create a variant skeleton such as a bloody or burning skeleton, but its Hit Dice cannot exceed
[half](ref/misc/fractions-and-rounding) her cleric level. She can dismiss her companion as a
**standard action**, which destroys it.

**Bonus Feats**

**At 1st Level:** All undead lords gain [Command Undead](ref/feat/command-undead) as a bonus feat.

**At 10th Level:** She may select one of the following as a bonus feat:
[Channel Smite](ref/feat/channel-smite), [Extra Channel](ref/feat/extra-channel),
[Improved Channel](ref/feat/improved-channel), [Quick Channel](ref/feat/quick-channel),
[Skeleton Summoner](ref/feat/skeleton-summoner), [Undead Master](ref/feat/undead-master).

**Unlife Healer (Su)**

**At 16th Level:** These effects automatically heal the maximum possible damage for the effect + the
extra 50%. This does not stack with abilities or feats such as
[Empower Spell](ref/feat/empower-spell) or [Maximize Spell](ref/feat/maximize-spell).

**At 8th Level:** The undead lord's spells, [spell-like abilities](ref/umr/spell-like-abilities),
and supernatural abilities used to heal undead heal an extra 50% damage.
