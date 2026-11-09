+++
id = "ref/template/soulbound-construct"
kind = "rule"
title = "Soulbound Construct"
source_ids = ["construct-handbook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "soulbound_construct", path = "json/monster_template4.json" },
]
[[sources]]
publication = "construct-handbook"
page = "60"

[fields]
kind = "none"
+++

**Soulbound Construct**

**Acquired:** present

**Challenge rating:** +1 or +2

A soulbound construct is a once-living creature that has had its soul bound to a construct host that
serves as its new body.

"Soulbound construct" is an acquired template that can be applied to a
[construct](ref/type/construct) (referred to hereafter as the host construct); this construct draws
several of its statistics from a living corporeal creature with an Intelligence score of 4 or more
(referred to hereafter as the base creature) whose soul is contained within a soul focus. A
soulbound construct uses all the host construct's statistics and special abilities except as noted
here.

**CR:** If the base creature has 10 or fewer Hit Dice, host construct's CR + 1; if the base creature
has 11 or more Hit Dice, host construct's CR + 2.

**Alignment:** As per base creature.

**Type:** A soulbound construct gains any alignment subtypes that the base creature had.

**AC:** A host construct gains a deflection bonus to AC equal to the base creature's Charisma
modifier.

**Weakness:** A soulbound construct retains all the weaknesses of the host construct and gains the
following additional weakness.

> **Susceptible to Mind-Affecting Effects (Ex):** A soulbound construct is not immune to
> mind-affecting effects.

**Special Attacks:** A soulbound construct gains the following special attack.

> **Spell-Like Abilities (Ex):** A soulbound construct has one or more alignment-based
> [spell-like abilities](ref/umr/spell-like-abilities), based upon the base creature's HD. If the
> base creature has 1-4 HD, the soulbound construct can cast the first spell-like ability listed in
> the table below for its alignment once per day. If the base creature has 5-10 HD, it can cast the
> first listed spell-like ability three times per day and the second ability once per day. If the
> base creature has 11-16 HD, it can cast the first listed spell-like ability at will, the second
> ability three times per day, and the third ability once per day. If the base creature has 17-20
> HD, it can cast the first and second listed spell-like abilities at will and the third ability
> three times per day. The caster level for these abilities is equal to the base creature's Hit
> Dice. The save DC for these abilities is based on the base creature's Intelligence, Wisdom, or
> Charisma, whichever is highest.
>
> |Alignment|First Ability|Second Ability|Third Ability|
> | --- | --- | --- | --- |
> |Lawful good|[Hold person](ref/spell/hold-person)|[Dimensional anchor](ref/spell/dimensional-anchor)|[Repulsion](ref/spell/repulsion)|
> |Neutral good|[Heroism](ref/spell/heroism)|[Greater invisibility](ref/spell/invisibility-greater)|[Heal](ref/spell/heal)|
> |Chaotic good|[Blink](ref/spell/blink)|[Shout](ref/spell/shout)|[Prismatic spray](ref/spell/prismatic-spray)|
> |Lawful neutral|[Suggestion](ref/spell/suggestion)|[Lesser globe of invulnerability](ref/spell/globe-of-invulnerability-lesser)|[Blade barrier](ref/spell/blade-barrier)|
> |Neutral|[Deep slumber](ref/spell/deep-slumber)|[Hold monster](ref/spell/hold-monster)|[Greater dispel magic](ref/spell/dispel-magic-greater)|
> |Chaotic neutral|[Rage](ref/spell/rage)|[Confusion](ref/spell/confusion)|[Disintegrate](ref/spell/disintegrate)|
> |Lawful evil|[Minor image](ref/spell/minor-image)|[Crushing despair](ref/spell/crushing-despair)|[Antilife shell](ref/spell/antilife-shell)|
> |Neutral evil|[Inflict moderate wounds](ref/spell/inflict-moderate-wounds)|[Enervation](ref/spell/enervation)|[Harm](ref/spell/harm)|
> |Chaotic evil|[Stinking cloud](ref/spell/stinking-cloud)|[Contagion](ref/spell/contagion)|[Eyebite](ref/spell/eyebite)|

**Ability Scores:** The host construct replaces its Intelligence, Wisdom, and Charisma scores with
those of the base creature.

**Skills:** A soulbound construct gains the Intelligence-, Wisdom-, and Charisma-based skills of the
soul held in the soul focus. If the host construct already has any of these skills, select the
higher total bonus between that of the base creature and that of the host construct.

**Feats:** A soulbound construct gains the base creature's feats as bonus feats. Feats that can't be
used by the host construct are not added in this way.

**Special Qualities:** A soulbound construct gains the following special qualities.

> **Bind Soul (Su):** The process to bind the soul focus to the construct body takes 1d10 days of
> continual concentration, and the target construct can attempt a Will save (DC = 10 + half the base
> creature's Hit Dice + the base creature's Intelligence, Wisdom, or Charisma modifier, whichever is
> highest) to negate the effect. Mindless constructs receive no save against this effect.
>
> **Soul Focus (Su):** The base creature's soul lives within a gem called a soul focus. As long as
> the soul focus remains intact, a soulbound construct gains the abilities granted by this template,
> and it retains the base creature's personality, memories, and thoughts, as well as its alignment,
> mental ability scores, feats, and skills that are based on mental ability scores. It does not
> retain racial modifiers to those skills (if any). A soul focus has [hardness](ref/umr/hardness) 8,
> 12 hit points, and a break DC of 20.

### Construction

A soulbound construct's soul focus is made from a gem worth 1,000 gp per Hit Die of the base
creature. Creating the soul-bound construct requires first binding the base creature's soul to the
gem in a 10-hour ritual using rare spell components worth 10,000 gp. The base creature dies at some
point during the process of creating the soul focus (this prevents the body from later being
revived, so long as the soul focus still remains intact). An unwilling soul can resist the procedure
with a successful DC 20 Will save.

### Soul Focus

**CL** 7th; **Price** 10,000 gp + 1,000 gp per Hit Die of the base creature

#### Construction

**Requirements** [Craft Construct](ref/feat/craft-construct),
[Craft Wondrous Item](ref/feat/craft-wondrous-item), [geas/quest](ref/spell/geas-quest),
[magic jar](ref/spell/magic-jar), soul of a living creature who dies or is slain during the creation
process; **Skill** [Craft (gemcutting)](ref/skill/craft-any); **Cost** 5,000 gp + 1,000 gp per Hit
Die of the base creature
