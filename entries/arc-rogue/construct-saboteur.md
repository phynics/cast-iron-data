+++
id = "ref/arc-rogue/construct-saboteur"
kind = "archetype"
title = "Construct Saboteur"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "construct_saboteur", path = "json/archetypes_rogue.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/rogue" },
]

[fields]
kind = "archetype"
replaces = ["Trapfinding", "Rogue talent gained at 2nd level", "Trap sense"]
+++

**Sources:** Construct Handbook pg 12\
The construct saboteur harnesses arcane energy to combat the golems and eldritch guardians that
prowl the depths of ancient ruins and forgotten tombs.

**Gained class skills:** ka, ke

**Lost class skills:** kd, kl

**Arcane Strike (Ex)**

**Ability:** A construct saboteur gains [Arcane Strike](ref/feat/arcane-strike) as a bonus feat,
even if she does not meet the prerequisites. She uses her construct saboteur class level in place of
her caster level for the purposes of the feat's effects.

**Replaces:** Trapfinding

**Arcane Sabotage (Su)**

**Ability:** She gains one sabotage ability (listed below). Whenever she uses Arcane Strike to
attack a construct, she can activate one of her sabotage abilities that she has gained.

**Flavor:** A construct saboteur can user her arcane prowess to hinder constructs.

**At 4th Level:** From here on out, she can select any sabotage ability in place of a rogue talent.

**Gained:** At 2nd Level

**Replaces:** Rogue talent gained at 2nd level

**Special:** The DC for any sabotage ability that requires a saving throw is 10 + half the construct
saboteur's level + the construct saboteur's Intelligence modifier.

**Diminish Senses**

**Ability:** A jolt of energy overwhelms the construct's senses. The construct is
[blinded](ref/misc/blinded) for 1 round. A construct saboteur can forgo dealing sneak attack damage
to extend the duration of the blindness by 1 round for every 2d6 points of sneak attack damage
forgone in this way. A construct can negate this effect with a successful Will save.

**Magic Vulnerability**

**Ability:** A field of energy enshrouds the construct, disabling its immunity to magic for 1 round.
The construct instead gains [spell resistance](ref/rule/spell-resistance) equal to 15 + its CR. A
construct saboteur can forgo dealing sneak attack damage to reduce this spell resistance. The
construct's spell resistance is reduced by 1 for every 1d6 points of sneak attack damage forgone in
this way. A construct can negate this effect with a successful Will save.

**Overwhelming Jolt**

**Ability:** A sudden burst of power moves over the surface of the construct, giving it the
[staggered](ref/misc/staggered) condition for 1 round. A construct can negate this effect with a
successful Will save.

**Slowing Pulse**

**Ability:** A surge of slowing energy ripples through the construct, reducing its speed by 5 feet
for a number of rounds equal to the construct saboteur's Intelligence modifier. A construct saboteur
can forgo dealing sneak attack damage to reduce the construct's speed by an additional 5 feet for
every 1d6 points of sneak attack damage forgone in this way. This ability cannot lower a construct's
movement speed below 5 feet. A construct can reduce the duration of this effect to 1 round with a
successful Reflex save.

**Dismantling Strikes (Ex)**

**At 3rd Level:** A construct saboteur ignores the first 2 points of DR or
[hardness](ref/umr/hardness) when attacking constructs.

**Replaces:** Trap sense

At 6th level: The amount of DR ignored 4.

At 9th level: The amount of DR ignored 6.

At 12th level: The amount of DR ignored 8.

At 15th level: The amount of DR ignored 10.

At 18th level: The amount of DR ignored 12.
