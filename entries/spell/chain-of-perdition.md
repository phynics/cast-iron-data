+++
id = "ref/spell/chain-of-perdition"
kind = "spell"
title = "Chain of Perdition"
source_ids = ["ultimate-combat"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "chain_of_perdition", path = "json/spells2.json" },
]
[[sources]]
publication = "ultimate-combat"
page = "225"

[fields]
kind = "spell"
school = "evocation"
descriptors = ["force"]
levels = [
  { class = "Arcanist", level = 3 },
  { class = "Bloodrager", level = 3 },
  { class = "Cleric", level = 3 },
  { class = "Oracle", level = 3 },
  { class = "Psychic", level = 3 },
  { class = "Sorcerer", level = 3 },
  { class = "Warpriest", level = 3 },
  { class = "Wizard", level = 3 },
]
casting_time = "1 standard action"
components = "V, S, M/DF (chain link)"
range = "close (25 ft. + 5 ft./2 levels)"
effects = [
  { label = "Effect", value = "10-ft. chain" },
]
duration = "1 round/level (D)"
saving_throw = "none"
spell_resistance = "yes"
+++

::: statblock
title = "Spell statistics"
School: evocation
Level: 3: Arcanist, Bloodrager, Cleric, Oracle, Psychic, Sorcerer, Warpriest, Wizard
Casting time: 1 standard action
Components: V, S, M/DF (chain link)
Range: close (25 ft. + 5 ft./2 levels)
Duration: 1 round/level (D)
Saving throw: none
Spell resistance: yes
Effect: 10-ft. chain
Descriptors: force
:::

A floating chain of force with hooks at each end appears within an unoccupied space of your choosing
within range. This chain is a Medium object that has a 10-foot reach. Physical attacks cannot hit or
harm the chain of perdition, but [dispel magic](ref/spell/dispel-magic),
[disintegrate](ref/spell/disintegrate), a
[sphere of annihilation](ref/magic-artifact/sphere-of-annihilation), or a
[rod of cancellation](ref/magic-rod/rod-of-cancellation) affects it normally. The chain's AC against
touch attacks is 10 + your Charisma modifier (sorcerer), Intelligence modifier (wizard), or Wisdom
modifier (cleric).

The chain can perform the dirty trick (blind or entangle), drag, reposition, and trip combat
maneuvers, using your caster level in place of your Combat Maneuver Bonus, and your Charisma
modifier (sorcerer), Intelligence modifier (wizard), or Wisdom modifier (cleric) in place of your
Strength or Dexterity modifier. The chain does not provoke attacks of opportunity for making combat
maneuvers. It suffers no penalty or miss chance due to darkness, invisibility, or other forms of
concealment.

As a move action, you can move the chain up to 30 feet. If the chain goes beyond the spell's range
or out of your sight, it returns to you.

If a creature that the chain attacks has [spell resistance](ref/rule/spell-resistance), you must
make a caster level check (1d20 + caster level) against that spell resistance the first time the
chain performs a successful maneuver against that creature. If the chain is successfully resisted,
the spell is dispelled. If not, the weapon has its normal full effect on that creature for the
duration of the spell.
