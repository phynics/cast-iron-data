+++
id = "ref/arc-investigator/toxin-codexer"
kind = "archetype"
title = "Toxin Codexer"
source_ids = ["potions-and-poisons"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "toxin_codexer", path = "json/archetypes_investigator.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/investigator" },
]

[fields]
kind = "none"
+++

**Sources:** Potions and Poisons pg 14\
While most investigators are well versed in the knowledge of poisons, the toxin codexer has made it
a way of life. He meticulously seeks out new poisons and catalogs their effects, both those that are
harmful and those that are potentially beneficial. A toxin codexer's detailed understanding of how
his toxins work allows him to blend them with exact precision, creating even more deadly venoms or
providing painful medicines for those in need.

**Poison Lore (Ex)**

**Ability:** A toxin codexer gains the _poison lore_ ability at 1st level. This ability is otherwise
identical to the investigator's _poison lore_ class feature.

**Alters:** Poison lore

**Gained:** At 1st Level

**Synthetic Venom (Ex)**

**Action:** Ability

**Alters:** Alchemy and replaces, trapfinding, investigator talent gained at 3rd level

When a toxin codexer prepares his extracts, he can use his slots to prepare short-lived poisons
instead of extracts. The following poisons can be prepared into extract slots:

**1st:** arsenic, giant wasp poison, medium spider venom

**2nd:** black adder venom, id moss, striped toadstool

**3rd:** blue whinnis, lich dust, sassone leaf residue

**4th:** dark reaver powder, purple worm poison, third eye

**5th:** deathblade, hemlock, witch hunter's sword

**6th:** black lotus extract, dragon bile, king's sleep

Additional poison selections can be added to this list with GM approval.

The Fortitude save DC of these poisons is 10 + the toxin codexer's Intelligence modifier + the
extract level of the poison. Poisons created in this way are unstable and become inert after 1 day
if not used. Once the poison is administered to a target, the duration is as normal for that
poison's type, even if longer than 1 day. These poisons can be applied to weapons (if applicable)
only by the toxin codexer, unless he has the [infusion](ref/discovery/infusion) alchemist discovery.

**Modify Toxin (Ex)**

**Action:** Ability

**Gained:** At 3rd Level

**Replaces:** Keen recollection, trap sense

A toxin codexer learns to unlock both the beneficial and detrimental side effects of his poisons.
These effects apply even if the target succeeds at her save against the poison, but they still count
as poison effects. A modified toxin becomes inert if not used within 1 hour.

As a **move action**, the toxin codexer can expend one use of _inspiration_ to apply one of the
following effects to a poison in his possession, choosing either the benefit or the detriment when
an effect has both options. These effects last for a number of rounds equal to the investigator's
Intelligence modifier unless otherwise stated.

- Grant a +2 alchemical bonus or impose a -2 alchemical penalty on saving throws against
  [exhaustion](ref/misc/exhausted), [fatigue](ref/misc/fatigued), and sleep effects.
- Grant a +4 alchemical bonus or impose a -4 alchemical penalty on saving throws against effects
  with the pain descriptor.

At 6th level, the toxin codexer can also choose from the following effects:

- Affect a target so the first time she takes damage each round, she takes an additional 1d6 points
  of nonlethal damage. This is a pain effect.
- Inflict or remove the fatigued condition.

At 9th level, the toxin codexer can also choose from the following effects:

- Deal 1 point of [bleed](ref/rule/bleed) damage or cure any ongoing bleed effects.
- Cure one disease or poison whose save DC does not exceed that of the modified poison. This has no
  effect on magical curses, diseases, or poisons.

At 12th level, the toxin codexer can also choose from the following effects:

- Cure one magical disease or poison whose save DC does not exceed that of the modified poison.
- Bestow a 30% spell failure chance on a target.
