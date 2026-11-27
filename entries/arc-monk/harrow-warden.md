+++
id = "ref/arc-monk/harrow-warden"
kind = "archetype"
title = "Harrow Warden"
aon = "ArchetypeDisplay.aspx?FixedName=Monk%20Harrow%20Warden"
source_ids = ["the-harrow-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "harrow_warden", path = "json/archetypes_monk.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/monk" },
]
[[sources]]
publication = "the-harrow-handbook"
page = "7"

[fields]
kind = "archetype"
features = [
  { anchor = "idiot-strike", level = 1 },
  { anchor = "mute-hag-stance", level = 9 },
  { anchor = "big-sky-stance", level = 11 },
  { anchor = "eclipse-strike", level = 15 },
]
trades = [
  { replaces = "Stunning fist", feature = "stunning-fist", by = ["idiot-strike"] },
  { replaces = "Improved evasion", feature = "improved-evasion", by = ["mute-hag-stance"] },
  { replaces = "Diamond body", feature = "diamond-body", by = ["big-sky-stance"] },
  { replaces = "Quivering palm", feature = "quivering-palm", by = ["eclipse-strike"] },
]
+++

Some who study the mysteries of the harrow do so to restore lost knowledge and pride to the Varisian
people. The harrow warden fulfills this role as she seeks to bring her mind and body into alignment,
and she protects her people by invoking the folklore that has guided them for so long. In mastering
her own place in fate, a harrow warden learns how to misalign the destinies of others.

## Weapon and Armor Proficiency {#weapon-and-armor-proficiency}

The harrow warden is proficient with all simple weapons, as well as with the
[klar](ref/eq-armor/klar), [rapier](ref/eq-weapon/rapier), [short sword](ref/eq-weapon/short-sword),
and [starknife](ref/eq-weapon/starknife). Additionally, harrow wardens treat starknives as monk
weapons.

## Idiot Strike (Su) {#idiot-strike}

At 1st level, the harrow warden can make an unarmed strike against a target and curse the creature
with bad luck. Foes damaged by an idiot strike must succeed at a Will save (DC 10 + 1/2 the monk's
level + the monk's Wisdom modifier) or become jinxed. A jinxed creature must roll twice whenever it
attempts an attack roll, a saving throw, a skill check, or a caster level check for 1 round, taking
the lower result in each instance. The harrow warden can use idiot strike once per day per monk
level. She must declare that she is using an idiot strike before making the attack roll; thus, a
failed roll wastes the attempt. At 4th level and again at 12th level, the jinx effect lasts an
additional round. At 16th level, a harrow warden can expend two uses of idiot strike to instead
curse her target as the _[bestow curse](ref/spell/bestow-curse)_ spell.

This ability replaces stunning fist.

## Mute Hag Stance (Su) {#mute-hag-stance}

Beginning at 9th level, the harrow warden can block opponents' metaphysical ties to one another.
Enemies threatened by the harrow warden do not gain the effects of any morale or insight bonuses on
attack rolls or skill checks as long as they are within the harrow warden's threatened area. This
ability replaces improved evasion.

## Big Sky Stance (Su) {#big-sky-stance}

At 11th level, the harrow warden becomes secure in her role within the larger story. She gains
immunity to curses and polymorph effects. This ability replaces diamond body.

## Eclipse Strike (Su) {#eclipse-strike}

Beginning at 15th level, the harrow warden can strike a target with enough force to realign its
place in the world. Foes damaged by the harrow warden's idiot strike can attempt a Fortitude save
(DC 10 + 1/2 the monk's level + the monk's Wisdom modifier). Those that fail are transmuted into a
harmless form, as per the _[baleful polymorph](ref/spell/baleful-polymorph)_ spell. This ability
replaces quivering palm.
