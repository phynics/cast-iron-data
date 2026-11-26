+++
id = "ref/arc-swashbuckler/whirling-dervish"
kind = "archetype"
title = "Whirling Dervish"
aon = "ArchetypeDisplay.aspx?FixedName=Swashbuckler%20Whirling%20Dervish"
source_ids = ["advanced-class-origins"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "whirling_dervish", path = "json/archetypes_swashbuckler.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/swashbuckler" },
]
[[sources]]
publication = "advanced-class-origins"
page = "23"

[fields]
kind = "archetype"
features = [
  { anchor = "dervish-finesse", level = 1 },
  { anchor = "dawnflower-s-mercy", level = 1 },
  { anchor = "dervish-dance", level = 4 },
  { anchor = "whirlwind-dance", level = 7 },
  { anchor = "dance-of-dawn", level = 11 },
  { anchor = "dance-of-mercy", level = 19 },
]
trades = [
  { replaces = "Superior feint", feature = "deeds", power = "superior feint", by = ["whirlwind-dance"] },
  { replaces = "targeted strike", feature = "deeds", power = "targeted strike", by = ["whirlwind-dance"] },
  { replaces = "Bleeding wound", feature = "deeds", power = "bleeding wound", by = ["dance-of-dawn"] },
  { replaces = "Deadly stab", feature = "deeds", power = "deadly stab", by = ["dance-of-mercy"] },
  { alters = "Swashbuckler finesse", feature = "swashbuckler-finesse", by = ["dervish-finesse"] },
  { alters = "Panache", feature = "panache", by = ["dawnflower-s-mercy"] },
]
+++

In Qadira and throughout the Padishah Empire, [Sarenrae's](ref/faith/sarenrae) worshipers praise the
Dawnflower through dance. Her more warlike followers adapted these dances into graceful martial
forms, and their swashbuckling style is feared throughout the Inner Sea region and beyond for its
ability to devastate foes with a scimitar through motion and agility regardless of strength of arms.

## Dervish Finesse (Ex) {#dervish-finesse}

A whirling dervish can treat a [scimitar](ref/eq-weapon/scimitar) as a one-handed piercing melee
weapon for the purposes of the swashbuckler's finesse and all feats and class abilities that refer
to such a weapon. She must not be carrying a weapon or shield in her off hand to gain this benefit.
This ability alters swashbuckler finesse.

## Dawnflower's Mercy (Ex) {#dawnflower-s-mercy}

While violence is sometimes necessary to cleanse evil, Sarenrae's desire for redemption prevents her
dervishes from reveling in a foe's defeat. A whirling dervish does not gain any panache for dropping
a foe below 0 hit points unless that foe is an evil outsider or undead, or if the damage she dealt
was nonlethal. Additionally, she gains 1 panache point if she causes an evildoer with a number of
Hit Dice equal to at least 1/2 her character level to surrender to her. She can gain this benefit no
more than once per round, even if multiple enemies surrender. This ability alters panache.

## Dervish Dance (Ex) {#dervish-dance}

At 4th level, a whirling dervish can use her Dexterity modifier instead of her Strength modifier on
melee damage rolls when using her swashbuckler finesse. She counts as having the
[Dervish Dance](ref/feat/dervish-dance) feat for purposes of meeting feat prerequisites.

## Deeds {#deeds}

A whirling dervish gains the following deeds.

## Whirlwind Dance (Ex) {#whirlwind-dance}

At 7th level, a whirling dervish can sweep through her opponents' lines like a cyclone. As a
full-round action, she can spend 1 panache point to move up to her speed. She can make attacks
against creatures with her reach during this movement, up to the number of attacks she's entitled to
with a full attack. Each attack is made at her highest attack bonus, and must target a different
creature. This movement provokes attacks of opportunity as normal. This deed replaces superior feint
and targeted strike.

## Dance of Dawn (Ex) {#dance-of-dawn}

At 11th level, whenever a whirling dervish is in conditions of
[dim light](ref/rule/vision-and-light) or brighter and hits with a melee attack, she can spend 1
panache point to reflect the light off her blade into the eyes of her target. That opponent is
[blinded](ref/misc/blinded) for 1 round. A successful Fortitude save (DC = 10 + 1/2 the whirling
dervish's class level + her Dexterity modifier) negates this effect. This deed replaces bleeding
wound.

## Dance of Mercy (Ex) {#dance-of-mercy}

At 19th level, when a whirling dervish confirms a critical hit with a light or one-handed piercing
melee weapon, in addition to the normal damage, she can spend 1 panache point to inflict a deadly
stab. The target must succeed at a Fortitude saving throw (DC = 10 + 1/2 the dervish's class level +
her Dexterity modifier) or take an amount of nonlethal damage equal to its current hit points + 1,
as well as becomes [paralyzed](ref/rule/paralyzed) for 1 hour. Performing this deed doesn't grant
the swashbuckler a panache point. This deed replaces deadly stab.
