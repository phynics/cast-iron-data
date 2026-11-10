+++
id = "ref/spell/green-caress"
kind = "spell"
title = "Green Caress"
aon = "SpellDisplay.aspx?ItemName=Green%20Caress"
source_ids = ["horror-adventures"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "green_caress", path = "json/spells5.json" },
]
[[sources]]
publication = "horror-adventures"
page = "119"

[fields]
kind = "spell"
school = "transmutation"
levels = [
  { class = "Druid", level = 6 },
  { class = "Hunter", level = 4 },
  { class = "Ranger", level = 4 },
  { class = "Shaman", level = 6 },
  { class = "Witch", level = 6 },
]
casting_time = "1 standard action"
components = "V, S, M (pinch of moss or a kudzu leaf)"
range = "touch"
effects = [
  { label = "Target", value = "one living creature" },
]
duration = "7 days (see text)"
saving_throw = "Fortitude partial (see text)"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: transmutation
Level: 4: Hunter, Ranger\
6: Druid, Shaman, Witch
Casting time: 1 standard action
Components: V, S, M (pinch of moss or a kudzu leaf)
Range: touch
Duration: 7 days (see text)
Saving throw: Fortitude partial (see text)
Spell resistance: yes
Target: one living creature
:::

You cause the target to transform into a plant over time. You must succeed at a melee touch attack
to infect the target. If the target succeeds at its Fortitude saving throw, it takes 1d4 points of
ability damage to each physical ability score (Strength, Dexterity, and Constitution) and the spell
ends. If the target fails its saving throw, it takes 1d4 points of ability damage to each physical
ability score immediately and continues to take 1d4 points of ability damage to each of its physical
ability scores every day, until the spell expires. It can't recover this ability damage as long as
the spell lasts, even with magic. While the spell continues, the target takes on physical plant
characteristics as appropriate to the environment. It begins to diminish in height and its skin
turns plant-like. For example, the target's skin might turn green and its hair is slowly replaced
with grass or leaves or the target's skin might become smooth, pale, and flabby as the creature
transforms into a large mushroom in an underground environment.

If the damage to any single ability score equals or exceeds that score, the target fully transforms
into a normal small tree or shrub. This final transformation is instantaneous, ending green caress.
The target remains alive but is considered the same as a regular tree, shrub, or other vegetation.
Any ability damage from other sources, like poison or disease, also applies toward transforming the
creature. If the target retains at least 1 point in all of its physical ability scores at the end of
7 days, the final transformation doesn't occur and the spell ends. Any changes in appearance
gradually reverse themselves as the ability damage heals.

[Break enchantment](ref/spell/break-enchantment), [dispel magic](ref/spell/dispel-magic), and
[remove curse](ref/spell/remove-curse) can end the spell before the duration expires, but the spell
is contagious. If a caster level check attempt to remove green caress fails by 5 or more, the
creature who attempted to remove the effect must attempt a Fortitude saving throw as if it had just
been targeted with the spell. If the spell's target attempts to remove the effect from itself and
fails, it causes the spell to behave as if affected by [plant growth](ref/spell/plant-growth) (as
described below).

[Polymorph any object](ref/spell/polymorph-any-object) ends the spell and totally restores the
target without any risk to the caster, even after the target has been finally transformed, as do
[limited wish](ref/spell/limited-wish), [miracle](ref/spell/miracle), and [wish](ref/spell/wish)
(treat polymorph any object as if it had an instantaneous duration if it is used in this way). If
the target is in the area of a plant growth spell as it is cast, it must attempt a Fortitude save at
green caress's DC or immediately take another 1d4 points of ability damage to each physical ability
score; this stacks with multiple castings of plant growth. If the target is in the area of
[diminish plants](ref/spell/diminish-plants) as it is cast, it ignores the next ability damage from
green caress to one of its three physical ability scores (chosen randomly); this doesn't stack with
multiple castings of diminish plants.
