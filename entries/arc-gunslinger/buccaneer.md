+++
id = "ref/arc-gunslinger/buccaneer"
kind = "archetype"
title = "Buccaneer"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Buccaneer"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "buccaneer", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "advanced-race-guide"
page = "73"

[fields]
kind = "archetype"
features = [
  { anchor = "deeds" },
  { anchor = "seadog-s-gait", level = 1 },
  { anchor = "pirate-s-jargon", level = 3 },
  { anchor = "rope-swing", level = 7 },
  { anchor = "captain-s-curse", level = 11 },
  { anchor = "grit" },
  { anchor = "liquid-courage", level = 2 },
  { anchor = "bonus-feat" },
  { anchor = "exotic-pet", level = 5 },
  { anchor = "sword-and-pistol", level = 9 },
  { anchor = "gun-training" },
  { anchor = "raider-s-riposte", level = 17 },
]
trades = [
  { replaces = "Quick clear deed", feature = "deeds", power = "quick clear", by = ["seadog-s-gait"] },
  { replaces = "Pistol whip deed", feature = "deeds", power = "pistol whip", by = ["pirate-s-jargon"] },
  { replaces = "Dead shot deed", feature = "deeds", power = "dead shot", by = ["rope-swing"] },
  { replaces = "Lightning reload deed", feature = "deeds", power = "lightning reload", by = ["captain-s-curse"] },
  { replaces = "Nimble", feature = "nimble", by = ["liquid-courage"] },
  { replaces = "Gun training 1", feature = "gun-training", levels = [5], by = ["exotic-pet"] },
  { replaces = "Gun training 2", feature = "gun-training", levels = [9], by = ["sword-and-pistol"] },
  { replaces = "Gun training 4", feature = "gun-training", levels = [17], by = ["raider-s-riposte"] },
  { alters = "Grit", feature = "grit", by = ["grit"] },
]
+++

Freebooters who cling to the convoluted codes that rule independent ships, the buccaneer is a
gunslinger of the high seas. Their exploits are fueled by the thrill of danger and often by the
temporary courage provided by grog. A buccaneer has the following class features.

## Deeds {#deeds}

A buccaneer swaps four of the normal gunslinger deeds for the following deeds.

## Seadog's Gait (Ex) {#seadog-s-gait}

At 1st level, the buccaneer gains [Sea Legs](ref/feat/sea-legs) as a bonus feat. If she spends 1
grit point, she can ignore [difficult terrain](ref/rule/terrain-and-obstacles) until the end of her
turn. This replaces the quick clear deed.

## Pirate's Jargon (Ex) {#pirate-s-jargon}

At 3rd level, the buccaneer's baffling palaver of nautical jargon and piratical cant provides a +2
bonus on Bluff and Intimidate checks. Furthermore, she can spend a swift action and 1 grit point to
cause a single living creature within 30 feet to make a Will saving throw (DC = 10 + 1/2 her
buccaneer level + her Charisma modifier) or become [confused](ref/misc/confused) for 1 round. This
is a mind-affecting language-dependent effect. This replaces the pistol whip deed.

## Rope Swing (Ex) {#rope-swing}

At 7th level, as long as the buccaneer has at least 1 grit point, she gains a bonus on Acrobatics
and Climb checks equal to her gunslinger level when climbing or swinging on a rope. If she spends 1
grit point, her move while climbing or swinging on a rope does not provoke attacks of opportunity.
This replaces the dead shot deed.

## Captain's Curse (Sp) {#captain-s-curse}

At 11th level, a buccaneer can spend 2 grit points to use
_[old salt's curse](ref/spell/old-salts-curse)_ as a
[spell-like ability](ref/umr/spell-like-abilities). At 15th level, she may use
_[black mark](ref/spell/black-mark)_ instead. The caster level for these
[spell-like abilities](ref/umr/spell-like-abilities) is equal to the buccaneer's class level, and
the save DC is equal to 10 + her buccaneer level + her Charisma modifier. This replaces the
lightning reload deed.

## Grit (Ex) {#grit}

Like the sea itself, a buccaneer is a force of nature. Instead of using her Wisdom modifier to
determine the number of grit points she gains at the start of each day, she uses her Charisma
modifier. This ability works in all other ways like the gunslinger's grit class feature.

## Liquid Courage (Ex) {#liquid-courage}

At 2nd level, a buccaneer gains the ability to fortify her grit with strong drink. The act of
drinking is a standard action that provokes attacks of opportunity, and each drink provides 1 grog
point. Grog points can be used in place of grit points to fuel deeds or grit feats (including those
requiring a minimum of 1 grit point to use). The buccaneer can gain a maximum number of grog points
each day equal to her Constitution modifier (minimum 1), and they last for 1 hour or until used,
whichever comes first. She gains a morale bonus on saves against fear and a dodge bonus to AC
against attacks of opportunity equal to her current grog point total. This ability replaces the
nimble ability.

## Bonus Feat {#bonus-feat}

In addition to combat and grit feats, a buccaneer can select from the following feats as her bonus
feats: [Expert Driver](ref/feat/expert-driver) (water vehicles only),
[Master Siege Engineer](ref/feat/master-siege-engineer), [Siege Engineer](ref/feat/siege-engineer),
[Siege Gunner](ref/feat/siege-gunner), [Skilled Driver](ref/feat/skilled-driver) (water vehicles
only).

## Exotic Pet (Ex) {#exotic-pet}

At 5th level, a buccaneer gains a [familiar](ref/sidekick/familiar) as a [wizard](ref/class/wizard)
of half the buccaneer's class level (though the exotic pet never gains the ability to deliver touch
spells or share spells). This pet is typically a [monkey](ref/monster/familiar-monkey) or parrot
(use the stats for a [raven](ref/monster/familiar-raven) familiar). Such animals are useful scouts,
even in the thick of combat. As long as the pet is within 30 feet of the buccaneer, the buccaneer
also gains the benefit of [evasion](ref/ability/evasion). This ability replaces gun training 1.

## Sword and Pistol {#sword-and-pistol}

At 9th level, a buccaneer gains [Sword and Pistol](ref/feat/sword-and-pistol) as a bonus feat even
if she does not meet the prerequisites. This ability replaces gun training 2.

## Gun Training (Ex) {#gun-training}

A buccaneer gains this ability only at 13th level with a single type of firearm.

## Raider's Riposte (Ex) {#raider-s-riposte}

At 17th level, whenever an enemy misses a buccaneer with an attack of opportunity, it provokes an
attack of opportunity from the buccaneer. This ability replaces gun training 4.
