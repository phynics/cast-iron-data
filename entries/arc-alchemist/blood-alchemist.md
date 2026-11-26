+++
id = "ref/arc-alchemist/blood-alchemist"
kind = "archetype"
title = "Blood Alchemist"
aon = "ArchetypeDisplay.aspx?FixedName=Alchemist%20Blood%20Alchemist"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "blood_alchemist", path = "json/archetypes_alchemist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/alchemist" },
]
[[sources]]
publication = "horror-adventures"
page = "44"

[fields]
kind = "archetype"
features = [
  { anchor = "lifeblood", level = 1 },
  { anchor = "alchemical-circles", level = 1 },
  { anchor = "blood-knowledge", level = 4 },
]
trades = [
  { replaces = "Mutagen", feature = "mutagen", by = ["lifeblood"] },
  { replaces = "Bombs", feature = "bomb", by = ["alchemical-circles"] },
]
+++

Most alchemists can transform matter and energy into other forms, but some wicked specialists
realize that life itself is an energy that can greatly fuel their alchemy.

## Alignment {#alignment}

A blood alchemist trades the lives of others for more power when using his lifeblood ability. A
nonevil blood alchemist can't use the lifeblood ability, but he can use his other archetype and
class abilities, and he can continue to advance in alchemist.

## Lifeblood (Su) {#lifeblood}

When a blood alchemist performs a [coup de grace](ref/misc/helpless) that kills an intelligent
humanoid creature (though, not a summoned intelligent humanoid creature), he can gather its
lifeblood into a vial; this is a death effect. He can use this lifeblood any time within the next 24
hours to create an extract of a spell level he can cast that is no higher than 1/2 the creature's
CR, without spending a daily extract slot. He can use this ability once for each spell level each
day (for example, a 13th-level blood alchemist can use lifeblood to gain additional 1st-, 2nd-,
3rd-, 4th-, and 5th-level extracts). A blood alchemist can't take the mutagen or cognatogen
discoveries.

This ability replaces mutagen.

## Alchemical Circles (Sp, Su) {#alchemical-circles}

A blood alchemist gains a blood pool with a number of points equal to his alchemist level + his
Intelligence modifier. He can spend 1 point from his blood pool to draw a complex alchemical circle
in blood on the ground or on another permanent fixture in a process that takes 1 minute. Depending
on his alchemist level, the alchemical circle can have one of several effects.

At 1st level, the blood alchemist can spend an unused extract slot to charge the circle with
alchemical energy. He chooses one of the spells listed on page 45 of equal or lower level to the
extract slot he spent, and until he refreshes his extract slots, as long as his body is in physical
contact with the circle, he can produce the effect of the spell he chose as a
[spell-like ability](ref/umr/spell-like-abilities). If the spell normally has an expensive material
component, he must still provide it, either grinding it up and mixing it with the blood used for the
circle or placing it in the circle (if the component is also the target). The chosen effect can
target or affect only something contained within the circle, or the surface on which the blood
alchemist drew the circle. To learn one of these effects, he must write it into his formula book,
with the same cost as usual for a formula (he can also use his free formula from leveling up to
learn the chosen effect instead of a normal formula).

The blood alchemist can choose from the following spells for this ability: 1st—_expeditious
excavation_, _fabricate bullets_, _jury-rig_, _magic weapon_, _reinforce armaments_; 2nd—_knock_,
_make whole_, _masterwork transformation_, _silk to steel_, _soften earth and stone_, _warp wood_;
3rd—_keen edge_, _magic vestment_, _greater magic weapon_, _obsidian flow_, _spike stones_, _stone
shape_; 4th—_fabricate_, _passwall_, _transmute mud to rock_, _transmute rock to mud_; 5th—_flesh to
stone_, _move earth_, _stone to flesh_, _tar pool_, _transmute metal to wood_; 6th—_polymorph any
object_, _transmute blood to acid_.

Starting at 8th level, the blood alchemist can also create a [magic circle](ref/spell/magic-circle),
as per the magic circles [occultist](ref/class/occultist) class ability (_Pathfinder RPG Occult
Adventures_ 49), though it costs 1 point from his blood pool instead of 1 point of mental focus.

Starting at 12th level, he can also create a binding circle, as per the occultist class ability of
the same name (_Occult Adventures_ 49), though it costs 2 points from his blood pool instead of 2
points of mental focus.

Starting at 16th level, the blood alchemist can draw magic circles and binding circles more quickly
but with a shorter duration, as per the occultist fast circles ability (_Occult Adventures_ 49).

This ability replaces bombs.

## Blood Knowledge (Sp) {#blood-knowledge}

Starting at 4th level, a blood alchemist can spend an unused extract slot of 2nd level while mixing
a drop of blood with various alchemical reagents in a process that takes 1 minute. If he does so, he
can drink the resulting concoction as a standard action to gain the information he would learn as if
he had cast _[blood biography](ref/spell/blood-biography)_ on the blood he just used. As per the
spell, living and undead creatures receive a Will saving throw (DC = 13 + the blood alchemist's
Intelligence modifier) to negate the effect.
