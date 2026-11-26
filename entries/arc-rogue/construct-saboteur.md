+++
id = "ref/arc-rogue/construct-saboteur"
kind = "archetype"
title = "Construct Saboteur"
aon = "ArchetypeDisplay.aspx?FixedName=Rogue%20Construct%20Saboteur"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "construct_saboteur", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]
[[sources]]
publication = "construct-handbook"
page = "12"

[fields]
kind = "archetype"
features = [
  { anchor = "arcane-strike", level = 1 },
  { anchor = "arcane-sabotage", level = 2 },
  { anchor = "dismantling-strikes", level = 3 },
]
trades = [
  { replaces = "Trapfinding", feature = "trapfinding", by = ["arcane-strike"] },
  { replaces = "Rogue talent gained at 2nd level", feature = "rogue-talents", levels = [2], by = ["arcane-sabotage"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["dismantling-strikes"] },
  { alters = "Class skills" },
]
+++

The construct saboteur harnesses arcane energy to combat the golems and eldritch guardians that
prowl the depths of ancient ruins and forgotten tombs.

## Class Skills {#class-skills}

A construct saboteur has Knowledge (arcana) and Knowledge (engineering) but does not have Knowledge
(dungeoneering) and Knowledge (local) as class skills.

This alters the rogue's class skills.

## Arcane Strike (Ex) {#arcane-strike}

A construct saboteur gains [Arcane Strike](ref/feat/arcane-strike) as a bonus feat, even if she does
not meet the prerequisites. She uses her construct saboteur class level in place of her caster level
for the purposes of the feat's effects.

This replaces trapfinding.

## Arcane Sabotage (Su) {#arcane-sabotage}

At 2nd level, a construct saboteur can use her arcane prowess to hinder constructs. Whenever she
uses Arcane Strike to attack a construct, she can activate one of the following sabotage abilities
that she has gained. She gains one sabotage ability at 2nd level and can thereafter select any
sabotage ability in place of a rogue talent. The DC for any sabotage ability that requires a saving
throw is 10 + half the construct saboteur's level + the construct saboteur's Intelligence modifier.

### Diminish Senses {#diminish-senses}

A jolt of energy overwhelms the construct's senses. The construct is [blinded](ref/misc/blinded) for
1 round. A construct saboteur can forgo dealing sneak attack damage to extend the duration of the
blindness by 1 round for every 2d6 points of sneak attack damage forgone in this way. A construct
can negate this effect with a successful Will save.

### Magic Vulnerability {#magic-vulnerability}

A field of energy enshrouds the construct, disabling its immunity to magic for 1 round. The
construct instead gains [spell resistance](ref/rule/spell-resistance) equal to 15 + its CR. A
construct saboteur can forgo dealing sneak attack damage to reduce this spell resistance. The
construct's spell resistance is reduced by 1 for every 1d6 points of sneak attack damage forgone in
this way. A construct can negate this effect with a successful Will save.

### Overwhelming Jolt {#overwhelming-jolt}

A sudden burst of power moves over the surface of the construct, giving it the
[staggered](ref/misc/staggered) condition for 1 round. A construct can negate this effect with a
successful Will save.

### Slowing Pulse {#slowing-pulse}

A surge of slowing energy ripples through the construct, reducing its speed by 5 feet for a number
of rounds equal to the construct saboteur's Intelligence modifier. A construct saboteur can forgo
dealing sneak attack damage to reduce the construct's speed by an additional 5 feet for every 1d6
points of sneak attack damage forgone in this way. This ability cannot lower a construct's movement
speed below 5 feet. A construct can reduce the duration of this effect to 1 round with a successful
Reflex save.

This replaces the rogue talent gained at 2nd level.

## Dismantling Strikes (Ex) {#dismantling-strikes}

At 3rd level, a construct saboteur ignores the first 2 points of DR or [hardness](ref/umr/hardness)
when attacking constructs. This value increases by 2 every 3 levels after 3rd, to a total of 12
points of DR or hardness ignored at level 18.

This replaces trap sense.
