+++
id = "ref/feat/thanatopic-spell"
kind = "feat"
title = "Thanatopic Spell"
aon = "FeatDisplay.aspx?ItemName=Thanatopic%20Spell"
source_ids = ["ultimate-magic", "osirion-land-of-the-pharaohs"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "thanatopic_spell", path = "json/feat16.json" },
]
[[sources]]
publication = "ultimate-magic"
page = "157"
[[sources]]
publication = "osirion-land-of-the-pharaohs"
page = "27"

[fields]
kind = "feat"
feat_types = ["Metamagic"]
prerequisites = "Knowledge (religion) 6 ranks, Spell Focus (necromancy)."
prerequisite_feats = ["ref/feat/spell-focus"]
benefit = "A thanatopic spell pierces defenses and immunities that protect against death effects, energy drain, and negative levels, affecting the target as if the protective barrier did not exist. For example, you could cast a thanatopic vampiric touch or enervation spell on a target under the effects of death ward, and the target would suffer the normal effect of the spell. Saving throws and SR (if any) still apply."
normal = "Defenses such as *death ward* negate death effects, negative levels, and energy drain. Undead are immune to these attacks."
+++

## Thanatopic Spell (Metamagic)

Your spells can pierce wards against negative energy and even affect undead targets.\
**Prerequisites:** Knowledge (religion) 6 ranks, [Spell Focus](ref/feat/spell-focus) (necromancy).\
**Benefit:** A thanatopic spell pierces defenses and immunities that protect against
[death](ref/spelldef/death) effects,
[energy drain, and negative levels](ref/rule/energy-drain-and-negative-levels), affecting the target
as if the protective barrier did not exist. For example, you could cast a thanatopic
[vampiric touch](ref/spell/vampiric-touch) or [enervation](ref/spell/enervation) spell on a target
under the effects of [death ward](ref/spell/death-ward), and the target would suffer the normal
effect of the spell. Saving throws and SR (if any) still apply.

Undead are susceptible to spells augmented by this feat, as it retunes the negative energy to be
harmful to them. A thanatopic spell that would kill a living creature (such as by giving it negative
levels equal to its Hit Dice) destroys an undead (though undead such as
[ghosts](ref/template/ghost), [liches](ref/template/lich), and [vampires](ref/template/vampire) may
reform as normal). Undead affected by thanatopic spells that give negative levels automatically make
their saving throws to remove negative levels after 24 hours.

A thanatopic spell uses up a spell slot two levels higher than the spell's actual level.

**Normal:** Defenses such as _[death ward](ref/spell/death-ward)_ negate death effects, negative
levels, and energy drain. [Undead](ref/type/undead) are immune to these attacks.
