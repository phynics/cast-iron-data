+++
id = "ref/arc-kineticist/psammokinetic"
kind = "archetype"
title = "Psammokinetic"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Psammokinetic"
source_ids = ["heroes-from-the-fringe"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "psammokinetic", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "heroes-from-the-fringe"
page = "6"

[fields]
kind = "archetype"
replaces = ["Elemental overflow"]
alters = ["Elemental focus", "Expanded element"]
replaces_features = ["elemental-overflow"]
alters_features = ["elemental-focus", "expanded-element"]
+++

Psammokinetics are ascetic kineticists who consider the harsh nature of the burning deserts of
Osirion to be a tempering fire that can purify all their imperfections. Trained by the Pahmet
dwarves, who also make up the majority of their numbers, these kineticists seek to master the powers
of sand and wind while focusing on self-improvement.

**Alignment**

**Info:** A psammokinetic kineticist must be lawful in alignment. If the psammokinetic ever becomes
nonlawful, she cannot gain any additional levels with this archetype and loses access to the _ki
pool_ class feature granted by this archetype.

**Burning Winds (Su)**

**Action:** ability

**Alters:** Elemental focus

**Special:** A psammokinetic cannot take the [chain](ref/kinetic/chain),
[magnetic infusion](ref/kinetic/magnetic-infusion), or
[thundering infusion](ref/kinetic/thundering-infusion) wild talents or the
[aerial adaptation](ref/kinetic/aerial-adaptation) or [celerity](ref/kinetic/celerity) utility wild
talents.

A psammokinetic must select air as her [elemental focus](ref/ability/elements). In place of the
[air blast](ref/kinetic/air-blast) and [electric blast](ref/kinetic/electric-blast) normally granted
to an aerokinetic, the psammokinetic gains a _sand blast_ or _sirocco blast._ Except as noted below,
_sand blast_ functions as _air blast,_ and _sirocco blast_ functions as _electric blast_ (including
when determining what infusion wild talents the psammokinetic can use with each blast). The
psammokinetic is also treated as having the fire element type for the purposes of meeting the
prerequisites for the [cold adaptation](ref/kinetic/cold-adaptation),
[flame shield](ref/kinetic/flame-shield), [heat adaptation](ref/kinetic/heat-adaptation), and
[heat wave](ref/kinetic/heat-wave) utility wild talents.

> **Sand Blast**\
> **Element** air; **Type** simple blast (Sp); **Level** -; **Burn** 0\
> **Blast Type** physical; **Damage** slashing\
> You slice at a single foe with a stream of sand.
>
> **Sirocco Blast**\
> **Element** air; **Type** simple blast (Sp); **Level** -; **Burn** 0\
> **Blast Type** energy; **Damage** fire\
> You shoot a wave of superheated air to burn a single foe.

**Ki Pool (Su)**

**Action:** Ability

**At 10th Level:** Her _sand blast_ is treated as a lawful weapon.

**At 16th Level:** Her _sand blast_ is treated as [adamantine](ref/eq-material/adamantine) for the
purpose of overcoming [damage reduction](ref/rule/damage-reduction) and bypassing
[hardness](ref/umr/hardness).

**At 7th Level:** As long as she has at least 1 point in her _ki pool,_ her _sand blast_ is treated
as cold iron for the purpose of overcoming [damage reduction](ref/rule/damage-reduction) (regardless
of what infusion it is used with).

**Gained:** At 3rd Level

**Replaces:** Elemental overflow

A psammokinetic gains a pool of ki points, supernatural energy she can use to accomplish amazing
feats. The number of points in a psammokinetic's _ki pool_ is equal to
[half](ref/misc/fractions-and-rounding) her kineticist level plus her Constitution modifier. As long
as she has at least 1 point in her _ki pool,_ she gains a bonus on damage rolls with kinetic blasts.
This bonus is equal to one-third of her kineticist level. The _kinetic blade_ infusion does not add
the bonus damage from this ability.

By spending 1 point from her _ki pool_ as a **swift action**, a psammokinetic can do one of the
following:

- Double her bonus (if any) on damage rolls for having at least 1 point in her _ki pool,_ and gain a
  bonus on attack rolls with her kinetic blasts. This bonus is equal to one-third of her kineticist
  level. This effect remains for 1d4 rounds.
- Gain a +2 dodge bonus to AC for 1 round.
- Increase her base speed by 20 feet for 1 round.

The _ki pool_ is replenished each morning after 8 hours of rest or meditation; these hours do not
need to be consecutive. If the psammokinetic has levels in another class that grants points to a
pool of ki points, her psammokinetic levels stack with the levels of that class to determine the
total number of ki points in the combined pool, but only one ability score modifier is added to the
total. The choice of which score to use is made when the second class ability is gained, and once
made, the choice cannot be changed. The psammokinetic can use ki points from this pool to power the
abilities of every class she has that grants a _ki pool._

**Sand Element (Su)**

**Alters:** Expanded element

**At 15th Level:** The psammokinetic must choose to expand her mastery of the air element as her
_expanded element._

**At 7th Level:** A psammokinetic must select the earth element as her _expanded element._ She
treats her kineticist level as 2 levels lower (rather than 4 levels lower) for the purpose of
determining which wild talents she can learn from the earth element.
