+++
id = "ref/arc-gunslinger/bolt-ace"
kind = "archetype"
title = "Bolt Ace"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Bolt%20Ace"
source_ids = ["advanced-class-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bolt_ace", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "advanced-class-guide"
page = "94"

[fields]
kind = "archetype"
features = [
  { anchor = "crossbow-maven", level = 1 },
  { anchor = "grit" },
  { anchor = "deeds" },
  { anchor = "sharp-shoot", level = 1 },
  { anchor = "vigilant-loading", level = 1 },
  { anchor = "shooter-s-resolve", level = 3 },
  { anchor = "distracting-shot", level = 7 },
  { anchor = "vigilant-shooter", level = 11 },
  { anchor = "inexplicable-reload", level = 11 },
  { anchor = "pinning-shot", level = 15 },
  { anchor = "crossbow-training", level = 5 },
]
trades = [
  { replaces = "Gunsmith", feature = "gunsmith", by = ["crossbow-maven"] },
  { replaces = "Deadeye", feature = "deeds", power = "deadeye", by = ["sharp-shoot"] },
  { replaces = "Quick clear", feature = "deeds", power = "quick clear", by = ["vigilant-loading"] },
  { replaces = "Utility shot", feature = "deeds", power = "utility shot", by = ["shooter-s-resolve"] },
  { replaces = "Startling shot", feature = "deeds", power = "startling shot", by = ["distracting-shot"] },
  { replaces = "Expert loading", feature = "deeds", power = "expert loading", by = ["vigilant-shooter"] },
  { replaces = "Lightning reload", feature = "deeds", power = "lightning reload", by = ["inexplicable-reload"] },
  { replaces = "Menacing shot", feature = "deeds", power = "menacing shot", by = ["pinning-shot"] },
  { replaces = "Gun training", feature = "gun-training", by = ["crossbow-training"] },
  { alters = "Weapon proficiencies", feature = "weapon-and-armor-proficiencies", power = "weapons", by = ["crossbow-maven"] },
  { alters = "Grit", feature = "grit", by = ["grit"] },
]
+++

While gunslingers are full of sound and fury, there is a class of gunslingers that never soil their
hands with powder or feel the sting of gun smoke. They commit their deeds in a more hushed manner,
but with just as much flair.

## Crossbow Maven {#crossbow-maven}

A bolt ace is proficient with all crossbows instead of all firearms and begins play with a
masterwork crossbow of her choice. This ability alters the gunslinger's weapon proficiencies and
replaces gunsmith.

## Grit (Ex) {#grit}

A bolt ace regains grit when she scores a critical hit or deals a killing blow with any kind of
crossbow. This ability modifies the grit class feature.

## Deeds {#deeds}

A bolt ace can perform the following deeds with a crossbow instead of a firearm:
[gunslinger initiative](ref/deed/gunslinger-initiative), [pistol-whip](ref/deed/pistol-whip),
[dead shot](ref/deed/dead-shot), targeting, [bleeding wound](ref/deed/bleeding-wound),
[death's shot](ref/deed/deaths-shot), and [stunning shot](ref/deed/stunning-shot). The bolt ace
swaps the following deeds.

## Sharp Shoot (Ex) {#sharp-shoot}

At 1st level, a bolt ace can resolve an attack against touch AC instead of normal AC when firing a
crossbow at a target within its first range increment. Performing this deed costs 1 grit point. This
deed's cost cannot be reduced by any ability or effect that reduces the amount of grit points a deed
costs (such as [Signature Deed](ref/feat/signature-deed)). This deed replaces deadeye.

## Vigilant Loading (Ex) {#vigilant-loading}

At 1st level, as long as a bolt ace has at least 1 grit point, she does not provoke attacks of
opportunity when loading a crossbow. This deed replaces quick clear.

## Shooter's Resolve (Ex) {#shooter-s-resolve}

At 3rd level, a bolt ace can spend 1 grit point when making a crossbow attack as a standard action
and ignore the effects of [concealment](ref/rule/concealment) (though not total concealment) and
[cover](ref/rule/cover) (other than total cover) against that shot. This deed replaces utility shot.

## Distracting Shot (Ex) {#distracting-shot}

At 7th level, a bolt ace can spend 1 grit point and choose to miss a target that she could normally
attack within her range with a crossbow attack. When she does, the target loses its Dexterity bonus
to AC (if any) for 1 round. This deed replaces startling shot.

## Vigilant Shooter (Ex) {#vigilant-shooter}

At 11th level, as long as a bolt ace spends 1 grit point when she does so, she does not provoke
attacks of opportunity when firing a crossbow. This deed replaces expert loading.

## Inexplicable Reload (Ex) {#inexplicable-reload}

At 11th level, loading a crossbow becomes unthinking and automatic for a bolt ace. As long as she
has at least 1 grit point, she always starts each round of combat (even a surprise round) with her
crossbow loaded. Also the amount of time needed to reload a crossbow decreases by one step: a
standard action becomes a move action, a move action becomes a swift action, a swift action becomes
a free action, and a free action becomes not an action. This deed replaces lightning reload.

## Pinning Shot (Ex) {#pinning-shot}

At 15th level, the bolt ace can spend 1 grit point while shooting a crossbow and attempt to pin down
its target with the bolt. If the crossbow attack hits, it pins the target to a nearby object, to a
wall, or to the ground, [entangling](ref/rule/entangled) and [staggering](ref/misc/staggered) the
target. While pinned by the bolt, the target cannot move out of its space until it takes a standard
action to free itself from the pinning bolt, except by means of teleportation. This deed replaces
menacing shot.

## Crossbow Training (Ex) {#crossbow-training}

Starting at 5th level, a bolt ace can select one specific type of crossbow, such as
[hand crossbow](ref/eq-weapon/hand-crossbow) or [heavy crossbow](ref/eq-weapon/heavy-crossbow). She
gains a bonus on damage rolls equal to her Dexterity modifier with that crossbow. Furthermore, when
she scores a critical hit with that type of crossbow, her critical modifier increases by 1 (a ×2
becomes a ×3, for example).

Every 4 levels thereafter, she can pick a different type of crossbow, gaining the bonus damage and
increased critical multiplier with that type of crossbow as well. This ability replaces gun
training.
