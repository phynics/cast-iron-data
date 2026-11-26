+++
id = "ref/arc-vigilante/hangman"
kind = "archetype"
title = "Hangman"
aon = "ArchetypeDisplay.aspx?FixedName=Vigilante%20Hangman"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "hangman", path = "json/archetypes_vigilante.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/vigilante" },
]
[[sources]]
publication = "horror-adventures"
page = "70"

[fields]
kind = "archetype"
features = [
  { anchor = "vigilante-specialization", level = 1 },
  { anchor = "hangman-s-noose", level = 2 },
  { anchor = "bound-to-truth", level = 3 },
  { anchor = "twisted-rope", level = 4 },
  { anchor = "chokehold", level = 5 },
  { anchor = "tighten-the-noose", level = 11 },
  { anchor = "suffocation", level = 17 },
]
trades = [
  { replaces = "2nd-level vigilante talent", feature = "vigilante-talent", levels = [2], by = ["hangman-s-noose"] },
  { replaces = "Unshakable", feature = "unshakable", by = ["bound-to-truth"] },
  { replaces = "4th-level vigilante talent", feature = "vigilante-talent", levels = [4], by = ["twisted-rope"] },
  { replaces = "Startling appearance", feature = "startling-appearance", by = ["chokehold"] },
  { replaces = "Frightening appearance", feature = "frightening-appearance", by = ["tighten-the-noose"] },
  { replaces = "Stunning appearance", feature = "stunning-appearance", by = ["suffocation"] },
  { alters = "Weapon and armor proficiencies", feature = "weapon-and-armor-proficiencies" },
  { alters = "Vigilante specialization", feature = "vigilante-specialization", by = ["vigilante-specialization"] },
]
+++

Wherever the guilty walk free, the hangman brings judgment.

## Weapon and Armor Proficiencies {#weapon-and-armor-proficiencies}

A hangman is proficient with [nets](ref/eq-weapon/net) and [whips](ref/eq-weapon/whip), but not
shields.

This alters the vigilante's weapon and armor proficiencies.

## Vigilante Specialization {#vigilante-specialization}

A hangman must choose the stalker specialization.

This alters vigilante specialization.

## Hangman's Noose (Ex) {#hangman-s-noose}

At 2nd level, a hangman can wield a rope noose as a net or whip, and also can use it to
[grapple](ref/rule/grapple), gaining the benefits of [Improved Grapple](ref/feat/improved-grapple)
with it. He takes no penalty on combat maneuver checks with the noose for having the noose in his
hand, but he still doesn't add any bonuses he might have with a net or whip (such as weapon
enhancement bonuses or benefits from [Weapon Focus](ref/feat/weapon-focus)) on the check. He can
spend 1 minute to weave a magical or masterwork net or whip into a noose, thereafter gaining these
benefits with it.

This ability replaces the 2nd-level vigilante talent.

## Bound to Truth (Ex, Sp) {#bound-to-truth}

At 3rd level, a hangman adds [half](ref/misc/fractions-and-rounding) his vigilante level to his
Sense Motive checks to notice lies told by a creature entangled or grappled by his noose, by feeling
the creature's throat clench or changes in its breathing. In addition, he can prevent a creature
entangled or grappled in his noose from lying by tightening the noose, as per a single-target
_[zone of truth](ref/spell/zone-of-truth)_ (the caster level equals his vigilante level; the save DC
is Charisma-based). He can use the latter ability a number of rounds per day equal to half his
vigilante level. These rounds don't need to be consecutive.

This ability replaces unshakable.

## Twisted Rope (Su) {#twisted-rope}

At 4th level, a hangman can spend 1 hour preparing his noose, granting it temporary hit points equal
to his vigilante level, giving it a [hardness](ref/rule/breaking-things) equal to 1/2 his vigilante
level plus double the weapon's enhancement bonus (or its current [hardness](ref/umr/hardness),
whichever is better), and changing its break DC to 23 + 1/2 his vigilante level (or its current
break DC, whichever is better). These benefits last for 8 hours, but end immediately if the hangman
prepares another noose. This ability replaces the 4th-level vigilante talent.

## Chokehold {#chokehold}

At 5th level, a hangman gains [Chokehold](ref/feat/chokehold) as a bonus feat.

This ability replaces startling appearance.

## Tighten the Noose (Ex) {#tighten-the-noose}

At 11th level, while a hangman is grappling a target with his noose, as a swift action he can deal
increased hidden strike damage to the target.

This ability replaces frightening appearance.

## Suffocation (Ex) {#suffocation}

At 17th level, the first time the hangman succeeds at a check to maintain a grapple (on his next
turn after establishing the grapple), in place of the other options, he can suffocate the target and
cause her to fall [unconscious](ref/misc/unconscious). A successful Fortitude save (DC = 15 + the
hangman's Strength bonus) negates the suffocation. On subsequent rounds, the hangman can maintain
the grapple to suffocate the target again. On the next failed save, the target drops to -1 hit
points and starts [dying](ref/misc/dying). On the third failed save, she dies. Even if the hangman
has the ability to maintain a grapple with less than a standard action, he can attempt to maintain a
grapple to suffocate only once per round.

This ability replaces stunning appearance.
