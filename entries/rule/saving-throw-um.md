+++
id = "ref/rule/saving-throw-um"
kind = "rule"
title = "Saving Throw"
source_ids = ["ultimate-magic"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "saving_throw_um", path = "json/rules_adv_magic01.json" },
]

[fields]
kind = "none"
+++

**Sources:** Ultimate Magic pg 131

Most spells that directly affect creatures with a magical effect should allow a saving throw. Spells
that create nonmagical materials that then strike or impede creatures (such as
[ice storm](ref/spell/ice-storm) and [sleet storm](ref/spell/sleet-storm)) do not normally require a
saving throw.

Spells that require the caster to make an attack roll to hit (even if it's a ranged touch attack)
may or may not require a saving throw ([enervation](ref/spell/enervation) and
[searing light](ref/spell/searing-light) do not, [disintegrate](ref/spell/disintegrate) does).
Attack effects that do not require rolling damage should always allow a saving throw to reduce or
negate the effect; otherwise, the spell becomes an obvious choice for anyone of the level to cast
it.

**Tip:** When deciding whether or not the spell should have a saving throw, consider how you'd feel
if someone used the spell on your favorite PC. If your PC didn't get any chance to resist the effect
with a save or to dodge it entirely because of a failed attack roll, would you be annoyed,
embarrassed, or angry? If so, you should give the spell some kind of save or attack roll, just so
it's not an always-effective option.

**Fortitude Saves:** Spells with Fortitude saves usually physically transform the target, apply an
effect you'd normally resist with a Fortitude save (such as disease or poison), or are a form of
attack that sheer physical toughness is enough to resist. In general, making a successful Fortitude
save means the effect hits, but the target toughs it out, like a bear shrugging off the stinky musk
sprayed by a skunk. Note that if your spell only affects creatures - not objects - then nonliving
creatures such as constructs and undead are immune to the spell. For example, this makes them immune
to creature-oriented polymorphing spells, but not spells such as
_[disintegrate](ref/spell/disintegrate),_ which can attack objects.

**Reflex Save:** Spells with Reflex saves usually create a physical burst or spread in an area, like
an explosion, which the target is able to dodge with a successful saving throw. In general, making a
successful Reflex save means the target dodged the effect, or the effect rolled over or around the
target with a lesser effect. Note that you shouldn't build a spell where the caster makes an attack
roll and the target also makes a Reflex saving throw; doing so brings Dexterity into play twice for
the same spell (once for the target's AC, once for the target's Reflex save modifier).

**Will Saves:** Spells with Will saves are mental, mind-affecting attacks; the target resists with
pure mental power, by using evasive thoughts or noticing flaws in the spell's assault that can
negate its effectiveness. A Will save is like a mental version of a Fortitude save; the effect
"hits" the target, and whether or not it succeeds depends on the target's willpower. Most
direct-attack Will-save spells (such as [sleep](ref/spell/sleep) and
[phantasmal killer](ref/spell/phantasmal-killer)) are mind-affecting effects (see
[Descriptors](ref/rule/school), below).

Some spells can be cast on objects, and the object only gets a saving throw if it is a magic item or
is held by a creature; these spells should have "(object)" listed after the type of saving throw
(see [shrink item](ref/spell/shrink-item)).

Helpful spells and spells that do not harm the target in any way either should have no saving throw,
or should allow a saving throw but have "(harmless)" listed after the type of saving throw (see
[fly](ref/spell/fly)).

Spells that only affect the caster never require a saving throw (you'd never try to resist a
beneficial spell you're casting on yourself), so you don't list a saving throw for those spells at
all (see [true strike](ref/spell/true-strike)).
