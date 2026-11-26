+++
id = "ref/arc-shifter/adaptive-shifter"
kind = "archetype"
title = "Adaptive Shifter"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Adaptive%20Shifter"
source_ids = ["distant-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "adaptive_shifter", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "distant-realms"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "adaptive-claws", level = 1 },
  { anchor = "reactive-aspect", level = 1 },
  { anchor = "reactive-form" },
  { anchor = "lasting-adaptation", level = 5 },
  { anchor = "unfettered-wild-shape", level = 6 },
]
trades = [
  { replaces = "Shifter aspect", feature = "shifter-aspect", by = ["reactive-aspect"] },
  { replaces = "chimeric aspect", feature = "chimeric-aspect", by = ["reactive-aspect"] },
  { replaces = "greater chimeric aspect", feature = "greater-chimeric-aspect", by = ["reactive-aspect"] },
  { replaces = "final aspect", feature = "final-aspect", by = ["reactive-aspect"] },
  { replaces = "Wild empathy", feature = "wild-empathy", by = ["lasting-adaptation"] },
  { replaces = "track", feature = "track", by = ["lasting-adaptation"] },
  { replaces = "woodland stride", feature = "woodland-stride", by = ["lasting-adaptation"] },
  { replaces = "trackless step", feature = "trackless-step", by = ["lasting-adaptation"] },
  { replaces = "Wild shape", feature = "wild-shape", by = ["unfettered-wild-shape"] },
  { alters = "Shifter claws", feature = "shifter-claws", by = ["adaptive-claws"] },
]
+++

Rather than emulate other animals entirely, some shifters learn to reshape their forms on the fly in
response to a range of stimuli, rarely taking on a new form for longer than necessary to overcome a
challenge.

## Adaptive Claws (Su) {#adaptive-claws}

When activating her shifter claws ability in her natural form, an adaptive shifter can instead
manifest a single bite attack that deals bludgeoning, piercing, and slashing damage; a gore attack
that deals piercing damage; or a tail slap that deals bludgeoning damage. This natural attack
otherwise deals damage as the shifter's claws.

This alters shifter claws.

## Reactive Aspect (Su) {#reactive-aspect}

An adaptive shifter gains the ability to change parts of her body to avoid harm, gain a physical
advantage, or overcome an obstacle. She can do so a number of times per day equal to 3 + her Wisdom
modifier + her shifter level. By activating this ability, either as an immediate action or as a
swift action, an adaptive shifter gains the benefits of one of her reactive forms until the
beginning of her next turn (see below). An adaptive shifter can assume only one reactive form at a
time. Activating a new reactive form (or forms) ends all reactive forms currently manifested.

At 9th level, an adaptive shifter gains the benefits of up to two reactive forms whenever she uses
this ability. At 14th level, she can assume up to three forms. At 20th level, she learns all
reactive forms and doubles her effective Wisdom modifier for the purpose of calculating her uses of
reactive aspect per day.

This replaces shifter aspect, chimeric aspect, greater chimeric aspect, and final aspect.

## Reactive Form (Su) {#reactive-form}

An adaptive shifter learns two reactive forms from the list below. At 2nd level and every 2 levels
thereafter, an adaptive shifter learns an additional reactive form. Forms marked with an asterisk
(\*) are lasting forms. An adaptive shifter can spend two uses of reactive aspect to increase a
lasting form's duration to 1 minute. Forms not marked with an asterisk always last only until the
beginning of her next turn.

### Adaptive Defense {#adaptive-defense}

When assuming this form, the adaptive shifter chooses one saving throw and gains a competence bonus
on the selected save equal to her Wisdom modifier.

### Aligned Adaptation\* {#aligned-adaptation}

When assuming this form, the adaptive shifter chooses one alignment within one step of her own
alignment on either the law/chaos axis or the good/evil axis. All spells, effects, and magic items
affect the adaptive shifter as though that were her actual alignment. If she is at least 10th level,
her natural weapon attacks overcome [damage reduction](ref/rule/damage-reduction) as if they were
weapons of her assumed alignment.

### Aquatic Form\* {#aquatic-form}

The adaptive shifter gains a swim speed equal to her base speed, and she can breathe underwater.

### Climbing Form\* {#climbing-form}

The adaptive shifter gains a climb speed equal to her base speed.

### Durable Form {#durable-form}

The adaptive shifter gains DR 5/adamantine. This damage reduction increases by 1 for every 2 levels
she has beyond 8th. She must be at least 8th level to select this form.

### Evasive Form\* {#evasive-form}

The adaptive shifter gains [compression](ref/umr/compression), a +4 dodge bonus to her CMD against
grapple combat maneuvers, and a competence bonus equal to her Wisdom modifier on Escape Artist
checks.

### Giant Form\* {#giant-form}

The adaptive shifter increases in size, as per _[enlarge person](ref/spell/enlarge-person)_. The
adaptive shifter can assume this form only as a swift action.

### Resistant Form\* {#resistant-form}

When assuming this form, the adaptive shifter chooses acid, cold, electricity, fire, or sonic
damage. She gains [resistance](ref/umr/resistance) to the chosen damage type equal to 5 plus
[half](ref/misc/fractions-and-rounding) her level. She can learn this form a second time, increasing
the resistance granted to 10 plus her level.

### Restoring Form {#restoring-form}

The adaptive shifter regains 1d8 hit points. For every 4 levels she has, the number of hit points
she regains increases by 1d8. The adaptive shifter can assume this form only as a swift action.

### Scouting Form\* {#scouting-form}

The adaptive shifter gains a competence bonus equal to her Wisdom modifier on Stealth checks, and
she gains the benefits of the shifter's trackless step ability. At 12th level, she can use Stealth
to hide, even if she does not have cover or concealment (but not if observed).

### Sensory Form\* {#sensory-form}

The adaptive shifter gains [low-light vision](ref/rule/low-light-vision) and [scent](ref/umr/scent).
She can learn this form a second time to also gain [darkvision](ref/rule/darkvision) with a range of
60 feet and a competence bonus on Perception checks equal to her Wisdom modifier.

### Sky Hunter Form\* {#sky-hunter-form}

The adaptive shifter gains a fly speed equal to her base speed with average maneuverability. She
must be at least 6th level to select this form. She can learn this form a second time, increasing
her fly speed by 20 feet and improving her maneuverability to good.

### Spiked Form\* {#spiked-form}

The adaptive shifter grows spines over her body. Any foe striking her with an unarmed strike or a
melee natural weapon takes an amount of piercing damage equal to the base damage of her shifter
claws, which ignores any [damage reduction](ref/rule/damage-reduction) her shifter claws would
ignore. She can learn this form a second time, allowing her to fling her spines as thrown natural
weapons that deal piercing damage, have a range increment of 30 feet, and allow her to make multiple
attacks with her spines as part of a full attack; these otherwise deal damage and overcome
[damage reduction](ref/rule/damage-reduction) as her shifter claws.

### Sprinting Form\* {#sprinting-form}

The adaptive shifter's base speed increases by 20 feet.

### Stretching Form {#stretching-form}

The adaptive shifter's reach with natural weapons increases by 5 feet.

## Lasting Adaptation (Su) {#lasting-adaptation}

At 5th level, an adaptive shifter can spend 1 minute willing her body to adapt in a more enduring
way. At the end of the minute, she expends two uses of her reactive aspect and selects one lasting
form she knows. She assumes this form and can maintain it until she regains her daily uses of
reactive aspect or uses this ability again. This adaptation does not count against the maximum
number of forms she can assume at once. She can select a form that has a minimum level only if her
character level is at least 3 higher than the minimum level.

At 15th level, the adaptive shifter can maintain up to two lasting adaptations simultaneously,
spending an additional minute and two uses of her reactive aspect each time she assumes a new
adaptation.

This replaces wild empathy, track, woodland stride, and trackless step.

## Unfettered Wild Shape (Su) {#unfettered-wild-shape}

At 6th level, an adaptive shifter gains the ability to turn into other creatures. This functions as
a [druid's](ref/class/druid) wild shape ability, except she does not gain the ability to turn into
an elemental. The shifter's effective druid level is equal to her class level. She can use this
ability for a number of hours per day equal to half her effective druid level. This duration does
not need to be consecutive, but must be spent in 1-hour increments. For abilities that function
based on "uses of wild shape," each hour of unfettered wild shape counts as a use.

This replaces wild shape.
