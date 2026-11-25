+++
id = "ref/arc-shifter/fiendflesh-shifter"
kind = "archetype"
title = "Fiendflesh Shifter"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Fiendflesh%20Shifter"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fiendflesh_shifter", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "80"

[fields]
kind = "archetype"
features = [
  { anchor = "infernal-claws" },
  { anchor = "fiendish-aspect", level = 1 },
  { anchor = "fiendish-resilience", level = 2 },
  { anchor = "chimeric-fiend", level = 9 },
  { anchor = "greater-chimeric-fiend", level = 14 },
]
trades = [
  { replaces = "Wild shape", feature = "wild-shape", by = ["fiendish-aspect"] },
  { replaces = "Shifter aspect, and all improvements to shifter aspect", feature = "shifter-aspect", by = ["fiendish-aspect"] },
  { replaces = "Defensive instinct", feature = "defensive-instinct", by = ["fiendish-resilience"] },
  { replaces = "Chimeric aspect", feature = "chimeric-aspect", by = ["chimeric-fiend"] },
  { replaces = "Greater chimeric aspect", feature = "greater-chimeric-aspect", by = ["greater-chimeric-fiend"] },
  { alters = "Alignment" },
  { alters = "Shifter claws", feature = "shifter-claws", by = ["infernal-claws"] },
]
+++

By forging dark pacts with extraplanar forces, fiendflesh shifters invoke sinister powers to assume
the strengths of daemons, demons, or devils. Fiendflesh shifters care nothing for the natural world
and are instead consumed by an ever-growing lust for power at any price. To other shifters, the
fiendflesh shifter is often viewed as a monster herself—an intrusion into the natural order of
things and a foe who must be sought out and destroyed. Very few druids will ever willingly ally with
fiendflesh shifters; this leaves these outcasts to live bitter, lonely lives or to seek out fiendish
cults or other abhorrent faiths for support and companionship.

## Alignment {#alignment}

A fiendflesh shifter must be evil in alignment. If the fiendflesh shifter becomes nonevil, she loses
all powers granted by this archetype.

This alters the shifter's alignment.

## Infernal Claws (Ex) {#infernal-claws}

A fiendflesh shifter's claws are infused with the unholy power of the evil Outer Planes. At 1st
level, a fiendflesh shifter's claws are treated as evil weapons for the purpose of overcoming
[damage reduction](ref/rule/damage-reduction). This ability otherwise functions as the shifter claws
class feature.

This alters shifter claws.

## Fiendish Aspect (Su) {#fiendish-aspect}

At 1st level, a fiendflesh shifter can temporarily transform her body into an amalgam of
otherworldly evil creatures as a swift action. While in this form, the fiendflesh shifter gains
[darkvision](ref/rule/darkvision) out to a range of 60 feet (or doubles the range of her darkvision
if she already has it), a gore natural attack that deals 1d6 points of damage (1d4 points of damage
if the shifter is Small), and DR 1/good. A fiendflesh shifter can maintain this form for a number of
minutes per day equal to 3 + her shifter level. The duration does not need to be consecutive but
must be spent in 1-minute increments.

At 5th level, the fiendflesh shifter's DR increases to 2/good and she also grows a pair of bat-like
wings when in her fiendish aspect, granting her a fly speed of 30 feet with average maneuverability.

At 10th level, the fiendflesh shifter's DR increases to 5/good, and the electricity and fire
resistance provided by her fiendish resilience ability (see below) doubles while she's in her
fiendish aspect.

At 15th level, the fiendflesh shifter's DR increases to 7/good and her fly speed increases to 60
feet.

At 20th level, the fiendflesh shifter's DR increases to 10/good. She also gains
[immunity](ref/umr/immunity) to electricity and fire and
[spell resistance](ref/rule/spell-resistance) equal to 15 + her shifter level.

This replaces wild shape, shifter aspect, and all improvements to shifter aspect.

## Fiendish Resilience (Su) {#fiendish-resilience}

At 2nd level, a fiendflesh shifter gains a +1 natural armor bonus to her AC and
[resistance](ref/umr/resistance) 5 to electricity and fire, but only while unencumbered and either
wearing no armor or wearing light or medium nonmetal armor. At 4th level, 12th level, and 20th
level, this natural armor bonus increases by 1. At 8th level and 16th level, the fiendflesh
shifter's resistance to electricity and fire increases by 5.

This replaces defensive instinct.

## Chimeric Fiend (Su) {#chimeric-fiend}

At 9th level, when a fiendflesh shifter uses her fiendish aspect ability, she can gain an additional
ability from the list below. The fiendflesh shifter can change which ability she gains each time she
uses fiendish aspect.

### Daemon {#daemon}

Acid resistance 10 and a +4 profane bonus on saves against disease.

### Demon {#demon}

The shifter's electricity resistance doubles.

### Devil {#devil}

The shifter's fire resistance doubles.

This replaces chimeric aspect.

## Greater Chimeric Fiend (Su) {#greater-chimeric-fiend}

At 14th level, a fiendflesh shifter's chimeric fiend ability grants her additional bonuses as noted
below.

### Daemon {#greater-chimeric-fiend-daemon}

The shifter gains a +4 enhancement bonus to her Constitution score and immunity to disease.

### Demon {#greater-chimeric-fiend-demon}

The shifter gains a +4 enhancement bonus to her Strength score and increases the damage die of all
natural attacks [by one step](ref/misc/damage-die-adjustments).

### Devil {#greater-chimeric-fiend-devil}

The shifter gains a +4 enhancement bonus to her Dexterity score and
[see in darkness](ref/umr/see-in-darkness) as per the universal monster rule.

This replaces greater chimeric aspect.
