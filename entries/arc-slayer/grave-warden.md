+++
id = "ref/arc-slayer/grave-warden"
kind = "archetype"
title = "Grave Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Slayer%20Grave%20Warden"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "grave_warden", path = "json/archetypes_slayer.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/slayer" },
]
[[sources]]
publication = "advanced-class-guide"
page = "120"

[fields]
kind = "archetype"
features = [
  { anchor = "holy-water-sprinkler", level = 2 },
  { anchor = "death-ward", level = 7 },
  { anchor = "dustbringer", level = 10 },
]
trades = [
  { replaces = "Slayer talent gained at 2nd level", feature = "slayer-talents", levels = [2], by = ["holy-water-sprinkler"] },
  { replaces = "Stalker", feature = "stalker", by = ["death-ward"] },
  { replaces = "Advanced slayer talent gained at 10th level", feature = "advanced-talents", levels = [10], by = ["dustbringer"] },
]
+++

While paladins and inquisitors use their connection with the divine to fight undead hordes and other
horrors of the night, a grave warden relies on knowledge, skill with weapons, and tenacity to put an
end to these night-born terrors.

## Holy Water Sprinkler (Ex) {#holy-water-sprinkler}

At 2nd level, a grave warden can draw a flask of [holy water](ref/eq-weapon/holy-water) as if it
were a weapon (and can thus the [Quick Draw](ref/feat/quick-draw) feat to draw flasks of holy
water). As a swift action, he can open a flask of holy water and pour it onto a held or adjacent
melee weapon. If the weapon successfully hits an undead creature before the end of the grave
warden's next turn, the undead takes damage as if it took a direct hit from the holy water, in
addition to the damage from the weapon, if any. This ability replaces the slayer talent gained at
2nd level.

## Death Ward (Sp) {#death-ward}

At 7th level, a grave warden learns to perform a short ritual that grants the benefits of
_[death ward](ref/spell/death-ward)_, using his slayer level as his caster level. Performing this
ritual takes 1 minute and uses 4 flasks of holy water. The grave warden can protect only himself
with this ability. This ability replaces stalker.

## Dustbringer (Ex) {#dustbringer}

At 10th level, a grave warden can slay a studied undead opponent. This functions as the
[assassinate](ref/slayertalent/assassinate) slayer talent, except it requires a successful Will
saving throw instead of a successful Fortitude save, affects only undead, and destroys the target
instead of killing it. If the target succeeds at its saving throw, it becomes immune to that grave
warden's dustbringer ability for 24 hours. This ability replaces the advanced slayer talent gained
at 10th level.

## Slayer Talents {#slayer-talents}

The following slayer talents (and rogue talents) complement the deliverer archetype: fast stealth,
finesse rogue, surprise attack, swift poison, terrain mastery, trap spotter, and unwitting ally.
(Those with asterisks \[\*\] are detailed in the slayer class, starting on page 53.)

## Advanced Slayer Talents {#advanced-slayer-talents}

The following advanced slayer talents (also available to rogues) complement the grave warden
archetype: hunter's surprise, and slayer camouflage.
