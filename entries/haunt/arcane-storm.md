+++
id = "ref/haunt/arcane-storm"
kind = "rule"
title = "Arcane Storm"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "arcane_storm", path = "json/haunts.json" },
]
[[sources]]
publication = "horror-adventures"
page = "174"

[fields]
kind = "none"
+++

Each spell, no matter how weak, leaves its signature on the world for a short time, which
spellcasters can perceive as a lingering magical aura. When dozens of powerful spells are hurled
against each other over a small area, reality itself can form scars that affect all who come near
them.

Magical scars have auras and count as ongoing spell effects for the purposes of
[detect magic](ref/spell/detect-magic) and similar spells. A successful Spellcraft check to identify
a scar reveals its effect and its weakness, and, if it succeeds by 10 or more, the scar's benefit. A
creature can't attempt to activate a benefit it hasn't identified. Spells that automatically reveal
the nature of magical effects, such as [greater arcane sight](ref/spell/arcane-sight-greater),
automatically reveal all of these properties. The destruction conditions for magical scars are more
obscure, and require research or exploration to uncover.

The arcane storm haunt arose when a pair of evokers dueled to the death centuries ago. An echo of
the duel still rages at the site of their battle, and the charred ground tells the bitter tale.

**Arcane Storm**

**Challenge rating:** 6

**XP** 2,400\
N persistent variant haunt (30-ft. radius)\
**Aura** faint evocation\
**Caster Level** 5th

**Notice:** Perception or Spellcraft DC 20 (to hear the sound of clashing energy or deduce the
effect from the charred ground)

**Hit points:** 27

**Weakness:** energy damage (immune to positive energy)

**Trigger:** proximity

**Reset:** 1 day

### Effect

Each round, the arcane storm fires a bolt of energy to hit as many creatures as possible in its area
(Reflex DC 15 halves). This functions as per [lightning bolt](ref/spell/lightning-bolt), except the
energy type cycles between acid, cold, electricity, and fire. The storm is immune to the most recent
type of energy damage it has dealt.

### Destruction

The arcane storm is destroyed if a character successfully [counterspells](ref/rule/counterspells)
four of its bolts in a row.
