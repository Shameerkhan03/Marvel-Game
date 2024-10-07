from typing import Final
from random import randint
from enum import Enum, auto


class CharacterType(Enum):
    SUPERHERO = auto()
    SUPERVILLAIN = auto()


class Character:
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        self.name = name
        self.attack_power = attack_power
        self.life = life

    def __str__(self) -> str:
        return (
            f"Name: {self.name}, Attack Power: {self.attack_power}, Life: {self.life}"
        )


class SuperHero(Character):
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.SUPERHERO

    def __str__(self) -> str:
        return (
            f"Super-hero=> Name: {self.name}, Attack Power: {self.attack_power},"
            f"Life: {self.life}"
        )


class SuperVillain(Character):
    def __init__(self, name: str, attack_power: int, life: int) -> None:
        super().__init__(name, attack_power, life)
        self.role = CharacterType.SUPERVILLAIN

    def __str__(self) -> str:
        return (
            f"Super-villain=> Name: {self.name}, Attack Power: {self.attack_power},"
            f"Life: {self.life}"
        )


class Life:
    hero_life = 0
    villain_life = 0

    @staticmethod
    def inc_hero_life(life: int) -> None:
        Life.hero_life += life

    @staticmethod
    def dec_hero_life(life: int) -> None:
        Life.hero_life -= life

    @staticmethod
    def inc_villain_life(life: int) -> None:
        Life.villain_life += life

    @staticmethod
    def dec_villain_life(life: int) -> None:
        Life.villain_life -= life


def get_all_heroes() -> list[SuperHero]:
    ironman = SuperHero(name="Ironman", attack_power=250, life=1000)
    blackwidow = SuperHero(name="BlackWidow", attack_power=180, life=800)
    spiderman = SuperHero(name="Spiderman", attack_power=190, life=700)
    hulk = SuperHero(name="Hulk", attack_power=300, life=1100)

    super_heroes: list[SuperHero] = [ironman, blackwidow, spiderman, hulk]
    return super_heroes


def get_hero(index: int) -> SuperHero:
    super_heroes = get_all_heroes()
    return super_heroes[index]


def get_all_villains() -> list[SuperVillain]:

    thanos = SuperVillain(name="Thanos", attack_power=1500, life=1500)
    redskull = SuperVillain(name="Redskull", attack_power=300, life=800)
    proxima = SuperVillain(name="Proxima", attack_power=320, life=800)

    super_villains: list[SuperVillain] = [thanos, redskull, proxima]
    return super_villains


def get_villain(index: int) -> SuperVillain:
    super_villains = get_all_villains()
    return super_villains[index]


# Attack
def attack() -> None:
    for attack_num in range(3):
        hero_index = randint(0, 3)
        villain_index = randint(0, 2)

        current_hero = get_hero(hero_index)
        current_villain = get_villain(villain_index)

        simulate_attack(attack_num, current_hero, current_villain)


def simulate_attack(num: int, hero: SuperHero, villain: SuperVillain) -> None:
    Life.inc_hero_life(hero.life)
    Life.inc_villain_life(villain.life)
    print(f"Attack: {num+1} => {hero.name} is going to attack {villain.name}.")

    Life.dec_hero_life(villain.attack_power)
    Life.dec_villain_life(hero.attack_power)


def win_or_lose() -> None:
    print("=" * 70)

    if Life.hero_life >= Life.villain_life:
        print("Enemies are dead. You have saved Zortan.")
    else:
        print("Avengers are dead. You lose.")


def main() -> None:
    attack()
    win_or_lose()


main()
