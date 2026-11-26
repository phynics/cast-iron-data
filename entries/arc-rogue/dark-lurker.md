+++
id = "ref/arc-rogue/dark-lurker"
kind = "archetype"
title = "Dark Lurker"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Dark%20Lurker"
source_ids = ["heroes-of-the-streets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dark_lurker", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "heroes-of-the-streets"
page = "26"

[fields]
kind = "archetype"
features = [
  { anchor = "blades-from-the-shadows", level = 2 },
  { anchor = "blind-fight", level = 2 },
  { anchor = "improved-blind-fight", level = 8 },
  { anchor = "greater-blind-fight", level = 14 },
  { anchor = "instinctual-sense", level = 20 },
  { anchor = "eerie-disappearance" },
  { anchor = "false-attacker" },
  { anchor = "pierce-the-darkness" },
]
trades = [
  { replaces = "Evasion", feature = "evasion", by = ["blades-from-the-shadows"] },
  { replaces = "Rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["blind-fight"] },
  { replaces = "Rogue talent gained at 8th level", feature = "rogue-talents", levels = [8], by = ["improved-blind-fight"] },
  { replaces = "Rogue talent gained at 14th level", feature = "rogue-talents", levels = [14], by = ["greater-blind-fight"] },
  { replaces = "Rogue talent gained at 20th level", feature = "rogue-talents", levels = [20], by = ["instinctual-sense"] },
]
+++

Dark lurkers use darkness as an ally. They are widely feared in many major metropolises, spoken of
as "living shadows" by guards of Magnimar who patrol under the Irespan and called "the hungry night"
by citizens of Absalom who mistake them for fetchling assassins.

## Blades from the Shadows (Ex) {#blades-from-the-shadows}

At 2nd level, a dark lurker gains [shadow strike](ref/feat/shadow-strike) as a bonus rogue talent.
(A character using the unchained rogue class from _Pathfinder RPG Pathfinder Unchained_ instead
gains the ability to make attacks of opportunity against foes with [cover](ref/rule/cover), though
not foes with improved cover or total cover). At 6th level, the dark lurker can deal precision
damage to targets with [total concealment](ref/rule/concealment) (though any miss chance applies
normally, and may prevent an attack from hitting in the first place).

This ability replaces [evasion](ref/ability/evasion); the dark lurker can take evasion as a rogue
talent.

## Blind-Fight (Ex) {#blind-fight}

At 2nd level, a dark lurker gains [Blind-Fight](ref/feat/blind-fight) as a bonus feat. This ability
replaces the rogue talent gained at 2nd level.

## Improved Blind-Fight (Ex) {#improved-blind-fight}

At 8th level, a dark lurker gains [Improved Blind-Fight](ref/feat/improved-blind-fight) as a bonus
feat. This ability replaces the rogue talent gained at 8th level.

## Greater Blind-Fight (Ex) {#greater-blind-fight}

At 14th level, a dark lurker gains [Greater Blind-Fight](ref/feat/greater-blind-fight) as a bonus
feat. This ability replaces the rogue talent gained at 14th level.

## Instinctual Sense (Ex) {#instinctual-sense}

At 20th level, a dark lurker gains [blindsight](ref/umr/blindsight) with a range of 30 feet. This
ability replaces the rogue talent gained at 20th level.

## Rogue Talents {#rogue-talents}

The following rogue talents complement the dark lurker archetype: befuddling strike, fast getaway,
fast stealth, [opportunist](ref/talent/opportunist), sniper's eye, and surprise attack.

## Rogue Talents {#instinctual-sense-rogue-talents}

The new talents below especially suit the dark lurker, but can also be taken by any rogue that meets
their prerequisites (including characters using the unchained rogue class from _Pathfinder
Unchained_).

## Eerie Disappearance (Ex) {#eerie-disappearance}

As a full-round action, the rogue can move up to her speed. If she successfully reaches a location
that offers her cover or concealment, any creature observing her must attempt a Perception check
opposed by the rogue's Stealth check. On a failed check, the observer loses track of the rogue and
fails to note where she moved to. The rogue does not take a penalty on this Stealth check for moving
up to her speed. At the end of her movement, the rogue can attempt an Intimidate check to demoralize
all foes within 60 feet who were aware of her at any point during her movement and are unaware of
her current location. She rolls the Intimidate check only once and compares her result to the DC for
each opponent. The rogue must be at least 6th level to select this talent.

## False Attacker (Ex) {#false-attacker}

Whenever the rogue strikes a foe from hiding, she can attempt a Bluff check as an immediate action
(opposed by the target's Sense Motive or Perception check, whichever has a higher bonus) before
rolling damage to convince the foe that another creature was the attacker. This Bluff check applies
the normal modifiers for convincing a creature of a falsehood, but can be accomplished with just
physical trickery (a shared language is not required). If the Bluff is successful, and the rogue
maintains concealment or cover, the rogue's stealth does not end.

## Pierce the Darkness (Ex) {#pierce-the-darkness}

The rogue can extend her senses of hearing and smell in darkness or when blinded. She gains
blindsense out to a range of 5 feet, but only against creatures concealed by darkness or her own
blindness. She still suffers the normal miss chance for attacking creatures with concealment.
