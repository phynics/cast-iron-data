+++
id = "ref/arc-kineticist/terrakineticist"
kind = "archetype"
title = "Terrakineticist"
aon = "ArchetypeDisplay.aspx?FixedName=Kineticist%20Terrakineticist"
source_ids = ["ultimate-wilderness"]
provenance = [
  { dataset = "pathfinder-data-1-e", record = "terrakineticist", path = "json/archetypes_kineticist.json" },
]
relations = [
  { kind = "archetype", target = "ref/class/kineticist" },
]
[[sources]]
publication = "ultimate-wilderness"
page = "63"

[fields]
kind = "archetype"
replaces = ["Expanded element", "Omnikinesis"]
alters = ["Elemental focus", "kinetic blast", "Elemental defense"]
+++

Terrakineticists have a stunted ability that allows them to access the Elemental Planes, but they've
learned how to turn this limited talent into an incredible strength by tapping into the ambient
elemental nature of the land surrounding them.

**Terrakinesis**

**Action:** Ability

**Alters:** Elemental focus, kinetic blast

Whenever a terrakineticist gains a wild talent that isn't a universal talent, she chooses one wild
talent of the appropriate level from each of the six [elements](ref/ability/elements) (aether, air,
fire, earth, water, and wood).^1^ She can use wild talents of the same element that she chose in
this way to meet prerequisites for these wild talents. Instead of gaining one kineticist blast, a
terrakineticist chooses one simple blast from each element that has more than one simple blast.

When in a corresponding terrain, as determined by the ranger
[favored terrain](ref/ability/favored-terrain) categories, her element changes to the corresponding
element (granting her class skills, basic utility wild talent, simple blast, and elemental defense
as appropriate), and she gains all the wild talents she selected from the corresponding element.

- Aether corresponds to urban and the Ethereal Plane
- Air corresponds to hill, mountain, plains, and the Plane of Air
- Fire corresponds to desert and the Plane of Fire
- Earth corresponds to underground and the Plane of Earth
- Water corresponds to cold, swamp, water, and the Plane of Water
- Wood corresponds to forest, jungle, the First World, and the Positive Energy Plane.

In areas that might count as multiple types of terrain, the GM decides which element predominates,
and in certain areas not covered by the ranger favored terrains (such as the upper atmosphere) or in
those with strong elemental energy (like an underground temple of a fire cult), the corresponding
element might differ. If the kineticist class gains additional elements, those elements also gain
corresponding terrains at the GM's discretion, and the terrakineticist chooses wild talents from
those elements. A terrakineticist should almost never be in a situation that doesn't correspond to
any of these elements, but in such an unusual circumstance (for instance, the void of space given
the standard six elements), she loses access to all her wild talents, even her universal wild
talents.

When her element changes, she loses the benefits of all active wild talents from the previous
element, even if it would usually last until the next time she recovers burn. However, time spent in
other terrain still counts against the ability's duration; if she changes back again to the original
element, the benefit returns only if it has any remaining duration.

**Terrakinetic Defense**

**Alters:** Elemental defense

**Info:** A terrakineticist's _elemental defense_ wild talent changes with her corresponding
element, just like her other wild talents. However, unlike her other wild talents, any burn she
invests in one element's elemental defense carries over to her elemental defense when her element
changes. For instance, if a 6th-level terrakineticist invested 2 points of burn in
[flesh of stone](ref/kinetic/flesh-of-stone) to gain 2 additional points of
[damage reduction](ref/rule/damage-reduction) and then entered a city and changed to aether, she
would have 2 points of burn invested in [force ward](ref/kinetic/force-ward) and increase the force
ward's temporary hit points by 6.

**Gained:** At 2nd Level

**Expanded Terrakinesis**

**Ability:** A terrakineticist gains both simple blasts for the element corresponding to her current
terrain, if that element has two, and the composite blast associated with expanding in that element
([force blast](ref/kinetic/force-blast), [thunderstorm blast](ref/kinetic/thunderstorm-blast),
[blue flame blast](ref/kinetic/blue-flame-blast), [metal blast](ref/kinetic/metal-blast),
[ice blast](ref/kinetic/ice-blast), and [verdant blast](ref/kinetic/verdant-blast)). She also gains
a universal infusion or utility talent for which she meets the prerequisites.

**At 15th Level:** She gains one infusion or utility wild talent for which she meets the
prerequisites.

**Gained:** At 7th Level

**Replaces:** Expanded element

**Omniterrakinesis (Su)**

**Ability:** A terrakineticist can accept 1 point of burn as a **free action** at the start of her
turn to change her element without regard to the surrounding terrain until the beginning of her next
turn.

**Gained:** At 20th Level

**Replaces:** Omnikinesis

^1^ This archetype was introduced before the \*void\* element was created. Consult your GM if you
wish to use that element, too. As a suggestion, consider terrains such as the lowest levels of the
Darklands, outer space, the Shadow Plane, and the Negative Energy Plane.
