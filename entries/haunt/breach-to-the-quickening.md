+++
id = "ref/haunt/breach-to-the-quickening"
kind = "rule"
title = "Breach to the Quickening"
source_ids = ["horror-realms"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "breach_to_the_quickening", path = "json/haunts.json" },
]

[fields]
kind = "none"
+++

**Sources:** Horror Realms pg 60\
The Quickening is the most chaotic portion of the First World, a region so unstable that most of the
denizens of [the First World](ref/rule/the-first-world) give it a wide berth. Even a brief journey
into the Quickening is enough to transform body and mind in unforeseeable ways. Connections between
the Quickening and the Material Plane are rare and fleeting, but their effects persist.

See [Echoes of the First World](ref/rule/echoes-of-the-first-world) for more info on this variant
haunt.

**Breach to the Quickening**

**Challenge rating:** 12

**XP** 19,200\
CN persistent variant haunt (30-ft. radius)\
**Caster Level** 12th

**Notice:** Perception DC 20 (to notice nearby plant and animal life beginning to twist and deform)

**Hit points:** 54

**Weakness:** negative energy (immune to positive energy)

**Trigger:** proximity

**Reset:** 1d20 days

### Effect

Colorful light and raw chaotic energy lash out in a dizzying display. All living creatures become
the target of a random quickening effect (see table below; DC 21 Fortitude saving throw negates). A
creature that remains in the breach's area of effect must attempt an additional saving throw each
round against a new random effect.

### Overcharge

Each affected target rolls twice on the quickening effect table if they fail to resist this haunt's
effects.

|d%|Quickening Effect|
| --- | --- |
|01-25|The target transforms into a Tiny animal that is not native to the local region (as per [baleful polymorph](ref/spell/baleful-polymorph)). As typical for that spell, a creature that fails the initial Fortitude saving throw must succeed at a secondary Will saving throw or lose significant mental abilities.|
|26-40|The target gains a random mutation from the [mutant](ref/template/mutant) creature template, with the exception of radiation affinity.^[1](ref/haunt/breach-to-the-quickening#footnote-m)^ Roll 1d20 to select the mutation.|
|41-75|The target gains a random deformity from the mutant creature template. Roll 1d12 to select the specific deformity.|
|76-95|The First World lashes out at the target vindictively, bestowing the [accursed](ref/rule/accursed) corruption.|
|96-99|The target gains a new form. This effect functions as per [reincarnate](ref/spell/reincarnate), with a few exceptions. It takes full effect when the breach triggers, rather than taking 1 hour to activate. Additionally, it works only on living creatures, it does not impose any negative levels, and it does not cause a spellcaster to lose spells. Restoring the target to its original form requires a [miracle](ref/spell/miracle) or [wish](ref/spell/wish) spell.|
|100|The target gains the [fey creature template](ref/template/fey-creature), and its alignment changes to chaotic neutral. Restoring the target's original form requires a _[miracle](ref/spell/miracle)_ or _[wish](ref/spell/wish)_ spell.|

### Destruction

Breaches to the Quickening spontaneously close or move on their own as unpredictably as they appear.
A [forbiddance](ref/spell/forbiddance) or [dimensional lock](ref/spell/dimensional-lock) cast on the
area of a breach prevents the breach from exerting influence on the Material Plane until it moves to
a different location. A _[wish](ref/spell/wish)_ or _[miracle](ref/spell/miracle)_ spell permanently
closes a breach.

###### ^1^ {#footnote-m}

No mutation mentioning "radiation affinity" exists in that template.
