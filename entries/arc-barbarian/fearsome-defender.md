+++
id = "ref/arc-barbarian/fearsome-defender"
kind = "archetype"
title = "Fearsome Defender"
aon = "ArchetypeDisplay.aspx?FixedName=Barbarian%20Fearsome%20Defender"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "fearsome_defender", path = "json/archetypes_barbarian.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/barbarian" },
]
[[sources]]
publication = "horror-adventures"
page = "47"

[fields]
kind = "archetype"
features = [
  { anchor = "intractable", level = 1 },
  { anchor = "off-the-leash", level = 2 },
  { anchor = "silent-threat", level = 3 },
  { anchor = "bloodlust", level = 5 },
]
trades = [
  { replaces = "Fast movement", feature = "fast-movement", by = ["intractable"] },
  { replaces = "Uncanny dodge", feature = "uncanny-dodge", by = ["off-the-leash"] },
  { replaces = "Trap sense", feature = "trap-sense", by = ["silent-threat"] },
  { replaces = "Improved uncanny dodge", feature = "improved-uncanny-dodge", by = ["bloodlust"] },
]
+++

Dark overlords frequently recruit their most bloodthirsty followers to serve as brutal bodyguards.
These savage slaves feel little pain and exist only to rain terror down on the enemies of their
pitiless masters.

## Intractable (Ex) {#intractable}

A combination of brainwashing and loyalty helps a fearsome defender resist pain and torture,
enduring grueling combat or questioning without betraying her dark lord. A fearsome defender gains a
+2 bonus on saving throws against pain effects, and the DCs of checks to coerce her or demoralize
her with Diplomacy or Intimidate increase by 2. Both the bonus and the increase to DCs increase by 2
when she gains greater rage and again by 2 when she gains mighty rage.

This ability replaces fast movement.

## Off the Leash (Ex) {#off-the-leash}

Beginning at 2nd level, a fearsome defender simmers on the edge of bloody combat. Whenever she
begins a rage, she can also draw an unconcealed weapon as part of the free action to begin raging.

This ability replaces uncanny dodge.

## Silent Threat (Ex) {#silent-threat}

At 3rd level, a fearsome defender exudes hostility, creating a threatening atmosphere in her
presence. The fearsome defender gains a +1 bonus on Intimidate checks, and the DCs of Intimidate
checks to demoralize her allies within 30 feet increase by 1. Both the bonus and the increase to DCs
increase by 1 at 6th level and every 3 barbarian levels thereafter.

This ability replaces trap sense.

## Bloodlust (Ex) {#bloodlust}

At 5th level, a fearsome defender's eagerness for bloodshed makes her quicker to act in a fight. She
adds her Charisma modifier to initiative checks and always acts during the surprise round. If the
fearsome defender is surprised during the surprise round, she acts last in that round and then
determines initiative order normally for the remainder of combat.

This ability replaces improved uncanny dodge.
