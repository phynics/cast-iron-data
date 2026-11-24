+++
id = "ref/arc-cleric/merciful-healer"
kind = "archetype"
title = "Merciful Healer"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Merciful%20Healer"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "merciful_healer", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "ultimate-combat"
page = "41"

[fields]
kind = "archetype"
features = [
  { anchor = "willing-healer" },
  { anchor = "channel-energy" },
  { anchor = "combat-medic" },
  { anchor = "merciful-healing", level = 3 },
  { anchor = "true-healer", level = 8 },
]
trades = [
  { replaces = "Channel energy", feature = "channel-energy", by = ["channel-energy"] },
]
+++

The merciful healer is a master of battlefield revivification, sustaining and restoring allies to
keep them in the fight.

## Willing Healer {#willing-healer}

A merciful healer must choose the [Healing](ref/domain/healing) domain. She does not gain a second
domain. If the cleric worships a deity, that deity must be one that grants the Healing domain. A
merciful healer must channel positive energy.

## Channel Energy (Su) {#channel-energy}

As the cleric ability, save that a merciful healer must channel positive energy, and when she does,
she cannot choose to target undead. This ability is otherwise identical to the cleric ability of the
same name.

## Combat Medic (Ex) {#combat-medic}

A merciful healer does not provoke attacks of opportunity when using the Heal skill to stabilize
another creature or casting healing spells.

## Merciful Healing (Su) {#merciful-healing}

At 3rd level, a merciful healer can channel positive energy to relieve one or more harmful
conditions. The merciful healer chooses one of the following harmful conditions at 3rd level:
[fatigued](ref/misc/fatigued), [shaken](ref/misc/shaken), or [sickened](ref/misc/sickened). When the
merciful healer channels energy she can remove the chosen condition from one living creature that
she heals within her channel energy burst. At 6th level, she can choose another condition. It can be
one of those she didn't choose at 3rd level, or one of the following conditions:
[dazed](ref/misc/dazed), diseased, or [staggered](ref/misc/staggered). She can remove the selected
condition or the one she chose at 3rd level from up to two creatures within her channel energy
burst. She gains another condition at 9th level, and can choose an above condition or one of the
following conditions: cursed, [exhausted](ref/misc/exhausted), [frightened](ref/misc/frightened),
[nauseated](ref/misc/nauseated), or poisoned. She can remove that condition, or a condition she
previously chose, from one or two creatures within the burst. Finally, at 12th level, she can choose
a lower-level condition or one of the following conditions: [blinded](ref/misc/blinded),
[deafened](ref/misc/deafened), [paralyzed](ref/rule/paralyzed), or [stunned](ref/misc/stunned). She
can remove that condition or one she previously chose from one, two, or three creatures within her
channel energy burst. Feats and effects that affect a paladin's mercy also affect this ability.

## True Healer (Su) {#true-healer}

At 8th level, when a merciful healer uses channel energy, she can choose to apply the benefits of
merciful healing or to reroll any 1s when determining how much damage she heals with channel energy.
She must choose which benefit to take before she rolls to see how much damage she heals.
