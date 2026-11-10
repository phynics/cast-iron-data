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
replaces = ["Poison lore", "Poison resistance", "immunity", "Investigator talents gained at 7th, 13th, and 19th level"]
alters = ["Inspiration", "studied combat", "studied strike"]
+++

The dread investigator observes human behavior after the fact, honing their intuition by delving
into the mysteries of death. They breach sealed tombs to recover research material rather than
riches. Many join - or found - cults dedicated to [Urgathoa](ref/faith/urgathoa), while others are
simply researchers or Osirionologists who must become accustomed to undeath to pursue their work.

**Delayed Inspiration**

**Alters:** Inspiration, studied combat, studied strike

**At 1st Level:** A dread investigator gains _inspiration_ at 4th level instead of 1st.

**At 7th Level:** He gains _studied combat_ and _studied strike_ at 7th level instead of 4th. A
dread investigator's _studied strike_ deals 1d6 fewer points of damage than normal.

**Embalming Fluids (Ex)**

**Info:** A dread investigator adds the following spells to his class list of extracts.

**Replaces:** Poison lore

**Spells:** Hide from undead, sanctify corpse

**Spells:** Gentle repose, lesser animate dead

**Spells:** Animate dead, speak with dead

**Spells:** Rest eternal

**Special:** A dread investigator can use these extracts to affect dead bodies as if using the
[infusion](ref/discovery/infusion) discovery to affect another creature.

**Negative Energy Resistance (Ex)**

**At 11th Level:** Effects created by undead that inflict
[ability drain, ability damage](ref/rule/ability-damage-drain), or energy drain have only half their
normal effect on a dread investigator (minimum 1 point of ability damage or ability drain, or 1
negative level).

**At 5th Level:** This bonus increases to +4.

**At 8th Level:** This bonus becomes +6.

**Gained:** At 2nd Level

**Passive:** A dread investigator gains a +2 bonus on saving throws against death effects,
[energy drain](ref/rule/energy-drain-and-negative-levels), and negative energy.

**Replaces:** Poison resistance, immunity

**Investigator Talent**

**Ability:** When a dread investigator selects the
[alchemist discovery](ref/invtalent/alchemist-discovery) talent, he can select from the following
additional discoveries: [alchemical zombie](ref/discovery/alchemical-zombie),
[mummification](ref/discovery/mummification), or [preserve organs](ref/discovery/preserve-organs).

**Reanimation Fluid (Ex)**

**Ability:** A dread investigator adds [undead anatomy I](ref/spell/undead-anatomy-1) to his formula
book, and he can share this extract with an unconscious creature as if he had the _infusion_
discovery. If the creature is dying when it receives the infusion, it stabilizes and gains
[temporary hit points](ref/rule/temporary-hit-points) equal to twice the dread investigator's level.
Rather than having the extract take effect immediately, the dread investigator may choose for the
extract to remain latent for up to 10 minutes per level. He can trigger the extract's effect at any
point by touching the creature as a **standard action**, and it automatically triggers if the
creature using it is reduced to 0 or fewer hit points. The dread investigator can also amplify the
effect of the extract, allowing it to function as [undead anatomy II](ref/spell/undead-anatomy-2),
but this reduces the extract's duration to 1 round per level and at the end of its duration the
creature using the extract is reduced to -1 hit points.

**At 13th Level:** A dread investigator adds _[undead anatomy II](ref/spell/undead-anatomy-2)_ to
his formula book.

**At 19th Level:** He adds [undead anatomy III](ref/spell/undead-anatomy-3), which he can use in the
same way, including amplifying the effect of the extract to the next-higher-level _undead anatomy_
spell.

**Gained:** At 7th Level

**Replaces:** Investigator talents gained at 7th, 13th, and 19th level
