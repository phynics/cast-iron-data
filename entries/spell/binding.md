+++
id = "ref/spell/binding"
kind = "spell"
title = "Binding"
aon = "SpellDisplay.aspx?ItemName=Binding"
source_ids = ["core-rulebook"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "binding", path = "json/spells12.json" },
]
[[sources]]
publication = "core-rulebook"
page = "248"

[fields]
kind = "spell"
school = "enchantment"
subschools = ["Compulsion"]
descriptors = ["mind-affecting"]
levels = [
  { class = "Arcanist", level = 8 },
  { class = "Psychic", level = 8 },
  { class = "Sorcerer", level = 8 },
  { class = "Summoner", level = 6 },
  { class = "Wizard", level = 8 },
]
casting_time = "1 minute"
components = "V, S, M (opals worth 500 gp per HD of the target creature, plus other components as specified below)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "see text (D)"
saving_throw = "Will negates; see text"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: enchantment
Level: 6: Summoner\
8: Arcanist, Psychic, Sorcerer, Wizard
Casting time: 1 minute
Components: V, S, M (opals worth 500 gp per HD of the target creature, plus other components as specified below)
Range: close (25 ft. + 5 ft./2 levels)
Duration: see text (D)
Saving throw: Will negates; see text
Spell resistance: yes
Target: one living creature
Subschool: Compulsion
Descriptors: mind-affecting
:::

A binding spell creates a magical restraint to hold a creature. The target gets an initial saving
throw only if its Hit Dice equal at least half your caster level.

You may have as many as six assistants help you with the spell. For each assistant who casts
suggestion, your caster level for this casting of binding increases by 1. For each assistant who
casts dominate animal, dominate person, or dominate monster, your caster level for this casting of
binding increases by a number equal to a third of that assistant's level, provided that the spell's
target is appropriate for a binding spell. Since the assistants' spells are cast simply to improve
your caster level for the purpose of the binding spell, saving throws and
[spell resistance](ref/rule/spell-resistance) against the assistants' spells are irrelevant. Your
caster level determines whether the target gets an initial Will saving throw and how long the
binding lasts. All binding spells are dismissible.

Regardless of the version of binding you cast, you can specify triggering conditions that end the
spell and release the creature whenever they occur. These triggers can be as simple or elaborate as
you desire, but the condition must be reasonable and have a likelihood of coming to pass. The
conditions can be based on a creature's name, identity, or alignment, but otherwise must be based on
observable actions or qualities. Intangibles such as level, class, Hit Dice, or hit points don't
qualify. Once the spell is cast, its triggering conditions cannot be changed. Setting a release
condition increases the save DC (assuming a saving throw is allowed) by 2.

If you cast any of the first three versions of binding (those with limited durations), you may cast
additional binding spells to prolong the effect, overlapping the durations. If you do so, the target
gets a saving throw at the end of the first spell's duration, even if your caster level was high
enough to disallow an initial saving throw. If the creature's save succeeds, all binding spells it
has received are broken.

The binding spell has six versions. Choose one of the following versions when you cast the spell.

> _Chaining:_ The subject is confined by restraints that generate an antipathy spell affecting all
> creatures who approach the subject, except you. The duration is 1 year per caster level. The
> subject of this form of binding is confined to the spot it occupied when it received the spell.
> Casting this version requires a chain that is long enough to wrap around the creature three times.
>
> _Slumber:_ This version causes the subject to become comatose for as long as 1 year per caster
> level. The subject does not need to eat or drink while slumbering, nor does it age. This form of
> binding is slightly easier to resist. Reduce the spell's save DC by 1. Casting this version
> requires a jar of sand or rose petals. This is a sleep effect.
>
> _Bound Slumber:_ This combination of chaining and slumber lasts for as long as 1 month per caster
> level. Reduce the save DC by 2. Casting this version requires both a long chain and a jar of sand
> or rose petals. This is a sleep effect.
>
> _Hedged Prison:_ The subject is transported to or otherwise brought within a confined area from
> which it cannot wander by any means. This effect is permanent. Reduce the save DC by 3. Casting
> this version requires a tiny golden cage worth 100 gp that is consumed when the spell is cast.
>
> _Metamorphosis:_ The subject assumes gaseous form, except for its head or face. It is held
> harmless in a jar or other container, which may be transparent if you so choose. The creature
> remains aware of its surroundings and can speak, but it cannot leave the container, attack, or use
> any of its powers or abilities. The binding is permanent. The subject does not need to breathe,
> eat, or drink while metamorphosed, nor does it age. Reduce the save DC by 4.
>
> _Minimus Containment:_ The subject is shrunk to a height of 1 inch or less and held within some
> gem, jar, or similar object. The binding is permanent. The subject does not need to breathe, eat,
> or drink while contained, nor does it age. Reduce the save DC by 4.

You can't dispel a binding spell with [dispel magic](ref/spell/dispel-magic) or a similar effect,
though an [antimagic field](ref/spell/antimagic-field) or
[mage's disjunction](ref/spell/mages-disjunction) affects it normally. A bound extraplanar creature
cannot be sent back to its home plane by [dismissal](ref/spell/dismissal),
[banishment](ref/spell/banishment), or a similar effect.
