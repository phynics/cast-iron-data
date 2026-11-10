+++
id = "ref/arc-inquisitor/faith-hunter"
kind = "archetype"
title = "Faith Hunter"
source_ids = ["ultimate-intrigue"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "faith_hunter", path = "json/archetypes_inquisitor.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/inquisitor" },
]
[[sources]]
publication = "ultimate-intrigue"
page = "28"

[fields]
kind = "archetype"
replaces = ["Domain", "justice and destruction judgments", "Detect alignment"]
alters = ["Judgment", "Bane"]
replaces_features = ["domain", "detect-alignment"]
alters_features = ["judgment", "bane"]
+++

Certain relentless inquisitors burn with special hatred for an enemy of specific convictions, and
they stop at nothing when obsessively hunting these foes down.

**Sworn Enemy (Sp, Su)**

**Ability:** She can detect creatures of the chosen alignment at will, functioning as
[detect evil](ref/spell/detect-evil), except this ability works only on creatures and detects the
specific alignment.

**Alters:** Judgment

**Choice:** A faith hunter chooses a single alignment (such as chaotic evil, rather than simply
chaotic or evil) that directly opposes her own along either the law/chaos axis or the good/evil axis
(so a lawful good faith hunter can choose chaotic good, chaotic neutral, chaotic evil, neutral evil,
or lawful evil, whereas a neutral good faith hunter can only choose chaotic evil, neutral evil, or
lawful evil). Creatures of this alignment are her **sworn enemies.**

**At 6th Level:** Once per day as a **swift action**, a faith hunter can smite one foe she can see.
If the foe is of the faith hunter's _sworn enemy_ alignment, the faith hunter gains a +4 sacred
bonus on attack rolls against that foe and a sacred bonus equal to half her inquisitor level on
damage rolls made against the foe. Smites against targets of the faith hunter's _sworn enemy_
alignment automatically bypass any DR the creature might possess. If the faith hunter targets a
creature that is not of her _sworn enemy_ alignment, the smite is wasted with no effect.

**Replaces:** Domain, justice and destruction judgments

**Special:** The smite effect remains until the foe is dead or the next time the faith hunter rests
and regains her uses of this ability. At 10th level and every 4 inquisitor levels thereafter, a
faith hunter can smite her enemies one additional time per day, to a maximum of four times per day
at 18th level. A faith hunter does not gain the justice or destruction judgments.

At 10th level: A faith hunter can now smite 2 times a day.

At 14th level: A faith hunter can now smite 3 times a day.

At 18th level: A faith hunter can now smite 4 times a day.

**Enemy Revealed (Su)**

**Ability:** When a faith hunter uses her _sworn enemy_ ability to identify a creature's alignment
(typically on the third round of concentrating on an area including the creature), she can reveal
that creature's alignment aura, causing it to glow for 1 round per inquisitor level so that even
creatures with regular vision can see the aura. This not only allows others to recognize the
creature's alignment, potentially exposing its true nature, it also allows them to track its
location easily by the glow. Even if such a creature is invisible, the telltale glow pinpoints the
creature's square or squares.

**Gained:** At 2nd Level

**Replaces:** Detect alignment

**Special:** This doesn't take any extra action on her part; this ability is part of the same action
as concentrating on her _sworn enemy_ detect ability.

**Usage:** Wisdom modifier times/day

**Hateful Bane (Su)**

**Alters:** Bane

**Gained:** At 5th Level

**Passive:** A faith hunter's _[bane](ref/spell/bane)_ ability functions only against creatures that
are both the selected creature type and her _sworn enemy_ alignment.
