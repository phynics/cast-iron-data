+++
id = "ref/arc-gunslinger/bushwhacker"
kind = "archetype"
title = "Bushwhacker"
aon = "ArchetypeDisplay.aspx?FixedName=Gunslinger%20Bushwhacker"
source_ids = ["advanced-race-guide"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "bushwhacker", path = "json/archetypes_gunslinger.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/gunslinger" },
]
[[sources]]
publication = "advanced-race-guide"
page = "134"

[fields]
kind = "archetype"
features = [
  { anchor = "trembling-grit", level = 1 },
  { anchor = "craven-deeds" },
  { anchor = "shifty-shot", level = 3 },
  { anchor = "long-range-shifty-shot", level = 7 },
  { anchor = "sneak-shot", level = 4 },
  { anchor = "class-skill" },
  { anchor = "bloodline-arcana" },
  { anchor = "bloodline-powers" },
]
trades = [
  { replaces = "Utility shot deed", feature = "deeds", power = "utility shot", by = ["shifty-shot"] },
  { replaces = "Targeting deed", feature = "deeds", power = "targeting", by = ["long-range-shifty-shot"] },
  { replaces = "Bonus feats the gunslinger gains at 4th, 8th, 12th, 16th, and 20th level", feature = "bonus-feats", levels = [4, 8, 12, 16, 20], by = ["sneak-shot"] },
  { alters = "Grit", feature = "grit", by = ["trembling-grit"] },
  { alters = "Deeds", feature = "deeds", by = ["craven-deeds"] },
]
+++

The bushwhacker specializes in the art of the ambush. For her, gunplay works best when it comes from
a concealed position and is directed against a target that falls with the very first volley and is
dead before the smoke clears. A bushwhacker has the following class features.

## Trembling Grit (Ex) {#trembling-grit}

At 1st level, at the start of each day, a bushwhacker gains grit points equal to her Wisdom
modifier - 1 (minimum of 1). In addition to all the ways any gunslinger can regain grit, a
bushwhacker who reduces a helpless or unaware opponent to 0 hit points or fewer also regains 1 grit
point. This expands the way in which the bushwhacker gains grit points, so a bushwhacker who gains
grit points in this way only gains 1 grit point for reducing a helpless or unaware opponent, not 2
grit points. This otherwise works like the gunslinger's grit ability and alters that ability.

## Craven Deeds (Ex) {#craven-deeds}

A bushwhacker replaces some of her deeds with the following deeds. This ability otherwise works like
the gunslinger's deed ability and alters that ability.

## Shifty Shot (Ex) {#shifty-shot}

At 3rd level, a bushwhacker with at least 1 grit point deals 1d6 points of extra damage when using
her firearm to attack opponents denied their Dexterity bonus to AC (whether the target actually has
a Dexterity bonus or not). Except for the requirement that she must use a firearm and must have at
least 1 grit point to use it, this deed otherwise works identically to a rogue's
[sneak attack](ref/ability/sneak-attack) class feature (including the requirement that she must be
within 30 feet of her target to deal this extra damage), and stacks with the sneak shot ability (see
below) and sneak attack. This deed replaces the utility shot deed.

## Long Range Shifty Shot (Ex) {#long-range-shifty-shot}

At 7th level, a bushwhacker can double the range at which she deals extra damage from a sneak attack
or shifty shot (from 30 feet to 60 feet) with a firearm by spending 1 grit point. When she spends
this grit point, she must still have at least 1 grit point left to deal extra damage from shifty
shot if she is using this deed. This deed replaces the targeting deed.

## Sneak Shot (Ex) {#sneak-shot}

At 4th level and every four levels thereafter, a bushwhacker deals 1d6 points of extra damage when
using a firearm to attack opponents who are unable to properly defend themselves. Unlike with the
shifty shot ability, she deals this extra damage regardless of whether or not she has any grit
points when making the attack. Except for the requirement that she makes a firearm attack, this
works identically to a rogue's sneak attack class feature. This extra damage stacks with sneak
attack and the damage from shifty shot. This ability replaces the bonus feats the gunslinger gains
at 4th, 8th, 12th, 16th, and 20th level. While many kobold sorcerers tout their purely draconic
bloodline, over generations of eldritch training, some such spellcasters have created a bloodline
that, while tinged with some draconic magic, is the embodiment of the race's virtue distilled into
arcane form. Many practitioners of this bloodline go on to lead powerful kobold tribes.

## Class Skill {#class-skill}

Disable Device.

## Bonus Spells {#bonus-spells}

_alarm_ (3rd), _create pit_ (5th), _explosive runes_ (7th), _dragon's breath_ (9th), _transmute rock
to mud_ (11th), _guards and wards_ (13th), _delayed blast fireball_ (15th), _form of the dragon III_
(17th), _imprisonment_ (19th).

## Bonus Feats {#bonus-feats}

Alertness, Combat Casting, Defensive Combat Training, Dodge, Improved Initiative, Lightning Ref
lexes, Silent Spell.

## Bloodline Arcana {#bloodline-arcana}

Whenever you cast a spell against a creature that is denied its Dexterity bonus to AC, increase that
spell's DC by +2.

## Bloodline Powers {#bloodline-powers}

Like all kobolds, you have a natural talent for ambushing, creating traps, and mining. As your power
increases, you discover ever more useful ways to blend your magic with these instinctive talents.

_Trap Rune (Sp)_: At 1st level, as a standard action, you can sketch a single, nearly invisible
magical rune on any 5-foot-square solid surface. When you create a rune, pick one of the following
energy types: acid, cold, electricity, or fire. While the rune is active, the next creature other
than you who steps on or touches the rune's area causes the rune to explode. The rune's explosion
deals a number of points of energy damage equal to 1d8 + 1 per sorcerer level you possess to
anything in its square. A Reflex saving throw halves the damage (DC 10 + 1/2 your sorcerer level +
your Charisma modifier). The rune is considered a magical trap for the purpose of perceiving it or
disabling it. The DC for both Perception and Disable Device checks is the same as the Reflex saving
throw to halve the damage. You can use this ability a number of times per day equal to 3 + your
Charisma modifier. Each rune lasts for 24 hours or until discharged.

_Trap Sense (Ex):_ At 3rd level, you develop a sixth sense that helps you avoid traps. You gain a +2
bonus on Perception checks made to notice traps. You also gain a +1 bonus on Reflex saves to avoid
traps and a +1 dodge bonus to AC against attacks made by traps. These bonuses increase by +1 at 7th
level and for every four sorcerer levels you gain thereafter (to a maximum of +5 at 19th level).
This bonus stacks with that provided by a rogue's trap sense and similar abilities.

_Arcane Ambush (Su)_: At 9th level, as a swift action, you can expend a spell slot in order to grant
you and your allies a bonus on attack and damage rolls. This bonus lasts 1 round, is equal to the
level of the spell expended, and only applies to opponents your allies are flanking or opponents
denied their Dexterity bonus against your allies. You grant this bonus to yourself plus up to one
ally for every four sorcerer levels you possess (to a maximum of five allies at 20th level). The
allies must be within 30 feet of you and you must have line of effect to each affected ally.

_Earth Glide (Su)_: At 15th level, you gain the earth glide universal monster ability with a speed
equal to your base speed. This does not give you the ability to breathe while passing through earth,
so you must hold your breath or use some alternate method to breathe while using this ability.

_Nimble Walker (Su)_: At 20th level, you gain a +5 racial bonus on Reflex saving throws and on
Acrobatics checks made to move through a creature's threatened area or through its space. You also
gain the ability to breathe while passing through earth using your earth glide ability.
