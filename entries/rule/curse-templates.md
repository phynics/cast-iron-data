+++
id = "ref/rule/curse-templates"
kind = "rule"
title = "Curse Templates"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "curse_templates", path = "json/rules_campaign_types02.json" },
]
[[sources]]
publication = "horror-adventures"
page = "143"

[fields]
kind = "none"
+++

Some curses function in an unusual fashion compared to others. The following section presents
several templates that can be applied to any curse to represent variants of that curse. These
templates function similarly to templates that can be applied to creatures, and you could
potentially apply several templates to the same curse to create a truly horrifying effect.

### Contagious Curse

**Effect** In addition to the curse's normal effect, the curse is transmissible to other creatures
by a particular means. This could be similar to transmission methods for a disease, or it could be
something more esoteric, such as by song or love.

**Cure** The accursed creature's attempts to remove its own curse with magic automatically fail,
though other creatures can do so as normal. Whatever its other means of transmission, a creature
attempting to cure the original creature's curse with magic is automatically exposed to the curse
and must succeed at a saving throw to avoid being afflicted by it.

### Death Curse

**Effect** A death curse usually occurs upon the deaths of [linnorms](ref/family/linnorm), some fey,
or hags, but other creatures can also curse their killers. The save DC is equal to 10 + 1/2 the
creature's Hit Dice + the creature's Charisma modifier, rather than the curse's normal DC. A death
curse's effect is the same as the original curse, and the effect tends to vary based on the cursing
creature's HD.

**Cure** In addition to the standard cures, the first time that the creature who placed the death
curse returns to life, the accursed creature receives a new saving throw to break the curse. If the
accursed contributes to this resurrection, she receives a +4 bonus on this saving throw.

|HD|Death Curse|
| --- | --- |
|1-5|[Minor haunting](ref/curse/haunting-minor) or [weeping wound](ref/curse/weeping-wound)|
|6-10|[Bestow curse](ref/spell/bestow-curse), [major haunting](ref/curse/haunting-major), or [tormenting visions](ref/curse/tormenting-visions)|
|11-15|[Hunt of the Bogeyman](ref/curse/hunt-of-the-bogeyman), [shattered self](ref/curse/shattered-self), or [unluck](ref/curse/unluck)|
|16-20|[Hunt of the Ankou](ref/curse/hunt-of-the-ankou) or [sealed fate](ref/curse/sealed-fate)|

### Generational Curse

**Effect** In addition to cursing the original target creature, this curse continues to curse the
target's children, and their children, and so on across multiple generations. It is possible it
might carry on only to certain children (such as daughters or firstborn children).

**Cure** Generational curses can usually be cured only by special means, though the extinction of a
family line also is able to end its threat. Even if [remove curse](ref/spell/remove-curse) can cure
the curse on an individual target, it doesn't stop the generational curse from affecting future
generations, which must deal with the curse in their own manner.
