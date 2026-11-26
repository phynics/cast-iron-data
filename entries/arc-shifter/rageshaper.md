+++
id = "ref/arc-shifter/rageshaper"
kind = "archetype"
title = "Rageshaper"
aon = "ArchetypeDisplay.aspx?FixedName=Shifter%20Rageshaper"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "rageshaper", path = "json/archetypes_shifter.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/shifter" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "82"

[fields]
kind = "archetype"
features = [
  { anchor = "devastating-form", level = 1 },
  { anchor = "terrible-slam", level = 1 },
  { anchor = "invulnerable-defenses", level = 2 },
  { anchor = "unrestrained-stride", level = 3 },
  { anchor = "terrible-leap", level = 5 },
]
trades = [
  { replaces = "Wild shape", feature = "wild-shape", by = ["devastating-form"] },
  { replaces = "Shifter aspect, and all improvements to shifter aspect", feature = "shifter-aspect", by = ["devastating-form"] },
  { replaces = "Defensive instinct", feature = "defensive-instinct", by = ["invulnerable-defenses"] },
  { replaces = "chimeric aspect", feature = "chimeric-aspect", by = ["invulnerable-defenses"] },
  { replaces = "greater chimeric aspect", feature = "greater-chimeric-aspect", by = ["invulnerable-defenses"] },
  { replaces = "Woodland stride", feature = "woodland-stride", by = ["unrestrained-stride"] },
  { replaces = "Trackless step", feature = "trackless-step", by = ["terrible-leap"] },
  { alters = "Alignment" },
  { alters = "Shifter claws", feature = "shifter-claws", by = ["terrible-slam"] },
]
+++

Not all shifters represent the balance of nature. The rageshaper is a destructive force of nature
brought to bear—a wild and uncontrollable engine of annihilation fueled by wrath. Rageshapers fly
into bloodletting frenzies and rain down devastation like unstoppable natural disasters.

## Alignment {#alignment}

A rageshaper can be any nonlawful alignment. A rageshaper who becomes lawful cannot take any further
levels in rageshaper, but he does not lose access to any rageshaper abilities he has already gained.

This alters the shifter's alignment.

## Devastating Form (Su) {#devastating-form}

A rageshaper can enter a state of intense fury, transforming into a living engine of destruction.
This ability functions as the [barbarian's](ref/class/barbarian) rage class feature, except entering
this state of fury requires a full-round action that provokes attacks of opportunity and has
additional effects as noted below. At the start of the rageshaper's next turn, he not only gains the
benefit of rage but also grows one size category larger (though worn equipment and held items do not
increase in size).

Armor or clothing the rageshaper wears that doesn't accommodate his changing size immediately gains
the [broken](ref/misc/broken) condition. If insufficient room is available to accommodate this
change, the rageshaper attains the maximum possible size for the available space and can attempt a
Strength check (using his increased Strength) to burst any enclosures in the process. If the check
fails, he is constrained but not harmed by the materials enclosing him.

A rageshaper can remain in his devastating form for a number of rounds per day equal to his shifter
level. He can dismiss devastating form only with a successful Will save (DC = 10 + his shifter
level) made as a free action. On a failed save, the attempted remains in devastating form for an
additional round. If the rageshaper does not successfully end his devastating form before he runs
out of daily rounds, the next time he fails his Will save to revert, he flies into an uncontrollable
frenzy as if affected by _[confusion](ref/spell/confusion)_, but he treats a roll of 26–50 as
"attacks nearest creature." Each round the rageshaper spends in an uncontrollable frenzy, the Will
save DC to exit devastating form decreases by 2.

When a rageshaper ends his devastating form ability, he is [fatigued](ref/misc/fatigued) for a
number of rounds equal to twice the number of rounds he spent in devastating form. A rageshaper
cannot enter devastating form again while fatigued or exhausted. If a rageshaper falls unconscious,
his devastating form ends immediately.

At 10th level, the rageshaper can grow up to a maximum of two size categories larger with
devastating form and his rage is now treated as greater rage.

At 20th level, the rageshaper can grow up to a maximum of three size categories larger with
devastating form and his rage is treated as mighty rage.

This replaces wild shape, shifter aspect, and all improvements to shifter aspect.

## Terrible Slam (Su) {#terrible-slam}

A rageshaper can deliver blows that demolish his foes. This functions as the shifter claws class
ability, except his natural weapons are treated as slam attacks. Additionally, rather than granting
the ability to bypass different kinds of [damage reduction](ref/rule/damage-reduction), the
rageshaper's terrible slam ignores some of an object's [hardness](ref/umr/hardness). At 1st level,
terrible slam ignores 5 points of an object's [hardness](ref/umr/hardness). This increases to 10
points at 5th level, 15 points at 10th level, and 20 points at 15th level.

This alters shifter claws.

## Invulnerable Defenses (Ex) {#invulnerable-defenses}

At 2nd level, a rageshaper becomes difficult to harm in his devastating form. Whenever the
rageshaper takes on his devastating form and is unencumbered and either wearing no armor or wearing
light or medium nonmetal armor, he gains a +2 natural armor bonus to his AC and DR 2/—.

This replaces defensive instinct, chimeric aspect, and greater chimeric aspect.

## Unrestrained Stride (Ex) {#unrestrained-stride}

At 3rd level, whenever the rageshaper is in devastating form, he ignores movement penalties from
[difficult terrain](ref/rule/terrain-and-obstacles) and is immune to the
[entangled](ref/rule/entangled) condition.

This replaces woodland stride.

## Terrible Leap (Ex) {#terrible-leap}

At 5th level, when a rageshaper is in his devastating form, he can perform a terrible leap as a move
action without attempting an Acrobatics check, jumping any distance up to his move speed (upward
movement counts as double, as when flying). He can leap in this way once per day per shifter level.

This replaces trackless step.
