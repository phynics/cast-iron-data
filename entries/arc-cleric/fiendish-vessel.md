+++
id = "ref/arc-cleric/fiendish-vessel"
kind = "archetype"
title = "Fiendish Vessel"
aon = "ArchetypeDisplay.aspx?FixedName=Cleric%20Fiendish%20Vessel"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fiendish_vessel", path = "json/archetypes_cleric.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/cleric" },
]
[[sources]]
publication = "advanced-race-guide"
page = "170"

[fields]
kind = "archetype"
features = [
  { anchor = "domains" },
  { anchor = "channel-evil", level = 1 },
  { anchor = "fiendish-familiar", level = 3 },
  { anchor = "fiendish-augury", level = 3 },
  { anchor = "fiendish-divination", level = 9 },
  { anchor = "extra-divination", level = 13 },
  { anchor = "fiendish-summoning" },
]
trades = [
  { replaces = "Channel energy", feature = "channel-energy", by = ["channel-evil"] },
]
+++

Many clerics pray to or make evil bargains with fiendish powers, devoting body and soul to the
insane plans and wicked aims of their despicable patrons. But these mortal clerics are often just
shallow beings searching for quick power or the caress of true and final oblivion - few truly grasp
the full scope of the entities they worship. Fiendish vessels, through their fiendish heritage,
share an innate connection with their patron, and that connection grants them understanding and
power. A fiendish vessel has the following class features.

**Prerequisites:** Tiefling; Alignment must match patron's

## Alignment {#alignment}

Unlike normal clerics, a fiendish vessel's alignment must match her patron's.

## Domains {#domains}

A fiendish vessel must select the Daemon, Demon, or Devil subdomain (_Advanced Player's Guide_ 88–
90) as one of her domain choices, based on the fiendish patron she chooses to serve.

## Channel Evil (Su) {#channel-evil}

At 1st level, a fiendish vessel, rather than channeling positive or negative energy, instead
channels the pure evil power of her fiendish patron. This ability is similar to channeling negative
energy, but instead of healing undead and dealing damage to living creatures, this blast of evil
energy automatically heals evil creatures and debilitates good creatures within its
[burst](ref/misc/burst).

Channeling this evil causes a burst that affects all creatures in a 30-foot radius centered on the
fiendish vessel. In the case of evil creatures, the amount of damage healed is equal to 1d4 points
of damage and increases by 1d4 at every two levels beyond 1st (to a maximum of 10d4 at 19th level).
Good creatures in the burst receive a Will saving throw to negate this damage. Good creatures that
fail their saving throws are [sickened](ref/misc/sickened) for 1d4 rounds. Good creatures with a
number of Hit Dice less than or equal to the fiendish vessel's class level - 5 that fail their
saving throws are [nauseated](ref/misc/nauseated) for 1 round and then sickened for 1d4 rounds
instead. The DC of this save is equal to 10 + 1/2 the fiendish vessel's level + the fiendish
vessel's Charisma bonus. Neutral creatures are unaffected by this burst of evil energy.

A fiendish vessel may channel this energy a number of times per day equal to 3 + her Charisma
modifier. Doing so is a standard action that does not provoke attacks of opportunity. A fiendish
vessel can choose whether or not to include herself in this effect. A fiendish vessel must present
her unholy symbol or use her familiar as the divine focus for this ability.

For the purposes of feats that affect channel energy, this ability counts as channeling negative
energy. If the feat changes the way the fiendish vessel channels or deals damage with her
channeling, use the amount of damage this ability heals evil creatures to determine the
damage-dealing potential of the affected ability. For instance, if a 5th-level fiendish vessel takes
the [Channel Smite](ref/feat/channel-smite) feat, her channeling deals an additional 3d4 points of
damage to living creatures on a successful hit (though they may save to negate the damage).

This ability replaces channel energy.

## Fiendish Familiar {#fiendish-familiar}

At 3rd level, a fiendish vessel's patron rewards her with a fiendish servant. The fiendish vessel
gains an [imp](ref/monster/devil-imp), [quasit](ref/monster/demon-quasit), or
[cacodaemon](ref/monster/daemon-cacodaemon) [familiar](ref/ability/familiars) based on the patron
she worships. If she worships Asmodeus or an archdevil, she gets an imp; if she worships a demon
lord, she gets a quasit; and if she worships one of the Four Horsemen, she gains a cacodaemon. This
ability is identical to the [wizard's](ref/class/wizard) arcane bond with a familiar and the
[Improved Familiar](ref/feat/improved-familiar) feat, using the fiendish vessel's character level in
place of the wizard level.

This tiny fiend acts like a perverse, manifest moral compass. Furthermore, this familiar can act as
a living divine focus and unholy symbol for her spellcasting if the fiendish vessel so desires,
which means that when she uses her channel evil ability, its burst can be centered on the familiar
instead, as long as that familiar is within 30 feet and line of sight. A fiendish vessel's familiar
tends to be fawning and subservient to the fiendish vessel. Should her familiar die, the fiendish
vessel's patron replaces the familiar with an identical one within 1 week, without the need for a
special ritual. Furthermore, the fiendish familiar gains the following special abilities beyond the
standard familiar special abilities.

## Fiendish Augury (Sp) {#fiendish-augury}

At 3rd level, the fiendish vessel can ask the familiar whether a particular course of action will
bring good or bad results for her in the immediate future. This ability acts like the
_[augury](ref/spell/augury)_ spell, with a caster level equal to the fiendish vessel's level, with
the familiar acting as the mouthpiece for the spell. This ability can be used once per day.

## Fiendish Divination (Sp) {#fiendish-divination}

At 9th level, the fiendish vessel can use a more powerful form of [divination](ref/spell/divination)
to gain intelligence from her patron through her fiendish familiar. This ability acts like the
_divination_ spell, with a caster level equal to the fiendish vessel's level; the familiar acts as
the mouthpiece for the spell. This ability can be used once per day.

## Extra Divination (Sp) {#extra-divination}

At 13th level, the fiendish vessel can gain intelligence from her patron more often each day. She
can use fiendish divination up to 3 times per day.

## Fiendish Summoning {#fiendish-summoning}

When casting _[summon monster](ref/spell/summon-monster)_ spells, a
[fiendish](ref/template/fiendish) vessel is limited to summoning fiendish creatures and evil
outsiders of the same alignment as her patron.
