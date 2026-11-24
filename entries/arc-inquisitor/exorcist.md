+++
id = "ref/arc-inquisitor/exorcist"
kind = "archetype"
title = "Exorcist"
aon = "ArchetypeDisplay.aspx?FixedName=Inquisitor%20Exorcist"
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
features = [
  { anchor = "verdict-of-exorcism", level = 8 },
  { anchor = "verdict-of-exile", level = 16 },
  { anchor = "closed-mind", level = 17 },
  { anchor = "verdict-of-anathema", level = 20 },
]
trades = [
  { replaces = "Second judgment", feature = "second-judgment", by = ["verdict-of-exorcism"] },
  { replaces = "Third judgment", feature = "third-judgment", by = ["verdict-of-exile"] },
  { replaces = "Slayer", feature = "slayer", by = ["closed-mind"] },
  { replaces = "True judgment", feature = "true-judgment", by = ["verdict-of-anathema"] },
]
+++

Some inquisitors, as they learn more about the threat of possession and the machinations of the
planes, task themselves to expel possessing spirits and conniving outsiders from the world whenever
possible. Eventually they learn the secret of the _verdicts of exorcism, exile,_ and _anathema._

## Verdict of Exorcism (Su) {#verdict-of-exorcism}

At 8th level, an inquisitor using judgment can unleash the verdict of exorcism on a creature. When
she does, her judgment ends, but the creature is [dazed](ref/misc/dazed) for 1 round (Will negates);
if the creature is possessed, the possessing entity must succeed at a Will saving throw (DC 10 + 1/2
inquisitor level + inquisitor's Wisdom bonus), or be exorcised and never again allowed in that same
body. This ability replaces second judgment.

## Verdict of Exile (Su) {#verdict-of-exile}

At 16th level, an inquisitor using judgment can unleash the verdict of exile on a creature. When she
does, her judgment ends, but the creature subject to that judgment is dazed for 1 round (Will
negates, DC of 10 + 1/2 inquisitor level + Wisdom bonus). If the creature is possessed or an
outsider, the possessing entity or the outsider is affected by _[dismissal](ref/spell/dismissal)_
(Will negates). This ability replaces third judgment.

## Closed Mind (Su) {#closed-mind}

An exorcist inquisitor must close off her mind to deny her enemies even a foothold. At 17th level,
the inquisitor becomes immune to compulsion effects and possession attempts (including
_[magic jar](ref/spell/magic-jar)_). This ability replaces slayer.

## Verdict of Anathema (Su) {#verdict-of-anathema}

At 20th level, an inquisitor using judgment can unleash the verdict of anathema on her enemies. When
she does, her judgment ends, and all enemy creatures within 10 feet are affected by her verdict of
exorcism. This ability replaces true judgment.
