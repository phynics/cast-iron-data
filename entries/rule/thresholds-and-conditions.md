+++
id = "ref/rule/thresholds-and-conditions"
kind = "rule"
title = "Thresholds and Conditions"
source_ids = ["pathfinder-unchained"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thresholds_and_conditions", path = "json/rules_opt_combat01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Pathfinder Unchained pg 136

This rules variant uses three special conditions that apply automatically when a character reaches
the corresponding wound thresholds: grazed, wounded, and critical. These conditions are not
cumulative - only the most severe one applies at a given time. The disabled and staggered conditions
have the same effects as in the core rules, but apply to a wider range of hit point totals, as
described below. Unlike grazed, wounded, and critical, the disabled and staggered conditions stack,
so a character who is disabled or staggered is still critical as well.

### Healthy

A character above her grazed threshold (3/4 of her maximum hit points) is healthy, applying no
special modifiers. The character doesn't gain a condition in this state.

### Grazed

A character above her wounded threshold (1/2 of her maximum hit points) but at or below 3/4 of her
maximum hit points is grazed. She takes a -1 penalty on all attack rolls, saving throws, skill
checks, and ability checks, as well as to AC and caster level.

### Wounded

A character above her critical threshold (1/4 of her maximum hit points) but at or below 1/2 of her
maximum hit points is wounded. She takes a -2 penalty on all attack rolls, saving throws, skill
checks, and ability checks, as well as to AC and caster level.

### Critical

A character at or below 1/4 of her maximum hit points is in critical condition. She takes a -3
penalty on all attack rolls, saving throws, skill checks, and ability checks, as well as to AC and
caster level.

### Disabled

A character with a Constitution score of 12 or higher who is at or below 0 hit points is disabled
until she falls below a number of hit points equal to the negative of her Constitution modifier. For
example, a character with a Constitution score of 18 would be disabled from 0 to -4 hit points and
unconscious at -5 hit points. A character with a Constitution score of 11 or lower is disabled only
while she has exactly 0 hit points.

### Staggered

Instead of being staggered only when their amount of nonlethal damage equals their remaining hit
points, characters using this system continue to be staggered from that point until their nonlethal
damage exceeds their current hit points by an amount greater than their Constitution bonus, at which
point they fall unconscious. A character with a Constitution score of 11 or lower is staggered only
when her nonlethal damage exactly equals her current hit point total.

### Caster Level Penalties

The penalty to caster level from the grazed, wounded, or critical condition can make it so an
injured spellcaster is unable to cast the highest levels of spells she would normally be able to.
However, it doesn't cause her to lose any prepared spells or spell slots. The penalty to caster
level also reduces her bonus on [concentration](ref/rule/concentration) checks and lowers the range,
duration, and effectiveness of her spells. The penalty can't make her effective caster level lower
than 1.
