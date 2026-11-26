+++
id = "ref/arc-investigator/dread-investigator"
kind = "archetype"
title = "Dread Investigator"
aon = "ArchetypeDisplay.aspx?FixedName=Investigator%20Dread%20Investigator"
source_ids = ["cohorts-and-companions"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "dread_investigator", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]
[[sources]]
publication = "cohorts-and-companions"
page = "14"

[fields]
kind = "archetype"
features = [
  { anchor = "delayed-inspiration", level = 1 },
  { anchor = "embalming-fluids" },
  { anchor = "negative-energy-resistance", level = 2 },
  { anchor = "investigator-talent" },
  { anchor = "reanimation-fluid", level = 7 },
]
trades = [
  { replaces = "Poison lore", feature = "poison-lore", by = ["embalming-fluids"] },
  { replaces = "Poison resistance", feature = "poison-resistance", levels = [2, 5, 8], by = ["negative-energy-resistance"] },
  { replaces = "immunity", feature = "poison-resistance", levels = [11], by = ["negative-energy-resistance"] },
  { replaces = "Investigator talents gained at 7th, 13th, and 19th level", feature = "investigator-talent", levels = [7, 13, 19], by = ["reanimation-fluid"] },
  { alters = "Inspiration", feature = "inspiration", by = ["delayed-inspiration"] },
  { alters = "studied combat", feature = "studied-combat", by = ["delayed-inspiration"] },
  { alters = "studied strike", feature = "studied-strike", by = ["delayed-inspiration"] },
]
+++

The dread investigator observes human behavior after the fact, honing their intuition by delving
into the mysteries of death. They breach sealed tombs to recover research material rather than
riches. Many join—or found—cults dedicated to [Urgathoa](ref/faith/urgathoa), while others are
simply researchers or Osirionologists who must become accustomed to undeath to pursue their work.

## Delayed Inspiration {#delayed-inspiration}

A dread investigator gains inspiration at 4th level instead of 1st and gains studied combat and
studied strike at 7th level instead of 4th. A dread investigator's studied strike deals 1d6 fewer
points of damage than normal. This alters inspiration, studied combat, and studied strike.

## Embalming Fluids (Ex) {#embalming-fluids}

A dread investigator adds the following spells to his class list of extracts: 1st—_hide from
undead_, _sanctify corpse_; 2nd—_gentle repose_, _lesser animate dead_; 3rd—_animate dead_, _speak
with dead_; 4th—_rest eternal_. A dread investigator can use these extracts to affect dead bodies as
if using the [infusion](ref/discovery/infusion) discovery to affect another creature. This ability
replaces poison lore.

## Negative Energy Resistance (Ex) {#negative-energy-resistance}

At 2nd level, a dread investigator gains a +2 bonus on saving throws against death effects,
[energy drain](ref/rule/energy-drain-and-negative-levels), and negative energy. This bonus increases
to +4 at 5th level and +6 at 8th level. At 11th level, effects created by undead that inflict
[ability drain, ability damage](ref/rule/ability-damage-drain), or energy drain have only half their
normal effect on a dread investigator (minimum 1 point of ability damage or ability drain, or 1
negative level). This ability replaces poison resistance and immunity.

## Investigator Talent {#investigator-talent}

When a dread investigator selects the [alchemical discovery](ref/invtalent/alchemist-discovery)
talent, he can select from the following additional discoveries:
[alchemical zombie](ref/discovery/alchemical-zombie), [mummification](ref/discovery/mummification),
or [preserve organs](ref/discovery/preserve-organs).

## Reanimation Fluid (Ex) {#reanimation-fluid}

At 7th level, a dread investigator adds _[undead anatomy I](ref/spell/undead-anatomy-1)_ to his
formula book, and he can share this extract with an unconscious creature as if he had the infusion
discovery. If the creature is dying when it receives the infusion, it stabilizes and gains
[temporary hit points](ref/rule/temporary-hit-points) equal to twice the dread investigator's level.
Rather than having the extract take effect immediately, the dread investigator may choose for the
extract to remain latent for up to 10 minutes per level. He can trigger the extract's effect at any
point by touching the creature as a standard action, and it automatically triggers if the creature
using it is reduced to 0 or fewer hit points. The dread investigator can also amplify the effect of
the extract, allowing it to function as _[undead anatomy II](ref/spell/undead-anatomy-2)_, but this
reduces the extract's duration to 1 round per level and at the end of its duration the creature
using the extract is reduced to -1 hit points.

At 13th level, a dread investigator adds _[undead anatomy II](ref/spell/undead-anatomy-2)_ to his
formula book, and at 19th level _[undead anatomy III](ref/spell/undead-anatomy-3)_, which he can use
in the same way, including amplifying the effect of the extract to the next-higher-level undead
anatomy spell. This ability replaces the investigator talents gained at 7th, 13th, and 19th level.
