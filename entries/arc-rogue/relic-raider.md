+++
id = "ref/arc-rogue/relic-raider"
kind = "archetype"
title = "Relic Raider"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Relic%20Raider"
source_ids = ["black-markets"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "relic_raider", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "black-markets"
page = "27"

[fields]
kind = "archetype"
features = [
  { anchor = "curse-sense", level = 4 },
  { anchor = "disable-curse", level = 8 },
]
trades = [
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["curse-sense"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["disable-curse"] },
]
+++

Relic raiders are rogues who specialize in recovering treasures from ruins and tombs, some in a
quest for knowledge, others out of a desire for riches. In addition to natural dangers and mundane
traps, these locations are often protected by ancient curses or the psychic imprints of former
occupants. Though not versed in magic, relic raiders learn to unweave these maledictions as easily
as they unlock ancient vaults.

## Curse Sense (Ex) {#curse-sense}

At 4th level, a relic raider adds 1/2 her rogue level on Perception checks to notice haunts and on
Spellcraft checks to identify cursed items (using _[detect magic](ref/spell/detect-magic)_ or
similar effects).

In addition, the relic raider gains a +1 bonus on saving throws against curses and haunts and a +1
dodge bonus to AC against attacks by haunts. These bonuses increase by 1 at 6th level and every 3
rogue levels thereafter (to a maximum of +6 at 18th level). This ability replaces uncanny dodge.

## Disable Curse (Su) {#disable-curse}

At 8th level, a relic raider can attempt to disable a curse as she would a magical trap. This
ability acts as _[remove curse](ref/spell/remove-curse)_, except instead of a caster level check,
the relic raider attempts a Disable Device check (DC = 15 + the DC of the curse). Disabling a curse
takes 2d4 rounds, and the relic raider cannot take 10 or 20 on this check. A relic raider can use
this ability once per day at 8th level. At 12th level and every 4 rogue levels thereafter, a relic
raider can use disable curse one additional time per day. This ability replaces improved uncanny
dodge.

## Advanced Talents {#advanced-talents}

A relic raider can select the following advanced talents. Talents marked with an asterisk add
effects to a rogue's sneak attack. Only one of these talents can be applied to an individual attack,
and the decision must be made before making the attack roll.

### Cursed Strike\* (Su) {#cursed-strike}

Once per day, when the relic raider would normally deal sneak attack damage, she can instead forgo
all bonus damage to attempt to curse her target (as per the spell
_[bestow curse](ref/spell/bestow-curse)_). The save is DC equal to 10 + 1/2 the relic raider's rogue
level + her Intelligence modifier. A relic raider must have the
[major magic](ref/talent/major-magic) rogue talent before choosing cursed strike. The relic raider
can use this ability an additional time per day at 15th level and 20th level.

### Etheric Strike\* (Su) {#etheric-strike}

With a successful sneak attack against haunts or undead, the relic raider can deal her sneak attack
damage as positive energy damage rather than physical damage. The additional damage affects undead
that are normally immune to sneak attacks because of their lack of a discernible anatomy (such as
[ghosts](ref/template/ghost)). A relic raider can make an etheric strike a number of times per day
equal to 3 + her Charisma modifier
