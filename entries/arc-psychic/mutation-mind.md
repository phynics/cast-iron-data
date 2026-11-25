+++
id = "ref/arc-psychic/mutation-mind"
kind = "archetype"
title = "Mutation Mind"
aon = "ArchetypeDisplay.aspx?FixedName=Psychic%20Mutation%20Mind"
source_ids = ["occult-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "mutation_mind", path = "json/archetypes_psychic.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/psychic" },
]
[[sources]]
publication = "occult-adventures"
page = "105"

[fields]
kind = "archetype"
features = [
  { anchor = "physical-mutation", level = 1 },
  { anchor = "bodily-mutations", level = 3 },
  { anchor = "phrenic-empowerment", level = 7 },
  { anchor = "improved-bodily-mutations", level = 11 },
]
trades = [
  { replaces = "1st-level phrenic amplification", feature = "phrenic-amplifications", levels = [1], by = ["physical-mutation"] },
  { alters = "Phrenic amplifications", feature = "phrenic-amplifications", by = ["bodily-mutations"] },
  { alters = "Major amplifications", feature = "major-amplifications", by = ["improved-bodily-mutations"] },
]
+++

Exposure to unintended spell effects, curses, or sources of radiation cause some to manifest psychic
powers. When a mutation mind uses her psychic abilities, her physical body changes under the stress,
and she risks losing control if she pushes too far.

## Physical Mutation (Su) {#physical-mutation}

A mutation mind's psychic powers warp her body, allowing her to physically mutate herself as a swift
action, which grants her a +4 enhancement bonus to Strength and a -2 penalty to Intelligence. At
12th level, the bonus to Strength increases to +6. A mutation mind can assume her physically mutated
form for a number of minutes per day equal to her psychic level. The minutes don't have to be used
consecutively, but must be used in 1-minute increments. When the duration runs out, the mutation
mind can spend 1 point from her phrenic pool to extend the duration by 1 round. She can continue
extending it in this way until she runs out of points. After the mutation ends, the mutation mind is
fatigued and can't activate a physical mutation again for 1 round. Turning back to normal before the
end of a 1-minute increment takes a standard action. This ability replaces the 1st-level phrenic
amplification.

## Bodily Mutations {#bodily-mutations}

Starting at 3rd level, whenever a mutation mind gains a phrenic amplification, she can select either
a phrenic amplification or a bodily mutation. A bodily mutation grants its benefit only when the
mutation mind is affected by her physical mutation. Each time she activates her physical mutation,
she can activate any number of bodily mutations she possesses.

### Adhesive (Ex) {#adhesive}

The mutation mind's skin becomes sticky, granting her a +4 bonus on [disarm](ref/rule/disarm) and
[grapple](ref/rule/grapple) combat maneuver checks.

### Bite Attack (Ex) {#bite-attack}

The mutation mind's mouth fills with sharp teeth, allowing her to make a
[bite attack](ref/umr/natural-attacks) as part of a full-attack action at her highest base attack
bonus. This attack deals 1d4 points of damage (1d3 if Small) and counts as a primary attack unless
combined with manufactured weapon attacks, as normal.

### Bulging Eyes (Ex) {#bulging-eyes}

The mutation mind's eyes grow large and round, granting her [darkvision](ref/rule/darkvision) with a
range of 60 feet.

### Claws (Ex) {#claws}

The mutation mind's hands turn into claws, allowing her to make two claw attacks as a full-attack
action at her highest base attack bonus. Each of these attacks deals 1d4 points of damage (1d3 if
Small) and counts as a primary attack unless combined with manufactured weapon attacks, as normal.

### Elongated Fingers (Ex) {#elongated-fingers}

The mutation mind's fingers grow long and supple, increasing her reach by 5 feet when she's making
melee touch attacks.

### Elongated Legs (Ex) {#elongated-legs}

The mutation mind's legs become long and spindly, increasing her base movement by 10 feet.

### Energy Resistance (Ex) {#energy-resistance}

The mutation mind's body changes in color and texture, and gains energy resistance 5 to one energy
type (acid, cold, electricity, fire, or sonic), chosen when this mutation is selected. This mutation
can be selected multiple times. Each time it is selected, the mutation mind either chooses an
additional energy type to gain energy resistance 5 against or increases the resistance granted to
one existing type by 5.

### Enlarged Torso (Ex) {#enlarged-torso}

The mutation mind's torso enlarges disproportionately with the rest of her body, granting her a +2
natural armor bonus to AC.

### Rubbery (Ex) {#rubbery}

The mutation mind's body becomes soft and rubbery, granting her DR 2/—.

### Slimy (Ex) {#slimy}

The mutation mind exudes a thin layer of oily slime over her body, granting her a +4 bonus to CMD.

This ability alters phrenic amplifications.

## Phrenic Empowerment (Su) {#phrenic-empowerment}

At 7th level, a mutation mind's phrenic amplifications empower her physical mutation. Whenever a
mutation mind modifies a spell with a phrenic amplification while affected by her physical mutation,
she can increase the bonus to her Strength score from her physical mutation by 2 for a number of
rounds equal to the level of the spell she cast. This bonus doesn't stack; if the mutation mind
activates it again, she uses the longer duration but doesn't increase the bonus.

While under the effect of phrenic empowerment, whenever the mutation mind takes damage, she risks
losing control of her powers. At the end of each turn that she takes hit point damage, the mutation
mind must succeed at a Will save (DC = 15 + 1/2 her character level) or take a -2 penalty on Will
saving throws and to Intelligence. These penalties last for 1 hour after the physical mutation ends
and stack with themselves.

If the penalty lowers her Intelligence score to 0, the mutation mind is comatose until 1 hour after
physical mutation ends.

## Improved Bodily Mutations {#improved-bodily-mutations}

At 11th level, a mutation mind can select one of the following improved bodily mutations instead of
a phrenic amplification.

### Aquatic Form (Ex) {#aquatic-form}

The mutation mind's legs fuse into a tail and fins to sprout from her back and side, granting her a
swim speed of 30 feet, [tremorsense](ref/umr/tremorsense) with a range of 30 feet (affecting other
creatures in contact with the same body of water), and the [aquatic](ref/subtype/aquatic) subtype.

Her base land speed is reduced to 10 feet.

### Enlarged Body (Ex) {#enlarged-body}

The mutation mind's body swells and stretches, enlarging her as the
_[enlarge person](ref/spell/enlarge-person)_ spell but up to two size categories larger (maximum
Huge).

### Multiple Eyes (Ex) {#multiple-eyes}

Multiple eyes erupt all over the mutation mind's body. She can't be [flanked](ref/rule/flanking) and
gains a +4 bonus on Perception checks.

### Recuperation (Ex) {#recuperation}

The mutation mind heals quickly from physical wounds, gaining
[fast healing](ref/umr/fast-healing) 5.

### Toppling Fists (Ex) {#toppling-fists}

The mutation mind's fists become large masses of flesh, allowing her to attempt a
[bull rush](ref/rule/bull-rush) combat maneuver check against one creature within 10 feet of her as
a standard action.

### Wings (Ex) {#wings}

The mutation mind sprouts a pair of fleshy, batlike wings, giving her a fly speed of 60 feet with
average maneuverability.

This ability alters major amplifications.
