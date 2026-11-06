+++
id = "ref/rule/spells"
kind = "rule"
title = "Spells"
source_ids = ["aquatic-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spells", path = "json/rules_campaign_types01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Aquatic Adventures\
While various spells have different effects underwater, the most fundamental hindrance to
spellcasting, at least at low levels, is the fact that a creature holding its breath must succeed at
a [concentration](ref/rule/concentration) check (DC = 15 + spell level) to cast a spell at all,
whether or not the spell has a verbal component. If the spell has a verbal component, expelling the
air needed to incant the spell reduces the creature's remaining number of rounds of breath by 3
(which stacks with the reduction from performing a standard or full-round action; see the
[Drowning section](ref/rule/drowning-aa)), and a creature can't finish the spell if it doesn't have
enough breath left. Spells that have verbal components and casting times of swift or immediate
actions instead decrease the caster's remaining number of rounds of breath by 1.

Mundane spell components generally work fine underwater as long as they're stored in watertight
containers, and aquatic-appropriate substitutions exist for any mundane component that would be
inherently impossible to use underwater. The Core Rulebook describes the effect of
[fire spells underwater](ref/rule/underwater-combat); some other spells exist that function
differently.

**Acid Spells:** Conjuration (creation) spells that conjure nonmagical acid, like
[acid arrow](ref/spell/acid-arrow), don't work properly underwater, as the water dilutes the acid
harmlessly. Evocation spells that deal magical acid damage, like a [fireball](ref/spell/fireball)
affected by the [Elemental Spell](ref/feat/elemental-spell) metamagic feat, work normally
underwater.

**Cloud and Weather Spells:** Cloud spells such as [fog cloud](ref/spell/fog-cloud) and
[obscuring mist](ref/spell/obscuring-mist) specifically say that they don't work underwater, though
the [Murky Spell](ref/feat/murky-spell) metamagic feat can create equivalent mist spells underwater.
Other spells that create weather that would be appropriate only on land, like
[ice storm](ref/spell/ice-storm) and [sleet storm](ref/spell/sleet-storm), do not function
underwater at all. [Twilight haze](ref/spell/twilight-haze), however, is an illusion and thus works
underwater.

**Cold Spells:** Spells that deal cold damage but don't normally conjure ice, like
[cone of cold](ref/spell/cone-of-cold), instead deal half cold damage and half piercing damage, as
the cold creates jagged ice shards underwater. This has no effect on spells that already create ice,
rather than just cold damage.

**Electricity Spells:** While normal electricity, such as that from a natural thunderstorm, tends to
disperse in all directions underwater, magical electricity spells hold their integrity enough to
have normal effects underwater, with one exception: visible and audible lightning bolts and sparks
are the result of combusted air, and they don't happen underwater. Because of this, creatures that
fail to identify an electricity spell that requires a ranged touch attack are flat-footed against
the first such ranged touch attack during a fight, as they don't realize they need to dodge the
invisible projectile (unless they otherwise have reason to expect it, like a spellcaster who can
cast such spells). This doesn't apply to melee touch spells like
[shocking grasp](ref/spell/shocking-grasp), since the creature can still see the spellcaster's hand
moving towards it.

**Fire Spells:** While normal fire (including alchemist's fire) and most supernatural fire can't
burn underwater at all, fire spells have a chance to transform into steam instead. Whenever you cast
a fire spell underwater, you must succeed at a caster level check (DC = 20 + the spell's level) in
order to channel the heat into the water and create steam, dealing the same amount of fire damage as
normal but without secondary effects of fire, like igniting combustibles. A fire spell must be
either entirely steam or entirely fire, which means that if it covers an area that would normally
extend beyond the water's surface, you must choose whether to affect the region above the water or
below, and the surface blocks line of effect for the rest of the spell. A spell or
[spell-like ability](ref/umr/spell-like-abilities) with the fire descriptor that already creates
steam (like a [kineticist's](ref/class/kineticist) steam blast) doesn't require the caster level
check to create steam; only spells that would normally create an actual fire require the check. The
[Steam Spell](ref/feat/steam-spell) metamagic feat makes it easier to cast fire spells underwater.

**Invisibility:** Underwater, an invisible creature still displaces water, making it possible to
spot and target it as if it had only [concealment](ref/rule/concealment), as per the description of
[invisibility](ref/spell/invisibility). The [invisibility bubble](ref/spell/invisibility-bubble)
series of spells hide the displaced water and thus allow effective invisibility underwater.

**Sonic Spells:** While sound travels four times faster and farther in water than air, it also takes
more energy to do so, so in the end sonic spells have the same results underwater as they do on
land. At the GM's discretion, a spellcaster can choose to instead double the range or area, halve
the damage, and decrease the DC by 2 for sonic attacks.
