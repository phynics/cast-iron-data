+++
id = "ref/arc-paladin/empyreal-knight"
kind = "archetype"
title = "Empyreal Knight"
aon = "ArchetypeDisplay.aspx?FixedName=Paladin%20Empyreal%20Knight"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "empyreal_knight", path = "json/archetypes_paladin.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/paladin" },
]
[[sources]]
publication = "ultimate-combat"
page = "62"

[fields]
kind = "archetype"
features = [
  { anchor = "voices-of-the-spheres", level = 2 },
  { anchor = "celestial-heart" },
  { anchor = "celestial-ally", level = 4 },
  { anchor = "divine-bond", level = 5 },
  { anchor = "empyreal-champion", level = 20 },
]
trades = [
  { replaces = "Divine grace", feature = "divine-grace", by = ["voices-of-the-spheres"] },
  { replaces = "Mercy", feature = "mercy", by = ["celestial-heart"] },
  { replaces = "Lay on hands", feature = "lay-on-hands", by = ["celestial-ally"] },
  { replaces = "channel positive energy", feature = "channel-positive-energy", by = ["celestial-ally"] },
  { replaces = "Holy champion", feature = "holy-champion", by = ["empyreal-champion"] },
  { alters = "Divine bond", feature = "divine-bond", by = ["divine-bond"] },
]
+++

The empyreal knight dedicates her life to serving the celestial beings that guide mortals in their
struggle toward the light.

## Voices of the Spheres {#voices-of-the-spheres}

At 2nd level, an empyreal knight learns to speak and read Celestial, if she could not already. This
ability replaces divine grace.

## Celestial Heart (Su) {#celestial-heart}

As an empyreal knight advances, her ties with the celestial realms grant her a portion of the
abilities and defenses of true [angels](ref/family/angel). At 3rd level, she gains resistance 5
against acid, cold, and electricity. At 6th level, she gains a +4 racial bonus on saves against
poison. At 9th level, her defenses improve to resistance 10 against acid, cold, and electricity. At
12th level, she gains immunity to petrification.

At 15th level, she gains truespeech, the ability to speak with any creature that has a language as
though using a _[tongues](ref/spell/tongues)_ spell. This ability functions with a caster level
equal to her character level, and is always active.

At 18th level, as a swift action, the empyreal knight can manifest a protective aura against evil.
Against abilities or effects created by evil creatures, this ability provides a +4 deflection bonus
to AC and a +4 resistance bonus on saving throws to anyone within 20 feet of her. It otherwise
functions as a _[magic circle against evil](ref/spell/magic-circle-against-evil)_. She can use this
ability for a maximum of 1 round per day per paladin level. These rounds do not need to be
consecutive. These abilities replace mercy.

## Celestial Ally (Sp) {#celestial-ally}

At 4th level, an empyreal knight can summon a [celestial](ref/template/celestial) ally as a
full-round action. This functions as _[summon monster I](ref/spell/summon-monster-1)_, except it can
only be used to summon celestial creatures, [archons](ref/family/archon), and angels. At 6th level,
this improves to _summon monster II_, increasing by one spell level for every two levels thereafter,
to a maximum of _summon monster IX_ at 20th level. This ability can be used a number of times per
day equal to the empyreal knight's Charisma modifier (minimum 1), but only one ally can be summoned
at a time. This ability replaces lay on hands and channel positive energy.

## Divine Bond (Su) {#divine-bond}

At 5th level, an empyreal knight forms a bond with a mount, as the standard paladin ability. Her
mount gains the celestial template at 8th level. At 12th level, her mount sprouts wings if it cannot
already fly, and gains a fly speed of twice its land speed and good maneuverability. If the mount
could already fly, its fly speed and maneuverability improve to at least this level. This ability
otherwise functions as the paladin ability of the same name.

## Empyreal Champion {#empyreal-champion}

At 20th level, an empyreal knight transcends her mortal self. Her DR increases to 10/evil. Her type
is treated as [outsider](ref/type/outsider) for the purposes of spells and magical effects. She
gains [darkvision](ref/rule/darkvision) 60 feet and [low-light vision](ref/rule/low-light-vision).
As a standard action and a supernatural ability, she can sprout wings that allow her to fly at twice
her land speed with average maneuverability. Any armor or clothing reshapes to allow her to fly when
she uses this ability. She can retract the wings as a free action. Unlike other outsiders, an
empyreal knight can still be brought back from the dead as if she were a member of her previous
creature type. This ability replaces holy champion.
