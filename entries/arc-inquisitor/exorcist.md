+++
id = "ref/arc-inquisitor/exorcist"
kind = "archetype"
title = "Exorcist"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "exorcist", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-magic"
page = "44"

[fields]
kind = "archetype"
replaces = ["Second judgment", "Third judgment", "Slayer", "True judgment"]
replaces_features = ["second-judgment", "third-judgment", "slayer", "true-judgment"]
+++

Some inquisitors, as they learn more about the threat of possession and the machinations of the
planes, task themselves to expel possessing spirits and conniving outsiders from the world whenever
possible. Eventually they learn the secret of the _verdicts of exorcism, exile,_ and _anathema._

**Verdict of Exorcism (Su)**

**Ability:** An inquisitor using _judgment_ can unleash the _verdict of exorcism_ on a creature.
When she does, her judgment ends, but the creature is [dazed](ref/misc/dazed) for 1 round (Will
negates); if the creature is possessed, the possessing entity must succeed at a Will saving throw
(DC 10 + 1/2 inquisitor level + inquisitor's Wisdom bonus), or be exorcised and never again allowed
in that same body.

**Gained:** At 8th Level

**Replaces:** Second judgment

**Verdict of Exile (Su)**

**Ability:** An inquisitor using _judgment_ can unleash the _verdict of exile_ on a creature. When
she does, her judgment ends, but the creature subject to that judgment is dazed for 1 round (Will
negates, DC of 10 + 1/2 inquisitor level + Wisdom bonus). If the creature is possessed or an
outsider, the possessing entity or the outsider is affected by [dismissal](ref/spell/dismissal)
(Will negates).

**Gained:** At 16th Level

**Replaces:** Third judgment

**Closed Mind (Su)**

**Flavor:** An exorcist inquisitor must close off her mind to deny her enemies even a foothold.

**Gained:** At 17th Level

**Passive:** The inquisitor becomes immune to compulsion effects and possession attempts (including
[magic jar](ref/spell/magic-jar)).

**Replaces:** Slayer

**Verdict of Anathema (Su)**

**Ability:** An inquisitor using _judgment_ can unleash the _verdict of anathema_ on her enemies.
When she does, her judgment ends, and all enemy creatures within 10 feet are affected by her
_verdict of exorcism._

**Gained:** At 20th Level

**Replaces:** True judgment
