+++
id = "ref/spell/spellcasting-contract-greater"
kind = "spell"
title = "Greater Spellcasting Contract"
source_ids = ["pathfinder-29-mother-of-flies"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "spellcasting_contract_greater", path = "json/spells9.json" },
]
relations = [
  { kind = "variant", target = "ref/spell/spellcasting-contract-lesser" },
]

[fields]
kind = "spell"
school = "evocation"
levels = [
  { class = "Cleric", level = 9 },
]
casting_time = "10 minutes"
components = "V, S, DF"
range = "touch"
effects = [
  { label = "Target", value = "creature touched" },
]
duration = "permanent until discharged (D)"
saving_throw = "Will negates (harmless)"
spell_resistance = "yes (harmless)"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 9: Cleric
Casting time: 10 minutes
Components: V, S, DF
Range: touch
Target: creature touched
Duration: permanent until discharged (D)
Saving throw: Will negates (harmless)
Spell resistance: yes (harmless)
:::

## Lesser Spellcasting Contract

**Sources:** Pathfinder \#29: Mother of Flies pg 67

> _These three spells are associated with [Asmodeus](ref/faith/asmodeus), but there are no
> restrictions on its use by others._

This spell functions exactly like imbue with spell ability, except that you can imbue the target
with any spell you have prepared (instead of just abjuration, divination, or conjuration \[healing\]
spells) and the target may have more than one use of the imbued spells, depending upon the
arrangements made when it is cast.

Casting this spell requires a contract between you and the target, explaining what spells are to be
imbued and the circumstances that cause the contract to expire. The contract may be as simple as
allowing the target one casting of each of the imbued spells (as per imbue with spell ability), or
may continue for multiple days or even indefinitely, with the target regaining use of the imbued
spells when you next prepare your own spells. You may include any proviso you see fit, such as
requiring the target to pray to Asmodeus each morning, or restricting the target to only casting the
imbued spells on himself. If the target does not agree to all the conditions in the contract, this
spell fails when cast. The contract (and this spell) automatically expires if you or the target
dies. While the contract remains in effect, you gain a profane bonus to your Armor Class, saving
throws, and checks equal to the highest-level spell you have imbued.

Once you cast this spell, you cannot prepare a new 5th-level spell to replace it until the contract
expires. If the number of 5th-level spells you can cast decreases, and that number drops below your
current number of active lesser spellcasting contract spells, the more recently cast imbued spells
are dispelled.

Unlike imbue with spell ability, how the target uses the spell has no reflection on your alignment
or relationship with Asmodeus; the Prince of Darkness accepts that allowing another access to his
magic for good may benefit his plans in the long run. Note that unlike imbue with spell ability, you
cannot dismiss this spell; you must abide by the contract's termination clause (though the contract
may include a proviso for at-will nullification by either or both parties). This spell cannot be
combined with imbue with spell ability or similar spells to give a target more spells than the
limit.

_Example:_ You cast this spell on your 5 HD fighter cohort after negotiating an appropriate
contract, imbuing him with the ability to cast cure moderate wounds, magic weapon, and shield of
faith once per day for 1 month. If he casts any of these spells, he recovers them when you prepare
your spells. Until the contract ends, your 5th-level spell slot used to cast this spell remains
expended and cannot be filled with a new spell. Because you imbued your cohort with a 2nd-level
spell, you gain a +2 profane bonus to attacks, saves, and checks while the contract remains in
effect.

### Spellcasting Contract

**Sources:** Pathfinder \#29: Mother of Flies pg 68

This spell functions like [lesser spellcasting contract](ref/spell/spellcasting-contract-lesser),
except if the target has 9 HD or more, you can imbue him with one or two 2nd-level spells and one
3rd-level spell.

### Greater Spellcasting Contract

**Sources:** Pathfinder \#29: Mother of Flies pg 68

This spell functions like lesser spellcasting contract, except if the target has 13 HD or more you
can imbue him with one or two 4th-level spells and one 5th-level spell.
